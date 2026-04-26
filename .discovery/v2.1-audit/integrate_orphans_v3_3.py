"""
integrate_orphans_v3_3.py — para cada prompt con tokens declarados-pero-no-usados,
inserta un paso explícito en EJECUCIÓN que indica cómo aplicar cada token.

Estrategia:
  1. Para cada prompt con huérfanos, derivá el propósito de cada token con tres heurísticas:
     A. Mapeo predefinido por convención de nombre (top 50 tokens cubren ~80% del volumen).
     B. Si el nombre del token aparece como palabra normal en RESUMEN/SITUACIÓN/PEDIDO
        (case-insensitive), extraer la oración y usar como descripción.
     C. Fallback genérico: "input específico — usar su valor literal en el bloque relevante del entregable".
  2. Insertar paso obligatorio "USO EXPLÍCITO DE PARÁMETROS" en EJECUCIÓN antes del paso
     INFERENCIA AMPLIFICADA (el último de la lista).
  3. Re-validar con certify_v3_3.py y verificar que orphan_inherited baja a 0.

Uso:
    python3 integrate_orphans_v3_3.py            # transform + write
    python3 integrate_orphans_v3_3.py --dry-run  # solo reporta sin escribir
"""
import json, re, sys
from pathlib import Path
from collections import Counter
from typing import Optional, Tuple, List

DIST = Path(__file__).resolve().parent.parent.parent
SRC = DIST / "prompts_universales_v3000.json"
OUT = DIST / "prompts_universales_v3000.json"
OUT_MIN = DIST / "prompts_universales_v3000.min.json"
OUT_PROMPSTER = DIST / "prompts_universales_v2026_prompster.json"
AUDIT_DIR = DIST / ".discovery" / "v2.1-audit"
DIFF_LOG = AUDIT_DIR / "v3_3_orphan_integration_log.md"

DRY_RUN = "--dry-run" in sys.argv

PARAM_RE = re.compile(r"\{\[([a-zA-Z_][a-zA-Z0-9_]*)\]\}")
WRAPPER_TOKENS = {"insumo_del_pipeline", "NIVEL_CONFIANZA_MINIMO"}

# ---------------------------------------------------------------------------
# Heurística A · mapeo por convención de nombre (lowercase).
# Cubre ~80% del volumen según diagnóstico.
# ---------------------------------------------------------------------------
TOKEN_PURPOSE_MAP = {
    # Top frecuencia
    "adjuntos": "lista de archivos/links que la IA debe leer PRIMERO antes de responder; cita su contenido cuando aplique",
    "contexto": "trasfondo del caso (decisiones previas, restricciones conocidas, datos accesorios); incorpóralo como marco antes de operar",
    "caso": "caso concreto sobre el que se aplica el método (descripción específica del problema y sus actores)",
    "objetivo": "objetivo medible que debe alcanzar el entregable (criterio explícito de éxito)",
    "audiencia": "perfil del destinatario del entregable; ajusta tono, profundidad y registro a este perfil",
    "tema": "tema central a desarrollar; toda la ejecución se orquesta alrededor de este eje",
    "restricciones": "restricciones operativas (tiempo, presupuesto, normativas, no-objetivos); respétalas como límites duros",
    "formato": "formato de salida deseado (markdown estructurado, tabla, párrafo corto, slide-deck, etc.); úsalo como template del entregable",
    "producto": "producto o servicio referenciado en el caso; integralo en cada bloque relevante",
    "material_base": "input documental sobre el que se trabaja (texto, draft, transcript, brief); úsalo como fuente primaria",
    "datos": "datos cuantitativos disponibles para sustentar afirmaciones; cítalos con etiqueta {ADJUNTO} o {EXTRAIDO_HILO}",
    "proyecto": "proyecto al que pertenece el caso; mantén su contexto como marco operativo",
    "herramienta": "herramienta específica a usar/configurar (ej. CRM, ERP, app); ajusta el output a sus capacidades",
    "herramientas": "set de herramientas disponibles; orquesta cuáles aplicar y cuándo",
    "problema": "problema raíz a resolver; resuélvelo con la metodología del prompt",
    "equipo": "equipo de trabajo (composición, roles); ajusta alcance y delegaciones a esta realidad",
    "rol": "rol asumido por el usuario en el caso (ej. PM, líder, comprador); ajusta perspectiva al rol",
    "duracion": "duración o plazo del trabajo; ajusta profundidad y alcance al tiempo disponible",
    "sector": "sector o industria del caso; ajusta vocabulario, regulaciones y benchmarks a este sector",
    "proceso": "proceso o flujo de referencia; respétalo como cadena de pasos esperada",
    "decision": "decisión a tomar; estructura el output como soporte para esa decisión",
    "empresa": "organización/empresa donde aplica el caso; ajusta cultura, escala y restricciones organizacionales",
    "agente": "agente o actor responsable de ejecutar; ajusta delegación y capacidad a este actor",
    "marca": "marca a la que pertenece el caso; respeta tono, voz y guías de marca",
    "tarea": "tarea concreta a ejecutar; resuélvela con la metodología del prompt",
    "volumen": "volumen de procesamiento esperado (cuántos items, cuántas iteraciones); ajusta granularidad",
    "concepto": "concepto central a explicar/explorar; profundiza con ejemplos y contraste",
    "persona": "persona específica involucrada (perfil, expectativas); ajusta comunicación a esa persona",
    "situacion": "situación inicial completa del caso; úsala como marco de partida",
    "estilo": "estilo o tono deseado (formal, conversacional, técnico, etc.); aplícalo en toda la pieza",
    # Continuaciones del top 50
    "publico": "público objetivo del entregable",
    "cliente": "cliente del proyecto; ajusta tono y prioridades a su perfil",
    "tipo": "tipo o variante del entregable (ajusta formato y profundidad)",
    "nombre": "nombre identificador del artefacto, recurso o entidad",
    "descripcion": "descripción detallada del input; léela completa antes de operar",
    "fecha": "fecha relevante (entrega, evento, cierre); úsala como ancla temporal",
    "lugar": "lugar físico o virtual relevante",
    "documento": "documento fuente; léelo y referéncialo con {ADJUNTO}",
    "documentos": "set de documentos fuente; intégralos como evidencia primaria",
    "mensaje": "mensaje principal a transmitir",
    "fondo": "fondo o background visual/temporal del caso",
    "imagen": "referencia visual usada como input",
    "video": "referencia audiovisual usada como input",
    "url": "enlace web a consultar; sigue su contenido como {WEB}",
    "lista": "lista de elementos a procesar; aplica el método sobre cada elemento",
    "items": "items individuales a recorrer en la ejecución",
    "elementos": "elementos discretos sobre los que opera el prompt",
    "datos_entrada": "datos crudos de entrada; valida su consistencia antes de operar",
    "schema": "esquema o estructura de datos esperada",
    "estructura": "estructura base del entregable; respétala literalmente",
    "trigger": "evento o condición que dispara el flujo",
    "disparador": "evento o condición que dispara el flujo automatizado",
    "aprobador": "rol o persona que valida/firma; agrega su revisión como gate explícito",
    "approver": "rol o persona que valida/firma",
    "accion": "acción específica a ejecutar; instánciala con verbo claro y entregable",
    "politica": "política o regla aplicable; cítala como restricción dura",
    "coleccion": "colección o set de datos de referencia",
    "logica": "lógica de negocio o regla a aplicar",
    "tipo_app": "tipo de aplicación (web, mobile, desktop, etc.); ajusta soluciones técnicas",
    "enfoque": "enfoque o ángulo de tratamiento del tema",
    "presupuesto": "presupuesto disponible; respétalo como restricción dura",
    "plazo": "plazo de cierre",
    "prioridad": "prioridad relativa entre opciones",
    "kpi": "KPI relevante; valida que el entregable lo mueva",
    "kpis": "set de KPIs relevantes; valida cada uno",
    "metricas": "métricas a reportar o seguir",
    "fuentes": "fuentes citables; referéncialas con etiqueta de procedencia",
    "fuentes_disponibles": "fuentes accesibles para citar; léelas y úsalas como evidencia primaria",
    "borrador": "borrador previo del entregable a iterar",
    "borrador_actual": "última versión del borrador en memoria viva",
    "version": "versión específica del entregable",
    "iteracion": "iteración del ciclo (1, 2, N) — ajusta profundidad",
    "criterio": "criterio explícito de aceptación",
    "criterios": "set de criterios de aceptación",
    "evidencia": "evidencia disponible para sustentar el entregable",
    "tipo_contenido": "tipo de contenido (post, video, slide, doc, etc.)",
    "longitud": "longitud objetivo del entregable",
    "idioma": "idioma del entregable",
    "tono": "tono comunicacional",
    "vacios_criticos": "vacíos críticos heredados; cierra cada uno o explicita por qué no se puede",
    "pendiente": "pendiente operativo a resolver",
    "verificar": "elemento marcado para verificación explícita",
    "reto_o_tarea": "reto o tarea concreta del usuario; resuélvelo con la metodología del prompt",
    "reto": "reto a abordar",
    "alcance": "alcance del entregable (in-scope vs out-of-scope)",
    "out_of_scope": "explícitamente fuera de alcance; no toques estos elementos",
    "deadline": "fecha límite",
    "prioridad_tarea": "prioridad de la tarea individual",
    "stakeholders": "stakeholders relevantes; ajusta comunicación e intereses",
    "stakeholder": "stakeholder principal",
    "riesgo": "riesgo identificado; documenta su mitigación",
    "riesgos": "riesgos identificados; mapea cada uno con mitigación",
    "supuesto": "supuesto operativo; márcalo con etiqueta {SUPUESTO}",
    "supuestos": "supuestos operativos; márcalos con etiqueta {SUPUESTO}",
    "hipotesis": "hipótesis falsable a probar",
    "experimento": "experimento concreto a ejecutar",
    "metodologia": "metodología de referencia (Lean, Agile, OKR, etc.); aplícala",
    "framework": "framework de referencia",
    "marco": "marco conceptual a aplicar",
    "industria": "industria o vertical del caso",
    "geografia": "geografía/región relevante",
    "region": "región geográfica",
    "country": "país relevante",
    "moneda": "moneda de referencia para cifras",
    "etiquetas": "etiquetas o tags a aplicar",
    "categorias": "categorías de clasificación",
    "categoria": "categoría a la que pertenece el caso",
    "tipo_tarea": "tipo de tarea",
    "complejidad": "nivel de complejidad",
    "objetivos": "objetivos múltiples a coordinar",
    "limitaciones": "limitaciones operativas",
    "input": "input crudo del usuario",
    "inputs": "inputs múltiples del usuario",
    "output": "output esperado del prompt",
    "outputs": "outputs esperados (múltiples)",
    "rubrica": "rúbrica de calidad para autoevaluación",
    "preguntas": "preguntas a responder o resolver",
    "respuestas": "respuestas esperadas",
    "topic": "topic o tema (inglés)",
    "title": "título a generar",
    "titulo": "título a generar",
    "subtitulo": "subtítulo a generar",
    "abstract": "abstract o resumen de cabecera",
    "resumen_caso": "resumen del caso original",
    "tamano": "tamaño del entregable o input",
    "tamaño": "tamaño del entregable",
    "limite": "límite operativo (palabras, tiempo, etc.)",
}

GENERIC_FALLBACK = "input específico del prompt — usá su valor literal en el bloque correspondiente del entregable, marcando con {AUTOCOMPLETADO} si lo inferís"

# ---------------------------------------------------------------------------
# Heurística B · derivar propósito desde el body del prompt
# ---------------------------------------------------------------------------
def derive_purpose_from_body(token: str, content: str) -> Optional[str]:
    """Si el nombre del token (sin braces) aparece como palabra en RESUMEN/SITUACIÓN/PEDIDO,
    extrae la oración que lo contiene y úsala como descripción."""
    # Extraer cuerpo descriptivo (RESUMEN + SITUACIÓN + PEDIDO + ABSTRACT)
    body_parts = []
    for marker, end_markers in [
        ("ABSTRACT:", ["RESUMEN:", "SPEC:"]),
        ("RESUMEN:", ["SPEC:"]),
        ("SITUACIÓN:", ["PEDIDO:"]),
        ("PEDIDO:", ["PROTOCOLO OBLIGATORIO:"]),
    ]:
        m = re.search(rf"\n{re.escape(marker)}\n(.+?)\n(?:{'|'.join(re.escape(em) for em in end_markers)})", content, re.DOTALL)
        if m:
            body_parts.append(m.group(1))
    body = " ".join(body_parts).lower()
    token_lower = token.lower()

    # Buscar oraciones que mencionan el token como palabra
    sentences = re.split(r"(?<=[.!?])\s+", body)
    matches = [s for s in sentences if re.search(rf"\b{re.escape(token_lower)}\b", s)]
    if not matches:
        return None
    # Tomar la oración más corta y específica (≤180 chars)
    matches.sort(key=lambda s: abs(len(s) - 100))
    chosen = matches[0].strip()
    if len(chosen) < 20 or len(chosen) > 220:
        return None
    # Limpiar y devolver como propósito
    chosen = re.sub(r"\s+", " ", chosen).strip().rstrip(".,;:!?")
    return f"derivado del prompt: \"{chosen}\""

def derive_purpose(token: str, content: str) -> str:
    """Cascada A → B → C."""
    # A: mapeo predefinido (case-insensitive)
    key = token.lower()
    if key in TOKEN_PURPOSE_MAP:
        return TOKEN_PURPOSE_MAP[key]
    # B: derivar del body
    body_derived = derive_purpose_from_body(token, content)
    if body_derived:
        return body_derived
    # C: fallback
    return GENERIC_FALLBACK

# ---------------------------------------------------------------------------
# Inserción del paso "USO EXPLÍCITO DE PARÁMETROS" en EJECUCIÓN
# ---------------------------------------------------------------------------
def integrate_orphans(content: str) -> Tuple[str, List[str]]:
    """Devuelve (nuevo_content, lista_de_tokens_integrados)."""
    # Detectar huérfanos
    m = re.search(r"\nINPUTS:\n(.+?)\n(?:ABSTRACT:|RESUMEN:)", content, re.DOTALL)
    if not m:
        return content, []
    declared = set(PARAM_RE.findall(m.group(1)))
    body = content.replace(m.group(1), "")
    used = set(PARAM_RE.findall(body))
    orphans = (declared - used) - {t for t in declared if t.lower() in {w.lower() for w in WRAPPER_TOKENS}}
    if not orphans:
        return content, []

    # Construir bloque de uso
    purposes = []
    for token in sorted(orphans):
        purpose = derive_purpose(token, content)
        purposes.append(f"   - `{{[{token}]}}`: {purpose}")
    purposes_block = "\n".join(purposes)

    # Localizar EJECUCIÓN
    exec_match = re.search(r"\nEJECUCIÓN:\n(.+?)\n\nSALIDA OBLIGATORIA:", content, re.DOTALL)
    if not exec_match:
        return content, []
    exec_text = exec_match.group(1)

    # Detectar el último número de paso para insertar el nuevo paso ANTES del INFERENCIA AMPLIFICADA
    # El paso INFERENCIA AMPLIFICADA es el último (lo añadió build_spec_v3_3)
    inferencia_match = re.search(r"\n(\d+)\.\s*INFERENCIA AMPLIFICADA", exec_text)
    if inferencia_match:
        # Renumerar: el actual último (INFERENCIA) sube 1, y el nuevo "USO EXPLÍCITO" toma su lugar
        old_num = int(inferencia_match.group(1))
        new_uso_num = old_num
        new_inferencia_num = old_num + 1

        new_uso_step = (
            f"\n{new_uso_num}. USO EXPLÍCITO DE PARÁMETROS DECLARADOS: integrá literal cada token de INPUTS en el cuerpo del entregable. "
            f"No los dejes huérfanos. Si un token no llega diligenciado, infiérelo desde hilo/memoria/adjuntos y márcalo con {{AUTOCOMPLETADO}}.\n"
            f"{purposes_block}"
        )

        # Reemplazar "{old_num}. INFERENCIA AMPLIFICADA" por "{new_uso_step}\n{new_inferencia_num}. INFERENCIA AMPLIFICADA"
        new_exec_text = re.sub(
            rf"\n{old_num}\.\s*INFERENCIA AMPLIFICADA",
            f"{new_uso_step}\n{new_inferencia_num}. INFERENCIA AMPLIFICADA",
            exec_text,
            count=1,
        )
    else:
        # No hay paso INFERENCIA AMPLIFICADA (raro post-v3.3) — añadir al final
        last_num_match = list(re.finditer(r"^\s*(\d+)\.", exec_text, re.MULTILINE))
        last_num = int(last_num_match[-1].group(1)) if last_num_match else 0
        new_num = last_num + 1
        new_uso_step = (
            f"\n{new_num}. USO EXPLÍCITO DE PARÁMETROS DECLARADOS: integrá literal cada token de INPUTS en el cuerpo del entregable. "
            f"No los dejes huérfanos. Si un token no llega diligenciado, infiérelo desde hilo/memoria/adjuntos y márcalo con {{AUTOCOMPLETADO}}.\n"
            f"{purposes_block}"
        )
        new_exec_text = exec_text.rstrip() + new_uso_step

    new_content = content[:exec_match.start(1)] + new_exec_text + content[exec_match.end(1):]
    return new_content, sorted(orphans)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"Loading {SRC} ...")
    with open(SRC) as f:
        d = json.load(f)
    prompts = d["prompts"] if isinstance(d, dict) and "prompts" in d else d

    print(f"Total prompts: {len(prompts)}")
    integrated = 0
    skipped = 0
    log_lines = ["# Orphan integration log v3.3 — 2026-04-26\n\n"]
    log_lines.append("Para cada prompt con tokens declarados-pero-no-usados, se insertó un paso explícito en EJECUCIÓN que integra cada token con su propósito derivado.\n\n")
    log_lines.append("| Prompt ID | Tokens integrados | Heurística |\n|---|---|---|\n")

    purpose_source_counter = Counter()

    for p in prompts:
        new_content, orphs_integrated = integrate_orphans(p["content"])
        if orphs_integrated:
            # Log
            sources = []
            for tok in orphs_integrated:
                if tok.lower() in TOKEN_PURPOSE_MAP:
                    sources.append("A")
                    purpose_source_counter["A_map"] += 1
                else:
                    body_derived = derive_purpose_from_body(tok, p["content"])
                    if body_derived:
                        sources.append("B")
                        purpose_source_counter["B_body"] += 1
                    else:
                        sources.append("C")
                        purpose_source_counter["C_fallback"] += 1
            tok_str = ", ".join(f"`{t}`({s})" for t, s in zip(orphs_integrated, sources))
            log_lines.append(f"| `/{p['id']}` | {tok_str} | {','.join(set(sources))} |\n")

            if not DRY_RUN:
                p["content"] = new_content
            integrated += 1
        else:
            skipped += 1

    print(f"Integrated: {integrated}")
    print(f"Skipped (no orphans): {skipped}")
    print(f"Purpose sources used:")
    for s, n in purpose_source_counter.most_common():
        print(f"  {s}: {n}")

    if DRY_RUN:
        print("DRY RUN — no files written")
        return

    # Recompute paramCount (no cambia · INPUTS no se toca, sólo EJECUCIÓN crece)
    print("\nWriting files...")
    with open(OUT, "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    with open(OUT_MIN, "w") as f:
        json.dump(d, f, ensure_ascii=False, separators=(",", ":"))
    biblioteca universal de prompts = {p["id"]: p["content"] for p in prompts}
    with open(OUT_PROMPSTER, "w") as f:
        json.dump(biblioteca universal de prompts, f, ensure_ascii=False, indent=2)

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    DIFF_LOG.write_text("".join(log_lines), encoding="utf-8")
    print(f"\n📄 Log → {DIFF_LOG}")

    for fp in [OUT, OUT_MIN, OUT_PROMPSTER]:
        sz = fp.stat().st_size / 1024 / 1024
        print(f"  {fp.name}: {sz:.2f} MB")

if __name__ == "__main__":
    main()

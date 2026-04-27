"""
apply_v3_4_per_prompt.py — aplica SPEC v3.4 ENTRUSTED+ a un set de prompts (whitelist).

Para cada prompt del whitelist:
  1. Lee `content` v3.3 actual.
  2. Determina categoría ENTRUSTED+ (tabla precomputada por id).
  3. Inyecta DEFINITION OF DONE personalizado (plantilla por categoría · personalizado).
  4. Inyecta CRITERIOS DE ACEPTACIÓN OBSERVABLES (5 por prompt).
  5. Inyecta EDGE CASES (3 por prompt).
  6. Inyecta 3 nuevas cláusulas paramétricas (EVIDENCIA_CITAS, NO_ALUCINACIÓN_EXPLÍCITA, INFERENCIA_VS_HECHO).
  7. Calcula score ENTRUSTED+ 8 ejes.
  8. Loguea diagnóstico forense + score.

Uso:
    python3 apply_v3_4_per_prompt.py --batch pipeline_0_6
    python3 apply_v3_4_per_prompt.py --ids 0 1 2 3 4 5 6
    python3 apply_v3_4_per_prompt.py --batch pipeline_0_6 --dry-run
"""
import json, re, sys, argparse, statistics
from pathlib import Path
from datetime import datetime

DIST = Path(__file__).resolve().parent.parent.parent
SRC = DIST / "prompts_universales_v3000.json"
AUDIT_DIR = DIST / ".discovery" / "v2.1-audit"
LOG_FORENSIC = AUDIT_DIR / "v3_4_per_prompt_log.md"
LOG_BATCH_TPL = AUDIT_DIR / "13.5{suffix}-pilot-{batch_name}-v3-4.md"

# ---------------------------------------------------------------------------
# Mapeo categoría ENTRUSTED+ por id (whitelist primer batch)
# ---------------------------------------------------------------------------
CATEGORY_MAP = {
    # Pipeline P.I.V.O.T.E. — categorías ENTRUSTED+
    "0": "agente",          # PRIMING — orquesta el contexto
    "1": "análisis",        # ENTENDER — descompone problema
    "2": "procedimiento",   # DEFINIR — construye SPEC paso-a-paso
    "3": "procedimiento",   # PLANIFICAR — construye plan
    "4": "generación",      # EJECUTAR — produce draft
    "5": "procedimiento",   # ROBUSTECER — endurece con evidencia
    "6": "procedimiento",   # SIMPLIFICAR — destila
    "7": "análisis",        # VALIDAR — audita
    "8": "generación",      # ENTREGAR — adapta formato
    "9": "procedimiento",   # CRISTALIZAR — plantilla
    # Frameworks clásicos — todos categoría estrategia
    "v11_artefacto_matriz_swot_completa": "estrategia",
    "v11_artefacto_5_fuerzas_porter": "estrategia",
    "v11_artefacto_lean_canvas": "estrategia",
    "v11_artefacto_okr": "estrategia",
    # Aceleradores 1-palabra — macros operativos de continuación/transformación
    "a": "procedimiento",        # Aprobado · proceder · macro de continuación
    "e": "procedimiento",        # Excelencia · activa bucle de validación
    "s": "generación",           # Sintetiza · combina opciones en una unificada
    "simplifica": "procedimiento", # Destilar · reduce a esencia
    "documenta": "generación",   # Documentar · produce artefacto doc
    "estructura": "procedimiento", # Estructurar · organiza con jerarquía
    "defiende": "generación",    # Argumentar · construye defensa
}

BATCHES = {
    "pipeline_0_6": ["0", "1", "2", "3", "4", "5", "6"],
    "pipeline_7_9_plus_4": [
        "7", "8", "9",
        "v11_artefacto_matriz_swot_completa",
        "v11_artefacto_5_fuerzas_porter",
        "v11_artefacto_lean_canvas",
        "v11_artefacto_okr",
    ],
    # Aceleradores 1-palabra · alta reutilización (macros operativos)
    "aceleradores_1": [
        "a",            # Aprobado · proceder
        "e",            # Excelencia (bucle 10/10)
        "s",            # Sintetiza
        "simplifica",   # Destilar
        "documenta",    # Documentar
        "estructura",   # Estructurar
        "defiende",     # Argumentar
    ],
}

# ---------------------------------------------------------------------------
# Plantillas DoD por categoría (operativas)
# ---------------------------------------------------------------------------
DOD_TEMPLATES = {
    "agente": {
        "dod": (
            "Produce un plan ejecutable con (a) acción concreta por paso · (b) input/output declarado · "
            "(c) precondición + postcondición observables · (d) handlers de error para los 3 fallos más probables · "
            "(e) estado memorizable entre pasos. Plan ejecutable sin reabrir el contexto."
        ),
        "criterios": [
            "Cada paso tiene precondición y postcondición verificables.",
            "≥3 handlers de error declarados con criterio de aborto.",
            "Estado entre pasos especificado (qué guardar para paso N+1).",
            "Cada input declarado de INPUTS se usa literal o etiquetado en al menos 1 paso.",
            "Bloque INSIGHTS_PROACTIVOS con riesgos del flujo + paths alternativos + métricas de éxito.",
        ],
        "edges": [
            "Step bloqueado por dependencia externa → declara gap + plan B + criterio de aborto.",
            "Output del paso N no cumple precondición de N+1 → loop de corrección con límite + abort criterio.",
            "Cambio de contexto entre invocaciones → mecanismo de resumen para reanudar (memoria viva).",
        ],
    },
    "análisis": {
        "dod": (
            "Produce análisis estructurado con (a) hechos extraídos con etiqueta de procedencia · "
            "(b) hallazgos numerados con confianza 0.0-1.0 · (c) recomendación priorizada con criterio operativo · "
            "(d) sección 'Lo que NO se sabe' con {VACIO_CRITICO}s y propuesta de cierre."
        ),
        "criterios": [
            "Cada hallazgo lleva ≥1 etiqueta de procedencia trazable ({ADJUNTO|EXTRAIDO_HILO|WEB|CONOCIMIENTO|INFERENCIA}).",
            "Recomendación final con criterio explícito de priorización (impacto/esfuerzo/riesgo).",
            "Lista de {VACIO_CRITICO}s con propuesta concreta de cómo cerrarlos.",
            "Cada input de INPUTS se incorpora en el análisis o se marca como autocompletado.",
            "Bloque INSIGHTS_PROACTIVOS con riesgos no obvios + oportunidades cercanas.",
        ],
        "edges": [
            "Material insuficiente → análisis parcial + lista de gaps + qué dato cierra cada gap.",
            "Material contradictorio → enumera conflictos + lado más sustentado + dato decisor faltante.",
            "Material PII detectado → anonimiza antes de analizar; declara qué se redactó.",
        ],
    },
    "procedimiento": {
        "dod": (
            "Produce plantilla / checklist / receta paso-a-paso con (a) precondición de inicio · "
            "(b) pasos numerados con verbo accionable + entregable observable · (c) validación intermedia · "
            "(d) postcondición de cierre · (e) plantilla reutilizable en casos similares del dominio."
        ),
        "criterios": [
            "Cada paso tiene verbo en imperativo + entregable verificable.",
            "Precondición y postcondición observables (no opinables).",
            "Validación intermedia con criterio cuantitativo o checkable.",
            "Cada input de INPUTS se usa en al menos 1 paso de la EJECUCIÓN.",
            "Bloque INSIGHTS_PROACTIVOS con anti-patrones, automatización futura, métricas.",
        ],
        "edges": [
            "Paso bloqueado por dato faltante → marca {VACIO_CRITICO} + skip condicional + recuperación.",
            "Caso fuera del scope del procedimiento → declara excepción + fallback manual + log para refinar.",
            "Postcondición no se cumple → diagnóstico + corrección + retry con criterio de aborto.",
        ],
    },
    "generación": {
        "dod": (
            "Produce el artefacto solicitado con (a) longitud y formato dentro del rango ±10% · "
            "(b) tono coherente con audiencia · (c) cada input de INPUTS utilizado o marcado {POR_CONFIRMAR} · "
            "(d) cero invenciones de citas, datos específicos o nombres reales sin marcar."
        ),
        "criterios": [
            "Longitud final dentro del rango ±10% del pedido.",
            "Tono verificable (registro, tutear/usted, jerga del dominio) coherente con audiencia.",
            "Cada input de INPUTS aparece literal o etiquetado como autocompletado en el output.",
            "Cero claims factuales no etiquetados (números, fechas, citas).",
            "Bloque INSIGHTS_PROACTIVOS con 1-3 variantes alternativas o ángulos no pedidos.",
        ],
        "edges": [
            "Tono pedido ≠ audiencia natural → entrega versión + alerta del conflicto + versión recomendada.",
            "Datos inventables (estadísticas, citas) → marca {POR_CONFIRMAR} + placeholder + sugerencia de fuente.",
            "Restricción de longitud impide profundidad → entrega versión + nota de qué se omitió + dónde recuperarlo.",
        ],
    },
}

# Categorías restantes con plantillas mínimas (se completarán en batches específicos)
DOD_TEMPLATES.update({
    "extracción": {
        "dod": "Produce estructura de datos (tabla/JSON/lista) con campos exactos, valores con etiqueta de procedencia, celdas faltantes marcadas {VACIO_CRITICO}, reporte de cobertura cuantitativo.",
        "criterios": ["Estructura final con mismos campos y orden.", "Cero celdas inferidas presentadas como hechos.", "Reporte de cobertura X/Y celdas + N% gap.", "Trazabilidad celda→fuente.", "Bloque INSIGHTS_PROACTIVOS con duplicados, anomalías, patrones."],
        "edges": ["Material parcial → estructura + celdas vacías marcadas + plan de completado.", "Datos contradictorios → reporta conflicto + valor más sustentado.", "Schema ambiguo → propone schema + valida con usuario."],
    },
    "automatización": {
        "dod": "Produce blueprint operativo (flow/script/config) con trigger declarado, acciones secuenciales con conectores específicos, variables tipadas, manejo de errores con notificación, gobernanza (logs/reintentos/escalación), prueba mínima.",
        "criterios": ["Trigger explícito con condiciones.", "Cada acción con conector específico.", "Variables con tipo y default.", "≥3 casos de error con handler.", "Bloque INSIGHTS_PROACTIVOS con cuellos de botella + métricas a monitorear."],
        "edges": ["Conector no autenticado → declara dependencia + fallback + alerta.", "Throttling/rate limit → reintentos exponenciales + dead-letter queue.", "Datos inválidos → validación antes de cada acción + notificación."],
    },
    "investigación": {
        "dod": "Produce reporte de investigación con preguntas guía explícitas, hallazgos con ≥3 fuentes citables por crítico, síntesis ejecutiva, brechas de conocimiento + siguiente paso, confianza por hallazgo.",
        "criterios": ["≥3 fuentes por hallazgo crítico ({WEB|ADJUNTO|CONOCIMIENTO}).", "Síntesis con confianza 0.0-1.0.", "Lista de brechas + cómo cerrarlas.", "Cero claims sin fuente o etiqueta.", "Bloque INSIGHTS_PROACTIVOS con preguntas no exploradas + hipótesis alternativas."],
        "edges": ["Fuentes contradictorias → conflicto + lado más sustentado + dato decisor.", "Tópico fuera del knowledge cutoff → declara + sugiere `ORQUESTACIÓN_RECURSOS: web=on`.", "Material insuficiente → brecha + fuentes alternativas."],
    },
    "estrategia": {
        "dod": "Produce análisis estratégico con framework aplicado completo (SWOT/Porter/BCG/etc.), datos del caso integrados con etiqueta, recomendación accionable con horizonte temporal, priorización con criterio cuantificado, riesgos + mitigaciones.",
        "criterios": ["Framework aplicado completo (no parcial).", "Datos del caso integrados con etiqueta en cada celda/dimensión.", "Recomendación con horizonte temporal explícito.", "Priorización cuantitativa (impacto/esfuerzo/riesgo).", "Bloque INSIGHTS_PROACTIVOS con suposiciones cuestionables + alternativas no consideradas."],
        "edges": ["Datos insuficientes para ≥1 dimensión → {VACIO_CRITICO} + cómo obtenerlo.", "Framework no encaja al 100% → adapta con justificación + alerta.", "Recomendación con riesgo alto → escenario + mitigación + plan de salida."],
    },
    "multimedia": {
        "dod": "Produce especificación visual/audiovisual ejecutable con parámetros técnicos completos, composición descrita (sujeto/fondo/iluminación/cámara), estilo declarado con referencias, brief de copy si aplica.",
        "criterios": ["Parámetros técnicos completos para herramienta destino.", "Composición ≥4 elementos visuales.", "Estilo declarado con atributos concretos.", "Cero ambigüedades sobre encuadre y aspect ratio.", "Bloque INSIGHTS_PROACTIVOS con variantes de mood + alternativas estilísticas."],
        "edges": ["Herramienta destino no especificada → versión genérica + parámetros típicos + alerta.", "Restricciones de herramienta → marca + sugiere reencuadre.", "Estilo conflictivo con marca → alerta + propone reconciliación."],
    },
})

# ---------------------------------------------------------------------------
# 3 cláusulas nuevas v3.4 (hibridar con las 9 v3.3)
# ---------------------------------------------------------------------------
NEW_CLAUSES_V34 = """
[EVIDENCIA_CITAS · params: obligatorio=on · formato=inline-tag · fuentes_minimas=1 · invento=prohibido]
Default: TODA afirmación factual lleva etiqueta de procedencia inline ({ADJUNTO} {WEB} {EXTRAIDO_HILO} {CONOCIMIENTO} {INFERENCIA}). Cero citas inventadas; si no hay fuente, marcar {POR_CONFIRMAR} con el placeholder.
Override al vuelo: `EVIDENCIA_CITAS: fuentes_minimas=3` para tareas de investigación; `EVIDENCIA_CITAS: obligatorio=off` solo para macros de continuación.

[NO_ALUCINACIÓN_EXPLÍCITA · params: prohibición=alta · marcar_dudas=on · declarar_brechas=obligatorio]
Default: nunca afirmas acceso a memoria, historial, adjuntos o herramientas que no estén disponibles. Si tu afirmación requiere material no presente, declara {VACIO_CRITICO} con el dato faltante. Si tu inferencia tiene confianza < 0.85, separa con {INFERENCIA} (no afirmar como hecho). Cero claims sobre material no accesible.
Override: `NO_ALUCINACIÓN_EXPLÍCITA: prohibición=media` para outputs creativos donde se permite ficción explícita.

[INFERENCIA_VS_HECHO · params: separar=obligatorio · etiqueta_inferencia=on · confianza_visible=on]
Default: cada output etiqueta cada bloque como FACT (con fuente trazable) o INFERENCE (con confianza explícita 0.0-1.0 + base inferencial declarada). Cero mezcla. La sección 'Lo que sé' lista FACTs; la sección 'Lo que infiero' lista INFERENCEs con confianza.
Override: `INFERENCIA_VS_HECHO: separar=inline` para mezclar inline con marcadores en lugar de secciones separadas."""

# ---------------------------------------------------------------------------
# Inyección al SPEC v3.3
# ---------------------------------------------------------------------------
def get_dod_block(prompt: dict, category: str) -> str:
    template = DOD_TEMPLATES.get(category, DOD_TEMPLATES["procedimiento"])
    label = prompt.get("label_title", prompt["id"])

    dod = template["dod"]
    criterios = "\n".join(f"- {c}" for c in template["criterios"])
    edges = "\n".join(f"- {e}" for e in template["edges"])

    block = (
        f"DEFINITION OF DONE (categoría ENTRUSTED+ = {category}):\n"
        f"{dod} Personalizado al output de \"{label}\".\n\n"
        f"CRITERIOS DE ACEPTACIÓN OBSERVABLES:\n"
        f"{criterios}\n\n"
        f"EDGE CASES:\n"
        f"{edges}"
    )
    return block

def inject_v3_4_blocks(content: str, dod_block: str) -> str:
    """Inserta DoD + Criterios + Edge cases ANTES de '— CLÁUSULAS TRANSVERSALES' y agrega 3 cláusulas nuevas DENTRO del bloque cláusulas."""
    if "DEFINITION OF DONE" in content and "CRITERIOS DE ACEPTACIÓN OBSERVABLES" in content:
        # Ya aplicado v3.4 — saltar
        return content

    # Localizar cláusulas
    clausulas_marker = "— CLÁUSULAS TRANSVERSALES"
    idx = content.find(clausulas_marker)
    if idx < 0:
        return content + "\n\n" + dod_block

    before_clausulas = content[:idx].rstrip()
    clausulas_block = content[idx:]

    # Insertar 3 cláusulas nuevas al final del bloque cláusulas (antes del newline final si lo hay)
    if "[EVIDENCIA_CITAS" not in clausulas_block:
        clausulas_block = clausulas_block.rstrip() + NEW_CLAUSES_V34 + "\n"

    return before_clausulas + "\n\n" + dod_block + "\n\n" + clausulas_block

# ---------------------------------------------------------------------------
# Score ENTRUSTED+ 8 ejes (heurístico)
# ---------------------------------------------------------------------------
def score_entrusted(content: str, prompt: dict) -> dict:
    scores = {}

    # E · Explicitud — chequea presencia de bloques claves
    explicitud = 60
    if "TÍTULO:" in content: explicitud += 5
    if "ABSTRACT:" in content: explicitud += 5
    if "RESUMEN:" in content: explicitud += 5
    if "SITUACIÓN:" in content: explicitud += 5
    if "PEDIDO:" in content: explicitud += 5
    if "EJECUCIÓN:" in content and re.search(r"\n\d+\.", content): explicitud += 5
    if "DEFINITION OF DONE" in content: explicitud += 5
    if "CRITERIOS DE ACEPTACIÓN" in content: explicitud += 5
    scores["E_explicitud"] = min(100, explicitud)

    # N · No-alucinación — etiquetas + protocolo + no-alucinación cláusula
    noalu = 50
    if "{SUPUESTO}" in content and "{INFERENCIA}" in content and "{VACIO_CRITICO}" in content: noalu += 20
    if "PROTOCOLO" in content or "PROTOCOLO_OBLIGATORIO" in content: noalu += 10
    if "[NO_ALUCINACIÓN_EXPLÍCITA" in content: noalu += 15
    if "[EVIDENCIA_CITAS" in content: noalu += 5
    scores["N_no_alucinacion"] = min(100, noalu)

    # T · Transferibilidad — auto-contención + standalone
    transfer = 70
    if "[AUTO-CONTENCIÓN" in content or "AUTO-CONTENCIÓN" in content or "AUTO_CONTENCIÓN" in content: transfer += 15
    if "standalone" in content.lower(): transfer += 10
    if "fallback" in content.lower(): transfer += 5
    scores["T_transferibilidad"] = min(100, transfer)

    # R · Rol — específico vs genérico
    rol = 60
    rol_match = re.search(r"\nROL:\s*\n([^\n]+)", content)
    if rol_match:
        rol_text = rol_match.group(1).lower()
        if "experto general" in rol_text or "asistente" in rol_text: rol += 0
        elif "senior" in rol_text or "especialista" in rol_text or "experto" in rol_text: rol += 25
        if "orquestador" in rol_text or "metacognitivo" in rol_text or "calibración" in rol_text: rol += 10
        if len(rol_text) > 100: rol += 5
    scores["R_rol"] = min(100, rol)

    # U · Uso de inputs — tokens declarados aparecen en EJECUCIÓN o CRITERIO
    uso = 100
    inputs_m = re.search(r"\nINPUTS:\n(.+?)\n(?:ABSTRACT:|RESUMEN:)", content, re.DOTALL)
    if inputs_m:
        declared = set(re.findall(r"\{\[([a-zA-Z_][a-zA-Z0-9_]*)\]\}", inputs_m.group(1)))
        body = content.replace(inputs_m.group(1), "")
        used = set(re.findall(r"\{\[([a-zA-Z_][a-zA-Z0-9_]*)\]\}", body))
        WRAPPER = {"insumo_del_pipeline", "NIVEL_CONFIANZA_MINIMO"}
        orphans = (declared - used) - WRAPPER
        if orphans: uso = max(0, 100 - 20 * len(orphans))
    scores["U_uso_inputs"] = uso

    # S · Structure — 26 markers v3.3 + nuevos v3.4
    structure = 60
    markers_v33 = ["PROTOCOLO OBLIGATORIO", "SISTEMA DE ETIQUETAS", "DECOMPOSE", "REGLA DE CONFIANZA",
                   "SALIDA OBLIGATORIA", "📊 METADATA DE RAZONAMIENTO", "[BUCLE DE EXCELENCIA",
                   "[ORQUESTACIÓN DE RECURSOS", "[INFERENCIA AMPLIFICADA", "[INSIGHTS PROACTIVOS",
                   "[AUTO-CONTENCIÓN", "[VACÍOS CRÍTICOS", "[PRIVACIDAD · PII",
                   "[METADATA DE RAZONAMIENTO", "[SINERGIA · PIPELINE"]
    structure += sum(2 for m in markers_v33 if m in content)
    if "DEFINITION OF DONE" in content: structure += 4
    if "CRITERIOS DE ACEPTACIÓN" in content: structure += 4
    if "EDGE CASES" in content: structure += 4
    if "[EVIDENCIA_CITAS" in content: structure += 3
    if "[NO_ALUCINACIÓN_EXPLÍCITA" in content: structure += 3
    if "[INFERENCIA_VS_HECHO" in content: structure += 3
    scores["S_structure"] = min(100, structure)

    # T · Tarea-fit — DoD coherente con categoría
    tareafit = 70
    if "DEFINITION OF DONE" in content and "categoría ENTRUSTED+" in content: tareafit += 20
    if "EDGE CASES" in content: tareafit += 10
    scores["T_tarea_fit"] = min(100, tareafit)

    # E · Edge cases — ≥3 casos
    edgecases = 0
    edge_block_m = re.search(r"EDGE CASES:\n(.+?)(?=\n\n|\n—|\Z)", content, re.DOTALL)
    if edge_block_m:
        n_edges = sum(1 for l in edge_block_m.group(1).split("\n") if l.strip().startswith("-"))
        edgecases = min(100, n_edges * 33)
    scores["E_edge_cases"] = edgecases

    # Score agregado promedio
    scores["AVG"] = round(statistics.mean(scores.values()), 1)
    return scores

# ---------------------------------------------------------------------------
# Diagnóstico forense por prompt
# ---------------------------------------------------------------------------
def diagnose_prompt(content: str, prompt: dict) -> list:
    """Detecta gaps específicos del prompt."""
    issues = []

    if "DEFINITION OF DONE" not in content:
        issues.append("v3.3 sin DoD explícito · v3.4 inyecta DoD por categoría")
    if "CRITERIOS DE ACEPTACIÓN OBSERVABLES" not in content:
        issues.append("Criterios actuales son CRITERIO DE ÉXITO genérico · v3.4 los hace observables")
    if "EDGE CASES" not in content:
        issues.append("Sin edge cases enumerados · v3.4 agrega 3 casos límite con manejo")
    if "[EVIDENCIA_CITAS" not in content:
        issues.append("Cláusula EVIDENCIA_CITAS ausente · v3.4 la agrega")
    if "[NO_ALUCINACIÓN_EXPLÍCITA" not in content:
        issues.append("Cláusula NO_ALUCINACIÓN_EXPLÍCITA ausente · v3.4 la agrega")
    if "[INFERENCIA_VS_HECHO" not in content:
        issues.append("Cláusula INFERENCIA_VS_HECHO ausente · v3.4 la agrega")

    rol_match = re.search(r"\nROL:\s*\n([^\n]+)", content)
    if rol_match:
        rol_text = rol_match.group(1).lower()
        if "general" in rol_text and "senior" not in rol_text:
            issues.append("ROL genérico · revisión recomendada")

    inputs_m = re.search(r"\nINPUTS:\n(.+?)\n(?:ABSTRACT:|RESUMEN:)", content, re.DOTALL)
    if inputs_m:
        declared = set(re.findall(r"\{\[([a-zA-Z_][a-zA-Z0-9_]*)\]\}", inputs_m.group(1)))
        body = content.replace(inputs_m.group(1), "")
        used = set(re.findall(r"\{\[([a-zA-Z_][a-zA-Z0-9_]*)\]\}", body))
        WRAPPER = {"insumo_del_pipeline", "NIVEL_CONFIANZA_MINIMO"}
        orphans = (declared - used) - WRAPPER
        if orphans:
            issues.append(f"Tokens huérfanos detectados: {sorted(orphans)}")

    return issues

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", choices=list(BATCHES.keys()), help="Nombre del batch predefinido")
    parser.add_argument("--ids", nargs="+", help="IDs específicos a procesar")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.batch:
        target_ids = BATCHES[args.batch]
        batch_name = args.batch
    elif args.ids:
        target_ids = args.ids
        batch_name = "custom"
    else:
        print("Error: provide --batch or --ids")
        sys.exit(1)

    print(f"Loading {SRC} ...")
    with open(SRC) as f:
        d = json.load(f)
    prompts = d["prompts"] if isinstance(d, dict) and "prompts" in d else d
    by_id = {p["id"]: p for p in prompts}

    # Procesar
    batch_log = [f"# {batch_name} · v3.4 ENTRUSTED+ pilot · {datetime.now().date()}\n\n"]
    summary_table = ["| ID | Categoría | E | N | T | R | U | S | T-fit | EC | **AVG** | Estado |\n",
                     "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|\n"]
    detailed_log = []

    score_avg_before_after = {}

    for tid in target_ids:
        if tid not in by_id:
            print(f"  MISS /{tid}")
            continue
        p = by_id[tid]
        content_before = p["content"]
        category = CATEGORY_MAP.get(tid, "procedimiento")

        # 1. Score before
        scores_before = score_entrusted(content_before, p)
        # 2. Diagnose
        issues = diagnose_prompt(content_before, p)
        # 3. Apply v3.4 blocks
        dod_block = get_dod_block(p, category)
        new_content = inject_v3_4_blocks(content_before, dod_block)
        # 4. Score after
        scores_after = score_entrusted(new_content, p)

        score_avg_before_after[tid] = (scores_before["AVG"], scores_after["AVG"])

        if not args.dry_run:
            p["content"] = new_content
            p["novelty_class"] = "spec_v3_4_entrusted"
            p["quality_score"] = scores_after["AVG"] / 100.0

        # Log
        status = "✅ MEJORADO" if scores_after["AVG"] > scores_before["AVG"] else "= sin cambio"
        summary_table.append(
            f"| /{tid} | {category} | "
            f"{scores_after['E_explicitud']} | {scores_after['N_no_alucinacion']} | "
            f"{scores_after['T_transferibilidad']} | {scores_after['R_rol']} | "
            f"{scores_after['U_uso_inputs']} | {scores_after['S_structure']} | "
            f"{scores_after['T_tarea_fit']} | {scores_after['E_edge_cases']} | "
            f"**{scores_after['AVG']}** | {status} |\n"
        )
        detailed_log.append({
            "id": tid,
            "category": category,
            "label": p.get("label_title", ""),
            "scores_before": scores_before,
            "scores_after": scores_after,
            "issues_diagnosed": issues,
        })

    # Escribir batch report
    batch_log.append("## Resumen agregado · score ENTRUSTED+ por prompt\n\n")
    batch_log.extend(summary_table)
    batch_log.append("\n## Diagnóstico forense por prompt\n\n")
    for entry in detailed_log:
        batch_log.append(f"### /{entry['id']} · {entry['category']} · \"{entry['label']}\"\n\n")
        before = entry['scores_before']
        after = entry['scores_after']
        batch_log.append(f"**Score before v3.4:** {before['AVG']}/100\n")
        batch_log.append(f"**Score after v3.4:** {after['AVG']}/100  ⬆ +{round(after['AVG']-before['AVG'],1)}\n\n")
        if entry['issues_diagnosed']:
            batch_log.append("**Diagnóstico forense (gaps detectados antes de v3.4):**\n")
            for i in entry['issues_diagnosed']:
                batch_log.append(f"- {i}\n")
            batch_log.append("\n")
        batch_log.append(f"**Detalle 8 ejes:**\n")
        batch_log.append(f"| Eje | Before | After | Δ |\n|---|---:|---:|---:|\n")
        for k in ['E_explicitud','N_no_alucinacion','T_transferibilidad','R_rol','U_uso_inputs','S_structure','T_tarea_fit','E_edge_cases']:
            delta = after[k] - before[k]
            sign = "+" if delta >= 0 else ""
            batch_log.append(f"| {k} | {before[k]} | {after[k]} | {sign}{delta} |\n")
        batch_log.append("\n")

    # Resumen agregado
    avg_before = round(statistics.mean(s[0] for s in score_avg_before_after.values()), 1)
    avg_after = round(statistics.mean(s[1] for s in score_avg_before_after.values()), 1)
    batch_log.append(f"\n## Promedio del batch · ENTRUSTED+\n\n")
    batch_log.append(f"- **Score promedio antes v3.4:** {avg_before}/100\n")
    batch_log.append(f"- **Score promedio después v3.4:** {avg_after}/100  ⬆ +{round(avg_after-avg_before,1)}\n")
    batch_log.append(f"- **Threshold v3.4 (≥92/100 EXCELLENT):** {'✅ alcanzado' if avg_after >= 92 else '⚠️ debajo del threshold'}\n")

    if args.dry_run:
        print("DRY RUN — no JSON written")
    else:
        # Update v3000.json
        print(f"\nWriting {SRC} ...")
        with open(SRC, "w") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

        # Update min.json
        min_path = DIST / "prompts_universales_v3000.min.json"
        with open(min_path, "w") as f:
            json.dump(d, f, ensure_ascii=False, separators=(",", ":"))

        sz = SRC.stat().st_size / 1024 / 1024
        print(f"  prompts_universales_v3000.json: {sz:.2f} MB")

    # Log batch report
    batch_path = AUDIT_DIR / f"13.5{['a','b','c','d','e','f','g','h','i'][0 if 'pipeline_0_6' in batch_name else 1]}-pilot-{batch_name}-v3-4.md"
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    batch_path.write_text("".join(batch_log), encoding="utf-8")
    print(f"\n📄 Batch report → {batch_path}")

    # Console summary
    print("\n" + "="*70)
    print(f"BATCH: {batch_name} · {len(target_ids)} prompts")
    print(f"  Avg ENTRUSTED+ before: {avg_before}/100")
    print(f"  Avg ENTRUSTED+ after:  {avg_after}/100 (+{round(avg_after-avg_before,1)})")
    if avg_after >= 92:
        print(f"  ✅ Threshold v3.4 EXCELLENT (≥92) alcanzado")
    else:
        print(f"  ⚠️ Threshold debajo de 92 — review needed")
    print("="*70)

if __name__ == "__main__":
    main()

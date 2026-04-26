"""
build_spec_v3_3_massive.py — refunde los 2026 prompts del v3000.json al estándar SPEC v3.3
(arquitectura limpia v3000 × profundidad metacognitiva v1492 + 4 mejoras pedidas por Javier).

Aprobado en plan §12 · 2026-04-26.

Uso:
    python3 build_spec_v3_3_massive.py            # transforma + escribe + sample
    python3 build_spec_v3_3_massive.py --check    # solo valida sin escribir

Salida:
    prompts_universales_v3000.json (rich, indent 2) — actualizado in-place
    prompts_universales_v3000.min.json (minificado)
    prompts_universales_v2026_prompster.json ({id: content})
    .discovery/v2.1-audit/sample_50_v3_3.md (50 prompts random para QA)
    .discovery/v2.1-audit/v3_3_validation_report.md (15 checks por prompt)
"""
import json, os, re, sys, random, hashlib
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent.parent  # → dist/
SRC = DIST / "prompts_universales_v3000.json"
OUT_V3000 = DIST / "prompts_universales_v3000.json"
OUT_MIN = DIST / "prompts_universales_v3000.min.json"
OUT_PROMPSTER = DIST / "prompts_universales_v2026_prompster.json"
AUDIT_DIR = DIST / ".discovery" / "v2.1-audit"
SAMPLE_OUT = AUDIT_DIR / "sample_50_v3_3.md"
VALIDATION_OUT = AUDIT_DIR / "v3_3_validation_report.md"

CHECK_ONLY = "--check" in sys.argv

# ===========================================================================
# Bloques estables (idénticos en los 2026 prompts)
# ===========================================================================

PROTOCOLO = """PROTOCOLO OBLIGATORIO:
1. Antes de responder, revisa EXPLÍCITAMENTE: hilo previo, memoria disponible, información conocida del usuario, adjuntos provistos y contexto recuperable del trabajo actual.
2. Declara qué capitalizaste usando etiquetas de procedencia y confianza; no asumas que el usuario sabe qué recuperaste.
3. Slots vacíos: completa con {EXTRAIDO_HILO}, {MEMORIA}, {ADJUNTO}, {CONOCIMIENTO}, {WEB}, {INFERENCIA} antes de pedir al usuario.
4. Si falta algo no crítico, continúa con default; si crítico, marca {VACIO_CRITICO} y pide solo eso.
5. Mantén memoria viva del pipeline P.I.V.O.T.E. (cuando aplique) con problema, objetivo, restricciones, supuestos, pendientes, riesgos, próximo checkpoint.
6. No presentes una ejecución como sólida si no puedes defender procedencia y confianza ≥ 0.95."""

ETIQUETAS = """SISTEMA DE ETIQUETAS DE PROCEDENCIA (obligatorio en outputs):
- {SUPUESTO}: hipótesis provisional sin evidencia suficiente.
- {INFERENCIA}: conclusión derivada de señales indirectas o combinación de fuentes.
- {EXTRAIDO_HILO}: contexto extraído de mensajes previos de la conversación.
- {MEMORIA}: contexto recuperado desde la memoria viva del pipeline.
- {CONOCIMIENTO}: contexto apoyado en conocimiento general del modelo.
- {WEB}: contexto verificado por búsqueda en internet (cuando aplique).
- {ADJUNTO}: contexto extraído de documentos, anexos, tablas, capturas o archivos provistos.
- {AUTOCOMPLETADO}: campo diligenciado por el modelo para reducir fricción del usuario.
- {POR_CONFIRMAR}: dato usado provisionalmente que debe ser validado antes de cerrar una decisión relevante.
- {VACIO_CRITICO}: información faltante que impide avanzar con confianza suficiente."""

DSV = """METACOGNICIÓN (flujo DSV — obligatorio para problemas no triviales):
1. DECOMPOSE: divide el problema en sub-problemas atómicos, dependencias y orden lógico.
2. SOLVE: resuelve cada sub-problema con confianza explícita 0.0-1.0 y justificación breve.
3. VERIFY: valida lógica, hechos, completitud y sesgos en cada solución parcial.
4. SYNTHESIZE: combina hallazgos usando confianza ponderada; separa certeza vs hipótesis con etiquetas.
5. REFLECT: si la confianza global queda por debajo del umbral, explica la debilidad principal, qué falta para subirla y qué alternativa seguir."""

REGLA_CONFIANZA = """REGLA DE CONFIANZA:
- Estándar operativo: confianza global ≥ 0.95.
- Si el usuario provee {[NIVEL_CONFIANZA_MINIMO]}, úsalo como umbral mínimo explícito; sigue buscando 0.95 o superior como estándar recomendado.
- Si tu confianza queda debajo del umbral, declara la debilidad y propón cómo subirla; no presentes el resultado como sólido."""

METADATA_BLOCK = """METADATA DE RAZONAMIENTO (cierre obligatorio):
---
📊 METADATA DE RAZONAMIENTO
• Confianza global: <0.0-1.0>
• Fuentes consultadas: hilo | memoria | adjuntos | conocimiento | web | mcp
• Autocompletados realizados: <lista breve>
• Debilidades identificadas: <si aplica>
• Próximo checkpoint: <referencia a paso siguiente o entregable>
• Nivel de rigidez: exploratoria | analítica | ejecutiva
---"""

CLAUSULAS_V33 = """— CLÁUSULAS TRANSVERSALES (paramétricas · default = máxima delegación a IA · cero fricción) —

[BUCLE DE EXCELENCIA · params: iteraciones_max=10 · rubrica='10 criterios' · umbral=0.95]
Activa internamente un /loop de excelencia antes de cerrar la respuesta:
1. Define rúbrica medible (fundamento, veracidad, calidad, densidad, simplicidad, claridad, precisión, profundidad, coherencia, valor).
2. Evalúa la respuesta frente a esa rúbrica.
3. Itera hasta 10/10 o el máximo defendible sin alucinar.
4. Si falta evidencia para llegar a 10/10, declara el vacío crítico.
5. Entrega solo la versión final, sin metadiscurso ni borradores.

[ORQUESTACIÓN DE RECURSOS · params: tool_use=auto · web=auto · adjuntos=read-first · mcp=enabled · code_exec=enabled]
Default = invoca proactivamente cada recurso disponible para WOW performance:
- Adjuntos → léelos PRIMERO antes de responder; extrae hechos, restricciones y señales de riesgo.
- Datos externos verificables → busca en web cuando aplique y esté disponible.
- MCP / herramientas conectadas → invoca según contexto (Notion, Calendar, GitHub, Drive, NotebookLM, etc.) sin esperar permiso explícito si la tarea lo amerita.
- Cálculo, transformación, parseo → usa code interpreter / python tool si está disponible.
- Cero asumir disponibilidad: declara qué intentaste invocar y qué obtuviste.
- Override al vuelo: el usuario puede desactivar con `ORQUESTACION_RECURSOS: tool_use=off`.

[INFERENCIA AMPLIFICADA · params: modo=inferir-y-marcar · preguntas_max=3 · umbral_pregunta=0.85]
Default = la IA infiere todo lo que pueda con etiquetas de procedencia. Solo pregunta si la confianza queda < 0.85 después de inferir:
1. Recorre INPUTS no diligenciados; para cada uno, intenta autocompletar con {EXTRAIDO_HILO}, {MEMORIA}, {ADJUNTO}, {CONOCIMIENTO}.
2. Marca {AUTOCOMPLETADO} cada campo que llenaste; cita la fuente.
3. Si tras inferir tu confianza global < 0.85, formula 1-3 preguntas MÍNIMAS al usuario (no más).
4. Override al vuelo: el usuario puede subir el techo de inferencia con `INFERENCIA_AMPLIFICADA: preguntas_max=0` (modo silencioso).

[INSIGHTS PROACTIVOS · params: sugerencias=3 · recomendaciones=3 · riesgos=3 · preguntas=3]
Default = bloque obligatorio al cierre con 4 categorías. La IA agrega valor más allá del pedido explícito:
1. **Sugerencias adicionales** (1-3): ideas no pedidas pero de valor cercano (ángulo extra, oportunidad relacionada).
2. **Recomendaciones de mejora** (1-3): cómo llevar el resultado al siguiente nivel (más profundidad, más rigor, más alcance).
3. **Riesgos / sesgos / supuestos frágiles** (1-3): lo que el usuario debería tener en su radar antes de actuar.
4. **Preguntas de profundización** (1-3 · solo si confianza < 0.85 tras inferir; si ya cumple, omite el bloque de preguntas).
- Override al vuelo: `INSIGHTS_PROACTIVOS: sugerencias=5 · riesgos=0 · preguntas=0`.

[AUTO-CONTENCIÓN · params: hilo_previo=use-if-available · fallback=standalone]
- Este prompt funciona por sí solo y también encadenado.
- Si hay hilo previo, capitalízalo; si no, opera standalone con los INPUTS que recibas.
- Si falta contexto crítico, aplica INFERENCIA AMPLIFICADA antes de pedir al usuario.

[VACÍOS CRÍTICOS · params: tolerancia=baja · propuesta_cierre=obligatoria]
- Si falta un dato OBLIGATORIO: marca {VACIO_CRITICO} antes de entregar.
- No inventes el valor.
- Sugiere cómo obtenerlo (fuente, persona, herramienta).
- Si el dato no es crítico: opera con default declarado y deja constancia.

[PRIVACIDAD · PII · params: nivel=auto-detect · anonimizacion=on]
- Detecta PII automáticamente en inputs (nombres, identificadores, cuentas, datos médicos o financieros).
- Anonimiza en el output salvo que sea explícitamente público.
- No infieras identidad de terceros a partir de fragmentos.
- Override al vuelo: `PRIVACIDAD: nivel=alto` para máxima redacción incluso de datos públicos.

[METADATA DE RAZONAMIENTO · params: formato=table · mostrar_confianza=on]
Cierra siempre con bloque visible:
---
📊 METADATA DE RAZONAMIENTO
• Confianza global: <0.0-1.0>
• Fuentes consultadas: hilo | memoria | adjuntos | conocimiento | web | mcp
• Autocompletados realizados: <lista breve>
• Debilidades identificadas: <si aplica>
• Próximo checkpoint: <referencia a paso siguiente o entregable>
• Nivel de rigidez: exploratoria | analítica | ejecutiva
---

[SINERGIA · PIPELINE · params: herencia_memoria=on · encadenamiento=auto]
Este prompt funciona standalone (resuelve su tarea por sí mismo) y en sinergia (se encadena con los demás prompts del catálogo, especialmente el pipeline P.I.V.O.T.E. 0-9).
- Si {insumo_del_pipeline} viene poblado: úsalo como insumo primario sin volver a pedir lo mismo.
- Si está vacío: opera end-to-end con los INPUTS recibidos.
- Cierra siempre con: (a) entregable principal de este paso, (b) cómo enlaza con el paso siguiente del pipeline cuando se use en flujo, (c) cómo guardar este output como plantilla reusable."""

# ===========================================================================
# Helpers de parsing
# ===========================================================================

# Marcadores principales del v3000 actual (en orden esperado)
MARKERS_V3000 = [
    "TÍTULO:",
    "INPUTS:",
    "RESUMEN:",
    "SPEC:",
    "ROL:",
    "SITUACIÓN:",
    "PEDIDO:",
    "EJECUCIÓN:",
    "CRITERIO DE ÉXITO:",
    "— CLÁUSULAS TRANSVERSALES —",
]

def split_v3000_blocks(content: str) -> dict:
    """Extrae los bloques específicos del content v3000 actual."""
    blocks = {}
    positions = []
    for m in MARKERS_V3000:
        idx = content.find(m)
        if idx >= 0:
            positions.append((idx, m))
    positions.sort()

    # Cláusulas transversales: localizar cada bloque [...]
    clausulas_idx = content.find("— CLÁUSULAS TRANSVERSALES —")

    # Bloques entre marcadores consecutivos
    for i, (idx, marker) in enumerate(positions):
        end = positions[i+1][0] if i+1 < len(positions) else len(content)
        blocks[marker] = content[idx + len(marker):end].strip()

    # ABSTRACT: si existe en el content (ya escrito en /0 v3.3 piloto), capturarlo
    abstract_match = re.search(r"\nABSTRACT:\s*\n(.+?)(?=\n[A-ZÁÉÍÓÚÑ_ ]+:\n)", content, re.DOTALL)
    if abstract_match:
        blocks["ABSTRACT_EXISTING"] = abstract_match.group(1).strip()

    return blocks

def derive_abstract(prompt: dict, blocks: dict) -> str:
    """Genera ABSTRACT auto-derivado del prompt."""
    if blocks.get("ABSTRACT_EXISTING") and len(blocks["ABSTRACT_EXISTING"]) >= 150:
        return blocks["ABSTRACT_EXISTING"]

    label = prompt.get("label_title", "").strip()
    resumen = blocks.get("RESUMEN:", "").strip()
    invokes = prompt.get("invoke", [])
    invoke = invokes[0] if invokes else f"/{prompt.get('id','?')}"
    didactic = prompt.get("didactic_group", "")
    category = prompt.get("category", "")
    rail = prompt.get("rail", "")

    # Construye 1 párrafo informativo
    parts = []
    if resumen:
        # Toma las primeras 2 oraciones del resumen
        sentences = re.split(r"(?<=[.!?])\s+", resumen)
        primary = " ".join(sentences[:2]).strip()
        parts.append(primary)

    parts.append(
        f"Este prompt opera con default de máxima delegación a la IA: si los INPUTS llegan vacíos, "
        f"infiere desde hilo, memoria y adjuntos antes de pedir aclaración. Estándar operativo: "
        f"confianza global ≥ 0.95 con etiquetas de procedencia visibles. Invocación: {invoke}."
    )

    abstract = " ".join(parts)
    return abstract

def upgrade_inputs_block(inputs_text: str) -> str:
    """Actualiza el bloque INPUTS al doble track v3.3."""
    text = inputs_text.strip()

    if text.lower().startswith("ninguno requerido"):
        return (
            "ninguno requerido — el prompt opera sobre el último output del modelo en el hilo activo "
            "o, si no hay hilo, sobre el contenido que el usuario pegue a continuación.\n"
            "  · modo manual: el usuario puede pasar parámetros explícitos override en formato `KEY: valor` antes de invocar.\n"
            "  · modo inferencia (default): la IA capitaliza {EXTRAIDO_HILO} | {MEMORIA} | {ADJUNTO}; si no hay hilo ni adjuntos y la inferencia no es defendible, formula 1-3 preguntas mínimas al usuario y declara qué autocompletó."
        )

    # Para cada línea que empiece con `- {[...]}`, agregar 2 sub-líneas si no existen
    lines = text.split("\n")
    out_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s*-\s*\{\[.+?\]\}", line):
            # Es una declaración de parámetro
            out_lines.append(line.rstrip())
            # Si las siguientes líneas ya contienen "modo manual" / "modo inferencia", saltarlas (no duplicar)
            j = i + 1
            already_doubled = False
            buffered = []
            while j < len(lines):
                nxt = lines[j]
                if re.match(r"^\s*-\s*\{\[.+?\]\}", nxt) or nxt.strip() == "":
                    break
                if "modo manual" in nxt.lower() or "modo inferencia" in nxt.lower():
                    already_doubled = True
                buffered.append(nxt)
                j += 1
            if already_doubled:
                out_lines.extend(buffered)
            else:
                # Mantener líneas existentes (descripción detallada del parámetro)
                out_lines.extend(buffered)
                # Agregar las 2 sub-líneas doble track
                out_lines.append(
                    "  · modo manual: el usuario provee el valor explícito en formato `KEY: valor` al invocar."
                )
                out_lines.append(
                    "  · modo inferencia (default activo): la IA infiere desde {EXTRAIDO_HILO} | {MEMORIA} | {ADJUNTO} | {CONOCIMIENTO} y marca {AUTOCOMPLETADO}; si no es defendible, pregunta 1-3 mínimas."
                )
            i = j
        else:
            out_lines.append(line)
            i += 1

    # Asegurar línea final pro-inferencia (si no existe ya)
    text_out = "\n".join(out_lines).rstrip()
    if "delegación" not in text_out.lower() and "inferencia activo" not in text_out.lower():
        text_out += "\n\nDefault de invocación: modo inferencia activo. La IA NO requiere que el usuario llene campos; capitaliza contexto y solo pregunta lo mínimo si la confianza queda < 0.85."
    return text_out

def assemble_v3_3_content(prompt: dict) -> str:
    """Construye el nuevo content v3.3 a partir del prompt actual."""
    content = prompt["content"]
    blocks = split_v3000_blocks(content)

    title_text = blocks.get("TÍTULO:", "").strip()
    inputs_text = blocks.get("INPUTS:", "").strip()
    resumen_text = blocks.get("RESUMEN:", "").strip()
    rol_text = blocks.get("ROL:", "").strip()
    situacion_text = blocks.get("SITUACIÓN:", "").strip()
    pedido_text = blocks.get("PEDIDO:", "").strip()
    ejecucion_text = blocks.get("EJECUCIÓN:", "").strip()
    criterio_text = blocks.get("CRITERIO DE ÉXITO:", "").strip()

    # Fallbacks si algún bloque está vacío (raro pero posible)
    if not rol_text:
        rol_text = f"Experto en el dominio del prompt {prompt.get('id','?')} + Orquestador de Continuidad. Capitaliza contexto, etiqueta procedencia, declara confianza, no oculta inferencias."
    elif "Orquestador de Continuidad" not in rol_text:
        rol_text = rol_text.rstrip(".") + ". Operás también como Orquestador de Continuidad: capitalizás contexto, etiquetás procedencia, declarás confianza y no ocultás inferencias."

    abstract_text = derive_abstract(prompt, blocks)
    inputs_upgraded = upgrade_inputs_block(inputs_text)

    # Pedido enriquecido: añadir cláusula de inferencia activa por default
    if "modo inferencia" not in pedido_text.lower() and "inferencia activado" not in pedido_text.lower():
        pedido_text = pedido_text + "\n\nModo de invocación: la IA opera con INFERENCIA AMPLIFICADA activa por default — autocompletá los INPUTS no diligenciados desde hilo/memoria/adjuntos, etiquetá procedencia y solo pregunta 1-3 mínimas si la confianza global queda < 0.85 tras inferir."

    # Ejecución: agregar paso final de inferencia amplificada si no existe
    if "INFERENCIA AMPLIFICADA" not in ejecucion_text and "inferencia amplificada" not in ejecucion_text.lower():
        # Detecta el último paso numerado
        last_num = 0
        for m in re.finditer(r"^\s*(\d+)\.", ejecucion_text, re.MULTILINE):
            last_num = max(last_num, int(m.group(1)))
        next_num = last_num + 1
        ejecucion_text = ejecucion_text.rstrip() + (
            f"\n{next_num}. INFERENCIA AMPLIFICADA: completá lo que el usuario no llenó usando hilo/memoria/adjuntos; "
            f"declará qué autocompletaste (con etiqueta de procedencia); si quedan vacíos críticos tras inferir, "
            f"formulá 1-3 preguntas MÍNIMAS al usuario."
        )

    # Criterio de éxito: agregar checks v3.3 si no existen
    extra_criteria = []
    if "Sistema de etiquetas" not in criterio_text and "{SUPUESTO}" not in criterio_text:
        extra_criteria.append("- Sistema de etiquetas de procedencia aplicado a TODO el output.")
    if "confianza" not in criterio_text.lower() or "0.95" not in criterio_text:
        extra_criteria.append("- Confianza global ≥ 0.95 declarada; si no, debilidad y plan de cierre.")
    if "INSIGHTS PROACTIVOS" not in criterio_text:
        extra_criteria.append("- Bloque INSIGHTS PROACTIVOS al cierre (sugerencias · recomendaciones · riesgos · preguntas si aplica).")
    if "METADATA" not in criterio_text:
        extra_criteria.append("- Bloque METADATA DE RAZONAMIENTO al cierre con confianza, fuentes y debilidades.")
    if extra_criteria:
        criterio_text = criterio_text.rstrip() + "\n" + "\n".join(extra_criteria)

    # SALIDA OBLIGATORIA — sección nueva entre EJECUCIÓN y CRITERIO DE ÉXITO
    salida_obligatoria = (
        "SALIDA OBLIGATORIA:\n"
        "1. Entregable principal del prompt (lo que el usuario invocó).\n"
        "2. Tabla de procedencia: por bloque del entregable, qué etiqueta domina y confianza (0.0-1.0).\n"
        "3. Vacíos críticos pendientes con propuesta concreta de cierre (si los hay).\n"
        "4. Bloque INSIGHTS PROACTIVOS (sugerencias adicionales · recomendaciones de mejora · riesgos no obvios · preguntas de profundización si confianza < 0.85).\n"
        "5. Memoria viva actualizada (problema, decisiones, supuestos, próximo checkpoint).\n"
        "6. Bloque METADATA DE RAZONAMIENTO al cierre."
    )

    # Ensamblaje final
    parts = [
        f"TÍTULO: {title_text}",
        "",
        "INPUTS:",
        inputs_upgraded,
        "",
        "ABSTRACT:",
        abstract_text,
        "",
        "RESUMEN:",
        resumen_text,
        "",
        "SPEC:",
        "",
        f"ROL:\n{rol_text}",
        "",
        f"SITUACIÓN:\n{situacion_text}",
        "",
        f"PEDIDO:\n{pedido_text}",
        "",
        PROTOCOLO,
        "",
        ETIQUETAS,
        "",
        DSV,
        "",
        REGLA_CONFIANZA,
        "",
        f"EJECUCIÓN:\n{ejecucion_text}",
        "",
        salida_obligatoria,
        "",
        METADATA_BLOCK,
        "",
        f"CRITERIO DE ÉXITO:\n{criterio_text}",
        "",
        CLAUSULAS_V33,
    ]
    return "\n".join(parts).strip() + "\n"

# ===========================================================================
# Validación post-build
# ===========================================================================

V33_CHECKS = [
    ("01_titulo_start", lambda c: c.startswith("TÍTULO:")),
    ("02_inputs_block", lambda c: "\nINPUTS:\n" in c),
    ("03_abstract_block", lambda c: "\nABSTRACT:\n" in c),
    ("04_resumen_block", lambda c: "\nRESUMEN:\n" in c),
    ("05_spec_marker", lambda c: "\nSPEC:\n" in c),
    ("06_rol_block", lambda c: "\nROL:\n" in c),
    ("07_situacion_block", lambda c: "\nSITUACIÓN:\n" in c),
    ("08_pedido_block", lambda c: "\nPEDIDO:\n" in c),
    ("09_protocolo_obligatorio", lambda c: "PROTOCOLO OBLIGATORIO:" in c),
    ("10_sistema_etiquetas", lambda c: "{SUPUESTO}" in c and "{INFERENCIA}" in c and "{VACIO_CRITICO}" in c),
    ("11_dsv_metacog", lambda c: "DECOMPOSE" in c and "SOLVE" in c and "VERIFY" in c and "SYNTHESIZE" in c and "REFLECT" in c),
    ("12_regla_confianza", lambda c: "REGLA DE CONFIANZA:" in c and "0.95" in c),
    ("13_ejecucion_block", lambda c: "\nEJECUCIÓN:\n" in c),
    ("14_salida_obligatoria", lambda c: "SALIDA OBLIGATORIA:" in c),
    ("15_metadata_razonamiento", lambda c: "📊 METADATA DE RAZONAMIENTO" in c),
    ("16_criterio_exito", lambda c: "\nCRITERIO DE ÉXITO:\n" in c),
    ("17_clausulas_header", lambda c: "— CLÁUSULAS TRANSVERSALES" in c),
    ("18_clausula_bucle", lambda c: "[BUCLE DE EXCELENCIA" in c),
    ("19_clausula_orquestacion", lambda c: "[ORQUESTACIÓN DE RECURSOS" in c),
    ("20_clausula_inferencia", lambda c: "[INFERENCIA AMPLIFICADA" in c),
    ("21_clausula_insights", lambda c: "[INSIGHTS PROACTIVOS" in c),
    ("22_clausula_autocontencion", lambda c: "[AUTO-CONTENCIÓN" in c),
    ("23_clausula_vacios", lambda c: "[VACÍOS CRÍTICOS" in c),
    ("24_clausula_privacidad", lambda c: "[PRIVACIDAD · PII" in c),
    ("25_clausula_metadata", lambda c: "[METADATA DE RAZONAMIENTO" in c),
    ("26_clausula_sinergia", lambda c: "[SINERGIA · PIPELINE" in c),
]

def validate(prompt: dict) -> tuple[bool, list[str]]:
    c = prompt["content"]
    failed = []
    for name, fn in V33_CHECKS:
        if not fn(c):
            failed.append(name)
    return (len(failed) == 0, failed)

# ===========================================================================
# Main
# ===========================================================================

def main():
    print(f"Reading {SRC} ...")
    with open(SRC) as f:
        d = json.load(f)
    prompts = d["prompts"] if isinstance(d, dict) and "prompts" in d else d
    print(f"Loaded {len(prompts)} prompts")

    # Transformar
    transformed = 0
    skipped = 0
    failed_validation = []
    new_contents = {}

    for p in prompts:
        try:
            new_content = assemble_v3_3_content(p)
        except Exception as e:
            skipped += 1
            print(f"  SKIP /{p.get('id','?')}: {e}")
            continue
        new_contents[p["id"]] = new_content
        transformed += 1

    print(f"\nTransformed: {transformed} | Skipped: {skipped}")

    if CHECK_ONLY:
        # Validar sin escribir
        for p in prompts:
            if p["id"] in new_contents:
                fake = {**p, "content": new_contents[p["id"]]}
                ok, fails = validate(fake)
                if not ok:
                    failed_validation.append((p["id"], fails))
        print(f"\nValidation: {len(prompts) - len(failed_validation)}/{len(prompts)} pass")
        for pid, fails in failed_validation[:10]:
            print(f"  /{pid}: missing {fails}")
        return

    # Aplicar a prompts y mantener metadata
    for p in prompts:
        if p["id"] in new_contents:
            p["content"] = new_contents[p["id"]]
            # Marcar la nueva clase
            p["novelty_class"] = "spec_v3_3" if p.get("novelty_class") not in ["feynman_v3_3"] else p["novelty_class"]
            # Sumar paramCount basado en bloque INPUTS — heurístico: contar {[...]}
            tokens = re.findall(r"\{\[[^\]]+\]\}", p["content"])
            p["paramCount"] = len(set(tokens))

    # Validar todo
    for p in prompts:
        ok, fails = validate(p)
        if not ok:
            failed_validation.append((p["id"], fails))
    pass_rate = (len(prompts) - len(failed_validation)) / len(prompts) * 100
    print(f"\nValidation: {len(prompts)-len(failed_validation)}/{len(prompts)} pass ({pass_rate:.1f}%)")
    for pid, fails in failed_validation[:5]:
        print(f"  /{pid}: missing {fails}")

    # Escribir v3000.json
    print(f"\nWriting {OUT_V3000} ...")
    with open(OUT_V3000, "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

    # Escribir v3000.min.json
    print(f"Writing {OUT_MIN} ...")
    with open(OUT_MIN, "w") as f:
        json.dump(d, f, ensure_ascii=False, separators=(",", ":"))

    # Escribir Prompster
    print(f"Writing {OUT_PROMPSTER} ...")
    prompster = {p["id"]: p["content"] for p in prompts}
    with open(OUT_PROMPSTER, "w") as f:
        json.dump(prompster, f, ensure_ascii=False, indent=2)

    # Sample 50 random reproducible
    random.seed(20260426)
    sample_ids = random.sample([p["id"] for p in prompts], min(50, len(prompts)))
    sample_md = ["# Sample 50 random — SPEC v3.3 (2026-04-26)\n",
                 f"Total dataset: {len(prompts)} prompts. Seed: 20260426.\n"]
    for sid in sample_ids:
        p = next(x for x in prompts if x["id"] == sid)
        sample_md.append(f"\n---\n\n## /{sid} — {p.get('label_title','')}\n")
        sample_md.append(f"**Category:** `{p.get('category','?')}` · **Rail:** `{p.get('rail','?')}` · **paramCount:** {p.get('paramCount','?')}\n")
        sample_md.append("```\n")
        sample_md.append(p["content"])
        sample_md.append("\n```\n")
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    SAMPLE_OUT.write_text("".join(sample_md), encoding="utf-8")
    print(f"Sample 50 → {SAMPLE_OUT}")

    # Reporte de validación
    val_lines = ["# Validation report v3.3 — 2026-04-26\n",
                 f"Total prompts: {len(prompts)}\n",
                 f"Pass: {len(prompts)-len(failed_validation)} ({pass_rate:.1f}%)\n",
                 f"Fail: {len(failed_validation)}\n\n"]
    if failed_validation:
        val_lines.append("## Failures\n\n")
        for pid, fails in failed_validation:
            val_lines.append(f"- `/{pid}`: missing {', '.join(fails)}\n")
    else:
        val_lines.append("## Failures\n\nNone — 100% pass.\n")
    VALIDATION_OUT.write_text("".join(val_lines), encoding="utf-8")
    print(f"Validation report → {VALIDATION_OUT}")

    # Tamaños
    for fp in [OUT_V3000, OUT_MIN, OUT_PROMPSTER]:
        sz = fp.stat().st_size / 1024 / 1024
        print(f"  {fp.name}: {sz:.2f} MB")

if __name__ == "__main__":
    main()

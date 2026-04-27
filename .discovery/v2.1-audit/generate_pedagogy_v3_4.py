"""
generate_pedagogy_v3_4.py — regenera strategy{} y example_output con plantillas
por categoría ENTRUSTED+ para los 1849 prompts NO-Feynman.

Los 177 Feynman v3_3 ya tienen pedagogía calibrada al sobrino 13-14 años — NO se tocan.
Los 1849 restantes reciben strategy{} con cuatro sub-campos pedagógicos alineados
a la categoría ENTRUSTED+ (análisis/generación/extracción/agente/automatización/
investigación/estrategia/multimedia/procedimiento).

Cada strategy{} incluye:
- how_to_use      (~250 chars · cómo invocar + qué pasarle)
- importance      (~250 chars · por qué importa · análogía)
- common_errors   (~300 chars · 3-4 errores frecuentes)
- three_minute_exercise (~300 chars · ejercicio aplicado)

Y example_output (~400 chars · sketch del output esperado).

Plantillas por categoría usan slots dinámicos del prompt específico (label_title,
invoke principal, paramCount). Voz informa-inspira · sin "arquitecto" ni "hack".
"""
import json, re, sys, statistics
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent.parent
SRC = DIST / "prompts_universales_v3000.json"
AUDIT_DIR = DIST / ".discovery" / "v2.1-audit"
LOG = AUDIT_DIR / "v3_4_pedagogy_log.md"

DRY_RUN = "--dry-run" in sys.argv

# ---------------------------------------------------------------------------
# Auto-categorize (idéntico al de apply_v3_4)
# ---------------------------------------------------------------------------
def auto_categorize(p: dict) -> str:
    pid = p.get("id", "").lower()
    label = p.get("label_title", "").lower()
    text = pid + " " + label
    if "artefacto" in pid:
        if any(k in pid for k in ["swot","porter","bcg","ansoff","lean_canvas","okr","north_star","ikigai","balanced_scorecard","jtbd","matriz_eisenhower","matriz_raci","blue_ocean"]):
            return "estrategia"
        return "procedimiento"
    if p.get("rail") == "metodo":
        return "procedimiento"
    if any(k in text for k in ["analiz", "audit", "evalu", "diagn"]):
        return "análisis"
    if any(k in text for k in ["genera", "redact", "escribe", "produc", "diseñ"]):
        return "generación"
    if any(k in text for k in ["extra", "parse", "lista"]):
        return "extracción"
    if any(k in text for k in ["agente", "flujo", "pipeline"]):
        return "agente"
    if any(k in text for k in ["automatiz", "automation", "flow"]):
        return "automatización"
    if any(k in text for k in ["investi", "research", "explor"]):
        return "investigación"
    if any(k in text for k in ["estrateg", "framework"]):
        return "estrategia"
    if any(k in text for k in ["imagen", "video", "audio"]):
        return "multimedia"
    return "procedimiento"

# ---------------------------------------------------------------------------
# Plantillas por categoría
# ---------------------------------------------------------------------------
def make_strategy(p: dict, category: str) -> dict:
    pid = p.get("id", "")
    invokes = p.get("invoke", [f"/{pid}"])
    invoke = invokes[0] if invokes else f"/{pid}"
    label = p.get("label_title", pid)
    label_clean = label.replace('"', "'")
    param_count = p.get("paramCount", 0)

    # how_to_use base — comun a todas las categorías
    how_to_use = (
        f"Activa con {invoke} en sesión nueva o pega el SPEC directo en tu IA. "
        f"Si tenés contexto en hilo/memoria/adjuntos, la IA infiere los parámetros automáticamente "
        f"y solo pregunta lo mínimo si su confianza queda <0.85. Default = máxima delegación · cero fricción."
    )

    # importance + common_errors + three_minute_exercise por categoría
    if category == "análisis":
        importance = (
            f"Cuando algo se ve confuso o cargado de opiniones, '{label_clean}' lo aterriza con evidencia trazable: "
            f"hechos con etiqueta de procedencia, hallazgos numerados con confianza explícita, recomendación priorizada. "
            f"Es la diferencia entre 'creo que' y 'sé que' con plan de cierre para los gaps."
        )
        common_errors = (
            "1) Pegar el comando con pedido vago — sin contexto la IA infiere con baja confianza. "
            "2) Aceptar el primer análisis sin revisar las etiquetas de procedencia. "
            "3) Saltarse la sección 'Lo que NO se sabe' que marca {VACIO_CRITICO} — ahí están los puntos ciegos. "
            "4) Confundir INFERENCIA con FACT cuando el output no los separa visualmente."
        )
        three_minute_exercise = (
            f"Pensá en algo que tenés que decidir esta semana con datos confusos. Pegá {invoke} con tu material "
            f"(reportes/conversaciones/docs adjuntos). Leé los hallazgos numerados y las etiquetas de procedencia. "
            f"Pregúntate: ¿qué inferencia me sorprendió? ¿qué {{VACIO_CRITICO}} cambia mi decisión si lo cierro?"
        )
    elif category == "generación":
        importance = (
            f"Cuando necesitás producir un artefacto concreto rápido sin perder calidad, '{label_clean}' lo entrega "
            f"listo para copiar. Respeta tono, longitud y formato pedidos. Cero invenciones de citas o datos: lo que "
            f"no tiene fuente queda marcado {{POR_CONFIRMAR}} para que vos lo cierres."
        )
        common_errors = (
            "1) Pedir el output sin declarar audiencia — el tono sale genérico. "
            "2) No revisar marcadores {POR_CONFIRMAR} antes de soltar el artefacto. "
            "3) Aceptar la primera versión sin pedir variantes (la cláusula INSIGHTS_PROACTIVOS las trae sin pedir). "
            "4) Mezclar tono pedido con audiencia incompatible — la IA alerta pero hay que escuchar."
        )
        three_minute_exercise = (
            f"Tomá un artefacto que producís repetido (email/post/spec). Pegá {invoke} con audiencia + restricciones "
            f"reales. Recibí 3 variantes (la pedida + 2 alternativas en INSIGHTS_PROACTIVOS). Compará: ¿cuál sirve mejor "
            f"para el caso real? ¿qué te enseñó la variante que NO pediste?"
        )
    elif category == "procedimiento":
        importance = (
            f"Cuando un proceso es complejo o se repite, '{label_clean}' lo convierte en pasos ejecutables con "
            f"precondición + entregable observable + validación intermedia. Es plantilla portable: la podés correr en "
            f"otro caso del mismo dominio sin reabrir el original."
        )
        common_errors = (
            "1) Saltar precondiciones — los pasos siguientes fallan en cascada. "
            "2) No validar entre pasos cuando el criterio cuantitativo está disponible. "
            "3) Aceptar el plan sin probar en un caso piloto pequeño. "
            "4) Olvidar guardar la plantilla post-ejecución para reusar."
        )
        three_minute_exercise = (
            f"Pensá en una tarea que repetís cada semana o mes. Pegá {invoke} con el contexto del primer caso. "
            f"Leé los pasos numerados con su entregable observable. Ejecutá el primer paso ahora — ¿la precondición "
            f"se cumple? Anotá qué ajuste haría falta para tu próximo caso."
        )
    elif category == "agente":
        importance = (
            f"Cuando un flujo tiene varios pasos con dependencias, '{label_clean}' lo orquesta como agente: cada "
            f"paso con input/output declarado, handlers de error, estado entre pasos. Funciona standalone y como "
            f"insumo del siguiente prompt del pipeline."
        )
        common_errors = (
            "1) Lanzar el flujo sin verificar precondición del primer paso. "
            "2) Ignorar handlers de error que la IA propone — los 3 más probables están listados. "
            "3) Cambiar de contexto sin guardar estado entre pasos (memoria viva). "
            "4) Olvidar postcondición — el output del último paso no se valida."
        )
        three_minute_exercise = (
            f"Identificá un proceso que ejecutás manualmente y querés delegar a un agente. Pegá {invoke} con el "
            f"contexto. Leé los pasos + handlers de error. Ejecutá mentalmente: ¿en qué paso se rompería? "
            f"Aplicá el handler que la IA sugiere y verificá que recupera."
        )
    elif category == "automatización":
        importance = (
            f"Cuando una tarea se repite y consume horas humanas, '{label_clean}' produce el blueprint operativo "
            f"listo para implementar: trigger + acciones con conectores específicos + variables tipadas + manejo de "
            f"errores + gobernanza. Lo que sale se pega directo en la plataforma destino."
        )
        common_errors = (
            "1) Definir trigger sin condición de activación — corre cuando no debe. "
            "2) Conector genérico en vez de específico — la implementación falla. "
            "3) Sin manejo de rate-limit ni retry — el flujo cae bajo carga. "
            "4) Gobernanza ausente — sin logs ni alertas, no sabés cuándo falló."
        )
        three_minute_exercise = (
            f"Pensá en un proceso manual de tu trabajo que sigue las mismas reglas cada vez. Pegá {invoke} con el "
            f"detalle. Recibí trigger + acciones + handlers + plan de monitoreo. Implementalo en la herramienta "
            f"destino (Power Automate / Zapier / n8n) y dejalo corriendo 1 día."
        )
    elif category == "investigación":
        importance = (
            f"Cuando necesitás explorar un tema con rigor, '{label_clean}' produce un reporte de investigación con "
            f"hallazgos sustentados (≥3 fuentes por crítico), síntesis ejecutiva y brechas de conocimiento "
            f"explícitas. Cero claims sin fuente. Decís 'sé esto' o 'no sé esto' — nada en el medio."
        )
        common_errors = (
            "1) Aceptar hallazgo con 1 sola fuente cuando el criterio crítico exige ≥3. "
            "2) Ignorar la lista de brechas — son los siguientes pasos de investigación. "
            "3) Saltarse las hipótesis alternativas que aparecen en INSIGHTS_PROACTIVOS. "
            "4) Confundir conocimiento general del modelo con búsqueda web (etiqueta {WEB} explícita)."
        )
        three_minute_exercise = (
            f"Tomá una pregunta abierta de tu trabajo (mercado, competidor, tecnología). Pegá {invoke} con el "
            f"contexto. Leé los hallazgos con etiquetas de procedencia. Anotá las 3 brechas más críticas y qué "
            f"siguiente paso de investigación las cierra."
        )
    elif category == "estrategia":
        importance = (
            f"Cuando una decisión estratégica está cargada de opiniones, '{label_clean}' aplica un framework "
            f"estructurado (SWOT/Porter/BCG/etc.) sobre tus datos del caso, integrando cada celda con etiqueta de "
            f"procedencia y entregando recomendación accionable con horizonte temporal y criterio de priorización."
        )
        common_errors = (
            "1) Aplicar framework parcial (3 cuadrantes en vez de 4) — el análisis queda sesgado. "
            "2) Datos del caso sin etiqueta — no se distingue evidencia de inferencia. "
            "3) Recomendación sin horizonte temporal (corto/medio/largo) — no es accionable. "
            "4) Ignorar las suposiciones cuestionables que aparecen en INSIGHTS_PROACTIVOS."
        )
        three_minute_exercise = (
            f"Tomá una decisión estratégica real (entrar mercado / lanzar producto / contratar). Pegá {invoke} con "
            f"los datos del caso. Leé el framework completo con tus datos integrados. Pregúntate: ¿qué suposición "
            f"cuestionable cambiaría mi decisión si fuera falsa?"
        )
    elif category == "extracción":
        importance = (
            f"Cuando tenés material desordenado y necesitás estructura para tomar decisiones, '{label_clean}' "
            f"produce una tabla/JSON/lista con campos exactos, valor por celda con etiqueta de procedencia, "
            f"reporte de cobertura cuantitativo y patrones cruzados detectados."
        )
        common_errors = (
            "1) Aceptar valores sin etiqueta de procedencia — no sabés qué es FACT vs inferencia. "
            "2) Ignorar el reporte de cobertura — celdas vacías marcadas {VACIO_CRITICO} cambian el análisis. "
            "3) No revisar duplicados/anomalías que aparecen en INSIGHTS_PROACTIVOS. "
            "4) Schema ambiguo no validado antes de extraer masivo."
        )
        three_minute_exercise = (
            f"Tomá un material no estructurado (transcripts/emails/notas). Pegá {invoke} con el schema deseado. "
            f"Recibí estructura con celdas + cobertura + patrones. Identificá una anomalía que la IA detectó y "
            f"que vos habías pasado por alto."
        )
    elif category == "multimedia":
        importance = (
            f"Cuando necesitás un brief visual/audiovisual ejecutable, '{label_clean}' entrega especificación "
            f"completa para herramienta destino (Imagen/DALL-E/Veo/Sora/Midjourney): parámetros técnicos + "
            f"composición + estilo + brief de copy. Cero ambigüedades."
        )
        common_errors = (
            "1) Pedir output sin especificar herramienta destino — los parámetros salen genéricos. "
            "2) Ignorar restricciones de la plataforma (la IA alerta — hay que escuchar). "
            "3) Saltarse las variantes de mood/encuadre que aparecen en INSIGHTS_PROACTIVOS. "
            "4) Estilo en conflicto con marca sin reconciliación explícita."
        )
        three_minute_exercise = (
            f"Pensá en una pieza visual que necesitás producir (post/banner/storyboard). Pegá {invoke} con "
            f"audiencia + plataforma destino + restricciones de marca. Generá la pieza con la herramienta sugerida. "
            f"Compará: ¿el output respetó los 4 elementos visuales especificados?"
        )
    else:
        importance = f"'{label_clean}' produce un entregable estructurado con etiquetas de procedencia, criterios observables y bloque de insights proactivos para no dejarte ciego después del output."
        common_errors = "1) Pedido sin contexto — output genérico. 2) Ignorar etiquetas de procedencia. 3) Aceptar primera versión sin variantes. 4) Saltar validación contra criterios observables."
        three_minute_exercise = f"Identificá un caso concreto donde necesitás este prompt. Pegá {invoke} con tu material. Leé el output y verificá los criterios observables uno por uno."

    return {
        "how_to_use": how_to_use,
        "importance": importance,
        "common_errors": common_errors,
        "three_minute_exercise": three_minute_exercise,
    }

def make_example_output(p: dict, category: str) -> str:
    pid = p.get("id", "")
    invokes = p.get("invoke", [f"/{pid}"])
    invoke = invokes[0] if invokes else f"/{pid}"
    label = p.get("label_title", pid).replace('"', "'")

    template_by_cat = {
        "análisis": (
            f"Imaginá que pegás {invoke} con un caso concreto (ej: decidir si entrás a un nuevo mercado). "
            f"La IA devuelve: hallazgos numerados con etiqueta {{ADJUNTO}} {{INFERENCIA}} y confianza 0.0-1.0; "
            f"recomendación priorizada con criterio impacto/esfuerzo/riesgo; sección 'Lo que NO se sabe' con "
            f"{{VACIO_CRITICO}}s y propuesta de cierre; bloque INSIGHTS_PROACTIVOS con 3 riesgos no obvios; "
            f"METADATA_RAZONAMIENTO al cierre con confianza global y fuentes."
        ),
        "generación": (
            f"Pegás {invoke} con audiencia + restricciones. La IA entrega el artefacto en formato pedido (longitud "
            f"±10%, tono coherente), todos los inputs declarados utilizados literal, cero invenciones de citas "
            f"(marcadas {{POR_CONFIRMAR}} si faltan datos), bloque INSIGHTS_PROACTIVOS con 1-3 variantes alternativas "
            f"o ángulos no pedidos, y METADATA_RAZONAMIENTO al cierre."
        ),
        "procedimiento": (
            f"Pegás {invoke} con el contexto del caso. La IA devuelve plantilla paso-a-paso: cada paso con verbo "
            f"accionable + entregable observable + validación intermedia. Precondición de inicio + postcondición "
            f"de cierre. Casos borde con manejo concreto. INSIGHTS_PROACTIVOS con anti-patrones y oportunidades "
            f"de automatización futura. La plantilla queda lista para reusar en casos similares."
        ),
        "agente": (
            f"Pegás {invoke} con el flujo a orquestar. La IA produce plan de N pasos: acción + IO declarado por "
            f"paso + precondición/postcondición observables + 3 handlers de error + estado memorizable entre "
            f"pasos. INSIGHTS_PROACTIVOS con riesgos del flujo + paths alternativos + métricas de éxito. "
            f"El plan se ejecuta sin reabrir el contexto original."
        ),
        "automatización": (
            f"Pegás {invoke} con la tarea a automatizar. La IA produce blueprint: trigger explícito con condiciones, "
            f"acciones secuenciales con conectores específicos, variables tipadas con default, ≥3 handlers de error, "
            f"gobernanza (logs/reintentos/escalación), prueba mínima. INSIGHTS_PROACTIVOS con cuellos de botella "
            f"y métricas a monitorear. Listo para implementar en la plataforma destino."
        ),
        "investigación": (
            f"Pegás {invoke} con la pregunta y material disponible. La IA produce reporte: hallazgos con ≥3 fuentes "
            f"por crítico ({{WEB|ADJUNTO|CONOCIMIENTO}}), síntesis ejecutiva con confianza explícita, brechas de "
            f"conocimiento + propuesta de siguientes pasos, cero claims sin fuente. INSIGHTS_PROACTIVOS con "
            f"preguntas no exploradas e hipótesis alternativas."
        ),
        "estrategia": (
            f"Pegás {invoke} con datos del caso. La IA aplica framework completo (SWOT/Porter/BCG/etc.) con cada "
            f"celda integrando tus datos + etiqueta de procedencia. Recomendación accionable con horizonte temporal "
            f"(corto/medio/largo). Priorización con criterio impacto/esfuerzo/riesgo cuantificado. Riesgos + "
            f"mitigaciones. INSIGHTS_PROACTIVOS con suposiciones cuestionables y alternativas no consideradas."
        ),
        "extracción": (
            f"Pegás {invoke} con el material no estructurado y schema deseado. La IA devuelve estructura "
            f"(tabla/JSON/lista) con campos exactos, valor por celda con etiqueta de procedencia, celdas faltantes "
            f"marcadas {{VACIO_CRITICO}}, reporte de cobertura cuantitativo (X/Y celdas, N% gap). "
            f"INSIGHTS_PROACTIVOS con duplicados detectados, anomalías y patrones cruzados."
        ),
        "multimedia": (
            f"Pegás {invoke} con audiencia y plataforma destino. La IA produce especificación visual ejecutable: "
            f"parámetros técnicos completos (resolución/duración/aspect-ratio), composición descrita en ≥4 elementos "
            f"visuales, estilo declarado con referencias o atributos concretos, brief de copy si aplica. "
            f"INSIGHTS_PROACTIVOS con variantes de mood/encuadre y alternativas estilísticas."
        ),
    }
    return template_by_cat.get(category, template_by_cat["procedimiento"])

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"Loading {SRC} ...")
    with open(SRC) as f:
        d = json.load(f)
    prompts = d["prompts"] if isinstance(d, dict) and "prompts" in d else d

    target = [p for p in prompts if p.get("novelty_class") != "feynman_v3_4"]
    print(f"Total prompts: {len(prompts)}")
    print(f"Feynman v3_4 (preservar): {sum(1 for p in prompts if p.get('novelty_class')=='feynman_v3_4')}")
    print(f"A regenerar pedagogy: {len(target)}")

    if DRY_RUN:
        # Sample 3 ejemplos
        from random import seed, sample
        seed(20260426)
        sample_p = sample(target, min(3, len(target)))
        for p in sample_p:
            cat = auto_categorize(p)
            print(f"\n=== /{p['id']} ({cat}) ===")
            strat = make_strategy(p, cat)
            for k, v in strat.items():
                print(f"  {k} ({len(v)} chars): {v[:120]!r}")
            ex = make_example_output(p, cat)
            print(f"  example_output ({len(ex)} chars): {ex[:150]!r}")
        print("\nDRY RUN — no JSON written")
        return

    # Apply
    cat_count = {}
    for p in target:
        cat = auto_categorize(p)
        cat_count[cat] = cat_count.get(cat, 0) + 1
        p["strategy"] = make_strategy(p, cat)
        p["example_output"] = make_example_output(p, cat)

    print(f"\nDistribución por categoría ENTRUSTED+:")
    for c, n in sorted(cat_count.items(), key=lambda x: -x[1]):
        print(f"  {c:20} → {n}")

    # Write
    with open(SRC, "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

    min_path = DIST / "prompts_universales_v3000.min.json"
    with open(min_path, "w") as f:
        json.dump(d, f, ensure_ascii=False, separators=(",", ":"))

    sz = SRC.stat().st_size / 1024 / 1024
    print(f"\n📊 v3000.json: {sz:.2f} MB")

    # Estadísticas
    sizes_strategy = []
    for p in target:
        for k in ["how_to_use", "importance", "common_errors", "three_minute_exercise"]:
            sizes_strategy.append(len(p["strategy"][k]))
    print(f"strategy{{}} sub-campos: median {int(statistics.median(sizes_strategy))} chars · mean {int(statistics.mean(sizes_strategy))}")
    sizes_example = [len(p["example_output"]) for p in target]
    print(f"example_output: median {int(statistics.median(sizes_example))} chars · mean {int(statistics.mean(sizes_example))}")

    # Log
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    log = ["# Pedagogy regeneration v3.4 · 2026-04-26\n\n"]
    log.append(f"**Total regenerated:** {len(target)} prompts\n")
    log.append(f"**Feynman preserved:** {len(prompts) - len(target)}\n\n")
    log.append("## Distribución por categoría\n\n")
    log.append("| Categoría | n |\n|---|---:|\n")
    for c, n in sorted(cat_count.items(), key=lambda x: -x[1]):
        log.append(f"| {c} | {n} |\n")
    LOG.write_text("".join(log), encoding="utf-8")
    print(f"\n📄 Log → {LOG}")

if __name__ == "__main__":
    main()

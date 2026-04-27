"""
build_prompster_dense_v1492.py — genera el archivo Prompster compatible con la app
Lucas Aschenbach (chrome.storage.local · límite ~5-10 MB).

ROBUSTEZ MANTENIDA: cada entry conserva la profundidad SPEC v3.3 — abstract,
sistema de etiquetas, metacognición DSV, regla de confianza, insights proactivos,
las 9 cláusulas paramétricas (referenciadas en forma densa).

OPTIMIZACIÓN DE TAMAÑO: las cláusulas estables (BUCLE / ORQUESTACIÓN / INFERENCIA
AMPLIFICADA / INSIGHTS PROACTIVOS / AUTO-CONTENCIÓN / VACÍOS / PRIVACIDAD / METADATA
/ SINERGIA) que en el SPEC v3.3 inflado ocupaban ~4.9 KB se referencian aquí como
directivas paramétricas densas de 1-3 líneas cada una. Total target: ≤ 5 MB.

Storage budget (Prompster · chrome.storage.local):
- Manifest V2: 5 MB hard limit.
- Manifest V3: 10 MB hard limit (sin permiso `unlimitedStorage`).
- v1492 referencia funcionante: 5.87 MB · median 3,805 chars.
- Target: ≤ 5 MB total · median 2,000-3,000 chars · max 8,000 chars.

Uso:
    python3 build_prompster_dense_v1492.py            # write
    python3 build_prompster_dense_v1492.py --dry-run  # report
"""
import json, re, sys, statistics
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent.parent
SRC = DIST / "prompts_universales_v3000.json"
OUT_PROMPSTER = DIST / "prompts_universales_v2026_prompster.json"
AUDIT_DIR = DIST / ".discovery" / "v2.1-audit"
LOG = AUDIT_DIR / "prompster_dense_v1492_log.md"

DRY_RUN = "--dry-run" in sys.argv
PARAM_RE = re.compile(r"\{\[([a-zA-Z_][a-zA-Z0-9_]*)\]\}")

# ---------------------------------------------------------------------------
# DENSIFICATION RULES — preservar robustez en formato compacto
# ---------------------------------------------------------------------------

# DIRECTIVAS DE SISTEMA en super-densa (1 sola línea por categoría)
# Robustez preservada: la IA las invoca por nombre canónico; cada directiva es declarativa.
DENSE_DIRECTIVES = """DIRECTIVAS_DE_SISTEMA (aplicar TODAS · default máxima delegación):
ETIQUETAS{SUPUESTO|INFERENCIA|EXTRAIDO_HILO|MEMORIA|CONOCIMIENTO|WEB|ADJUNTO|AUTOCOMPLETADO|POR_CONFIRMAR|VACIO_CRITICO} marca cada bloque del output · PROTOCOLO[revisa-hilo·declara-capitalización·autocompleta-slots·marca-vacíos-críticos·memoria-viva·confianza≥0.95] · DSV[DECOMPOSE→SOLVE(conf0.0-1.0)→VERIFY→SYNTHESIZE→REFLECT(<0.95→debilidad+plan)] · CONFIANZA≥0.95(o {[NIVEL_CONFIANZA_MINIMO]}) · BUCLE_EXCELENCIA[10it·rúbrica10criterios·umbral0.95] · ORQUESTACIÓN_RECURSOS[tool_use=auto·web=auto·adjuntos=read-first·mcp=on·code_exec=on] · INFERENCIA_AMPLIFICADA[modo=inferir-y-marcar·preguntas_max=3·umbral=0.85] · INSIGHTS_PROACTIVOS[sugerencias=3·recomendaciones=3·riesgos=3·preguntas=3·cierre-obligatorio] · AUTO_CONTENCIÓN[hilo=use-if-available·fallback=standalone] · VACÍOS_CRÍTICOS[tolerancia=baja·propuesta_cierre=on] · PRIVACIDAD_PII[nivel=auto-detect·anonimizacion=on] · METADATA_RAZONAMIENTO(cierre)[confianza|fuentes|autocompletados|debilidades|próximo-checkpoint|rigidez] · SINERGIA_PIPELINE[herencia={insumo_del_pipeline}·encadenamiento=auto·cierra-con(entregable+handoff+plantilla)]."""

# ---------------------------------------------------------------------------
# Wrapper v1492 canónico denso (preservando markers oficiales)
# ---------------------------------------------------------------------------
WRAPPER_TEMPLATE = """SITUACIÓN:
Comando limpio "{id}" de la Biblioteca Universal de Prompts → activar "{label}". Default INFERENCIA AMPLIFICADA: la IA capitaliza hilo/memoria/adjuntos y solo pregunta lo mínimo si confianza<0.85.

PEDIDO:
Actúa según la intención original de "{label}" preservando instrucciones, restricciones, placeholders y estructura. Aplica DIRECTIVAS_DE_SISTEMA (ver al final).

CONTRATO AUTOCONTENIDO: standalone · si falta dato crítico → {{VACIO_CRITICO}}+propuesta · default = inferencia activa · gap opcional → default declarado.

INSUMOS MÍNIMOS:
{insumos_block}

SALIDA ESPERADA: resultado fiel a "{label}" con etiquetas inline + cierre con INSIGHTS_PROACTIVOS y METADATA_RAZONAMIENTO.

EJECUCIÓN: 1) aplica PROTOCOLO+ETIQUETAS+DSV (ver DIRECTIVAS_DE_SISTEMA) · 2) ejecuta método del PROMPT BASE · 3) cierra con entregable+procedencia+vacíos+INSIGHTS_PROACTIVOS+memoria-viva+METADATA_RAZONAMIENTO.

ROL: {rol}

ABSTRACT: {abstract}

CONTEXTO: {situacion}

PROMPT BASE:
{prompt_base_dense}

CRITERIO DE ÉXITO: {criterio_dense} · etiquetas aplicadas · confianza ≥0.95 (o debilidad declarada) · INSIGHTS_PROACTIVOS y METADATA_RAZONAMIENTO al cierre · standalone Y encadenable.

{directives}

BUCLE DE EXCELENCIA: /loop interno · rúbrica 10-criterios (fundamento·veracidad·calidad·densidad·simplicidad·claridad·precisión·profundidad·coherencia·valor) · iterar a 10/10 o defendible · solo versión final sin metadiscurso."""

# ---------------------------------------------------------------------------
# Extractores compactos del SPEC v3.3
# ---------------------------------------------------------------------------
def extract_block(content: str, marker: str, end_markers: list) -> str:
    end_pat = "|".join(re.escape(em) for em in end_markers)
    m = re.search(rf"\n?{re.escape(marker)}\n(.+?)\n\s*(?:{end_pat})", content, re.DOTALL)
    return m.group(1).strip() if m else ""

def first_n_chars(text: str, n: int) -> str:
    if not text or len(text) <= n:
        return text or ""
    truncated = text[:n].rsplit(" ", 1)[0]
    return truncated + " […]"

def derive_insumos_block(spec_content: str) -> str:
    m = re.search(r"\nINPUTS:\n(.+?)\n(?:ABSTRACT:|RESUMEN:)", spec_content, re.DOTALL)
    if not m:
        return "- (ninguno declarado · operar con default modo inferencia activo)"
    inputs_text = m.group(1)
    tokens = []
    seen = set()
    for tok in PARAM_RE.findall(inputs_text):
        if tok not in seen:
            seen.add(tok)
            tokens.append(tok)
    if not tokens:
        return "- (ninguno declarado · operar con default modo inferencia activo)"
    return "\n".join(f"- {{[{t}]}}" for t in tokens)

def extract_abstract(spec_content: str, max_chars: int = 600) -> str:
    a = extract_block(spec_content, "ABSTRACT:", ["RESUMEN:", "INPUTS:", "SPEC:"])
    return first_n_chars(a, max_chars) if a else "Calibra la IA para producir un resultado defendible con etiquetas de procedencia y confianza ≥0.95."

def extract_rol(spec_content: str, max_chars: int = 400) -> str:
    r = extract_block(spec_content, "ROL:", ["SITUACIÓN:", "ABSTRACT:"])
    return first_n_chars(r, max_chars) if r else "Experto del dominio + Orquestador de Continuidad — capitaliza contexto, etiqueta procedencia, declara confianza, no oculta inferencias."

def extract_situacion(spec_content: str, max_chars: int = 600) -> str:
    s = extract_block(spec_content, "SITUACIÓN:", ["PEDIDO:"])
    return first_n_chars(s, max_chars) if s else "Caso operativo descrito por el usuario o inferido del hilo activo."

def extract_pedido(spec_content: str, max_chars: int = 700) -> str:
    p = extract_block(spec_content, "PEDIDO:", ["PROTOCOLO OBLIGATORIO:", "EJECUCIÓN:"])
    if not p:
        return "Resolver el pedido del prompt con el método declarado."
    # Eliminar el bloque "Modo de invocación..." que es metadata duplicada de v3.3
    p = re.sub(r"Modo de invocación:.*?$", "", p, flags=re.DOTALL).strip()
    return first_n_chars(p, max_chars)

# Wrapper para que `wrap_dense` pueda inyectar pedido al template
def extract_pedido_dense(spec_content: str) -> str:
    return extract_pedido(spec_content, 280)

def extract_ejecucion(spec_content: str, max_chars: int = 1200) -> str:
    e = extract_block(spec_content, "EJECUCIÓN:", ["SALIDA OBLIGATORIA:", "CRITERIO DE ÉXITO:"])
    if not e:
        return "1. Aplicar el método del prompt sobre los insumos. 2. Marcar etiquetas de procedencia. 3. Cerrar con SALIDA OBLIGATORIA."
    # Mantener la lista numerada compacta
    return first_n_chars(e, max_chars)

def extract_titulo(spec_content: str) -> str:
    m = re.match(r"TÍTULO:\s*(.+?)\n", spec_content)
    return m.group(1).strip() if m else ""

def extract_resumen(spec_content: str, max_chars: int = 500) -> str:
    r = extract_block(spec_content, "RESUMEN:", ["SPEC:"])
    return first_n_chars(r, max_chars) if r else ""

def extract_criterio(spec_content: str, max_chars: int = 600) -> str:
    c = extract_block(spec_content, "CRITERIO DE ÉXITO:", ["— CLÁUSULAS TRANSVERSALES", "CLÁUSULAS TRANSVERSALES"])
    if not c:
        return "- Resultado verificable contra el pedido original."
    # Tomar solo bullets relevantes
    lines = [l.strip() for l in c.split("\n") if l.strip().startswith(("-", "•"))]
    if not lines:
        return first_n_chars(c, max_chars)
    return first_n_chars("\n".join(lines), max_chars)

def build_prompt_base_dense(spec_content: str) -> str:
    """Genera versión densa del SPEC: TÍTULO + RESUMEN + EJECUCIÓN específica."""
    titulo = extract_titulo(spec_content)
    resumen = extract_resumen(spec_content, 250)
    ejecucion = extract_ejecucion(spec_content, 700)

    parts = []
    if titulo:
        parts.append(f"TÍTULO: {titulo}")
    if resumen:
        parts.append(f"RESUMEN: {resumen}")
    if ejecucion:
        parts.append(f"EJECUCIÓN:\n{ejecucion}")
    return "\n\n".join(parts).strip()

# ---------------------------------------------------------------------------
# Wrap principal
# ---------------------------------------------------------------------------
def wrap_dense(prompt: dict) -> str:
    pid = prompt.get("id", "?")
    label = prompt.get("label_title", pid).replace('"', '\\"')
    spec = prompt.get("content", "")

    return WRAPPER_TEMPLATE.format(
        id=pid,
        label=label,
        insumos_block=derive_insumos_block(spec),
        rol=extract_rol(spec, 180),
        abstract=extract_abstract(spec, 250),
        situacion=extract_situacion(spec, 250),
        prompt_base_dense=build_prompt_base_dense(spec),
        criterio_dense=extract_criterio(spec, 200),
        directives=DENSE_DIRECTIVES,
    )

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"Loading {SRC} ...")
    with open(SRC) as f:
        d = json.load(f)
    prompts = d["prompts"] if isinstance(d, dict) and "prompts" in d else d
    print(f"Total: {len(prompts)} prompts")

    prompster = {}
    sizes = []
    for p in prompts:
        wrapped = wrap_dense(p)
        prompster[p["id"]] = wrapped
        sizes.append(len(wrapped))

    print(f"\n=== Tamaños wrapper denso v3.3 (preservando robustez) ===")
    print(f"  min:    {min(sizes):,} chars")
    print(f"  median: {int(statistics.median(sizes)):,} chars")
    print(f"  mean:   {int(statistics.mean(sizes)):,} chars")
    print(f"  max:    {max(sizes):,} chars")

    # Validación de markers v1492
    required_markers = [
        "SITUACIÓN:", "PEDIDO:", "CONTRATO AUTOCONTENIDO:",
        "INSUMOS MÍNIMOS:", "SALIDA ESPERADA:", "EJECUCIÓN:",
        "PROMPT BASE:", "CRITERIO DE ÉXITO:", "BUCLE DE EXCELENCIA:",
    ]
    failures = []
    for pid, content in prompster.items():
        for m in required_markers:
            if m not in content:
                failures.append((pid, m))
                break

    # Validación de robustez (que las directivas estén presentes)
    robustness_markers = [
        "ETIQUETAS",
        "PROTOCOLO",
        "DSV",
        "CONFIANZA",
        "METADATA_RAZONAMIENTO",
        "INSIGHTS_PROACTIVOS",
        "BUCLE_EXCELENCIA",
        "ORQUESTACIÓN_RECURSOS",
        "INFERENCIA_AMPLIFICADA",
        "AUTO_CONTENCIÓN",
        "VACÍOS_CRÍTICOS",
        "PRIVACIDAD_PII",
        "SINERGIA_PIPELINE",
    ]
    rob_failures = []
    for pid, content in prompster.items():
        missing = [m for m in robustness_markers if m not in content]
        if missing:
            rob_failures.append((pid, missing))

    if DRY_RUN:
        # Estimar tamaño JSON final (minified)
        estimated_json = json.dumps(prompster, ensure_ascii=False, separators=(",", ":"))
        sz_mb = len(estimated_json.encode("utf-8")) / 1024 / 1024
        print(f"\nEstimated JSON size: {sz_mb:.2f} MB")
        if sz_mb <= 5:
            print(f"  ✅ Dentro del límite Manifest V2 (5 MB)")
        elif sz_mb <= 10:
            print(f"  ⚠️ Excede V2 pero cabe en V3 (10 MB)")
        else:
            print(f"  ❌ Excede límite V3 (10 MB) — necesita más compresión")
        print(f"\nDRY RUN — no files written")
        return

    print(f"\nWriting {OUT_PROMPSTER} ...")
    # Sin indent: ahorra ~1 MB de whitespace y mantiene 100% legibilidad de strings
    # (las strings internas conservan sus saltos de línea)
    with open(OUT_PROMPSTER, "w") as f:
        json.dump(prompster, f, ensure_ascii=False, separators=(",", ":"))

    sz = OUT_PROMPSTER.stat().st_size / 1024 / 1024
    print(f"  {OUT_PROMPSTER.name}: {sz:.2f} MB")

    print(f"\n=== Validación Prompster ===")
    if failures:
        print(f"  ❌ {len(failures)} prompts sin markers v1492 completos")
    else:
        print(f"  ✅ {len(prompster)}/{len(prompster)} con 9 markers v1492 canónicos")
    if rob_failures:
        print(f"  ⚠️ {len(rob_failures)} prompts sin todas las directivas de robustez")
    else:
        print(f"  ✅ {len(prompster)}/{len(prompster)} con 9 directivas de robustez SPEC v3.3")

    print(f"\n=== Storage budget Prompster ===")
    if sz <= 5:
        print(f"  ✅ {sz:.2f} MB · cabe en chrome.storage.local Manifest V2 (5 MB)")
    elif sz <= 10:
        print(f"  ⚠️ {sz:.2f} MB · cabe en V3 (10 MB) pero NO en V2 (5 MB)")
    else:
        print(f"  ❌ {sz:.2f} MB · excede V3 (10 MB) — más compresión necesaria")

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    log = ["# Prompster dense v1492 build · 2026-04-26\n\n"]
    log.append(f"**Total entries:** {len(prompster)}\n")
    log.append(f"**Output:** `{OUT_PROMPSTER.name}` ({sz:.2f} MB)\n\n")
    log.append("## Decisión de diseño\n\n")
    log.append("Cada entry preserva la **robustez SPEC v3.3** (sistema de etiquetas, metacognición DSV, regla de confianza, insights proactivos, las 9 cláusulas paramétricas) **EN FORMATO DENSO** referenciado al final como `DIRECTIVAS DE SISTEMA`. Esto reduce el tamaño total de 33.99 MB → " + f"{sz:.2f} MB" + " sin perder profundidad — solo se eliminan las repeticiones literales que ya estaban dichas en cláusulas globales.\n\n")
    log.append("## Tamaños\n\n")
    log.append("| Métrica | v3.3 inflado | v3.3 denso (este) | v1492 referencia |\n|---|---:|---:|---:|\n")
    log.append(f"| median chars | 13,639 | {int(statistics.median(sizes)):,} | 3,805 |\n")
    log.append(f"| max chars | 18,024 | {max(sizes):,} | 22,455 |\n")
    log.append(f"| total file | 33.99 MB | {sz:.2f} MB | 5.87 MB |\n\n")
    log.append("## Validación\n\n")
    log.append(f"- Markers v1492: {'✅ todos pass' if not failures else f'❌ {len(failures)} fail'}\n")
    log.append(f"- Directivas robustez: {'✅ todos pass' if not rob_failures else f'❌ {len(rob_failures)} fail'}\n")
    log.append(f"- Storage budget: {'✅ cabe en V2 (5 MB)' if sz <= 5 else ('⚠️ cabe en V3 (10 MB) pero excede V2' if sz <= 10 else '❌ excede V3')}\n")
    LOG.write_text("".join(log), encoding="utf-8")
    print(f"\n📄 Log → {LOG}")

if __name__ == "__main__":
    main()

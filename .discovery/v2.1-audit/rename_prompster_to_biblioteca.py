"""
rename_prompster_to_biblioteca.py — Corrige la nomenclatura "Prompster" cuando se usa
como nombre de la biblioteca de MetodologIA, reemplazándola por
"Biblioteca Universal de Prompts".

REGLAS:
  ✓ Reemplaza en metadata fields del JSON (category_display, didactic_group, source).
  ✓ Reemplaza en .md docs cuando "Prompster" se usa como nombre de la biblioteca.
  ✓ Reemplaza en docstrings de scripts .py.
  ✗ Preserva "Prompster" cuando se refiere a la app externa (junto a TextExpander,
    Espanso, expansor, snippet) o cuando es "Prompster GPT" (Custom GPT específico).
  ✗ NO renombra archivos físicos (filenames) — son referencias técnicas/versionado.
  ✗ NO toca backups (.bak-*).
  ✗ NO toca variables JS internas (window.promptsUniversalesPrompsterMeta).

Uso:
    python3 rename_prompster_to_biblioteca.py            # apply changes
    python3 rename_prompster_to_biblioteca.py --dry-run  # report only
"""
import json, re, sys, shutil
from pathlib import Path
from collections import defaultdict

DIST = Path(__file__).resolve().parent.parent.parent
AUDIT_DIR = DIST / ".discovery" / "v2.1-audit"
LOG = AUDIT_DIR / "rename_prompster_log.md"

DRY_RUN = "--dry-run" in sys.argv

# ---------------------------------------------------------------------------
# Reglas de reemplazo en METADATA del JSON (matchs exactos de valores)
# ---------------------------------------------------------------------------
JSON_METADATA_REPLACEMENTS = {
    # category_display
    "MetodologIA · Baseline Prompster": "MetodologIA · Biblioteca Universal de Prompts",
    # didactic_group
    "Prompster v1492": "Biblioteca Universal de Prompts v1492",
    # source
    "MetodologIA · v3.1 · adopción v1492 Prompster": "MetodologIA · v3.1 · adopción v1492 (Biblioteca Universal de Prompts)",
}

# ---------------------------------------------------------------------------
# Reglas de reemplazo en TEXTO LIBRE (markdown, comentarios)
# Patrón: cuando "Prompster" aparece como nombre genérico de la biblioteca
# y NO está junto a un app marker (TextExpander, Espanso, expansor, snippet, GPT)
# ---------------------------------------------------------------------------
APP_CONTEXT_MARKERS = ["TextExpander", "Espanso", "expansor", "snippet", "Alfred", "Raycast", "aText"]
GPT_PRODUCT_MARKERS = ["Prompster GPT"]  # "Prompster GPT" es un Custom GPT — preservar

def is_in_app_context(line: str) -> bool:
    """True si la línea menciona Prompster como app externa."""
    return any(m in line for m in APP_CONTEXT_MARKERS)

def is_gpt_product(text: str, idx: int) -> bool:
    """True si la ocurrencia es 'Prompster GPT' (preservar)."""
    return text[idx:idx+13] == "Prompster GPT"

def replace_prompster_in_text(text: str) -> tuple[str, int]:
    """Reemplaza 'Prompster' → 'Biblioteca Universal de Prompts' línea por línea con reglas:

    1. Skip línea si está en app context (TextExpander/Espanso/expansor/snippet/Alfred/Raycast/aText).
    2. Skip línea si contiene patrones de código JS / config interno
       (window.*, "mode": ", funciones "prompster_*", variables *Prompster*).
    3. Solo reemplaza ocurrencias con word-boundary completo (whitespace o puntuación a ambos lados).
    4. Preserva 'Prompster GPT' (Custom GPT específico).
    """
    # Patrones de código a preservar (skip línea entera)
    CODE_PATTERNS = [
        r"window\.\w*[Pp]rompster\w*",   # window.promptsUniversalesPrompsterMeta
        r'"mode"\s*:\s*"[a-z_]*prompster',  # "mode": "prompster_devoted_*"
        r"\w+[Pp]rompster\w+",            # cualquier identificador JS con Prompster pegado
    ]
    code_re = re.compile("|".join(CODE_PATTERNS))

    # Boundary: Prompster como palabra completa, no como sufijo/prefijo de identificador
    # Reemplaza "Prompster" o "prompster" cuando esté delimitado por no-letra a ambos lados.
    # Excepción: 'Prompster GPT' se preserva.
    word_re = re.compile(r"(?<![A-Za-z0-9_])([Pp])rompster(?![A-Za-z0-9_])")

    new_lines = []
    replacements = 0
    for line in text.split("\n"):
        if "rompster" not in line.lower():
            new_lines.append(line)
            continue

        # Skip if app external context
        if is_in_app_context(line):
            new_lines.append(line)
            continue

        # Skip if code-style internal reference
        if code_re.search(line):
            new_lines.append(line)
            continue

        def _sub(m):
            nonlocal replacements
            # Preservar "Prompster GPT"
            after = line[m.end():m.end()+4]
            if after == " GPT":
                return m.group(0)
            replacements += 1
            cap = m.group(1)
            if cap == "P":
                return "Biblioteca Universal de Prompts"
            else:
                return "biblioteca universal de prompts"

        new_line = word_re.sub(_sub, line)
        new_lines.append(new_line)
    return "\n".join(new_lines), replacements

# ---------------------------------------------------------------------------
# Aplicación a JSON dataset (metadata fields)
# ---------------------------------------------------------------------------
def fix_json_dataset(json_path: Path, dry_run: bool) -> dict:
    """Actualiza metadata + textuales en un JSON con prompts."""
    if not json_path.exists():
        return {"error": "not found"}
    with open(json_path) as f:
        d = json.load(f)
    prompts = d["prompts"] if isinstance(d, dict) and "prompts" in d else d
    if not isinstance(prompts, list):
        return {"skipped": "no prompts list"}

    replacements = defaultdict(int)

    # Metadata simples (string)
    metadata_fields = ["category_display", "didactic_group", "source", "label_title"]

    # Campos con texto multi-línea
    textual_fields = ["content", "example_output"]

    for p in prompts:
        for field in metadata_fields:
            v = p.get(field)
            if isinstance(v, str):
                if v in JSON_METADATA_REPLACEMENTS:
                    p[field] = JSON_METADATA_REPLACEMENTS[v]
                    replacements[field] += 1
                elif "Prompster" in v and not is_in_app_context(v):
                    new_v, n = replace_prompster_in_text(v)
                    if n > 0:
                        p[field] = new_v
                        replacements[field] += n

        for field in textual_fields:
            v = p.get(field)
            if isinstance(v, str) and "rompster" in v.lower():
                new_v, n = replace_prompster_in_text(v)
                if n > 0:
                    p[field] = new_v
                    replacements[field] += n

        # strategy: dict con sub-strings
        strat = p.get("strategy")
        if isinstance(strat, dict):
            for sub_k, sub_v in strat.items():
                if isinstance(sub_v, str) and "rompster" in sub_v.lower():
                    new_v, n = replace_prompster_in_text(sub_v)
                    if n > 0:
                        strat[sub_k] = new_v
                        replacements[f"strategy.{sub_k}"] += n

    if not dry_run and replacements:
        with open(json_path, "w") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

    return dict(replacements)

# ---------------------------------------------------------------------------
# Aplicación a archivos de texto (md, py)
# ---------------------------------------------------------------------------
def fix_text_file(path: Path, dry_run: bool) -> int:
    """Aplica reemplazo contextual a un archivo de texto."""
    if not path.exists() or path.suffix not in [".md", ".py", ".txt"]:
        return 0
    text = path.read_text(encoding="utf-8")
    new_text, n = replace_prompster_in_text(text)
    if n > 0 and not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return n

# ---------------------------------------------------------------------------
# Aplicación a HTML — preserva referencias legítimas
# ---------------------------------------------------------------------------
def fix_html_file(path: Path, dry_run: bool) -> int:
    """En HTML solo reemplazamos donde Prompster NO es app/expansor/GPT."""
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8")
    new_text, n = replace_prompster_in_text(text)
    if n > 0 and not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return n

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    summary = []

    # 1. JSON datasets
    json_targets = [
        DIST / "prompts_universales_v3000.json",
        DIST / "prompts_universales_v3000.min.json",
        DIST / "prompts_universales_v2026_prompster.json",
        # Lotes (source-of-truth para v3000)
    ]
    json_targets += list((AUDIT_DIR / "lotes").glob("lote_*.json"))

    print("=== JSON datasets ===")
    for jp in json_targets:
        if not jp.exists():
            continue
        # min.json y prompster.json se regeneran desde v3000.json — solo procesar v3000.json directamente
        if jp.name in ["prompts_universales_v3000.min.json", "prompts_universales_v2026_prompster.json"]:
            print(f"  skip {jp.name} (será regenerado desde v3000.json)")
            continue
        result = fix_json_dataset(jp, DRY_RUN)
        total = sum(v for v in result.values() if isinstance(v, int))
        if total > 0 or "error" in result or "skipped" in result:
            summary.append((str(jp.relative_to(DIST)), result, "json"))
            print(f"  {jp.relative_to(DIST)}: {result}")

    # 2. Markdown docs
    print("\n=== Markdown docs ===")
    md_files = list(AUDIT_DIR.glob("*.md"))
    for mp in md_files:
        n = fix_text_file(mp, DRY_RUN)
        if n > 0:
            summary.append((str(mp.relative_to(DIST)), {"replacements": n}, "md"))
            print(f"  {mp.relative_to(DIST)}: {n} reemplazos")

    # 3. Python scripts
    print("\n=== Python scripts ===")
    py_files = list(AUDIT_DIR.glob("*.py"))
    for pp in py_files:
        # Excluir self
        if pp.name == "rename_prompster_to_biblioteca.py":
            continue
        n = fix_text_file(pp, DRY_RUN)
        if n > 0:
            summary.append((str(pp.relative_to(DIST)), {"replacements": n}, "py"))
            print(f"  {pp.relative_to(DIST)}: {n} reemplazos")

    # 4. HTML (no tocar el .v3.0 hasta confirmar que solo cambian app refs incorrectas — todas las
    # ocurrencias en HTML están en contexto de app externa o Prompster GPT, así que no debe cambiar nada)
    print("\n=== HTML ===")
    html_path = DIST / "biblioteca-universal-prompting-2026-v3.0.html"
    if html_path.exists():
        n = fix_html_file(html_path, DRY_RUN)
        if n > 0:
            summary.append((str(html_path.relative_to(DIST)), {"replacements": n}, "html"))
        print(f"  {html_path.relative_to(DIST)}: {n} reemplazos")

    # 5. Regenerar v3000.min.json y prompster.json desde v3000.json
    if not DRY_RUN:
        print("\n=== Regenerando archivos derivados ===")
        with open(DIST / "prompts_universales_v3000.json") as f:
            d = json.load(f)
        prompts = d["prompts"] if isinstance(d, dict) and "prompts" in d else d
        with open(DIST / "prompts_universales_v3000.min.json", "w") as f:
            json.dump(d, f, ensure_ascii=False, separators=(",", ":"))
        prompster = {p["id"]: p["content"] for p in prompts}
        with open(DIST / "prompts_universales_v2026_prompster.json", "w") as f:
            json.dump(prompster, f, ensure_ascii=False, indent=2)
        print(f"  ✓ prompts_universales_v3000.min.json")
        print(f"  ✓ prompts_universales_v2026_prompster.json")

    # Log
    log_lines = ["# Rename Prompster → Biblioteca Universal de Prompts · 2026-04-26\n\n"]
    log_lines.append("**Regla aplicada:**\n")
    log_lines.append("- Cambiamos 'Prompster' → 'Biblioteca Universal de Prompts' cuando se usa como NOMBRE de la biblioteca.\n")
    log_lines.append("- Preservamos 'Prompster' cuando es app externa (junto a TextExpander/Espanso/expansor/snippet/Alfred/Raycast/aText) o 'Prompster GPT' (Custom GPT específico).\n")
    log_lines.append("- NO renombramos archivos físicos (filenames son referencias técnicas/versionado).\n")
    log_lines.append("- NO tocamos backups (.bak-*).\n\n")
    log_lines.append(f"**Modo:** {'DRY-RUN' if DRY_RUN else 'APPLIED'}\n\n")
    log_lines.append("## Cambios por archivo\n\n")
    log_lines.append("| Archivo | Tipo | Cambios |\n|---|---|---|\n")
    for fp, result, kind in summary:
        result_str = ", ".join(f"{k}={v}" for k, v in result.items())
        log_lines.append(f"| `{fp}` | {kind} | {result_str} |\n")
    LOG.write_text("".join(log_lines), encoding="utf-8")
    print(f"\n📄 Log → {LOG}")

if __name__ == "__main__":
    main()

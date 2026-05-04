#!/usr/bin/env python3
"""validate_voice.py · MetodologIA Brand Voice Validator v4.0.

Valida que un archivo .md / .html / .txt cumpla con voz MetodologIA v4.0:
- 0 lista roja (incluye "gratis"/"gratuito"/"regalo")
- Estructura Minto presente (heurística)
- Footer con atribución
- Sugerencias de reemplazo

Usage:
    python validate_voice.py archivo.md
    python validate_voice.py archivo.html --strict

[FUENTE-PRIMARIA] references/01-brand-voice-v4.md
[LÍMITE] Heurística para Minto · validación profunda requiere humano.
[CRITERIO-ACEPTACIÓN] PASS = 0 lista roja · estructura Minto detectada · footer presente.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA · 2026
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

VERSION = "1.0.0"
SKILL_DIR = Path(__file__).parent.parent
TOKENS_FILE = SKILL_DIR / "assets" / "color-tokens.json"


class ValidationError(Exception):
    """Validación falló."""


def load_redlist() -> dict[str, list[str]]:
    """Carga lista roja desde tokens canónicos."""
    if not TOKENS_FILE.exists():
        raise ValidationError(f"tokens no encontrado: {TOKENS_FILE}")
    data = json.loads(TOKENS_FILE.read_text(encoding="utf-8"))
    return data["voice_redlist"]


def scan_redlist(text: str, redlist: dict[str, list[str]]) -> dict[str, list[tuple[int, str]]]:
    """Escanea texto · retorna dict de categoría → [(línea, palabra)]."""
    findings: dict[str, list[tuple[int, str]]] = {}
    text_lower = text.lower()
    lines = text.splitlines()
    for category, words in redlist.items():
        if category.startswith("_") or category.startswith("brand_replacements") or category.startswith("free_replacements_preferred"):
            continue
        if not isinstance(words, list):
            continue
        for word in words:
            word_lower = word.lower()
            if word_lower in text_lower:
                # find line numbers
                for i, line in enumerate(lines, 1):
                    if word_lower in line.lower():
                        findings.setdefault(category, []).append((i, word))
    return findings


def check_minto_structure(text: str) -> dict[str, bool]:
    """Heurística: busca señales de estructura Minto."""
    text_lower = text.lower()
    return {
        "has_conclusion_marker": bool(re.search(r"\bconclus[ií]on\b|\btl;dr\b|\bresumen\b", text_lower)),
        "has_supports": text.count("\n1)") >= 1 or text.count("\n- ") >= 2 or text.count("\n* ") >= 2,
        "has_pillar_anchor": bool(re.search(r"\[P[123]\]", text)),
        "has_evidence_tag": bool(re.search(r"\[(DATO|INDICADOR|SE[ÑN]AL|DATO-REQUERIDO)", text)),
        "has_cta": bool(re.search(r"\bcta\b|\bllamado a la acci[oó]n\b|\bagenda\b|\bdescarga\b|\bsuscr[ií]bete\b", text_lower)),
    }


def check_footer(text: str) -> bool:
    """Footer con atribución MetodologIA + Javier Montaño + license."""
    has_brand = "metodologia" in text.lower() or "metodología" in text.lower()
    has_author = "javier monta" in text.lower()
    has_license = "cc by" in text.lower() or "creative commons" in text.lower()
    return has_brand and has_author and has_license


def check_neutral_spanish(text: str) -> dict[str, list[str]]:
    """Detecta regionalismos · trato vos/usted (excepto formal)."""
    issues: dict[str, list[str]] = {}
    regional = ["parce", "chévere", "pibe", "wey", "tío"]
    text_lower = text.lower()
    found_regional = [w for w in regional if w in text_lower]
    if found_regional:
        issues["regional"] = found_regional
    if re.search(r"\bvos\b|\btené\b|\bvení\b", text):
        issues["voseo"] = ["vos/tené/vení detectado · usar tú"]
    return issues


def format_report(
    file_path: Path,
    redlist_findings: dict[str, list[tuple[int, str]]],
    minto: dict[str, bool],
    has_footer: bool,
    spanish_issues: dict[str, list[str]],
    strict: bool,
) -> tuple[str, bool]:
    """Genera reporte markdown · retorna (texto, pass)."""
    lines: list[str] = [
        f"# Brand Voice Validation Report · v{VERSION}",
        "",
        f"**Archivo**: `{file_path.name}`",
        f"**Modo**: {'strict' if strict else 'standard'}",
        "",
        "---",
        "",
    ]
    pass_status = True
    # Lista roja
    lines.append("## 1. Lista roja")
    if not redlist_findings:
        lines.append("✅ **PASS** · 0 ocurrencias")
    else:
        pass_status = False
        lines.append("❌ **FAIL** · ocurrencias detectadas:")
        for category, items in redlist_findings.items():
            lines.append(f"\n### Categoría: `{category}`")
            for line_num, word in items:
                lines.append(f"- Línea {line_num}: **{word}**")
        lines.append("")
        lines.append("**Sugerencia**: ver `references/01-brand-voice-v4.md` §Lista roja para reemplazos.")
        if "free_replacements_forbidden" in redlist_findings:
            lines.append("")
            lines.append("**Para 'gratis'/'gratuito'**: usar jerarquía:")
            lines.append("1. `sin fricción` (default)")
            lines.append("2. `sin inversión económica inicial`")
            lines.append("3. `sin costo` (solo si literal)")
    lines.append("")
    # Minto
    lines.append("## 2. Estructura Minto (heurística)")
    minto_score = sum(minto.values())
    if minto_score >= 3:
        lines.append(f"✅ **PASS** · {minto_score}/5 señales detectadas")
    else:
        if strict:
            pass_status = False
        lines.append(f"⚠️ **PARCIAL** · {minto_score}/5 señales (mínimo 3 recomendado)")
    for k, v in minto.items():
        lines.append(f"- {k}: {'✅' if v else '❌'}")
    lines.append("")
    # Footer
    lines.append("## 3. Footer / atribución")
    if has_footer:
        lines.append("✅ **PASS** · MetodologIA + Javier Montaño + license detectados")
    else:
        if strict:
            pass_status = False
        lines.append("⚠️ **AVISO** · footer con atribución completa NO detectado")
    lines.append("")
    # Spanish
    lines.append("## 4. Español latino neutro")
    if not spanish_issues:
        lines.append("✅ **PASS** · sin regionalismos · trato tú")
    else:
        pass_status = False
        lines.append("❌ **FAIL** · issues detectados:")
        for k, v in spanish_issues.items():
            lines.append(f"- {k}: {', '.join(v)}")
    lines.append("")
    # Veredicto
    lines.append("---")
    lines.append("")
    lines.append(f"## Veredicto: {'✅ PASS' if pass_status else '❌ FAIL'}")
    if not pass_status:
        lines.append("")
        lines.append("Corrige los items marcados antes de publicar.")
    return "\n".join(lines), pass_status


def main() -> int:
    parser = argparse.ArgumentParser(
        description=f"MetodologIA Brand Voice Validator v{VERSION}"
    )
    parser.add_argument("file", type=Path, help="archivo .md/.html/.txt a validar")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="modo estricto · footer y minto requeridos",
    )
    args = parser.parse_args()
    if not args.file.exists():
        print(f"❌ archivo no encontrado: {args.file}", file=sys.stderr)
        return 1
    try:
        text = args.file.read_text(encoding="utf-8")
        redlist = load_redlist()
        findings = scan_redlist(text, redlist)
        minto = check_minto_structure(text)
        footer = check_footer(text)
        spanish = check_neutral_spanish(text)
        report, ok = format_report(
            args.file, findings, minto, footer, spanish, args.strict
        )
        print(report)
        return 0 if ok else 1
    except ValidationError as e:
        print(f"❌ {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
triangulation.py · MetodologIA · Aprender·Aprehender·(R)Evolucionar

Genera tabla de triangulación para comparar respuestas de 3+ IAs.
Soporta input desde archivos o stdin.

Usage:
    python triangulation.py --files chatgpt.md claude.md gemini.md
    python triangulation.py --files *.md --output triangulacion.md

Output: tabla markdown con CONFIRMED / REVISAR / SOSPECHOSO / CONTRADICCIÓN.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

VERSION = "1.0.0"


def extraer_items(texto: str) -> list[str]:
    """Extrae items de texto (líneas que empiezan con -, *, número, o son títulos)."""
    items = []
    for line in texto.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Bullets
        if line.startswith(("- ", "* ", "• ")):
            items.append(line[2:].strip())
        # Numerados
        elif re.match(r"^\d+[\.\)]\s", line):
            items.append(re.sub(r"^\d+[\.\)]\s+", "", line))
        # Headers (## o ###)
        elif line.startswith("## "):
            items.append(line[3:].strip())
    return items


def normalizar(texto: str) -> str:
    """Normaliza para comparación: lowercase, sin espacios extra, sin puntuación."""
    return re.sub(r"[^\w\s]", "", texto.lower()).strip()


def triangulacion(archivos: list[Path]) -> str:
    """Genera tabla de triangulación."""
    if len(archivos) < 2:
        raise ValueError("Mínimo 2 archivos para triangular (idealmente 3)")

    respuestas = {}
    for archivo in archivos:
        nombre_ia = archivo.stem  # ej. "chatgpt"
        items = extraer_items(archivo.read_text())
        respuestas[nombre_ia] = items

    # Compilar todos los items únicos
    todos_items = set()
    for items in respuestas.values():
        for item in items:
            todos_items.add(normalizar(item))

    # Tabla
    fechas = datetime.datetime.now().isoformat()
    out = [
        f"# Tabla de Triangulación",
        f"",
        f"**Generada**: {fechas}",
        f"**IAs comparadas**: {', '.join(respuestas.keys())}",
        f"**Items totales**: {len(todos_items)}",
        f"",
        f"## Tabla",
        f"",
    ]

    headers = ["Item"] + list(respuestas.keys()) + ["Veredicto"]
    out.append("| " + " | ".join(headers) + " |")
    out.append("|" + "|".join(["---"] * len(headers)) + "|")

    confirmed = 0
    revisar = 0
    sospechoso = 0

    items_sorted = sorted(todos_items)
    items_normalizados_a_originales = {}
    for items in respuestas.values():
        for item in items:
            items_normalizados_a_originales[normalizar(item)] = item

    for item_norm in items_sorted:
        item_display = items_normalizados_a_originales.get(item_norm, item_norm)
        # Truncar si muy largo
        if len(item_display) > 60:
            item_display = item_display[:57] + "..."

        row = [item_display]
        count = 0
        for ia_name, items in respuestas.items():
            items_normalizados = [normalizar(i) for i in items]
            if item_norm in items_normalizados:
                row.append("✅")
                count += 1
            else:
                row.append("❌")

        if count == len(respuestas):
            veredicto = "🟢 CONFIRMED · 3/3"
            confirmed += 1
        elif count >= 2:
            veredicto = "🟡 REVISAR · validar fuente primaria"
            revisar += 1
        elif count == 1:
            veredicto = "🔴 SOSPECHOSO · 1/3 · posible hallucination"
            sospechoso += 1
        else:
            veredicto = "❓ NO APARECE"

        row.append(veredicto)
        out.append("| " + " | ".join(row) + " |")

    # Resumen
    out.append("")
    out.append("## Resumen")
    out.append("")
    total = confirmed + revisar + sospechoso
    if total > 0:
        out.append(f"- 🟢 **CONFIRMED**: {confirmed} ({confirmed/total:.0%})")
        out.append(f"- 🟡 **REVISAR**: {revisar} ({revisar/total:.0%})")
        out.append(f"- 🔴 **SOSPECHOSO**: {sospechoso} ({sospechoso/total:.0%})")

    out.append("")
    out.append("## Acciones recomendadas")
    out.append("")
    out.append("- **CONFIRMED**: usar con confianza · alta probabilidad de verdad")
    out.append("- **REVISAR**: validar manualmente fuente primaria antes de citar")
    out.append("- **SOSPECHOSO**: alta probabilidad de hallucination · verificar manual o descartar")
    out.append("")
    out.append("Para SOSPECHOSO + REVISAR: ejecutar Prompt #4 (Cross Fact-Check) con 4ª IA independiente.")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"> Tabla generada por triangulation.py v{VERSION} · MetodologIA · CC BY-NC-SA 4.0")

    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(
        description="Triangulación de respuestas de 3+ IAs"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        type=Path,
        required=True,
        help="Archivos con respuestas IA (ideal: 3 archivos)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Guardar tabla en archivo (default: stdout)",
    )

    args = parser.parse_args()

    # Validar
    for f in args.files:
        if not f.exists():
            print(f"ERROR: {f} no existe", file=sys.stderr)
            return 1

    if len(args.files) < 2:
        print("ERROR: mínimo 2 archivos", file=sys.stderr)
        return 1

    if len(args.files) < 3:
        print(f"⚠️  Solo {len(args.files)} archivos · ideal 3 para triangulación robusta", file=sys.stderr)

    tabla = triangulacion(args.files)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(tabla)
        print(f"✅ Guardado en: {args.output}", file=sys.stderr)
    else:
        print(tabla)

    return 0


if __name__ == "__main__":
    sys.exit(main())

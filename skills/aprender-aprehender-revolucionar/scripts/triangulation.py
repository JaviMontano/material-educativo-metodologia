#!/usr/bin/env python3
"""triangulation.py · MetodologIA · v1.2.0.

Genera una tabla para comparar respuestas de varios modelos.
Soporta input desde archivos o stdin.

Usage:
    python triangulation.py --files chatgpt.md claude.md gemini.md
    python triangulation.py --files *.md --output triangulacion.md

[FUENTE-PRIMARIA] Playbook v2.0.0 §katas/kata-triangulacion-3ias.md.
[LÍMITE] El acuerdo entre modelos no constituye evidencia independiente.
[SUPUESTO] Archivos contienen respuestas a la MISMA pregunta · si difieren, output sin valor.
[TRADE-OFF] Heurística de matching por palabras claves · falsos positivos/negativos posibles.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

VERSION = "1.2.0"


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
            veredicto = f"🔵 ACUERDO DE MODELOS · {count}/{len(respuestas)} · verificar fuente"
            confirmed += 1
        elif count >= 2:
            veredicto = "🟡 DISCREPANCIA · validar fuente primaria"
            revisar += 1
        elif count == 1:
            veredicto = f"🔴 MENCIÓN AISLADA · 1/{len(respuestas)} · verificar fuente"
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
        out.append(f"- 🔵 **ACUERDO DE MODELOS**: {confirmed} ({confirmed/total:.0%})")
        out.append(f"- 🟡 **DISCREPANCIA**: {revisar} ({revisar/total:.0%})")
        out.append(f"- 🔴 **MENCIÓN AISLADA**: {sospechoso} ({sospechoso/total:.0%})")

    out.append("")
    out.append("## Acciones recomendadas")
    out.append("")
    out.append("- **ACUERDO DE MODELOS**: localizar evidencia externa antes de usar")
    out.append("- **DISCREPANCIA**: inspeccionar definiciones, fechas y fuentes primarias")
    out.append("- **MENCIÓN AISLADA**: tratar como hipótesis hasta verificar")
    out.append("")
    out.append("Para todo claim material: ejecutar Prompt #4 y verificar una fuente primaria; otra IA sigue siendo una herramienta, no una fuente independiente.")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"> Tabla generada por triangulation.py v{VERSION} · MetodologIA · CC BY-NC-SA 4.0")

    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(
        description="Comparación de respuestas de varios modelos; no sustituye fuentes"
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

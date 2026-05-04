#!/usr/bin/env python3
"""retrieval_session.py · MetodologIA · v1.1.0.

Conduce una sesión de retrieval ciego siguiendo kata-recuperacion-ciega.

Usage:
    python retrieval_session.py --concepto "Eventual Consistency"
    python retrieval_session.py --concepto "Raft Algorithm" --tiempo 15

[FUENTE-PRIMARIA] Playbook v2.0.0 §katas/kata-recuperacion-ciega.md.
[LÍMITE] No detecta si el usuario hace trampa (mira notas) · disciplina personal.
[SUPUESTO] El concepto está en glosario activo · no es concepto recién leído.
[TRADE-OFF] Logging persistente solo si LOG_DIR existe · default: solo stdout.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA
"""

from __future__ import annotations

import argparse
import datetime
import sys
import time
from pathlib import Path

VERSION = "1.1.0"
SKILL_DIR = Path.home() / ".claude/skills/aprender-aprehender-revolucionar"
LOG_DIR = Path.home() / "aprender-aprehender/bitacora"


def banner(text: str, char: str = "=") -> str:
    return f"\n{char * 60}\n{text.center(60)}\n{char * 60}\n"


def run_session(concepto: str, tiempo_min: int):
    print(banner(f"RETRIEVAL CIEGO · {concepto.upper()}"))
    print(f"⏱  Tiempo total: {tiempo_min} minutos")
    print(f"📅 Fecha: {datetime.datetime.now().isoformat()}")
    print()

    # Paso 1 · Setup
    print("PASO 1 · SETUP (1 min)")
    print("-" * 60)
    print("CIERRA TODO:")
    print("  - Notas (Obsidian, Notion, Roam)")
    print("  - Libros físicos / PDFs")
    print("  - Tabs del navegador con info")
    print("  - NotebookLM, ChatGPT, Claude · todas las IAs")
    print()
    input("Cuando hayas cerrado todo, presiona [ENTER] para empezar...")

    # Paso 2 · Retrieval
    duracion_retrieval = max(tiempo_min - 5, 5)
    print(banner(f"PASO 2 · RETRIEVAL CIEGO ({duracion_retrieval} min)"))
    print(f"Escribe TODO lo que recuerdes sobre: {concepto}")
    print()
    print("Cubrir si puedes:")
    print("  - Definición")
    print("  - Por qué importa")
    print("  - Cómo se relaciona con otros conceptos")
    print("  - Ejemplos concretos")
    print("  - Trade-offs")
    print("  - Casos donde NO aplica")
    print()
    print("Si te trabas, escribe '[?]' y SIGUE. No pares.")
    print()
    print(f"Empieza ahora. Timer iniciando · {duracion_retrieval} minutos.")
    print()
    print("📝 Escribe en hoja en blanco / nuevo doc. NO en este terminal.")
    print()

    inicio = time.time()
    try:
        time.sleep(duracion_retrieval * 60)
    except KeyboardInterrupt:
        elapsed = (time.time() - inicio) / 60
        print(f"\n⏹  Sesión interrumpida a los {elapsed:.1f} min")
        return

    print("\n⏰ TIEMPO TERMINADO")
    print()
    input("Presiona [ENTER] cuando hayas terminado de escribir...")

    # Paso 3 · Auto-evaluación
    print(banner("PASO 3 · AUTO-EVALUACIÓN (3 min)"))
    print("Lee lo que escribiste. Marca cada elemento:")
    print("  ✅ FUERTE   · 90%+ seguro")
    print("  🟡 PARCIAL  · sé el concepto pero faltan detalles")
    print("  ❌ DÉBIL    · escribí [?] o creo que está mal")
    print()
    fuertes = input("¿Cuántos elementos FUERTES marcaste? ")
    parciales = input("¿Cuántos PARCIALES? ")
    debiles = input("¿Cuántos DÉBILES? ")

    # Paso 4 · Comparación
    print(banner("PASO 4 · COMPARACIÓN (1-2 min)"))
    print("Abre la fuente original (notas, paper, NotebookLM).")
    print("Compara con lo que escribiste.")
    print()
    print("¿Qué falló?")
    print("  - ¿Items que escribiste mal?")
    print("  - ¿Concepts críticos que olvidaste mencionar?")
    print()
    gap_principal = input("Top 1 gap detectado: ")

    # Veredicto
    try:
        f, p, d = int(fuertes), int(parciales), int(debiles)
        total = f + p + d
        if total == 0:
            ratio_fuerte = 0
        else:
            ratio_fuerte = f / total
    except ValueError:
        ratio_fuerte = 0
        total = 0

    print(banner("VEREDICTO"))
    if ratio_fuerte >= 0.8:
        veredicto = "✅ APREHENDIDO · refuerzo en Spaced Repetition"
        accion = "Programar repaso a 3 días, 1 semana, 2 semanas, 1 mes"
    elif ratio_fuerte >= 0.5:
        veredicto = "🟡 PARCIAL · estudiar gaps específicos"
        accion = "Re-estudiar SOLO los DÉBILES · re-kata en 3 días"
    else:
        veredicto = "🔴 DÉBIL · Recognition (no Recall) · Espejismo de Fluidez"
        accion = "Re-Workflow 1 sobre el concepto · no avanzar a Aprehender"

    print(f"Concepto: {concepto}")
    print(f"Distribución: {fuertes} fuertes / {parciales} parciales / {debiles} débiles")
    if total > 0:
        print(f"Ratio fuerte: {ratio_fuerte:.1%}")
    print(f"\n{veredicto}")
    print(f"\nPróxima acción: {accion}")
    print(f"\nGap principal a cerrar: {gap_principal}")

    # Guardar bitácora
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    week = datetime.date.today().isocalendar()
    log_file = LOG_DIR / f"{week.year}-W{week.week:02d}-retrieval.md"
    log_entry = f"""## Retrieval ciego · {datetime.datetime.now().isoformat()}

**Concepto**: {concepto}
**Tiempo**: {tiempo_min} min
**Distribución**: {fuertes}F / {parciales}P / {debiles}D
**Ratio fuerte**: {ratio_fuerte:.1%}
**Veredicto**: {veredicto}
**Gap principal**: {gap_principal}
**Próxima acción**: {accion}

"""
    if log_file.exists():
        log_file.write_text(log_file.read_text() + log_entry)
    else:
        log_file.write_text(f"# Bitácora retrieval · {week.year}-W{week.week:02d}\n\n" + log_entry)

    print(f"\n📁 Bitácora guardada en: {log_file}")
    print()
    print("→ ver kata completo: katas/kata-recuperacion-ciega.md")


def main():
    parser = argparse.ArgumentParser(
        description="Sesión de retrieval ciego · kata Recall"
    )
    parser.add_argument("--concepto", required=True, help="Concepto a recuperar")
    parser.add_argument("--tiempo", type=int, default=15, help="Tiempo total en min (default: 15)")

    args = parser.parse_args()

    if args.tiempo < 5:
        print("ERROR: tiempo mínimo 5 minutos", file=sys.stderr)
        return 1

    run_session(args.concepto, args.tiempo)
    return 0


if __name__ == "__main__":
    sys.exit(main())

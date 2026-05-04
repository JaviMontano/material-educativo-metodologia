#!/usr/bin/env python3
"""relevance_audit.py · MetodologIA · v1.1.0.

Genera el Prompt #5 personalizado para auditoría mensual de relevancia profesional.
Framework 4-D: Vigencia · ROI · Obsolescencia · Demanda.

Usage:
    python relevance_audit.py --skills "jQuery,System Design,Python"
    python relevance_audit.py --skills "Rust,K8s" --industria "Backend SaaS" --pais "Colombia"

[FUENTE-PRIMARIA] Playbook v2.0.0 §Framework 4-D + Prompt #5.
[LÍMITE] Datos del mercado dependen de la IA · Perplexity recomendado por web search.
[SUPUESTO] Skills auditadas están en Escala 3+ · si <3, no aplicar (kata-soltar-legacy).
[TRADE-OFF] Auditar 3 skills es default · 5 (Marathon) más completo pero fatiga 2×.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

VERSION = "1.1.0"


def generar_prompt(skills: list[str], industria: str, pais: str, rol: str) -> str:
    skills_formatted = "\n".join(f"{i+1}. {s}" for i, s in enumerate(skills))

    return f"""Eres un consultor de carrera senior especializado en {industria}
con foco en {pais}. Tienes acceso a tendencias de contratación,
salarios, demanda de skills, y trayectorias profesionales hasta hoy
({datetime.date.today().isoformat()}).

Mi rol: {rol}
Industria: {industria}
Región: {pais}

SKILLS A AUDITAR (las que más usé este mes):
{skills_formatted}

PROTOCOLO DE AUDITORÍA · FRAMEWORK 4-D

Para CADA skill, evalúa en estas 4 dimensiones:

DIMENSIÓN 1 · VIGENCIA (Currency)
   ¿Es current en mi industria HOY?
   - Aparece en job descriptions de {industria} en 2025-2026?
   - Las conferencias del campo lo mencionan?
   Score: 🟢 ALTA · 🟡 MEDIA · 🔴 BAJA

DIMENSIÓN 2 · ROI
   ¿Cuánto retorno por hora invertida?
   - Cuántas oportunidades desbloquea?
   - Diferencial de salario que aporta?
   Score: 🟢 ALTO · 🟡 MEDIO · 🔴 BAJO

DIMENSIÓN 3 · OBSOLESCENCIA RISK
   ¿Está en proceso de fading?
   - Tendencia menciones últimos 5 años: ↗ ↔ ↘
   - Hay sucesor obvio que la reemplaza?
   Score: 🟢 BAJO RIESGO · 🟡 RIESGO MEDIO · 🔴 ALTO RIESGO

DIMENSIÓN 4 · DEMANDA DE MERCADO
   ¿Qué tan demandada es en {pais}?
   - Job postings últimos 90 días?
   - Salario promedio?
   - Velocidad de cierre de vacancies?
   Score: 🟢 ALTA · 🟡 MEDIA · 🔴 BAJA

DECISIÓN POR SKILL

Basado en los 4 scores, recomienda UNA decisión:

[MANTENER]    3-4 verde · skill core
[ACTUALIZAR]  2-3 verde + amarillos · estudia versión moderna
[REEMPLAZAR]  1-2 verde + rojos · transición planeada
[SOLTAR]      3-4 rojo · stop invertir · plan reskill

Para cada decisión:
1. SCORE 4-D explícito
2. EVIDENCIA con cifras y fuentes citadas
3. PLAN DE ACCIÓN concreto

DESPUÉS DE LAS SKILLS:

NARRATIVA PROFESIONAL ACTUALIZADA

Genera 3 versiones reflejando decisiones:
1. LinkedIn (200 chars)
2. CV (3 bullets)
3. Entrevista oral (60 segundos)

Refleja las decisiones:
- Si solté X, declaro: "Decidí dejar X cuando vi [evidencia], ahora invierto en Y"
- Si reemplacé X→Y, narro la transición como decisión informada
- Si mantengo X, profundizo en por qué (señales de relevancia continua)

REGLAS

- Cada afirmación con evidencia · cita fuentes
- No reciclar mi narrativa actual · cuestionar honestamente
- Si dato no disponible, marca [NO DATA · estimado conservador]
- Tono: directo, sin endulzar · honestidad > comodidad

---

> Prompt #5 generado por relevance_audit.py v{VERSION} · MetodologIA · CC BY-NC-SA 4.0
> Pegar en Perplexity (con búsqueda web · datos de mercado actualizados)
"""


def main():
    parser = argparse.ArgumentParser(
        description="Genera Prompt #5 personalizado para auditoría mensual"
    )
    parser.add_argument(
        "--skills",
        required=True,
        help="Skills separadas por coma · ej. 'jQuery,System Design,Python'",
    )
    parser.add_argument(
        "--industria",
        default="Consultoría · PreSales SAP/Cloud",
        help="Industria (default: Javier's)",
    )
    parser.add_argument(
        "--pais",
        default="Colombia · LatAm",
        help="País / región (default: Colombia)",
    )
    parser.add_argument(
        "--rol",
        default="PreSales Architect Sofka + Founder MetodologIA",
        help="Tu rol",
    )
    parser.add_argument(
        "--save",
        type=Path,
        help="Guardar prompt en archivo",
    )

    args = parser.parse_args()
    skills = [s.strip() for s in args.skills.split(",") if s.strip()]

    if len(skills) < 1 or len(skills) > 5:
        print("ERROR: 1-5 skills (recomendado: 3)", file=sys.stderr)
        return 1

    if len(skills) < 3:
        print(f"⚠️  Solo {len(skills)} skill(s) · recomendado 3 para auditoría completa", file=sys.stderr)

    prompt = generar_prompt(skills, args.industria, args.pais, args.rol)
    print(prompt)

    if args.save:
        args.save.parent.mkdir(parents=True, exist_ok=True)
        args.save.write_text(prompt)
        print(f"\n✅ Guardado en: {args.save}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())

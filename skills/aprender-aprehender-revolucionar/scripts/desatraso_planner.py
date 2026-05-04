#!/usr/bin/env python3
"""desatraso_planner.py · MetodologIA · Aprender·Aprehender·(R)Evolucionar · v1.1.0.

Genera plan time-boxed de catch-up sobre conocimiento acumulado.
Modos: Express 4h / Sprint 20h / Marathon 64h.

Usage:
    python desatraso_planner.py --tema "LLMs 2026" --tiempo 4h
    python desatraso_planner.py --tema "Kubernetes" --tiempo 20h --escala-actual 1
    python desatraso_planner.py --tema "Rust" --tiempo 64h --escala-actual 0
    python desatraso_planner.py --tema "Rust" --tiempo 4h --audit  # check coherencia

[FUENTE-PRIMARIA] Playbook v2.0.0 §Workflows + §Modos por tiempo.
[LÍMITE] Plan asume disponibilidad continua · si tu disponibilidad es errática
         (viajes frecuentes, on-call), considera reducir el target en 30-40%.
[SUPUESTO] Estimaciones de tiempo basadas en dominio promedio · dominios densos
           (matemática avanzada, sistemas formales) requieren 1.5-2× más.
[TRADE-OFF] Express 4h sacrifica triangulación profunda · solo Escala 0→1.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

VERSION = "1.1.0"


class DesatrasoError(Exception):
    """[NUEVO-APORTE] Errores de validación o coherencia del plan."""

MODES = {
    "4h": {
        "label": "Express",
        "horas": 4,
        "semanas": 1,
        "objetivo_escala": 1,
        "workflow": "Workflow 1 condensado",
    },
    "20h": {
        "label": "Sprint",
        "horas": 20,
        "semanas": 4,
        "objetivo_escala": 2,
        "workflow": "Workflow 2",
    },
    "64h": {
        "label": "Marathon",
        "horas": 64,
        "semanas": 16,
        "objetivo_escala": 3,
        "workflow": "Workflow 3 + Práctica Deliberada",
    },
}


def plan_express(tema: str, escala_actual: int, hoy: datetime.date) -> str:
    """Plan Express 4h · 1 sesión condensada."""
    return f"""# Plan Express · {tema} · 4 horas

> Mode: Express · Escala objetivo: 1 (Curioso) · Tiempo: 4h en 1 sesión

**Fecha**: {hoy.isoformat()}
**Escala actual**: {escala_actual}
**Objetivo**: cubrir Workflow 1 condensado

## Cronograma

| Tiempo | Actividad |
|---|---|
| 0:00–0:30 | Triangulación Blueprint en 3 IAs (Prompt #1) |
| 0:30–1:00 | Consolidación + tabla de triangulación |
| 1:00–1:30 | Fact-Check cruzado (Prompt #4) |
| 1:30–2:00 | Concept map mermaid + glosario |
| 2:00–2:30 | NotebookLM setup + sources |
| 2:30–3:00 | Coach config (Prompt #2) + test |
| 3:00–3:30 | Primera sesión con coach (5 preguntas) |
| 3:30–4:00 | Documentar + plan próxima sesión |

## Output esperado

- ✅ BoK triangulado en 3+ IAs
- ✅ Glosario ≥15 términos
- ✅ Concept map mermaid
- ✅ NotebookLM con coach activo
- ✅ Escala 1 (Curioso) alcanzada

## Próximos pasos

Si pasas Quality Gate G-Aprender → considera Sprint 20h para llegar a Escala 2.

→ ver `workflows/workflow-1-curioso.md`.

## Comando útil

```bash
pbcopy < ~/.claude/skills/aprender-aprehender-revolucionar/prompts/01-research-blueprint.md
# Personalizar [TU TEMA] = "{tema}"
# Ejecutar en ChatGPT, Claude, Gemini
```

---

> Plan generado por desatraso_planner.py v{VERSION} · MetodologIA · CC BY-NC-SA 4.0
""".format(VERSION=VERSION, tema=tema, escala_actual=escala_actual, hoy=hoy)


def plan_sprint(tema: str, escala_actual: int, hoy: datetime.date) -> str:
    """Plan Sprint 20h · 4 semanas, 1h × 5 días/sem."""
    semana_1_inicio = hoy
    semana_4_fin = hoy + datetime.timedelta(weeks=4)

    return f"""# Plan Sprint · {tema} · 20 horas en 4 semanas

> Mode: Sprint · Escala objetivo: 2 (Explorador) · 1h × 5 días/sem × 4 sem

**Fecha inicio**: {semana_1_inicio.isoformat()}
**Fecha cierre**: {semana_4_fin.isoformat()}
**Escala actual**: {escala_actual}
**Objetivo**: Workflow 2 completo

## Cronograma

### Semana 1 · Profundidad por subtema (5h)
- Lunes-Viernes: 1h cada subtema del BoK
- Output: 5 subtemas profundizados con casos

### Semana 2 · Fuentes primarias (5h)
- Lunes-Miércoles: 3 papers fundacionales (1h cada uno)
- Jueves-Viernes: 1 libro canónico (4 capítulos clave)

### Semana 3 · Triangulación de controversias (5h)
- 3 controversias del campo identificadas
- Argumentos de ambos lados
- Tu posición preliminar documentada

### Semana 4 · Consolidación (5h)
- BoK refinado con flujos
- Glosario expandido (50+ términos)
- Auditoría NotebookLM (Prompt #7)
- Quiz Nivel 2 aprobado (4/5)

## Quality Gate G-Explorador

Pre-Workflow 3:
- [ ] BoK refinado con casos de uso
- [ ] ≥3 papers + 1 libro cubierto
- [ ] 3 controversias mapeadas
- [ ] NotebookLM con 10-15 sources auditadas
- [ ] Quiz Nivel 2 aprobado

## Pre-requisito

Si escala_actual < 1 → ejecutar Plan Express ANTES de Sprint.

→ ver `workflows/workflow-2-explorador.md`.

## Próximos pasos

Workflow 3 (Marathon 64h) si quieres alcanzar Escala 3 (defender sin notas).

---

> Plan generado por desatraso_planner.py v{VERSION} · MetodologIA · CC BY-NC-SA 4.0
""".format(VERSION=VERSION, tema=tema, escala_actual=escala_actual,
           semana_1_inicio=semana_1_inicio, semana_4_fin=semana_4_fin)


def plan_marathon(tema: str, escala_actual: int, hoy: datetime.date) -> str:
    """Plan Marathon 64h · 16 semanas."""
    semana_1 = hoy
    semana_16 = hoy + datetime.timedelta(weeks=16)

    return f"""# Plan Marathon · {tema} · 64 horas en 16 semanas

> Mode: Marathon · Escala objetivo: 3 (Iniciado) · 1h × 4 días/sem × 16 sem

**Fecha inicio**: {semana_1.isoformat()}
**Fecha cierre**: {semana_16.isoformat()}
**Escala actual**: {escala_actual}
**Objetivo**: Programa completo de práctica deliberada

## Estructura · 16 semanas

### Semanas 1-2 · El Curioso (Workflow 1)
- BoK triangulado · glosario · concept map · NotebookLM
- Output: Escala 1 alcanzada

### Semanas 3-4 · El Explorador (Workflow 2)
- Fuentes primarias · controversias · profundidad
- Output: Escala 2 alcanzada

### Semanas 5-12 · El Iniciado (Workflow 3 extendido · 8 semanas)
- Aplicación de las 6 técnicas cognitivas
- Defensa preliminar y profunda
- Mock interviews progresivos
- Output: Escala 3 alcanzada · Quality Gate G-Aprehender pasado

### Semanas 13-16 · Consolidación
- Spaced Repetition profundo
- Aplicación a problema real
- Meta-aprendizaje (cómo aprendiste)
- Output: hábito instalado · método transferible a futuros temas

## Cadencia semanal típica

| Día | Foco |
|---|---|
| Lunes | Lectura activa + Elaboration |
| Martes | Práctica · aplicación a casos |
| Miércoles | Feynman a no-experto |
| Jueves | Quiz / Mock (Prompt #8 / #9) |
| Viernes | Retrieval + Spaced Repetition planning |

## Quality Gate G-Aprehender (al cerrar semana 12)

- [ ] Feynman grabado · sin notas · 5 min
- [ ] Quiz Nivel 3 aprobado (4/5)
- [ ] Mock interview LEAN HIRE+
- [ ] Self vs AI alignment ±1 escala
- [ ] 3 conceptos defendidos ante hostil

## Calendar invite

Bloque 17:00-18:00 lunes-viernes durante 16 semanas.
→ generar ICS con scripts auxiliares.

→ ver `rituals/ritual-practica-deliberada.md`.

---

> Plan generado por desatraso_planner.py v{VERSION} · MetodologIA · CC BY-NC-SA 4.0
""".format(VERSION=VERSION, tema=tema, escala_actual=escala_actual,
           semana_1=semana_1, semana_16=semana_16)


def main():
    parser = argparse.ArgumentParser(
        description="Plan time-boxed de catch-up · MetodologIA",
        epilog="Ejemplo: python desatraso_planner.py --tema 'LLMs 2026' --tiempo 4h",
    )
    parser.add_argument("--tema", required=True, help="Tema a aprender (específico)")
    parser.add_argument(
        "--tiempo",
        choices=list(MODES.keys()),
        required=True,
        help="Modo: 4h Express / 20h Sprint / 64h Marathon",
    )
    parser.add_argument(
        "--escala-actual",
        type=int,
        default=0,
        help="Tu Escala actual (0-9, default 0)",
    )
    parser.add_argument(
        "--industria",
        default="general",
        help="Tu industria (para context, default 'general')",
    )
    parser.add_argument(
        "--save",
        type=Path,
        help="Guardar plan en archivo (default: stdout solamente)",
    )
    parser.add_argument(
        "--audit",
        action="store_true",
        help="[NUEVO-APORTE v1.1] Solo audit de coherencia escala/tiempo · no genera plan",
    )

    args = parser.parse_args()

    if args.escala_actual < 0 or args.escala_actual > 9:
        print("ERROR: --escala-actual debe estar entre 0 y 9", file=sys.stderr)
        return 1

    # [NUEVO-APORTE v1.1] Audit de coherencia escala/tiempo
    target_escala = MODES[args.tiempo]["objetivo_escala"]
    if args.escala_actual >= target_escala:
        print(
            f"⚠️  Audit: escala_actual={args.escala_actual} ya ≥ "
            f"target {target_escala} para modo {args.tiempo}. "
            f"Considera modo más largo o un nuevo tema.",
            file=sys.stderr,
        )
        if args.audit:
            return 1
    if args.tiempo == "4h" and args.escala_actual > 1:
        print(
            f"⚠️  Audit: Express 4h objetivo Escala 1 · ya estás en {args.escala_actual} · "
            f"sugerido: modo 20h (Sprint) o 64h (Marathon).",
            file=sys.stderr,
        )

    if args.audit:
        print("✅ Audit OK · escala_actual coherente con modo elegido", file=sys.stderr)
        return 0

    hoy = datetime.date.today()

    if args.tiempo == "4h":
        plan = plan_express(args.tema, args.escala_actual, hoy)
    elif args.tiempo == "20h":
        plan = plan_sprint(args.tema, args.escala_actual, hoy)
    elif args.tiempo == "64h":
        plan = plan_marathon(args.tema, args.escala_actual, hoy)

    print(plan)

    if args.save:
        args.save.parent.mkdir(parents=True, exist_ok=True)
        args.save.write_text(plan)
        print(f"\n✅ Plan guardado en: {args.save}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())

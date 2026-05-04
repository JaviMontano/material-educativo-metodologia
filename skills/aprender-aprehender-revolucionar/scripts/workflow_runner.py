#!/usr/bin/env python3
"""workflow_runner.py · MetodologIA · v1.1.0.

Ejecuta Workflow 1/2/3 de forma interactiva · imprime checkpoints · valida gates.

Usage:
    python workflow_runner.py --workflow 1 --tema "Rust"
    python workflow_runner.py --workflow 2 --tema "Sistemas Distribuidos"
    python workflow_runner.py --workflow 3 --tema "Kubernetes" --semanas 4

[FUENTE-PRIMARIA] Playbook v2.0.0 §Workflows 1/2/3.
[LÍMITE] Imprime checkpoints · NO ejecuta los workflows · es guía interactiva.
[SUPUESTO] Usuario sigue checkpoints en buena fe · sin verificación automatizada.
[TRADE-OFF] Modo interactivo agregaría valor pero requiere stdin · stdout solo es portable.

License: CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

VERSION = "1.1.0"
SKILL_DIR = Path.home() / ".claude/skills/aprender-aprehender-revolucionar"


def workflow_1(tema: str) -> str:
    return f"""# Workflow 1 · El Curioso · {tema}

> Tiempo: 1-4 horas · Output: BoK triangulado · Escala 1 alcanzada

## Cronograma · 4 horas

| Tiempo | Actividad | Comando útil |
|---|---|---|
| 0:00–0:15 | Declaración de intención | Editar 00-declaracion.md |
| 0:15–1:00 | Triangulación Blueprint en 3 IAs | `pbcopy < prompts/01-research-blueprint.md` |
| 1:00–2:00 | Consolidación + tabla | `python scripts/triangulation.py --files *.md` |
| 2:00–2:30 | Fact-Check cruzado | `pbcopy < prompts/04-cross-fact-check.md` |
| 2:30–3:00 | NotebookLM Setup | notebooklm.google.com |
| 3:00–3:30 | Coach config | `pbcopy < prompts/02-coach-system-prompt.md` |
| 3:30–4:00 | Documentar + plan | Actualizar `.aprender-state.json` |

## Checkpoints

### CP1 · Tras triangulación (1h)
- [ ] 3 respuestas IA guardadas
- [ ] Tabla de triangulación generada
- [ ] Items 3/3 identificados como CONFIRMED

### CP2 · Tras fact-check (2.5h)
- [ ] Hallucinations eliminadas
- [ ] [NO SOURCE] críticos verificados manualmente
- [ ] BoK consolidado y limpio

### CP3 · Tras NotebookLM (3.5h)
- [ ] Sources cargadas (mínimo 3)
- [ ] Coach activo con Prompt #2
- [ ] Test de 5 preguntas exitoso

## Quality Gate G-Aprender

```
[ ] BoK triangulado en 3+ IAs
[ ] Glosario ≥15 términos
[ ] Concept map mermaid generado
[ ] ≥3 fuentes primarias verificadas
[ ] Auditor cruzado sin HALLUCINATION crítico
[ ] NotebookLM configurado con coach activo
```

Si todo ✅: avanzar a Workflow 2 · Escala 1 → 2

## Comandos paralelos

```bash
# Track progress
python {SKILL_DIR}/scripts/progress_tracker.py --add-tema "{tema}"

# Generar coach NotebookLM
python {SKILL_DIR}/scripts/notebook_config_generator.py \\
    --arquetipo coach --tema "{tema}"

# Si llegas con tiempo limitado:
python {SKILL_DIR}/scripts/desatraso_planner.py \\
    --tema "{tema}" --tiempo 4h
```

→ ver workflows/workflow-1-curioso.md (manual completo)
""".format(SKILL_DIR=SKILL_DIR, tema=tema)


def workflow_2(tema: str) -> str:
    return f"""# Workflow 2 · El Explorador · {tema}

> Tiempo: 4-20 horas · Output: BoK profundo · controversias · Escala 2

## Cronograma · 4 semanas (1h × 5 días/sem)

### Semana 1 · Profundidad por subtema
- Lun-Vie: 1h cada subtema del BoK
- Output: 5 subtemas profundizados

### Semana 2 · Fuentes primarias
- Lun-Mié: 3 papers fundacionales
- Jue-Vie: 1 libro canónico (4 caps)

### Semana 3 · Triangulación de controversias
- 3 controversias del campo identificadas
- Argumentos de ambos lados
- Tu posición preliminar

### Semana 4 · Consolidación
- BoK refinado
- Glosario expandido (50+ términos)
- Quiz Nivel 2 (Prompt #8)

## Quality Gate G-Explorador

```
[ ] BoK refinado con casos de uso
[ ] ≥3 papers + 1 libro cubierto
[ ] 3 controversias mapeadas
[ ] NotebookLM con 10-15 sources auditadas
[ ] Quiz Nivel 2 aprobado (4/5)
```

## Comandos útiles

```bash
# Cada deep research
pbcopy < {SKILL_DIR}/prompts/03-deep-research.md

# Audit del notebook
pbcopy < {SKILL_DIR}/prompts/07-notebook-audit.md

# Quiz Nivel 2
python {SKILL_DIR}/scripts/notebook_config_generator.py \\
    --arquetipo evaluador --certificacion "{tema}"
```

→ ver workflows/workflow-2-explorador.md
""".format(SKILL_DIR=SKILL_DIR, tema=tema)


def workflow_3(tema: str, semanas: int) -> str:
    fin = datetime.date.today() + datetime.timedelta(weeks=semanas)
    return f"""# Workflow 3 · El Iniciado · {tema}

> Tiempo: {semanas * 5}h en {semanas} semanas · Output: Escala 3 · defensa pública

**Cierre estimado**: {fin.isoformat()}

## Estructura · {semanas} semanas

### Semanas 1 · Vocabulario activo
- Retrieval ciego diario de glosario
- Spaced Repetition agendado
- Quiz Nivel 1 aprobado

### Semana 2 · Aplicación + trade-offs
- 5 casos de uso reales
- Trade-offs documentados
- Feynman a un trade-off

### Semana 3 · Defensa preliminar
- Mock interview hostil (Prompt #9)
- Cierre de gaps detectados
- Mock #2

### Semana 4 · Validación final
- Mock #3 · target LEAN HIRE+
- Quiz Nivel 3 aprobado (4/5)
- Feynman a humano real

## Las 6 técnicas integradas

| Semana | Retrieval | Spaced | Feynman | Interleaving | Elaboration | Dual Coding |
|---|---|---|---|---|---|---|
| 1 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| 2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Quality Gate G-Aprehender

```
[ ] Feynman grabado · sin notas · 5 min
[ ] Quiz Nivel 3 aprobado (4/5)
[ ] Mock interview LEAN HIRE+
[ ] Self-assess + AI-assess ±1 escala
[ ] 3 conceptos defendidos ante hostil
[ ] Spaced Repetition agendado (días 30/60/90)
```

## Comandos clave

```bash
# Daily retrieval
python {SKILL_DIR}/scripts/retrieval_session.py \\
    --concepto "[CONCEPTO]" --tiempo 15

# Mock interview
pbcopy < {SKILL_DIR}/prompts/09-interview-simulator.md

# Quiz progresivo
pbcopy < {SKILL_DIR}/prompts/08-evaluator-certification.md

# Track progress
python {SKILL_DIR}/scripts/progress_tracker.py \\
    --update "{tema}" --escala 3
```

→ ver workflows/workflow-3-iniciado.md
→ rituales: rituals/ritual-aprehension-semanal.md · rituals/ritual-practica-deliberada.md
""".format(SKILL_DIR=SKILL_DIR, tema=tema, semanas=semanas, fin=fin)


def main():
    parser = argparse.ArgumentParser(
        description="Ejecutor de Workflow 1/2/3 · Aprender·Aprehender"
    )
    parser.add_argument("--workflow", type=int, choices=[1, 2, 3], required=True)
    parser.add_argument("--tema", required=True)
    parser.add_argument("--semanas", type=int, default=4, help="Semanas para Workflow 3")
    parser.add_argument("--save", type=Path, help="Guardar plan en archivo")

    args = parser.parse_args()

    if args.workflow == 1:
        plan = workflow_1(args.tema)
    elif args.workflow == 2:
        plan = workflow_2(args.tema)
    elif args.workflow == 3:
        plan = workflow_3(args.tema, args.semanas)

    print(plan)

    if args.save:
        args.save.parent.mkdir(parents=True, exist_ok=True)
        args.save.write_text(plan)
        print(f"\n✅ Guardado en: {args.save}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())

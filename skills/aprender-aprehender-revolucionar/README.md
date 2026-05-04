# Aprender · Aprehender · (R)Evolucionar

> **Companion personal de aprendizaje y desatraso · MetodologIA v3.0**
> *El playbook te dice qué hacer. Esta skill lo hace contigo.*

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE.md)
[![Brand: MetodologIA](https://img.shields.io/badge/Brand-MetodologIA%20v3.0-122562)](https://metodologia.info)
[![Version: 1.1.0](https://img.shields.io/badge/version-1.1.0-FFD700)](CHANGELOG.md)

---

## Qué es esto

Una **skill de Claude Code** que activa el ciclo completo del conocimiento profesional: **adquirir** con método, **retener** para defender bajo presión, **soltar** lo que ya no sirve.

Basada fielmente en el **Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0** (CC BY-NC-SA 4.0) diseñado por Javier Montaño · MetodologIA.

**No reemplaza el playbook** — lo opera. El playbook es el cerebro; esta skill es el cuerpo.

---

## Cómo invocarla

Una vez instalada en `~/.claude/skills/aprender-aprehender-revolucionar/`, Claude la activa automáticamente cuando detecta señales como:

| Lo que dices | Lo que pasa |
|---|---|
| "ayúdame a aprender Rust desde cero" | Coach Aprender + Workflow 1 + Prompt #1 (Blueprint) |
| "deep research sobre LLMs 2026, tengo 4h" | Desatraso Express + Workflow 2 + Prompt #3 + #4 |
| "voy a presentar QBR el viernes" | Coach Aprehender + Prompt #10 + kata-defensa-hostil |
| "tengo certificación AWS la próxima semana" | Coach Aprehender + Prompt #8 (4 niveles) + Quiz progresivo |
| "mock interview" | Coach Aprehender + Prompt #9 (entrevistador 15+ años) |
| "jQuery ya no me sirve" | Coach (R)Evolucionar + Prompt #5 (4-D framework) |
| "este research, ¿es confiable?" | Auditor Cruzado + Prompt #4 + Triangulación |
| "configura mi NotebookLM como coach" | Generator + Prompt #2 + 8 arquetipos |

O explícitamente:
```
/aprender-aprehender-revolucionar Rust --fase=aprender --tiempo=4h
```

---

## Las 3 fases

### 1 · APRENDER · 1–4h
Transición Ignorante (Escala 0) → Curioso (Escala 1).
Salida: Blueprint declarado · BoK triangulado · glosario 30 términos · concept map · 3-5 fuentes primarias.

### 2 · APREHENDER · 20–64h
Transición Curioso (Escala 1) → Iniciado (Escala 3).
Salida: explicar sin notas (Feynman) · defender ante hostil · quiz progresivo aprobado.

### 3 · (R)EVOLUCIONAR · 1h/mes
Audit cycle · soltar lo obsoleto · liberar espacio mental.
Salida: 3+ skills evaluadas con framework 4-D · decisiones [MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR] documentadas.

---

## Modos de desatraso (catch-up)

Cuando llegas atrasado a un tema, la skill te ofrece tres modos:

| Modo | Tiempo | Salida |
|---|---|---|
| **Express** | 4 horas | Mapa conceptual + glosario + 3 fuentes primarias |
| **Sprint** | 20 horas | Defender sin notas en 4 semanas (1h × 5 días) |
| **Marathon** | 64 horas | Hábito instalado · cualquier tema futuro en 4h |

Invocar:
```bash
python ~/.claude/skills/aprender-aprehender-revolucionar/scripts/desatraso_planner.py \
  --tema="LLMs 2026" \
  --tiempo=4h
```

---

## Estructura de archivos

```
aprender-aprehender-revolucionar/
├── SKILL.md                 ← orquestador raíz (frontmatter + routing)
├── README.md                ← este archivo
├── CHANGELOG.md             ← histórico de versiones
├── LICENSE.md               ← CC BY-NC-SA 4.0
│
├── agents/                  ← 5 subagentes especializados
│   ├── companion-orchestrator.md   ← detecta fase, enruta
│   ├── coach-aprender.md            ← Fase 1
│   ├── coach-aprehender.md          ← Fase 2
│   ├── coach-revolucionar.md        ← Fase 3
│   └── auditor-cruzado.md           ← triangulación + fact-check
│
├── scripts/                 ← 7 helpers Python ejecutables
│   ├── workflow_runner.py          ← ejecuta Workflow 1/2/3 interactivo
│   ├── desatraso_planner.py        ← plan time-boxed (4h/20h/64h)
│   ├── relevance_audit.py          ← auditoría mensual con Prompt #5
│   ├── retrieval_session.py        ← sesión de retrieval ciega
│   ├── triangulation.py            ← compara 3+ IAs lado-a-lado
│   ├── progress_tracker.py         ← tracking en 10 escalas
│   └── notebook_config_generator.py ← system prompts ≤10K para NotebookLM
│
├── references/              ← 6 knowledge-deep RAG-able
│   ├── 01-seis-tecnicas-cognitivas.md
│   ├── 02-tres-modelos-fundacionales.md
│   ├── 03-diez-escalas-maestria.md
│   ├── 04-anti-patrones-y-trampas.md
│   ├── 05-glosario-aprendizaje.md
│   └── 06-ciencia-cognitiva-fuentes.md
│
├── prompts/                 ← 14 prompts copy-paste (10 + 4 meta)
│   ├── README.md
│   ├── 01-research-blueprint.md
│   ├── 02-coach-system-prompt.md
│   ├── 03-deep-research.md
│   ├── 04-cross-fact-check.md
│   ├── 05-relevance-audit.md
│   ├── 06-meta-prompt-generator.md
│   ├── 07-notebook-audit.md
│   ├── 08-evaluator-certification.md
│   ├── 09-interview-simulator.md
│   ├── 10-presentation-coach.md
│   └── meta/                ← 4 meta-prompts (generadores de prompts)
│       ├── M1-coach-generator.md
│       ├── M2-evaluator-generator.md
│       ├── M3-interviewer-generator.md
│       └── M4-presentation-generator.md
│
├── workflows/               ← 3 workflows nombrados
│   ├── workflow-1-curioso.md       ← 1–4h · declarar + mapear
│   ├── workflow-2-explorador.md    ← 4–20h · blueprint + triangular
│   └── workflow-3-iniciado.md      ← 20–64h · defender + sustentar
│
├── rituals/                 ← 4 cadencias temporales
│   ├── ritual-curiosidad-diaria.md     ← 15 min/día
│   ├── ritual-aprehension-semanal.md   ← 1h/semana
│   ├── ritual-auditoria-mensual.md     ← 1h/mes
│   └── ritual-practica-deliberada.md   ← 16 semanas
│
├── katas/                   ← 6 ejercicios deliberados
│   ├── kata-feynman-novato.md
│   ├── kata-triangulacion-3ias.md
│   ├── kata-recuperacion-ciega.md
│   ├── kata-defensa-hostil.md
│   ├── kata-soltar-legacy.md
│   └── kata-fuente-primaria.md
│
├── assets/                  ← plantillas + integraciones
│   ├── notebooklm-archetypes.json      ← 8 personas configurables
│   ├── plantilla-blueprint.md
│   ├── plantilla-glosario.md
│   ├── plantilla-concept-map.mermaid
│   ├── plantilla-triangulacion.md
│   ├── plantilla-quiz-scaling.md
│   ├── plantilla-fichas-anki.csv
│   ├── plantilla-bitacora-aprehension.md
│   └── calendar-invites/    ← ICS pre-llenados
│       ├── curiosidad-diaria.ics
│       ├── aprehension-semanal.ics
│       └── auditoria-mensual.ics
│
├── examples/                ← 4 sesiones reales documentadas
│   ├── ejemplo-aprender-rust.md
│   ├── ejemplo-aprehender-system-design.md
│   ├── ejemplo-revolucionar-jquery.md
│   └── ejemplo-desatraso-llms-2024.md
│
└── knowledge-base/          ← profundidad metodológica
    ├── filosofia-arete-virtud.md
    ├── deteccion-alucinaciones-ia.md
    ├── modos-uso-companion.md
    └── manifiesto-metodologia.md
```

**Total**: 62 archivos · ~7,000 líneas. Excede el benchmark Anthropic skill-creator (18 archivos · 5,654 líneas).

---

## Brand voice (HARD RULES)

**Usar**: Diseñador · (R)Evolución · Método · Soberanía Profesional · Areté.
**Bloqueado**: ❌ "Arquitecto" · ❌ "Transformación" · ❌ "Hacks".

**Paleta MetodologIA**:
- navy `#122562` · gold `#FFD700` · blue `#137DC5` · dark `#1F2833` · lilac `#BBA0CC` · gray `#808080`

**Tipografía**: Poppins (titulares) · Montserrat (cuerpo) · Trebuchet MS (notas).

**Pilares**: Ciencia Cognitiva · Pensamiento Crítico · Soberanía Profesional · Areté.

---

## Filosofía

> *Método primero, IA después.*
> *Cadencia > intensidad.*
> *Intención antes que intensidad.*
> *Lo que era vanguardia se vuelve legado.*

Las preguntas centrales del playbook:
1. ¿Sabes lo que sabes? *(Aprender)*
2. ¿Lo puedes defender sin notas, ante hostil, bajo presión? *(Aprehender)*
3. ¿Lo que sabes hoy aún sirve mañana? *((R)Evolucionar)*

---

## Atribución y licencia

- **Fuente canónica**: [Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0](file:///Users/deonto/Downloads/playbook-aprender-aprehender-revolucionar-v2.0.html) · 2026-04-29
- **Diseñador**: Javier Montaño · Founder/CEO MetodologIA
- **Brand voice**: MetodologIA v3.0
- **License**: CC BY-NC-SA 4.0 (Atribución · NoComercial · CompartirIgual)
- **Estructura inspirada en**: Anthropic skill-creator (benchmark de profundidad)

Si compartes, modificas o redistribuyes esta skill: **mantén la atribución a la fuente**, mantén la licencia CC BY-NC-SA 4.0, no la uses comercialmente sin permiso explícito.

---

## Quick links

- [SKILL.md](SKILL.md) — orquestador y routing completo
- [CHANGELOG.md](CHANGELOG.md) — histórico de versiones
- [LICENSE.md](LICENSE.md) — términos legales
- [agents/companion-orchestrator.md](agents/companion-orchestrator.md) — punto de entrada
- [prompts/README.md](prompts/README.md) — índice de los 14 prompts
- [knowledge-base/manifiesto-metodologia.md](knowledge-base/manifiesto-metodologia.md) — filosofía completa

---

*MetodologIA · 2026 · CC BY-NC-SA 4.0*

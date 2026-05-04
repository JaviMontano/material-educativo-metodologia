---
name: aprender-aprehender-revolucionar
version: 1.1.0
description: >
  Use proactively when the user asks to "aprender X", "estoy atrasado en Y",
  "deep research sobre Z", "preparar QBR/certificación/entrevista",
  "auditar mi relevancia profesional", "soltar legacy", "configurar NotebookLM",
  or mentions learning new topics, catching up on knowledge debt, defending
  knowledge under pressure, or evaluating obsolete skills.
  Activates the 3-phase MetodologIA cycle (Aprender · Aprehender · (R)Evolucionar)
  with 14 prompts, 3 workflows, 4 rituals, 6 katas, 8 NotebookLM archetypes, 10
  mastery scales. Routes to specialist coaches and maintains state. Use whenever
  rigorous evidence-based learning is preferred over fluent-but-shallow AI consumption.
argument-hint: "<tema o pregunta> [--fase=aprender|aprehender|revolucionar] [--tiempo=4h|20h|64h]"
author: Javier Montaño · MetodologIA
license: CC BY-NC-SA 4.0
model: opus
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion, WebFetch, WebSearch]
---

# Aprender · Aprehender · (R)Evolucionar

> Companion de aprendizaje y desatraso · MetodologIA v3.0 · *El playbook te dice qué hacer; esta skill lo hace contigo.*

Activa el ciclo completo del conocimiento profesional: **adquirir** con método · **retener** para defender bajo presión · **soltar** lo obsoleto. Encarnación operativa del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0.

`[FUENTE-PRIMARIA]` Playbook v2.0.0 · CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA.

## Contrato de la skill

| Hace | No hace |
|---|---|
| Acompaña aprendizaje técnico/profesional con método | Reemplaza al playbook fuente · lo **opera** |
| Diagnostica fase correcta de la conversación (Aprender/Aprehender/(R)Evolucionar/Auditoría) | Promete dominios en horas que requieren 10K horas (respeta las 10 escalas) |
| Ofrece los 14 prompts copy-paste y los rutea | Sale de la marca MetodologIA · esta skill es 100% MetodologIA |
| Genera planes time-boxed (Express 4h · Sprint 20h · Marathon 64h) | Produce afirmaciones sin evidence tag |
| Configura NotebookLM con 8 arquetipos | Coachea directamente desde el orquestador (delega al coach) |
| Triangula research en 3+ IAs · audita hallucinations con 4ª IA | Inventa fase cuando intent es ambiguo (pregunta) |

`[LÍMITE]` La skill cubre **Escalas 0-3** directamente (primeras 64 h). Para Escalas 4+ ayuda a planear pero el trabajo es **práctica en mundo real**.

## Voces canónicas

Diseñador · (R)Evolución · Método · Soberanía Profesional · Areté · Ciencia Cognitiva · Pensamiento Crítico.

## 1 · Detección de fase · matriz

| Señal del usuario | Fase | Coach destino |
|---|---|---|
| "no sé nada de X" · "quiero aprender Y" · "deep research sobre Z" | **APRENDER** (0→1) | `coach-aprender` |
| "voy a presentar QBR" · "tengo certificación X" · "no me siento defendible" · "atrasado tengo Xh" · "mock interview" | **APREHENDER** (1→3) | `coach-aprehender` |
| "X ya no me sirve" · "auditar relevancia" · "soltar legacy" · "auditoría mensual" | **(R)EVOLUCIONAR** (audit) | `coach-revolucionar` |
| "este research, ¿es confiable?" · "verificar" · "fact-check" · "alucinación" | **AUDITORÍA** post-research | `auditor-cruzado` |
| Ambiguo o multi-fase | Routing manual | `companion-orchestrator` (default) |

`[CRITERIO-ACEPTACIÓN]` Si confianza de detección <80% · NO inventar fase · `AskUserQuestion` con 4 opciones.

`[CASO-BORDE]` Casos hostiles documentados en `agents/companion-orchestrator.md` §1.1: tema en Escala ≥2 + señal "aprender" · self-eval Escala 3 sin workflow · urgencia <72h en Escala 0 · 3+ skills release-pending >60 días · estado JSON corrupto · idioma distinto a es-CO.

## 2 · Routing por intent

```
Usuario dice...                                  → Skill responde con...

"ayúdame a aprender Rust"                        coach-aprender · workflow-1-curioso · prompt #1
"deep research sobre LLMs 2026"                  coach-aprender · workflow-2-explorador · prompts #3 #4
"atrasado 6 meses en X, tengo 4h"                desatraso_planner.py --tiempo=4h · workflow-2 Express
"voy a presentar QBR el viernes"                 coach-aprehender · prompt #10 · ritual aprehensión acelerado
"certificación AWS la próxima semana"            coach-aprehender · prompt #8 · katas defensa-hostil + recall-ciega
"mock interview"                                 coach-aprehender · prompt #9
"jQuery ya no me sirve"                          coach-revolucionar · prompt #5 · kata soltar-legacy
"este research, ¿es confiable?"                  auditor-cruzado · prompts #4 #7
"configurar NotebookLM como coach Kubernetes"    notebook_config_generator.py --arquetipo=coach
"auditoría de relevancia mensual"                coach-revolucionar · relevance_audit.py · ritual mensual
```

## 3 · Modos por tiempo

| Modo | Tiempo | Workflow | Output esperado | Trade-off |
|---|---|---|---|---|
| **Express** | 4 h | W2 condensado | Concept map + glosario 30 + 3 fuentes 1° | Sacrifica triangulación profunda · solo Escala 0→1 viable |
| **Sprint** | 20 h | W3 (4 sem · 1h × 5 días) | Defender sin notas · quiz nivel 3 aprobado | Asume 5 días/sem disponibles · si miss ≥2 días, plan se quiebra |
| **Marathon** | 64 h | Programa 16 semanas | Hábito instalado · cualquier tema futuro en 4h | Compromiso sostenido · falla si <4h/sem |

Invocar: `python scripts/desatraso_planner.py --tema="<X>" --tiempo=4h|20h|64h`

## 4 · Las 3 fases (resumen ejecutivo)

Detalle: `agents/coach-*.md` · `references/02-tres-modelos-fundacionales.md`.

### 4.1 · APRENDER (Escala 0→1 · 1-4 h)

**Output mandatory**: Blueprint declarado · BoK triangulado 3+ IAs · glosario ≥15 términos (target 30) · concept map mermaid · 3-5 fuentes 1° verificadas.

**Anti-patrón principal**: aceptar BoK de 1 sola IA. Las omisiones de una aparecen en otra `[DOC: Triangulation Protocol · Playbook v2.0]`.

**Gate G-Aprender**: BoK triangulado 3+ IAs · glosario ≥15 · concept map · ≥3 fuentes 1° verificadas · auditor cruzado sin `[HALLUCINATION]` crítico.

### 4.2 · APREHENDER (Escala 1→3 · 20-64 h)

**Output mandatory**: explicación Feynman sin notas (audio/texto) · quiz nivel 3 aprobado (4/5 mínimo) · 3+ preguntas hostiles defendidas · self+IA assessment ±1 escala.

**6 técnicas** activadas (detalle `references/01-seis-tecnicas-cognitivas.md`):

1. Retrieval Practice — recuperar de memoria sin pistas
2. Spaced Repetition — intervalos crecientes (día 0, 3, 7, 14, 30, 90)
3. Feynman — explicar a niño 12 años · jerga = gap
4. Interleaving — mezclar problemas de subtemas
5. Elaboration — conectar con previo · 4 preguntas (¿por qué? ¿cómo? ¿qué pasaría si? ¿dónde NO?)
6. Dual Coding — texto + visual + audio

**Anti-patrón principal**: *Espejismo de Fluidez* `[DOC: Bjork & Bjork · 2011]` · respuesta IA elocuente confunde "suena lógico" con "yo entiendo".

**Gate G-Aprehender**: Feynman sin notas · quiz nivel 3 4/5 · 3 preguntas hostiles defendidas.

### 4.3 · (R)EVOLUCIONAR (audit cycle · 1 h/mes)

**Framework 4-D**: Vigencia · ROI · Obsolescencia · Demanda.

**Output mandatory**: 3 skills evaluadas con 4-D · decisiones documentadas `[MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR]` · plan reskill si aplica · narrativa profesional actualizada.

**Anti-patrón principal**: Identity Attachment · aferrarse a skill obsoleta porque es identidad.

**Gate G-(R)Evolucionar**: 3+ skills evaluadas · decisión por cada · plan reskill si SOLTAR/REEMPLAZAR.

## 5 · 10 Escalas de Maestría (referencia rápida)

Detalle: `references/03-diez-escalas-maestria.md`.

| Escala | Nombre | Horas | Criterio binario | Reto |
|---|---|---|---|---|
| 0 | Ignorante | — | No sabe que existe | Describe en 1 frase |
| 1 | Curioso | 1–4 | BoK triangulado | Enseña a Escala 0 |
| 2 | Explorador | 4–20 | Triangula fuentes | Enseña a Escala 1 |
| 3 | Iniciado | 20–64 | Explica sin notas | Mentoriza Escala 1-2 |
| 4 | Practicante | 64–200 | Ejecuta confiablemente | Mejora procesos medibles |
| 5 | Competente | 200–500 | Maneja casos novel | Entrena Escala 3+ |
| 6 | Versado | 500–1,000 | Innova en límites | Tus alumnos llegan a 5+ |
| 7 | Experto | 1K–10K | Define límites del campo | Contribuye al avance documentable |
| 8 | Maestro | 10K+ | Cross-disciplina | Forma dirección de industria |
| 9 | Referente | 10K+ | Tú **eres** el estándar | Tu sucesor define escala nueva |

`[FUENTE-PRIMARIA]` Ericsson 1993 · Ericsson & Pool 2016 (refinamiento de "10K horas").

## 6 · Quality gates (HARD STOP)

Cada gate es **bloqueante** · NO avanzar sin pasarlo. On failure: detener, presentar 3 opciones numeradas, esperar selección.

```
G-APRENDER → APREHENDER
[ ] BoK triangulado 3+ IAs
[ ] Glosario ≥15 términos
[ ] Concept map mermaid
[ ] ≥3 fuentes 1° verificadas
[ ] Prompt #4 sin [HALLUCINATION] crítico

G-APREHENDER → (R)EVOLUCIONAR (cíclico)
[ ] Explicación Feynman sin notas
[ ] Quiz nivel 3 4/5 (Prompt #8)
[ ] 3 preguntas hostiles defendidas (kata-defensa-hostil)
[ ] Self+IA assessment ±1 escala

G-(R)EVOLUCIONAR (mensual)
[ ] 3+ skills evaluadas con 4-D
[ ] Decisión documentada por cada una
[ ] Plan reskill si SOLTAR/REEMPLAZAR
[ ] Narrativa profesional actualizada
```

## 7 · Rituales (cadencia > intensidad)

`[DECISIÓN]` Cadencia diaria/semanal/mensual produce 80%+ adherencia · intensidad sin sistema produce 30-40% · `[DOC: Knowles 1980 · andragogía]`.

| Ritual | Frecuencia | Tiempo | Archivo |
|---|---|---|---|
| Curiosidad diaria | Cada mañana | 15 min | `rituals/ritual-curiosidad-diaria.md` |
| Aprehensión semanal | 1× / semana | 60 min | `rituals/ritual-aprehension-semanal.md` |
| Auditoría mensual | 1× / mes | 60 min | `rituals/ritual-auditoria-mensual.md` |
| Práctica deliberada | 1h × 16 semanas | 16 h | `rituals/ritual-practica-deliberada.md` |

Calendar invites pre-llenados (Cal.com / Google) en `assets/calendar-invites/*.ics`.

## 8 · Anti-patrones globales

Detalle: `references/04-anti-patrones-y-trampas.md`.

| Anti-patrón | Síntoma | Antídoto |
|---|---|---|
| Espejismo de Fluidez | "Suena tan lógico" | Cierra · Feynman a niño 12 años |
| Single-AI BoK | "ChatGPT me dio el mapa" | Triangulación 3+ IAs · Prompt #4 |
| Dunning-Kruger | Self-eval Escala 4 vs IA-eval Escala 2 | Diagnóstico abierto · no multiple choice |
| Cramming | Maratón 8h sábado | Spaced: día 0, 3, 7, 14, 30 |
| Recognition vs Recall | "Sí, lo conozco al verlo" | Retrieval ciego · papel en blanco |
| Hallucination IA | Citas + año pero sin fuente verificable | Prompt #4 · 4ª IA · Primary Source Rule |
| Sycophancy IA | "Tu hipótesis es correcta" sin contra | Diablo's Advocate · pídele opuesto |
| Identity Attachment | "Esto soy yo, no puedo soltarlo" | Auditoría 4-D · ROI vs costo |

## 9 · Estado persistente

`.aprender-state.json` (schema v1.1 detallado en `agents/companion-orchestrator.md` §2). Read-before-write siempre. Backup automático antes de cada escritura: `.aprender-state.{YYYYMMDD}.bak`.

`scripts/progress_tracker.py` automatiza lectura/escritura.

`[LÍMITE]` Estado vive local (no sincroniza entre máquinas). Solución: `rclone`/`iCloud` manual.

## 10 · Estructura

```
SKILL.md            ← este archivo (orquestador raíz · ≤350 líneas)
README · CHANGELOG · LICENSE

agents/             5 (orchestrator + 3 coaches + auditor)
scripts/            7 helpers Python + __init__
references/         6 (técnicas · modelos · escalas · anti-patrones · glosario · fuentes)
prompts/            10 directos + README + 4 meta = 15
workflows/          3 (Curioso · Explorador · Iniciado)
rituals/            4 (diaria · semanal · mensual · 16-sem)
katas/              6 ejercicios deliberados
assets/             plantillas · NotebookLM configs · ICS calendars
examples/           4 sesiones reales documentadas
knowledge-base/     4 (Areté · hallucinations · modos · manifiesto)
```

`[DECISIÓN]` Progressive Disclosure 3 niveles · SKILL.md ≤350 líneas · profundidad en `references/` y `agents/`. Nunca duplicar aquí lo que ya está en otro archivo · referenciar.

## 11 · Invocación rápida

```
"ayúdame a aprender Rust desde cero"
"deep research sobre LLMs 2026, tengo 4 horas"
"voy a presentar QBR sobre system design el viernes"
"jQuery ya no me sirve, ¿qué hago?"
"configura mi NotebookLM como coach para Kubernetes"
"auditoría mensual de relevancia"
"este research, ¿es confiable?" + texto adjunto
```

## Atribución

`[FUENTE-PRIMARIA]` Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · CC BY-NC-SA 4.0 · Javier Montaño · Founder/CEO MetodologIA · 2026.

Estructura inspirada en Anthropic skill-creator (benchmark de profundidad).

> v1.1.0 · *Método primero, IA después.*

# Prompts · 14 Prompts Canónicos del Playbook

> Copy-paste-ready · cada archivo es independiente · `pbcopy < prompts/N.md` funciona directo. v1.1.0.

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §14 Prompts.

## Tabla maestra · trigger · severidad · tiempo · IA recomendada

| # | Prompt | Trigger principal | Severidad | Tiempo | IA recomendada | Fase |
|---|---|---|---|---|---|---|
| 1 | [research-blueprint](01-research-blueprint.md) | "quiero aprender X" | ⭐⭐⭐⭐⭐ | 30 min | ChatGPT + Claude + Gemini | Aprender |
| 2 | [coach-system-prompt](02-coach-system-prompt.md) | "configura mi NotebookLM coach" | ⭐⭐⭐⭐⭐ | 15 min | NotebookLM (Custom Goal) | Aprender + Aprehender |
| 3 | [deep-research](03-deep-research.md) | "research exhaustivo sobre X" | ⭐⭐⭐⭐ | 60-90 min | Perplexity / Kimi (web search) | Aprender |
| 4 | [cross-fact-check](04-cross-fact-check.md) | "audita este research" | ⭐⭐⭐⭐⭐ | 15-30 min | 4ª IA independiente · idealmente conservadora | Cross-fase |
| 5 | [relevance-audit](05-relevance-audit.md) | "auditar mi relevancia mensual" | ⭐⭐⭐⭐ | 60 min | Perplexity (datos mercado actuales) | (R)Evolucionar |
| 6 | [meta-prompt-generator](06-meta-prompt-generator.md) | "necesito coach custom para X" | ⭐⭐⭐ | 10 min | Claude (estructura clara) | Setup |
| 7 | [notebook-audit](07-notebook-audit.md) | "auditar mis sources NotebookLM" | ⭐⭐⭐⭐ | 15 min | Claude (rigor estructural) | Cross-fase |
| 8 | [evaluator-certification](08-evaluator-certification.md) | "examen / pre-cert" | ⭐⭐⭐⭐⭐ | 60 min | NotebookLM (Custom Goal) | Aprehender |
| 9 | [interview-simulator](09-interview-simulator.md) | "mock interview hostil" | ⭐⭐⭐⭐ | 60 min | NotebookLM (Custom Goal) | Aprehender |
| 10 | [presentation-coach](10-presentation-coach.md) | "preparar QBR / pitch" | ⭐⭐⭐⭐ | 60 min × 3 sesiones | NotebookLM (Custom Goal) | Aprehender |

### Meta-Prompts (M1-M4) · generan otros prompts

| Meta | Genera | Cuándo |
|---|---|---|
| [M1](meta/M1-coach-generator.md) | Coach NotebookLM custom | Caso nicho no cubierto por #2 |
| [M2](meta/M2-evaluator-generator.md) | Evaluador para certificación específica | Cert no cubierta por #8 |
| [M3](meta/M3-interviewer-generator.md) | Entrevistador para rol/empresa específica | Entrevista nicho no cubierta por #9 |
| [M4](meta/M4-presentation-generator.md) | Coach de presentación con audiencia específica | Audiencia no cubierta por #10 |

## Cómo invocar

| Modo | Comando | Cuándo |
|---|---|---|
| Copy-paste directo | `pbcopy < prompts/01-research-blueprint.md` | Trabajo fuera de Claude Code |
| Vía la skill | "Hazme un blueprint para Rust" | Dentro de Claude Code · activa coach correcto |
| Vía script | `python scripts/notebook_config_generator.py --arquetipo=coach --tema=Rust` | Configura NotebookLM directamente |

## Variables comunes (TODOS los prompts)

| Variable | Significado | Ejemplo |
|---|---|---|
| `[TU TEMA]` | Dominio · sea preciso | "Rust async runtime" no "Rust" |
| `[TU INDUSTRIA]` | Tu industria | "Banca digital LatAm" |
| `[TU ROL]` | Rol actual / objetivo | "PreSales Architect" |
| `[TU NIVEL]` | Escala 0-9 honesta | "Escala 2 Explorador" |
| `[OBJETIVO]` | Resultado medible | "Aprobar AWS SAA-C03" |
| `[TIEMPO DISPONIBLE]` | Horas | "4h" / "20h" / "64h" |

`[CRITERIO-ACEPTACIÓN]` Si dejas `[TU TEMA]` literal sin reemplazar, el output será genérico sobre "Tu Tema" como concepto abstracto · output inservible.

## Combos canónicos

### Setup de un tema nuevo (Workflow 1 · 2-3 h)

```
1. Prompt #1 en 3 IAs (triangulación)
2. Prompt #4 en 4ª IA (audita las 3 anteriores)
3. Prompt #2 → configurar NotebookLM coach
4. Prompt #7 cada 5 sources nuevas
```

### Pre-defensa pública (Workflow 3 · 4 semanas)

```
Semana 1-2: Prompt #2 activo + #8 (Foundations + Intermediate)
Semana 3:   #8 Advanced + #9 mock interview
Semana 4:   #10 si es QBR/pitch + ensayos
Día 0:      Defensa real
```

### Auditoría mensual relevancia (1 h / mes)

```
1. Prompt #5 sobre 3 skills más usadas
2. Decisiones documentadas [MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR]
3. Si SOLTAR/REEMPLAZAR → invocar coach-aprender en próxima sesión
```

### Crear coach custom (avanzado)

```
1. Meta-Prompt M1/M2/M3/M4 según necesidad
2. Genera system prompt ≤10K chars
3. Pegar en NotebookLM Custom Goal
4. Test con 5 preguntas · iterar
```

## 5 reglas de oro

1. **Triangulación** para Prompts #1 y #3 · 3 IAs distintas. Las omisiones de una aparecen en otra.
2. **Primary Source Rule** mandatory para cualquier afirmación factual (cita autor + año). Si no existe → hallucination.
3. **Reemplazar variables** antes de enviar · sin esto el output es genérico inservible.
4. **Iterar** · primera respuesta = punto de partida. Pregunta seguimientos: "Profundiza en X", "¿Dónde NO aplica?", "Da ejemplos concretos".
5. **Documentar** · guarda respuestas en NotebookLM o `examples/`. Cada sesión es activo, no consumible.

## Anti-patrones al usar prompts

| Anti-patrón | Síntoma | Corrección |
|---|---|---|
| 1 sola IA | Solo el sesgo de esa IA | Triangular en 3+ |
| Aceptar primera respuesta | Output superficial | Iterar mínimo 2× |
| No reemplazar variables | Output genérico | Cada `[X]` reemplazado |
| Citar sin verificar | Hallucinations en QBR | Prompt #4 obligatorio pre-uso público |
| 8+ NotebookLMs sin auditar | Caos de notebooks | Prompt #7 cada 5 sources |

`[LÍMITE]` Estos prompts asumen que tienes acceso a 3+ IAs distintas. Si solo tienes 1, los Prompts #1 y #3 pierden su valor de triangulación · valor cae 60%.

## Técnicas cognitivas activadas por cada prompt

| Prompt | Técnicas (ver `references/01-seis-tecnicas-cognitivas.md`) |
|---|---|
| #1 Blueprint | Elaboration · Dual Coding (concept map) |
| #2 Coach | Retrieval · Spaced · Feynman · Elaboration |
| #3 Deep Research | Triangulation · BoK profundo |
| #4 Fact-Check | Detección de hallucinations |
| #5 Relevance Audit | Framework 4-D · (R)Evolucionar |
| #6 Meta-Prompt Gen | Generación de coaches custom |
| #7 Notebook Audit | Calidad y diversidad de fuentes |
| #8 Evaluator | Retrieval · Interleaving · progresión 4 niveles |
| #9 Interviewer | Defensa hostil · retrieval bajo presión |
| #10 Presentation | Minto Pyramid · Feynman · objection handling |

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · 14 prompts canónicos del Playbook v2.0.0

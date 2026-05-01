# Prompts · Índice de los 14 Prompts Canónicos

> Los 14 prompts del Playbook MetodologIA, listos para copy-paste. Cada uno es un archivo independiente para que `pbcopy < prompts/05-relevance-audit.md` funcione directo.

**Fuente canónica**: Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · §14 Prompts Copy-Paste.

---

## Tabla de Prompts

### Prompts Directos (10)

| # | Archivo | Cuándo usarlo | IA recomendada |
|---|---|---|---|
| 1 | [01-research-blueprint.md](01-research-blueprint.md) | Tema nuevo · Workflow 1 | ChatGPT, Claude, Gemini |
| 2 | [02-coach-system-prompt.md](02-coach-system-prompt.md) | Configurar NotebookLM como coach 24/7 | NotebookLM (Custom Goal) |
| 3 | [03-deep-research.md](03-deep-research.md) | Investigación exhaustiva | Perplexity, Kimi, ChatGPT Plus |
| 4 | [04-cross-fact-check.md](04-cross-fact-check.md) | Auditar research existente | 4ª IA independiente |
| 5 | [05-relevance-audit.md](05-relevance-audit.md) | Auditoría mensual de skills | Cualquier IA |
| 6 | [06-meta-prompt-generator.md](06-meta-prompt-generator.md) | Crear system prompts custom | Cualquier IA |
| 7 | [07-notebook-audit.md](07-notebook-audit.md) | Cada 5+ fuentes nuevas | Cualquier IA |
| 8 | [08-evaluator-certification.md](08-evaluator-certification.md) | Pre-certificación · 4 niveles | NotebookLM (Custom Goal) |
| 9 | [09-interview-simulator.md](09-interview-simulator.md) | Mock interview hostil | NotebookLM (Custom Goal) |
| 10 | [10-presentation-coach.md](10-presentation-coach.md) | QBR / pitch / defensa pública | NotebookLM (Custom Goal) |

### Meta-Prompts (4)

Los meta-prompts **generan** otros prompts custom para tus necesidades específicas.

| # | Archivo | Genera |
|---|---|---|
| M1 | [meta/M1-coach-generator.md](meta/M1-coach-generator.md) | Coach NotebookLM personalizado |
| M2 | [meta/M2-evaluator-generator.md](meta/M2-evaluator-generator.md) | Evaluador de certificación específica |
| M3 | [meta/M3-interviewer-generator.md](meta/M3-interviewer-generator.md) | Entrevistador para rol/empresa específica |
| M4 | [meta/M4-presentation-generator.md](meta/M4-presentation-generator.md) | Coach de presentación con audiencia específica |

---

## Cómo usar un prompt

### Opción A · Copy-paste directo
```bash
pbcopy < ~/.claude/skills/aprender-aprehender-revolucionar/prompts/01-research-blueprint.md
# Ahora pega en ChatGPT/Claude/Gemini con Cmd+V
```

### Opción B · Vía la skill
La skill `aprender-aprehender-revolucionar` invoca el prompt correcto según tu intent.
*"Hazme un blueprint para aprender Rust"* → activa Prompt #1 con tema=Rust.

### Opción C · Vía script Python
```bash
python ~/.claude/skills/aprender-aprehender-revolucionar/scripts/notebook_config_generator.py \
  --arquetipo=coach \
  --tema="Rust"
```

---

## Variables comunes

Todos los prompts usan placeholders entre corchetes para personalizar:

| Variable | Significado | Ejemplo |
|---|---|---|
| `[TU TEMA]` | El dominio que vas a aprender | "Rust", "Sistemas Distribuidos" |
| `[TU INDUSTRIA]` | Tu industria profesional | "Banca", "SaaS B2B" |
| `[TU ROL]` | Tu rol actual o objetivo | "Backend Senior", "Tech Lead" |
| `[TU NIVEL]` | Tu Escala actual (0-9) | "Escala 2 Explorador" |
| `[OBJETIVO]` | Qué quieres lograr | "Pasar AWS SAA-C03" |
| `[TIEMPO DISPONIBLE]` | Horas que puedes invertir | "4h", "20h", "64h" |

**Reemplaza siempre antes de enviar.** Si dejas variables sin reemplazar, el output será genérico.

---

## Combos canónicos

### Para aprender un tema nuevo (Workflow 1)
```
1. Prompt #1 (Blueprint) en 3 IAs (triangulación)
2. Prompt #4 (Fact-Check) en 4ª IA
3. Prompt #2 (Coach) configurar NotebookLM
4. Prompt #7 (Audit) cada 5 fuentes nuevas
```

### Para aprehender (Workflow 3 · pre-defensa)
```
1. Prompt #2 (Coach NotebookLM activo durante 4 semanas)
2. Prompt #8 (Evaluator) cada semana
3. Prompt #9 (Interview) la semana antes
4. Prompt #10 (Presentation) si es QBR/pitch
```

### Para auditoría de relevancia (mensual)
```
1. Prompt #5 (Relevance Audit) sobre 3 skills usadas este mes
2. Decisión documentada [MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR]
3. Si hay [REEMPLAZAR] o [SOLTAR] → activar Workflow 1 con la nueva skill
```

### Para crear coaches custom (avanzado)
```
1. Meta-Prompt M1 → genera tu propio Coach NotebookLM
2. Meta-Prompt M2 → genera tu propio Evaluator
3. Meta-Prompt M3 → genera tu propio Interviewer
4. Meta-Prompt M4 → genera tu propio Presentation Coach
```

---

## Reglas de oro al usar los prompts

### 1 · Siempre triangulación
Para Prompts #1 y #3, **úsalos en 3 IAs distintas** y compara respuestas. Las omisiones de una aparecen en otra.

### 2 · Validar fuentes primarias
Para cualquier afirmación factual, exige citas y verifica que el documento original existe. Si no → hallucination probable.

### 3 · Personalizar variables
No envíes prompts con `[TU TEMA]` literal. La IA respondería sobre "Tu Tema" como concepto abstracto.

### 4 · Iterar
La primera respuesta es punto de partida, no final. Pregunta seguimientos:
- *"Profundiza en [X subtema]"*
- *"Da ejemplos concretos"*
- *"¿Dónde NO aplica esto?"*

### 5 · Documentar
Guarda las respuestas en NotebookLM o en `examples/`. Cada sesión con prompts es un activo, no un consumible.

---

## Anti-patrones al usar prompts

❌ **Usar 1 sola IA y creer que tienes la verdad** → Triangular en 3+
❌ **Aceptar la primera respuesta** → Iterar siempre
❌ **No reemplazar variables** → Output genérico inútil
❌ **Citar la respuesta IA en presentación sin verificar** → Hallucination en producción
❌ **Crear 8 NotebookLMs sin auditarlos** → Caos · usa Prompt #7 cada 5 fuentes

---

## Sustento

Cada prompt está diseñado para evocar las 6 técnicas cognitivas:

| Prompt | Técnicas activadas |
|---|---|
| #1 Blueprint | Elaboration · Dual Coding (concept map) |
| #2 Coach | Retrieval · Spaced · Feynman · Elaboration |
| #3 Deep Research | Triangulation · BoK |
| #4 Fact-Check | Detección de hallucinations |
| #5 Relevance Audit | Framework 4-D · (R)Evolucionar |
| #6 Meta-Prompt Gen | Generación de coaches custom |
| #7 Notebook Audit | Calidad de fuentes |
| #8 Evaluator | Retrieval · Interleaving · progresión |
| #9 Interviewer | Defensa hostil · retrieval bajo presión |
| #10 Presentation | Estructuración · Feynman · objection handling |

→ ver `references/01-seis-tecnicas-cognitivas.md` para evidencia académica.

---

> **Atribución**: 14 Prompts del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · CC BY-NC-SA 4.0 · Javier Montaño · MetodologIA.

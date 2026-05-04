# DR Catalog 2026 — 24 Deep Researches para las 2 Familias de Notebooks

**Método de referencia:** `playbook-aprender-aprehender-revolucionar-2026.html` §Aprender/Aprehender/(R)Evolucionar + §BoK/Capability/Maturity
**Triangulación (§2066):** cada DR se ejecuta en **3 IAs**: **Kimi (deep)** + **ChatGPT Deep Research (O3/GPT-5)** + **Perplexity Pro** — cruce obligatorio.
**Output por DR:** un documento markdown que entra a NotebookLM como **source** con tag `[DR-BoK]`, `[DR-Capability]` o `[DR-Maturity]`.
**Anti-patrón del playbook §1800:** confundir "fluent" con "correct" → cada output pasa verificación de contradicciones entre las 3 IAs.

---

## Convenciones

- **Audiencia target:** profesionales LATAM, español primario, 2–15 años de experiencia.
- **Horizonte temporal:** corpus 2023-01-01 → 2026-04-18. Priorizar fuentes 2024–2026.
- **Formato de salida:** Markdown estructurado (H2/H3), tablas, citas con URL, ≤3.500 palabras por artefacto.
- **Criterio de inclusión (fuentes):** peer-reviewed, libros de autores con h-index >15, reportes de firmas top (McKinsey, MIT, Gartner, WEF), OR testimonio directo de practitioners identificables.
- **Criterio de exclusión:** blogs corporativos sin autor, LinkedIn influencers sin evidencia, contenido generado por IA sin curaduría.

---

# FAMILIA A — "De Ocupado a Productivo 2026"

## A1 — Ocupado-Baseline — Diagnóstico del Ejecutor Reactivo

### A1-BoK — Body of Knowledge
**Pregunta-guía:** ¿Qué marco conceptual describe hoy el fenómeno del "ocupado reactivo" en el knowledge worker 2026, y cuáles son sus síntomas observables?
**Hipótesis:** El constructo "ocupado" en 2026 es distinto al de 2015 (pre-IA) porque la IA absorbió tareas ejecutivas, dejando al humano con decisión + ambigüedad + emocional.
**Fuentes primarias a exigir:**
- *Busy: How to Thrive in a World of Too Much* — Tony Crabbe
- *Four Thousand Weeks* — Oliver Burkeman
- *Essentialism* — Greg McKeown
- Microsoft Work Trend Index 2024/2025/2026
- Gallup State of the Global Workplace 2025/2026
- Papers sobre "attention residue" — Sophie Leroy
**Prompt maestro (Playbook #2 adaptado):** *"Genera el Body of Knowledge del fenómeno 'profesional ocupado reactivo' en 2026. Incluye: definiciones operativas, 5 subdominios (tiempo, atención, energía, decisión, identidad), actores clave del debate, cronología de evolución del constructo 2015–2026, 10 fuentes primarias con DOI/URL y 3 áreas de controversia vigente."*

### A1-Capability — Capability Model
**Pregunta-guía:** ¿Qué capacidades distinguen al ocupado-crónico del productivo-intencional en 5 niveles progresivos?
**Hipótesis:** Existe un continuum S1 (ocupado-ciego) → S5 (intencional-maestro) con 6 dimensiones (priorización, energía, foco, decisión, sistemas, recuperación).
**Output esperado:** matriz 5×6 con descriptores observables por nivel + criterio de tránsito entre niveles.
**Prompt maestro (Playbook #4 Capability adaptado):** *"Construye un Capability Model de 5 niveles (S1 Ocupado-ciego → S5 Intencional-maestro) para el dominio 'productividad personal post-IA'. Para cada nivel define: 6 dimensiones (priorización, energía, foco, decisión, sistemas, recuperación), 3 comportamientos observables, 2 métricas cuantificables, 1 anti-patrón común. Cierra con criterios de tránsito entre niveles."*

### A1-Maturity — Maturity Model
**Pregunta-guía:** ¿Cómo se autoevalúa un profesional para ubicarse en el Capability Model y qué plan de intervención corresponde a cada nivel?
**Output esperado:** instrumento diagnóstico de 30 preguntas (6 por dimensión) con escala Likert + algoritmo de scoring + 5 rutas de intervención (una por nivel).
**Prompt maestro (Playbook #6 adaptado):** *"Diseña un Maturity Assessment Instrument para el Capability Model anterior. Incluye: 30 preguntas diagnósticas (6 × 5 dimensiones), scoring algorítmico, reporte auto-generable con ubicación en el modelo, 5 planes de intervención (uno por nivel) con horizonte 90 días, hitos semanales, y señales de progreso."*

---

## A2 — Energía > Tiempo — Gestión Circadiana y Recuperación

### A2-BoK
**Pregunta-guía:** ¿Cuál es el cuerpo de conocimiento científico 2023-2026 sobre gestión de energía del knowledge worker (vs. gestión de tiempo)?
**Fuentes primarias:**
- *The Power of Full Engagement* — Tony Schwartz (actualizaciones 2023+)
- *Why We Sleep* — Matthew Walker + papers post-2022
- *The Upside of Stress* — Kelly McGonigal
- *When: The Scientific Secrets of Perfect Timing* — Daniel Pink
- Papers sobre ultradian rhythms (Kleitman, Rossi)
- HRV research (Porges, Shaffer)
- Estudios de burnout post-pandemia (WHO ICD-11)
**Prompt maestro:** *"Body of Knowledge sobre gestión de energía del knowledge worker 2023–2026. Cubre: cronobiología aplicada, ultradian rhythms, deliberate rest, HRV como métrica, sueño profundo, recovery paradigms, 5 controversias abiertas, 12 fuentes primarias."*

### A2-Capability
**Output:** 5 niveles × dimensiones (sueño, nutrición, movimiento, recuperación, ritmo ultradian, gestión del estrés).
**Prompt maestro:** *"Capability Model 5 niveles para 'gestión de energía personal en knowledge workers 2026'. 6 dimensiones: sueño, nutrición, movimiento, recuperación, ritmo ultradian, regulación del estrés. Por nivel: comportamientos observables, métricas (HRV, horas de sueño profundo, pasos, resting HR), anti-patrones."*

### A2-Maturity
**Output:** 30-Q diagnóstico + tracking de 4 semanas + prescripción protocolos por nivel.
**Prompt maestro:** *"Maturity Assessment de gestión de energía. 30 preguntas auto-aplicables, 28-day tracking con 5 métricas, 5 protocolos de intervención (por nivel) con foco primero en 1 dimensión bottleneck. Cada protocolo: hábitos a instalar, hábitos a desinstalar, rituales semanales, señales de éxito a 30/60/90 días."*

---

## A3 — Foco Profundo Post-IA — Deep Work en Era Agentica

### A3-BoK
**Pregunta-guía:** ¿Cómo se redefine Deep Work cuando agentes IA ejecutan tareas sub-atómicas y el humano se especializa en decisión, creatividad y juicio?
**Fuentes primarias:**
- *Deep Work* + *A World Without Email* — Cal Newport
- *Focus* — Daniel Goleman
- *Co-Intelligence* — Ethan Mollick (2024)
- Papers de cognitive offloading (Risko, Storm)
- MIT Task Force on AI + Future of Work 2024-2026
- *The Coming Wave* — Mustafa Suleyman (contexto)
**Prompt maestro:** *"BoK sobre 'Deep Work en era agentica 2026'. Incluye: redefinición post-IA del trabajo no-automatizable, cognitive offloading (beneficios/riesgos), nueva taxonomía de tareas humanas irreducibles, 8 fuentes primarias 2023–2026, 3 escuelas de pensamiento en tensión."*

### A3-Capability
**Prompt maestro:** *"Capability Model 5 niveles para 'Deep Work asistido por IA 2026'. 6 dimensiones: diseño del entorno, gestión de notificaciones, selección de tareas no-delegables, colaboración humano-agente, producción cognitiva, evaluación de calidad. Por nivel: observables, métricas, anti-patrones."*

### A3-Maturity
**Prompt maestro:** *"Maturity Assessment de Deep Work post-IA. 30 preguntas + time-audit de 1 semana + protocolo de 'cognitive fitness' por nivel con 4 semanas de hábitos escalonados."*

---

## A4 — Sistemas Personales vs. Heroísmo — Del Improvisador al Diseñador

### A4-BoK
**Pregunta-guía:** ¿Cuál es el estado del arte 2026 de sistemas personales de conocimiento y workflow (PKM + automation) para el diseñador-de-su-propio-trabajo?
**Fuentes primarias:**
- *Building a Second Brain* + *The PARA Method* — Tiago Forte
- *How to Take Smart Notes* — Sönke Ahrens (Zettelkasten)
- *Getting Things Done* — David Allen (revisión 2023)
- *The Bullet Journal Method* — Ryder Carroll
- *The 4 Disciplines of Execution* — McChesney/Covey/Huling
- Frameworks OKR (John Doerr) + outcomes-based planning
**Prompt maestro:** *"BoK sobre sistemas personales de productividad 2023–2026 (PKM + workflow + OKR). Cubre 6 sistemas (GTD, PARA, Zettelkasten, BuJo, OKR, Building a Second Brain), comparativa honesta, casos de falla, integración con IA en 2026, 10 fuentes primarias."*

### A4-Capability
**Prompt maestro:** *"Capability Model 5 niveles 'diseño de sistemas personales'. 6 dimensiones: captura, organización, destilación, producción, revisión, evolución. Por nivel: observables, métricas, anti-patrón del héroe-improvisador."*

### A4-Maturity
**Prompt maestro:** *"Maturity Assessment 'sistemas personales'. 30 preguntas + auditoría de 7 días (qué capturo, dónde vive, cuándo lo reviso, cómo lo convierto en producto) + plan de migración por nivel (del héroe al diseñador)."*

---

# FAMILIA B — "Automatismo y Presencia 2026"

**Marco rector renovado (2026):** el automatismo NO es enemigo de la presencia. Es su aliado cuando está **diseñado conscientemente**. El enemigo es el automatismo **inconsciente / heredado / reactivo**. La maestría está en el **diseño dual**.

---

## B1 — Hábitos que Liberan — Diseño de Automatismos Positivos

### B1-BoK
**Pregunta-guía:** ¿Qué sabemos en 2026 sobre diseño consciente de hábitos que liberan atención para lo importante?
**Fuentes primarias:**
- *Atomic Habits* — James Clear
- *Tiny Habits* — BJ Fogg
- *Good Habits, Bad Habits* — Wendy Wood
- *The Power of Habit* — Charles Duhigg
- Papers sobre basal ganglia y habit formation (Graybiel, Wood)
- Papers sobre implementation intentions (Gollwitzer)
- *Hooked* — Nir Eyal (para entender el inverso)
**Prompt maestro:** *"BoK 2023–2026 sobre ciencia del hábito aplicada a knowledge workers. Cubre: neurociencia del habit loop, diferencia entre habit y routine y ritual, habit stacking con IA, 'automatismos positivos vs negativos', 3 controversias vigentes (21 días mito, willpower vs context, identidad vs acción), 12 fuentes primarias."*

### B1-Capability
**Prompt maestro:** *"Capability Model 5 niveles 'diseño de automatismos positivos'. 6 dimensiones: detección del trigger, diseño del cue, diseño de reward, stacking, medición, evolución. Por nivel: observables, métricas (cumplimiento, drop-off, habit strength), anti-patrones."*

### B1-Maturity
**Prompt maestro:** *"Maturity Assessment 'habit portfolio'. Inventario de 15 hábitos actuales (productivos vs reactivos vs tóxicos), 30 preguntas de diseño, plan de instalación por nivel (1 hábito nuevo por semana, máximo; un hábito a desinstalar por mes) con ritual de revisión mensual."*

---

## B2 — Flujo Operativo — Fricción Cero en Tareas Repetitivas

### B2-BoK
**Pregunta-guía:** ¿Cómo orquestar IA + plantillas + sistemas para que lo repetitivo fluya sin consumir foco, y entrar más seguido en flow?
**Fuentes primarias:**
- *Flow* — Mihaly Csikszentmihalyi
- *The Rise of Superman* + *Stealing Fire* — Steven Kotler
- Papers sobre cognitive offloading (Risko, Storm 2016+)
- *Indistractable* — Nir Eyal
- *The Checklist Manifesto* — Atul Gawande
- Automation literacy (Sherry Turkle contexto crítico)
**Prompt maestro:** *"BoK sobre 'flujo operativo: fricción cero en tareas repetitivas 2023–2026'. Cubre: flow state science, cognitive offloading (beneficios y deuda), automation literacy, checklists + SOPs personales, IA como extensión del workflow, 3 tensiones abiertas, 10 fuentes."*

### B2-Capability
**Prompt maestro:** *"Capability Model 5 niveles 'flujo operativo personal'. 6 dimensiones: identificación de tarea repetitiva, diseño de plantilla, automatización (No-Code/agentic), checkpoint de calidad, cierre del loop, mantenimiento. Por nivel: observables, métricas (tiempo ahorrado, tasa de error, frecuencia de flow), anti-patrones."*

### B2-Maturity
**Prompt maestro:** *"Maturity Assessment 'flujo operativo'. 30 preguntas + auditoría semanal de 20 tareas repetitivas con clasificación (automatizable total / parcial / no) + plan de 12 semanas para bajar fricción con 4 artefactos concretos (plantilla, agente, checklist, SOP)."*

---

## B3 — Señales de Presencia — Cuándo Desactivar el Piloto

### B3-BoK
**Pregunta-guía:** ¿En qué situaciones el automatismo traiciona y requiere presencia consciente, y cómo detectarlas en tiempo real?
**Fuentes primarias:**
- *Thinking, Fast and Slow* — Daniel Kahneman (System 1/2)
- *Mindfulness* — Ellen Langer (2014 + updates)
- *Full Catastrophe Living* — Jon Kabat-Zinn
- *The Craving Mind* — Judson Brewer
- *Nudge* — Thaler & Sunstein (contexto de inercia)
- Papers sobre metacognición (Flavell, Nelson-Narens)
- *Making Sense* — Sam Harris (contexto filosófico)
**Prompt maestro:** *"BoK 2023–2026 sobre 'señales que requieren presencia consciente'. Taxonomía de situaciones donde el automatismo traiciona (decisiones irreversibles, relaciones de confianza, ética, creatividad, aprendizaje nuevo, riesgo físico, dilema moral), neurociencia de System 1 vs 2, mindfulness clínico, 10 fuentes primarias."*

### B3-Capability
**Prompt maestro:** *"Capability Model 5 niveles 'detección de señales de presencia requerida'. 6 dimensiones: reconocimiento del trigger, interrupción consciente, re-anclaje corporal, re-evaluación cognitiva, decisión intencional, post-mortem reflexivo. Por nivel: observables, métricas (tiempo de reacción de interrupción, calidad de decisión), anti-patrones."*

### B3-Maturity
**Prompt maestro:** *"Maturity Assessment 'presencia intencional'. 30 preguntas + auto-observación de 2 semanas con 1 evento/día logged (qué gatilló, si hubo interrupción consciente, qué resultó) + ritual semanal de revisión por nivel."*

---

## B4 — Meta-Atención — Diseño de Decisión Dual

### B4-BoK
**Pregunta-guía:** ¿Cómo se construye un framework personal de decisión "¿automatizo o estoy presente?" y cómo se mantiene vivo?
**Fuentes primarias:**
- Metacognition research (Flavell 1979, Nelson-Narens 1990, updates 2020+)
- *Thinking in Bets* — Annie Duke
- *Superforecasting* — Tetlock & Gardner
- *The Art of Thinking Clearly* — Rolf Dobelli
- *Decisive* — Heath Brothers
- *The Checklist Manifesto* — Atul Gawande (loop back)
- Attention economy research (Odell, Williams)
**Prompt maestro:** *"BoK 2023–2026 sobre 'meta-atención y diseño de decisión dual automatismo/presencia'. Incluye: metacognición ejecutiva, monitoring & control framework, decision matrices, attention economy, 3 controversias (free will vs determinism, attention as resource vs capacity, flow vs deliberate practice), 12 fuentes."*

### B4-Capability
**Prompt maestro:** *"Capability Model 5 niveles 'meta-atención'. 6 dimensiones: conciencia del portfolio atencional, ruleset explícito (qué automatizo, qué preservo para presencia), rituales de revisión, métricas de calidad de decisión, ajuste adaptativo, enseñanza a otros. Por nivel: observables, métricas, anti-patrones."*

### B4-Maturity
**Prompt maestro:** *"Maturity Assessment 'meta-atención'. Scorecard de 30 ítems + árbol de decisión personal (template) + plan trimestral de 'portfolio review' de automatismos (qué promuevo, qué jubilo, qué rediseño) + ritual de onboarding de un nuevo automatismo con gate de 30 días."*

---

# Meta-prompts transversales (aplican a las 8 notebooks)

## MT1 — Blueprint previo a cada DR (del playbook §914)
*"Actúa como Research Blueprint Architect. Antes de lanzar un Deep Research sobre [TEMA], produce: (1) 5 preguntas-guía en orden de profundidad, (2) 3 hipótesis falsificables, (3) lista de 10 fuentes primarias candidatas con justificación, (4) criterios de inclusión/exclusión, (5) definición operacional de 'suficiente' (cuándo parar), (6) 3 riesgos de sesgo del corpus probable, (7) formato del output final."*

## MT2 — Triangulación (del playbook §1828)
*"Te paso 3 BoK sobre [TEMA] generados por 3 IAs distintas (A: Kimi, B: ChatGPT, C: Perplexity). Identifica: (1) puntos de consenso (aparecen en ≥2), (2) contradicciones explícitas, (3) omisiones de cada una, (4) qué IA tiene mejor evidencia citada en cada contradicción, (5) síntesis consolidada con trazabilidad a fuente original. Output: un solo BoK con tabla de confianza por sección."*

## MT3 — Verificación anti-"fluent ≠ correct" (playbook §1800)
*"El documento que sigue parece bien escrito. Audítalo contra 6 red flags: (1) afirmaciones sin citación, (2) plurales vagos ('estudios muestran'), (3) cifras sin fuente, (4) metáforas disfrazadas de mecanismo, (5) citas de libros sin página, (6) conclusiones que no se derivan de las premisas. Marca cada sección con verde/ámbar/rojo y sugiere correcciones."*

## MT4 — Ingesta a NotebookLM (playbook §2552)
*"Tengo un [BoK|Capability|Maturity] sobre [TEMA]. Antes de cargarlo como source en NotebookLM, genera: (1) título de source (≤80 chars), (2) descripción (≤200 chars) para el panel lateral, (3) 3 notas de estudio derivadas (1 resumen, 1 flashcard set, 1 quiz de 5 preguntas), (4) 1 prompt de conversación sugerido para el chat del notebook."*

---

# Plan operativo de ejecución

| # | Entregable | Artefacto | Orden |
|---|---|---|---|
| 1 | Este catálogo (`DR-CATALOG-2026.md`) | Markdown | ✅ este turno |
| 2 | Notebook A1 + 3 DR artifacts (BoK/Cap/Mat) | NotebookLM + 3 sources text | iter 2 |
| 3 | Notebook B1 + 3 DR artifacts | NotebookLM + 3 sources text | iter 3 |
| 4 | Notebook A2 + 3 DR | iter 4 |
| 5 | Notebook B2 + 3 DR | iter 5 |
| 6 | Notebook A3 + 3 DR | iter 6 |
| 7 | Notebook B3 + 3 DR | iter 7 |
| 8 | Notebook A4 + 3 DR | iter 8 |
| 9 | Notebook B4 + 3 DR | iter 9 |
| 10 | Tagging + cross-check brand + studio artifacts | 8 audios + 8 briefing docs + 8 mind maps | iter 10-11 |

**Gates de calidad por iteración:**
1. Cada BoK cita ≥10 fuentes primarias con URL/DOI.
2. Cada Capability Model tiene matriz 5×6 completa con anti-patrón por nivel.
3. Cada Maturity tiene 30 preguntas + scoring + 5 planes de intervención.
4. Cada notebook tiene 3 sources + 1 nota-índice + research_start lanzado + al menos 1 studio artifact.
5. Cross-check contra `faf4416f` (Contenido con Branding MetodologIA) para voz Artesano.

**Criterio de "done" por notebook:**
- [ ] 3 sources DR (BoK + Cap + Mat) agregados
- [ ] 1 research_start ejecutado (para triangular con corpus web NotebookLM)
- [ ] 1 nota-índice con objetivos + escala playbook + entregables esperados
- [ ] Tags aplicados: `family-A|family-B`, `ciclo-2-2026`, `brand-metodologia`, `playbook-aprender-aprehender`
- [ ] 1 audio deep-dive creado
- [ ] 1 briefing doc generado

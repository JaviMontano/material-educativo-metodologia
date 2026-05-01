# Glosario · 30+ Términos Canónicos

> Ontología única de la skill. Todos los agentes y referencias citan estos términos exactos. **No inventar sinónimos.**

**Fuente canónica**: Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · §Glosario.

---

## Cómo usar este glosario

- **Es la fuente única de verdad** terminológica de la skill.
- Cuando un agente o output usa un término, debe usar **exactamente** la definición aquí.
- Si un concepto no está aquí pero es relevante → primero proponer agregarlo, no improvisar.
- Términos en español es-CO. Equivalente inglés cuando aplica.

---

## A

### Aprender (Acquire)
Primera fase del ciclo. Adquirir información y construir estructuras conceptuales iniciales. Transición Escala 0→1.
**Tiempo típico**: 1–4h.
**Salida**: BoK + glosario + concept map.
→ ver `agents/coach-aprender.md`.

### Aprehender (Apprehend / Retain)
Segunda fase. Retener para recuperar, explicar y defender sin notas. Transición Escala 1→3.
**Tiempo típico**: 20–64h.
**Distinción crítica**: aprender ≠ aprehender. La diferencia es la capacidad de recuperación bajo presión.
→ ver `agents/coach-aprehender.md`.

### Areté (Ἀρετή)
Concepto griego: excelencia mediante práctica deliberada · virtud como hábito.
**Pilar narrativo** del playbook (junto con Pensamiento Crítico, Ciencia Cognitiva, Soberanía Profesional).
→ ver `knowledge-base/filosofia-arete-virtud.md`.

### Arquetipo (NotebookLM)
Configuración persona específica para NotebookLM. 8 arquetipos canónicos: Coach · Evaluador · Entrevistador · QBR · Auditor · Relevance · Fact-Check · Generator.
→ ver `assets/notebooklm-archetypes.json`.

### Auditoría de Relevancia
Evaluación mensual de tus skills usando framework 4-D (Vigencia · ROI · Obsolescencia · Demanda).
**Output**: decisiones [MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR].
→ ver Prompt #5 + `rituals/ritual-auditoria-mensual.md`.

---

## B

### Blueprint (Research Blueprint)
Plan metodológico de investigación: declaración de tema, hipótesis, criterios de fuente primaria, glosario inicial, concept map.
**Output del Workflow 1**.
→ ver Prompt #1 + `assets/plantilla-blueprint.md`.

### BoK (Body of Knowledge)
Mapa completo de un dominio: subtemas, conexiones, fuentes primarias/secundarias/terciarias, controversias, estado del arte.
**Anti-patrón**: BoK de 1 sola IA. Triangular en 3+ IAs es mandatory.
→ ver `references/02-tres-modelos-fundacionales.md`.

---

## C

### Cadencia
Frecuencia de práctica. **Principio MetodologIA**: *"Cadencia > intensidad. 15 min diarios > 3 horas el sábado."*

### Capability Model
Modelo de progresión de habilidades en niveles (Fundamentos · Intermedio · Avanzado · Experto). Define lo que necesitas saber **HACER**, no solo saber.
**Validación**: requiere experto humano del campo, no solo IA.
→ ver `references/02-tres-modelos-fundacionales.md`.

### Ciencia Cognitiva
Disciplina que estudia cómo el cerebro adquiere, procesa, retiene información. **Pilar del playbook**.
**Aplicación**: las 6 técnicas (retrieval, espaciado, Feynman, intercalado, elaboración, dual coding) están respaldadas por evidencia cognitiva.

### Compañero (Companion)
Esta skill como acompañante personal. **No es** instructor (no impone), **no es** manual (no es estático), **es** companion (responde a tu contexto cambiante).

### Concept Map (Mapa Conceptual)
Diagrama jerárquico de un dominio: tema central → subtemas → conceptos. Formato preferido: Mermaid.
→ ver `assets/plantilla-concept-map.mermaid`.

### Cross-fact-check
Auditoría de un research usando una IA #4 independiente. Detecta hallucinations, sycophancy, citas inventadas.
→ ver Prompt #4.

### Curioso (Escala 1)
Primera escala con conocimiento real. Tienes vocabulario, concept map, BoK triangulado.
**Tiempo**: 1-4h.
**Reto**: enseñar a Escala 0 sin trabarte.

---

## D

### Desatraso
Catch-up sobre conocimiento acumulado / industria que avanzó. Modos: Express (4h) · Sprint (20h) · Marathon (64h).
→ ver `scripts/desatraso_planner.py` + `examples/ejemplo-desatraso-llms-2024.md`.

### Diseñador
**Voz canónica MetodologIA**. Usar en lugar de "Arquitecto" (palabra bloqueada).
**Implicación**: diseñas métodos · no impones arquitecturas grandilocuentes.

### Dual Coding
Técnica cognitiva: combinar texto + visual + audio para múltiples canales de codificación.
**Evidencia**: +30% retención vs solo texto `[DOC: Mayer · Multimedia Learning · 2001]`.
→ ver `references/01-seis-tecnicas-cognitivas.md` §Dual Coding.

### Dunning-Kruger
Sesgo cognitivo: bajos niveles sobreestiman su nivel; altos niveles subestiman.
**Antídoto**: tests abiertos, no multiple choice; feedback de pares senior.
→ ver `references/04-anti-patrones-y-trampas.md`.

---

## E

### Elaboration (Elaboración)
Técnica cognitiva: conectar lo nuevo con lo existente preguntando *por qué, cómo, qué pasaría si, dónde no aplica*.
→ ver `references/01-seis-tecnicas-cognitivas.md` §Elaboration.

### Escala
Una de las 10 escalas de maestría (0 Ignorante → 9 Referente). Mide dónde estás hoy en un dominio específico.
→ ver `references/03-diez-escalas-maestria.md`.

### Espejismo de la Fluidez (Fluency Illusion)
Anti-patrón crítico: confundir "suena lógico" con "yo entiendo" porque la respuesta IA es elocuente.
**Antídoto**: Feynman + retrieval ciego.
→ ver `references/04-anti-patrones-y-trampas.md` §1.

### Evidence Tag
Marcador obligatorio de origen de cualquier afirmación factual:
- `[CÓDIGO]` · `[CONFIG]` · `[DOC]` · `[FUENTE-PRIMARIA]` · `[INFERENCIA]` · `[SUPUESTO]`
**Regla**: claim sin tag = se asume `[SUPUESTO]`.

### Experto (Escala 7)
1,000-10,000h. Define los límites del campo. Contribuye al avance.
→ ver `references/03-diez-escalas-maestria.md` §Escala 7.

### Explorador (Escala 2)
4-20h. Triangula fuentes, distingue primarias de derivadas, identifica controversias del campo.
**Workflow**: `workflows/workflow-2-explorador.md`.

---

## F

### Feynman Technique (Técnica Feynman)
Explicar un concepto a un niño de 12 años, sin jerga. Donde uses jerga, ahí está el gap.
**Atribuida** a Richard Feynman (Nobel Física 1965).
→ ver `references/01-seis-tecnicas-cognitivas.md` §Feynman.

### Fluencia Ilusoria
Ver "Espejismo de la Fluidez".

### Fuente Primaria
Documento original donde se publicó por primera vez una afirmación: paper académico, reporte oficial, dataset, patente.
**Regla**: si una IA cita algo y la fuente primaria no existe → hallucination.

### Fuente Secundaria
Autoridad reconocida que cita y comenta fuentes primarias. Ej: libros de texto, reviews académicos.

### Fuente Terciaria
Material derivado: blog posts, artículos divulgativos, cursos resumidos. **No usar como base de un BoK** — solo como punto de entrada.

---

## G

### Glosario
Lista de términos canónicos del dominio con definiciones precisas. **Mínimo 15 términos** para Escala 1, ideal 30+.
→ ver `assets/plantilla-glosario.md`.

---

## H

### Hallucination
Cuando una IA fabrica datos, citas, fechas, ecuaciones que no existen, presentándolos con tono autoritativo.
**Detector**: Primary Source Rule + Triangulation.
→ ver `references/04-anti-patrones-y-trampas.md` §2.

---

## I

### Identity Attachment
Anti-patrón: aferrarse a una skill obsoleta porque es parte de tu identidad profesional.
**Antídoto**: framework 4-D objetivo + decisión documentada.

### Iniciado (Escala 3)
20-64h. Puedes explicar sin notas, defender ante hostil, mentorizar Escala 1-2.
**Última escala que esta skill cubre directamente**.
→ ver `references/03-diez-escalas-maestria.md` §Escala 3.

### Intención antes que Intensidad
Principio MetodologIA. Declarar el qué y el por qué antes de invertir tiempo en el cómo.

### Interleaving (Intercalado)
Técnica cognitiva: mezclar problemas de subtemas distintos en una sesión.
→ ver `references/01-seis-tecnicas-cognitivas.md` §Interleaving.

---

## K

### Kata
Ejercicio deliberado, repetible, con criterios de éxito claros. Inspirado en artes marciales (kata = forma).
**6 katas en esta skill**: feynman-novato · triangulacion-3ias · recuperacion-ciega · defensa-hostil · soltar-legacy · fuente-primaria.
→ ver `katas/`.

---

## M

### Maestro (Escala 8)
10,000+h. Ve cross-disciplina. Forma dirección de industria.

### Marathon (Modo)
Programa de 64 horas en 16 semanas. Instala el hábito de aprehensión.
→ ver `rituals/ritual-practica-deliberada.md`.

### Maturity Model
Modelo que mide DÓNDE ESTÁS HOY en un dominio. 5 niveles: Inconsciente · Consciente-incompetente · Consciente-competente · Inconsciente-competente · Maestro.
→ ver `references/02-tres-modelos-fundacionales.md` §Maturity Model.

### Meta-Prompt
Prompt que genera otros prompts. 4 meta-prompts en esta skill (M1-M4): coach generator · evaluator generator · interviewer generator · presentation generator.
→ ver `prompts/meta/`.

### Método primero, IA después
Principio fundacional MetodologIA. La IA es herramienta, no el método. Sin método, la IA produce ruido.

### MetodologIA
Brand del playbook fuente y de esta skill. Brand voice v3.0. License CC BY-NC-SA 4.0. Founder: Javier Montaño.

---

## N

### NotebookLM
Plataforma de Google para creación de notebooks aumentados con IA. Studio Artifacts: audio overview, video overview, infografía, mind map, slide deck, briefing doc, study guide, quiz, flashcards, data table.
**8 arquetipos** configurables vía system prompts ≤10,000 chars.
→ ver `assets/notebooklm-archetypes.json`.

---

## P

### Pensamiento Crítico
Pilar narrativo del playbook. Capacidad de cuestionar fuentes, detectar sesgos, formular contra-hipótesis.

### Practicante (Escala 4)
64-200h. Ejecuta confiablemente en producción. Métricas estables.

### Práctica Deliberada
Práctica con feedback inmediato, fuera de la zona de comodidad, con objetivos específicos.
**Distinto de** "horas de oficina pasivas".
`[DOC: Ericsson · Peak · 2016]`.

### Primary Source Rule
Si una IA cita algo, busca la fuente original. Si no existe → hallucination.

### Progressive Disclosure
Patrón estructural de skills: 3 niveles de carga (frontmatter → SKILL.md body → references/agents/scripts on demand).
**Aplicado aquí**: SKILL.md ≤550 líneas; profundidad en references/.

---

## Q

### QBR (Quarterly Business Review)
Presentación trimestral de resultados. Usa Prompt #10 / Meta-Prompt M4 para preparación.

### Quiz Progresivo
Cuestionario que escala dificultad: Foundations → Intermediate → Advanced → Expert. Solo avanza si 4/5 correctas.
→ ver Prompt #8 + `assets/plantilla-quiz-scaling.md`.

---

## R

### Recall (Recuperación)
Generar información desde memoria sin pistas. Distinto de Recognition.

### Recognition (Reconocimiento)
Identificar información cuando la ves (con pistas). Más fácil que Recall.

### Referente (Escala 9)
Tú **eres** el estándar del campo. Tu sucesor define una escala nueva.

### (R)Evolucionar
Tercera fase del ciclo. Soltar lo obsoleto. Audit cycle mensual.
**Notación**: la (R) entre paréntesis es intencional. Significa "evolución consciente con potencial revolucionario", no "revolución" sola.
→ ver `agents/coach-revolucionar.md`.

### Retrieval Practice
Técnica cognitiva: recuperar de memoria sin pistas. Más efectiva que releer.
→ ver `references/01-seis-tecnicas-cognitivas.md` §Retrieval.

### Ritual
Práctica recurrente con cadencia fija. **4 rituales** en esta skill: diaria · semanal · mensual · 16 semanas.
→ ver `rituals/`.

---

## S

### Soberanía Profesional
Pilar MetodologIA. Capacidad de decidir tu trayectoria sin depender de mandatos externos. Requiere método propio.

### Spaced Repetition (Repetición Espaciada)
Técnica cognitiva: revisar en intervalos crecientes (mismo día → 3 días → 1 semana → 2 semanas → 1 mes).
→ ver `references/01-seis-tecnicas-cognitivas.md` §Spaced.

### Sprint (Modo)
Catch-up de 20 horas en 4 semanas. 1h × 5 días/semana.

### Sycophancy
Anti-patrón IA: la IA está de acuerdo contigo aunque estés equivocado.
**Antídoto**: Diablo's Advocate Protocol.

---

## T

### Triangulation Protocol
Proceso de cruzar 3+ IAs en la misma pregunta:
- Coincidencias 3/3 → verdad probable
- Coincidencias 2/3 → revisar fuente
- 1/3 → sospechoso
- Contradicciones → ORO (área de debate)

→ ver `katas/kata-triangulacion-3ias.md`.

---

## V

### Versado (Escala 6)
500-1,000h. Innova dentro de los límites del campo. Tus alumnos llegan a Escala 5+.

### Vigencia
Una de las 4 dimensiones del framework de auditoría de relevancia. ¿Es current en tu industria HOY?

---

## W

### Workflow
Secuencia estructurada de pasos para una fase. **3 workflows** en esta skill: Curioso (1-4h) · Explorador (4-20h) · Iniciado (20-64h).
→ ver `workflows/`.

---

## Términos NO usar (HARD RULE)

| ❌ Bloqueado | ✅ Usar en su lugar |
|---|---|
| Arquitecto | Diseñador · Orquestador |
| Transformación | (R)Evolución |
| Hacks | Método · Técnica |
| Best practices (suelto) | Práctica basada en evidencia |
| Senior (suelto) | Escala N (con número) |
| Experto en todo | (no decir esto · Dunning-Kruger) |
| Game-changer | Cambio metodológico |
| Disruptive (sin contexto) | (R)Evolutivo |

---

## Términos en evolución (revisar v1.1.0)

- "Companion" — alguien propuso "Acompañante" en revisión 2026
- "Skill" — manteniendo en inglés por contexto Claude Code
- "Workflow" — manteniendo · alternativa "Protocolo de fase"

---

> **Atribución**: Glosario consolidado del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 §Glosario, ampliado con terminología técnica de Claude Code Skills.
> *MetodologIA · CC BY-NC-SA 4.0*

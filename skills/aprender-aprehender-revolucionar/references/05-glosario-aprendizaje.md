# Glosario · 35+ Términos Canónicos

> Ontología única de la skill. Todos los agentes, prompts y workflows citan **exactamente** estos términos. NO inventar sinónimos. v1.1.0.

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Glosario · ampliado en v1.1 con términos operativos.

## Reglas de uso

- **Fuente única de verdad** terminológica de la skill.
- Si concepto no está · proponer agregarlo, NO improvisar.
- Términos en es-CO · equivalente EN cuando aplica.
- Cada término tiene `→` con archivo donde se opera.
- `[NUEVO-APORTE]` columna **anti-confusión**: pares de términos que se confunden con frecuencia y su distinción operativa.

## Anti-confusión · pares que se confunden

| Si pensaste... | Era... | Distinción |
|---|---|---|
| Aprender | Aprehender | Aprender = adquirir · Aprehender = defender bajo presión |
| Recognition | Recall | Recognition = reconocer con pista · Recall = generar de memoria sin pista |
| BoK | Capability | BoK = qué existe · Capability = qué saber HACER |
| Maturity Level | Escala | Maturity Level = 0-4 (5 niveles cognitivos) · Escala = 0-9 (10 niveles operativos del playbook) |
| Hallucination | Sycophancy | Hallucination = invento factual · Sycophancy = acuerdo sin sustento |
| Triangulación | Cross fact-check | Triangulación = 3+ IAs simultáneas · Cross fact-check = 1 IA auditando otra |
| Soltar (release) | Olvidar | Soltar = decisión activa con plan reskill · Olvidar = pasivo sin reemplazo |
| Cramming | Spaced Repetition | Cramming = sesión maratón · Spaced = sesiones espaciadas con intervalos crecientes |

---

## A

### Aprender (Acquire) · Fase 1
Adquirir información y construir estructura inicial. Transición Escala 0→1. Tiempo típico 1-4 h. Salida: BoK + glosario + concept map. → `agents/coach-aprender.md`

### Aprehender (Apprehend / Retain) · Fase 2
Retener para recuperar, explicar y defender sin notas, bajo presión. Transición Escala 1→3. Tiempo típico 20-64 h. **Distinción crítica**: Aprender ≠ Aprehender. La diferencia es recuperación bajo presión. → `agents/coach-aprehender.md`

### Areté (Ἀρετή)
Concepto griego: excelencia mediante hábito · virtud como práctica deliberada. Pilar narrativo del playbook. → `knowledge-base/filosofia-arete-virtud.md`

### Arquetipo (NotebookLM)
Persona configurable en NotebookLM Custom Goal. 8 arquetipos canónicos: Coach · Evaluador · Entrevistador · QBR · Auditor · Relevance · Fact-Check · Generator. → `assets/notebooklm-archetypes.json`

### Auditoría de Relevancia
Evaluación mensual de skills con framework 4-D. Output: decisiones [MANTENER/ACTUALIZAR/REEMPLAZAR/SOLTAR] con plan reskill. → Prompt #5 · `rituals/ritual-auditoria-mensual.md`

### Auditor cruzado
Subagente que detecta hallucinations, sycophancy, silent uncertainty, single-AI bias post-research. → `agents/auditor-cruzado.md`

## B

### Blueprint (Research Blueprint)
Plan metodológico de investigación: tema · objetivo · hipótesis · glosario inicial · concept map · fuentes 1°. Output Workflow 1. → Prompt #1 · `assets/plantilla-blueprint.md`

### BoK (Body of Knowledge)
Mapa completo del dominio: subtemas · conexiones · fuentes 1°/2°/3° · controversias · estado del arte · futuro. **Anti-patrón**: BoK de 1 sola IA · triangular 3+ IAs es mandatory. → `references/02-tres-modelos-fundacionales.md`

## C

### Cadencia
Frecuencia de práctica. **Principio MetodologIA**: cadencia > intensidad. 15 min diarios > 3 h el sábado.

### Capability Model
Niveles de progresión de habilidades (Fundamentos · Intermedio · Avanzado · Experto) con criterios testables. Define qué saber **HACER**, no solo saber. **Validación**: requiere experto humano del campo. → `references/02-tres-modelos-fundacionales.md` §Capability

### Casos borde (caso-borde)
Escenarios donde el camino feliz falla. Cada agente y workflow debe documentar ≥3. Tag `[CASO-BORDE]`. v1.1 introduce esta práctica formal.

### Ciencia Cognitiva
Estudio de cómo el cerebro adquiere, procesa, retiene información. **Pilar narrativo**. Sustenta las 6 técnicas. → `references/06-ciencia-cognitiva-fuentes.md`

### Companion (Compañero)
Esta skill como acompañante personal. NO es instructor (no impone) · NO es manual (no estático) · ES companion (responde a contexto cambiante).

### Concept Map
Diagrama jerárquico del dominio. Formato preferido: Mermaid (mindmap o graph TD). → `assets/plantilla-concept-map.mermaid`

### Cramming
Anti-patrón: maratón intensivo pre-evento. Olvidas 90% en 1 sem. → `references/04-anti-patrones-y-trampas.md` §7

### Cross-fact-check
Auditoría con 4ª IA independiente. Detecta hallucinations, sycophancy, single-AI bias. → Prompt #4

### Curioso (Escala 1)
Vocabulario básico ≥15 términos · BoK triangulado · sabes qué no sabes. Tiempo: 1-4 h. Reto: enseñar a Escala 0 sin trabarte.

## D

### Desatraso
Catch-up sobre conocimiento acumulado o industria que avanzó. Modos: Express (4 h) · Sprint (20 h) · Marathon (64 h). → `scripts/desatraso_planner.py`

### Diseñador
Voz canónica MetodologIA. Diseñas métodos · no impones arquitecturas grandilocuentes.

### Dual Coding
Técnica cognitiva: combinar texto + visual + audio. +30% retención `[DOC: Mayer 2014]`. → §técnicas

### Dunning-Kruger
Sesgo: bajos niveles sobreestiman, altos subestiman. Detector: diff auto-eval vs IA-eval ≥2 escalas. → `references/04-anti-patrones-y-trampas.md` §6

## E

### Elaboration
Conectar lo nuevo con previo · 4 preguntas (¿por qué? ¿cómo? ¿qué pasaría si? ¿dónde NO aplica?). → §técnicas

### Escala
Una de las 10 escalas de maestría (0 Ignorante → 9 Referente). NO confundir con Maturity Level (5 niveles cognitivos). → `references/03-diez-escalas-maestria.md`

### Espejismo de Fluidez (Fluency Illusion)
Anti-patrón crítico: confundir "suena lógico" con "yo entiendo" porque la respuesta IA es elocuente. Antídoto: Feynman + Retrieval. → §anti-patrones #1

### Evidence Tag
Marcador obligatorio de origen factual: `[CÓDIGO]` · `[CONFIG]` · `[DOC]` · `[FUENTE-PRIMARIA]` · `[INFERENCIA]` · `[SUPUESTO]`. v1.1 amplía con `[NUEVO-APORTE]` · `[CASO-BORDE]` · `[TRADE-OFF]` · `[CRITERIO-ACEPTACIÓN]` · `[LÍMITE]` · `[DECISIÓN]`. Regla: claim sin tag = se asume `[SUPUESTO]`.

### Experto (Escala 7)
1,000-10,000 h · define los límites del campo · contribuye al avance documentable.

### Explorador (Escala 2)
4-20 h · triangula fuentes · distingue 1°/2°/3° · identifica controversias. → `workflows/workflow-2-explorador.md`

## F

### Feynman Technique
Explicar un concepto a un niño de 12 años sin jerga. Donde uses jerga, ahí está el gap. Atribución: formalizada por Gleick (1992) y Oakley (2014), no por Feynman directamente. → §técnicas · `katas/kata-feynman-novato.md`

### Fluencia Ilusoria
= Espejismo de Fluidez. Ver Espejismo.

### Fuente Primaria
Documento original donde se publicó por primera vez una afirmación. Papers académicos · reportes oficiales · datasets · patentes. **Regla**: si IA cita y la fuente 1° no existe → hallucination.

### Fuente Secundaria
Autoridad reconocida que cita y comenta primarias. Libros de texto · reviews académicos.

### Fuente Terciaria
Material derivado: blog posts · artículos divulgativos · cursos resumidos. **NO usar como base de BoK** · solo como punto de entrada.

## G

### Gate (Quality Gate)
Punto de validación binario · NO avanzar a fase siguiente sin pasarlo. G-Aprender · G-Aprehender · G-(R)Evolucionar.

### Glosario
Lista de términos canónicos con definiciones precisas. Mínimo 15 para Escala 1, target 30 (este archivo). → `assets/plantilla-glosario.md`

## H

### Hallucination
IA fabrica datos · citas · fechas · ecuaciones que no existen, con tono autoritativo. Detector: Primary Source Rule + Triangulation. → §anti-patrones #2

## I

### Identity Attachment
Anti-patrón: aferrarse a skill obsoleta porque es parte de identidad profesional. Antídoto: framework 4-D + decisión documentada. → §anti-patrones #9

### Iniciado (Escala 3)
20-64 h · explica sin notas · defiende ante hostil · mentoriza Escala 1-2. **Última escala que la skill cubre directamente**. → `workflows/workflow-3-iniciado.md`

### Intención antes que Intensidad
Principio MetodologIA. Declarar el qué y por qué antes de invertir tiempo en el cómo.

### Interleaving (Intercalado)
Técnica cognitiva: mezclar problemas de subtemas distintos. Práctica intercalada > bloqueada para transferencia. → §técnicas

## K

### Kata
Ejercicio deliberado, repetible, con criterios de éxito. Inspirado en artes marciales. **6 katas** en esta skill. → `katas/`

## M

### Maestro (Escala 8)
10,000+ h · cross-disciplina · forma dirección de industria.

### Marathon
Programa 64 h en 16 semanas. Instala hábito de aprehensión. → `rituals/ritual-practica-deliberada.md`

### Maturity Model
Mide DÓNDE ESTÁS HOY. 5 niveles: Inconsciente · Consciente-Incompetente · Consciente-Competente · Inconsciente-Competente · Maestro. → `references/02-tres-modelos-fundacionales.md` §Maturity

### Meta-Prompt
Prompt que genera otros prompts. 4 meta-prompts (M1-M4). → `prompts/meta/`

### Método primero, IA después
Principio fundacional. La IA es herramienta · sin método produce ruido fluido.

### MetodologIA
Brand del playbook fuente y de esta skill. v3.0. License CC BY-NC-SA 4.0. Founder: Javier Montaño.

## N

### NotebookLM
Plataforma de Google para notebooks aumentados con IA. Studio Artifacts: audio · video · infografía · mind map · slide deck · briefing · study guide · quiz · flashcards · data table. **8 arquetipos** configurables vía system prompts ≤10K chars. → `assets/notebooklm-archetypes.json`

## P

### Pensamiento Crítico
Pilar narrativo · capacidad de cuestionar fuentes, detectar sesgos, formular contra-hipótesis.

### Practicante (Escala 4)
64-200 h · ejecuta confiablemente en producción · métricas estables.

### Práctica Deliberada
Práctica con feedback inmediato, fuera de zona de confort, con objetivos específicos. **Distinto de** "horas de oficina pasivas". `[DOC: Ericsson · Peak · 2016]`

### Primary Source Rule
Si una IA cita algo, busca fuente original. Si no existe → hallucination confirmada.

### Progressive Disclosure
Patrón: 3 niveles de carga (frontmatter → SKILL.md → references/agents/scripts on-demand). SKILL.md ≤550 líneas · profundidad en `references/`.

## Q

### QBR (Quarterly Business Review)
Presentación trimestral de resultados. Usa Prompt #10 / Meta-Prompt M4 para preparación.

### Quiz Progresivo
4 niveles: Foundations → Intermediate → Advanced → Expert. Solo avanza si 4/5 correctas. → Prompt #8 · `assets/plantilla-quiz-scaling.md`

## R

### Recall (Recuperación)
Generar información de memoria sin pistas. Distinto de Recognition (que es pasivo).

### Recognition (Reconocimiento)
Identificar info cuando la ves (con pistas). Más fácil que Recall.

### Referente (Escala 9)
Tú **eres** el estándar del campo. Externo · NO auto-declarable.

### (R)Evolucionar
Tercera fase · soltar consciente lo obsoleto. **Notación**: la (R) entre paréntesis es intencional · "evolución consciente con potencial revolucionario", no "revolución" sola. → `agents/coach-revolucionar.md`

### Retrieval Practice
Recuperar de memoria sin pistas. Más efectiva que releer. → §técnicas · `katas/kata-recuperacion-ciega.md`

### Ritual
Práctica recurrente con cadencia fija. **4 rituales** en la skill: diaria · semanal · mensual · 16 sem. → `rituals/`

## S

### Soberanía Profesional
Pilar MetodologIA · capacidad de decidir trayectoria sin depender de mandatos externos. Requiere método propio.

### Spaced Repetition (Repetición Espaciada)
Técnica: revisar en intervalos crecientes (día 0, 3, 7, 14, 30, 90). → §técnicas

### Sprint (Modo)
Catch-up 20 h en 4 semanas (1 h × 5 días/sem).

### Sycophancy
Anti-patrón IA: la IA está de acuerdo aunque estés equivocado. Antídoto: Diablo's Advocate Protocol. → §anti-patrones #3

## T

### Triangulation Protocol
Cruzar 3+ IAs en la misma pregunta:
- 3/3 → verdad probable
- 2/3 → revisar fuente
- 1/3 → sospechoso
- contradicciones → ORO (área de debate)

→ `katas/kata-triangulacion-3ias.md` · Prompt #4

## V

### Versado (Escala 6)
500-1,000 h · innova dentro de los límites · tus alumnos llegan a Escala 5+.

### Vigencia
Una de las 4 dimensiones del framework auditoría de relevancia. ¿Es current en tu industria HOY?

### Voces canónicas
Diseñador · (R)Evolución · Método · Soberanía Profesional · Areté · Ciencia Cognitiva · Pensamiento Crítico.

## W

### Workflow
Secuencia de pasos para una fase. **3 workflows**: Curioso (1-4 h) · Explorador (4-20 h) · Iniciado (20-64 h). → `workflows/`

---

## Términos en evolución (revisar v1.2)

- "Companion" — alternativa propuesta "Acompañante" pendiente de revisión
- "Skill" — manteniendo en EN por contexto Claude Code
- "Workflow" — manteniendo · alternativa "Protocolo de fase" descartada por extensión

---

## Referencias cruzadas

- Modelos: `references/02-tres-modelos-fundacionales.md`
- Técnicas: `references/01-seis-tecnicas-cognitivas.md`
- Anti-patrones: `references/04-anti-patrones-y-trampas.md`
- Sustento académico: `references/06-ciencia-cognitiva-fuentes.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0 §Glosario

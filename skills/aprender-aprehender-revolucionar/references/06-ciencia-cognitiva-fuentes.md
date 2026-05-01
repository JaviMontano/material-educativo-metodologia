# Ciencia Cognitiva · Fuentes Académicas

> Sustento académico de cada técnica, modelo y anti-patrón usado en esta skill. Una afirmación sin fuente es una opinión.

**Filosofía**: cada técnica del playbook tiene base académica reconocida. Esta página documenta las fuentes para que puedas verificar, profundizar, defender ante un escéptico.

**Tag**: `[DOC]` para artículos académicos · `[LIBRO]` para libros · `[META]` para meta-análisis.

---

## 1 · Retrieval Practice

### Fuente fundacional
**Karpicke, J. D., & Roediger, H. L. (2008). *The Critical Importance of Retrieval for Learning*. Science, 319(5865), 966–968.** `[DOC]`

> Estudio seminal que demostró que la recuperación activa (testing) supera a la re-lectura para retención a largo plazo, en estudiantes universitarios con material de biología.

### Meta-análisis clave
**Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). *Rethinking the Use of Tests: A Meta-Analysis of Practice Testing*. Review of Educational Research, 87(3), 659–701.** `[META]`

> Meta-análisis de 118 estudios. Effect size promedio g = 0.61 (efecto medio-grande). Confirma utilidad amplia.

### Libro divulgativo recomendado
**Brown, P. C., Roediger, H. L., & McDaniel, M. A. (2014). *Make It Stick: The Science of Successful Learning*. Belknap Press.** `[LIBRO]`

> Síntesis para audiencia general. Imprescindible si trabajas con aprendizaje profesional.

### Aplicación en esta skill
- `references/01-seis-tecnicas-cognitivas.md` §1
- `katas/kata-recuperacion-ciega.md`
- `scripts/retrieval_session.py`

---

## 2 · Spaced Repetition

### Fuente fundacional
**Ebbinghaus, H. (1885). *Über das Gedächtnis* (On Memory). Translated by H. A. Ruger & C. E. Bussenius (1913).** `[LIBRO]`

> Curva del olvido: olvidamos exponencialmente (50% en 1h, 70% en 24h, 90% en 1 semana).

### Estudio moderno clave
**Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). *Spacing Effects in Learning: A Temporal Ridgeline of Optimal Retention*. Psychological Science, 19(11), 1095–1102.** `[DOC]`

> Identificó intervalos óptimos según objetivo de retención. Para retener 6 meses: revisar a los días 1, 7, 30, 60, 180.

### Meta-análisis clave
**Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Distributed Practice in Verbal Recall Tasks: A Review and Quantitative Synthesis*. Psychological Bulletin, 132(3), 354–380.** `[META]`

### Aplicación
- `references/01-seis-tecnicas-cognitivas.md` §2
- `assets/plantilla-fichas-anki.csv`
- `assets/calendar-invites/aprehension-semanal.ics`

---

## 3 · Feynman Technique

### Fuente fundacional · auto-explicación
**Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). *Self-Explanations: How Students Study and Use Examples in Learning to Solve Problems*. Cognitive Science, 13(2), 145–182.** `[DOC]`

> Demostró que los estudiantes que se auto-explican aprenden significativamente mejor que los que no. Base experimental de la Técnica Feynman.

### Atribución a Feynman
**Gleick, J. (1992). *Genius: The Life and Science of Richard Feynman*. Pantheon Books.** `[LIBRO]`

> Documenta el método de Feynman aunque él nunca lo formalizó así.

### Operacionalización moderna
**Oakley, B. (2014). *A Mind for Numbers: How to Excel at Math and Science (Even If You Flunked Algebra)*. TarcherPerigee.** `[LIBRO]`

> Capítulo dedicado al "Feynman Technique" como protocolo de 4 pasos.

### Aplicación
- `references/01-seis-tecnicas-cognitivas.md` §3
- `katas/kata-feynman-novato.md`

---

## 4 · Interleaving

### Fuente fundacional
**Rohrer, D., & Pashler, H. (2010). *Recent Research on Human Learning Challenges Conventional Instructional Strategies*. Educational Researcher, 39(5), 406–412.** `[DOC]`

> Demostró que práctica intercalada (mezclando tipos de problemas) supera a práctica bloqueada para transferencia y retención, contraintuitivamente — los estudiantes sienten que aprenden peor con intercalado, pero retienen más.

### Estudio adicional
**Rohrer, D., Dedrick, R. F., & Stershic, S. (2015). *Interleaved Practice Improves Mathematics Learning*. Journal of Educational Psychology, 107(3), 900–908.** `[DOC]`

### Aplicación
- `references/01-seis-tecnicas-cognitivas.md` §4
- `prompts/08-evaluator-certification.md` (quiz mixto multi-subtema)

---

## 5 · Elaboration

### Fuente fundacional
**Pressley, M., Wood, E., Woloshyn, V. E., Martin, V., King, A., & Menke, D. (1992). *Encouraging Mindful Use of Prior Knowledge: Attempting to Construct Explanatory Answers Facilitates Learning*. Educational Psychologist, 27(1), 91–109.** `[DOC]`

> Mostró que pedirle al estudiante elaborar el "por qué" de un hecho mejora retención significativamente vs solo memorizar el hecho.

### Aplicación a aprendizaje técnico
**Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *Improving Students' Learning With Effective Learning Techniques: Promising Directions From Cognitive and Educational Psychology*. Psychological Science in the Public Interest, 14(1), 4–58.** `[META]`

> El meta-análisis canónico que rankeó las 10 técnicas de estudio más populares. Elaborative Interrogation (las preguntas "por qué" de Elaboration) recibió calificación "moderate utility".

### Aplicación
- `references/01-seis-tecnicas-cognitivas.md` §5

---

## 6 · Dual Coding

### Fuente fundacional
**Paivio, A. (1971). *Imagery and Verbal Processes*. Holt, Rinehart and Winston.** `[LIBRO]`

> Teoría del codificación dual: el cerebro tiene canales separados para procesamiento verbal y visual; usar ambos crea 2 rutas de recuperación.

### Aplicación a multimedia
**Mayer, R. E. (2001). *Multimedia Learning*. Cambridge University Press.** `[LIBRO]`

> Cognitive Theory of Multimedia Learning. Demuestra que combinar texto + imagen produce +30% retención vs solo texto, cuando se sigue principios específicos (proximidad espacial, modalidad complementaria, etc.).

### Versión actualizada
**Mayer, R. E. (2014). *The Cambridge Handbook of Multimedia Learning* (2nd ed.). Cambridge University Press.** `[LIBRO]`

### Aplicación
- `references/01-seis-tecnicas-cognitivas.md` §6
- NotebookLM artifacts: audio overview + mind map + slide deck (3 representaciones del mismo material)

---

## 7 · Dunning-Kruger Effect

### Fuente fundacional
**Kruger, J., & Dunning, D. (1999). *Unskilled and Unaware of It: How Difficulties in Recognizing One's Own Incompetence Lead to Inflated Self-Assessments*. Journal of Personality and Social Psychology, 77(6), 1121–1134.** `[DOC]`

> Estudio canónico. Cuatro experimentos demostrando el sesgo de auto-evaluación inversa: los menos competentes sobreestiman sus habilidades.

### Crítica metodológica importante
**Krueger, J., & Mueller, R. A. (2002). *Unskilled, Unaware, or Both? The Better-Than-Average Heuristic and Statistical Regression Predict Errors in Estimates of Own Performance*. Journal of Personality and Social Psychology, 82(2), 180–188.** `[DOC]`

> Argumenta que parte del efecto Dunning-Kruger es regresión a la media (artefacto estadístico), no sesgo cognitivo real. Sin embargo, replicaciones modernas confirman que el efecto sustantivo persiste.

### Aplicación
- `references/04-anti-patrones-y-trampas.md` §6
- `references/03-diez-escalas-maestria.md` (todas las escalas)

---

## 8 · Bjorks' Desirable Difficulties

### Fuente fundacional
**Bjork, R. A., & Bjork, E. L. (2011). *Making Things Hard on Yourself, but in a Good Way: Creating Desirable Difficulties to Enhance Learning*. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers.** `[DOC]`

> Concepto fundacional: el aprendizaje que **se siente fácil** durante la sesión típicamente produce **menos retención**. La "dificultad deseable" (esfuerzo productivo) es el indicador real de codificación profunda.

### Implicación
La **fluidez de procesamiento** (que IA produce abundantemente) es engañosa como indicador de aprendizaje.

### Aplicación
- `references/04-anti-patrones-y-trampas.md` §1 (Espejismo de Fluidez)

---

## 9 · 10,000-Hour Rule (Práctica Deliberada)

### Fuente original
**Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). *The Role of Deliberate Practice in the Acquisition of Expert Performance*. Psychological Review, 100(3), 363–406.** `[DOC]`

> Estudio en violinistas que mostró correlación entre horas de **práctica deliberada** (no horas pasivas) y nivel de expertise.

### Popularización (con caveats)
**Gladwell, M. (2008). *Outliers: The Story of Success*. Little, Brown and Company.** `[LIBRO]`

> Popularizó la "10,000 horas". El propio Ericsson criticó la simplificación: no es solo cantidad, sino calidad de la práctica.

### Refinamiento por Ericsson
**Ericsson, A., & Pool, R. (2016). *Peak: Secrets from the New Science of Expertise*. Houghton Mifflin Harcourt.** `[LIBRO]`

> Aclara: práctica deliberada (con feedback, en zona de stretch, con propósito) es lo que importa. Las "10,000 horas" son aproximación, no regla mágica.

### Aplicación
- `references/03-diez-escalas-maestria.md` (Escalas 7-9)

---

## 10 · IA Hallucinations & Sycophancy

### Hallucinations
**Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). *Survey of Hallucination in Natural Language Generation*. ACM Computing Surveys, 55(12), 1–38.** `[DOC]`

> Survey académico de tipos y causas de hallucinations en LLMs. Recomienda triangulación + verificación de fuente primaria.

### Sycophancy
**Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., Cheng, N., Durmus, E., Hatfield-Dodds, Z., Johnston, S. R., Kravec, S., Maxwell, T., McCandlish, S., Ndousse, K., Rausch, O., Schiefer, N., Yan, D., Zhang, M., & Perez, E. (2023). *Towards Understanding Sycophancy in Language Models*. arXiv:2310.13548.** `[DOC]`

> Estudio de Anthropic. Identifica que RLHF puede inducir sycophancy: modelos aprenden a coincidir con usuarios para maximizar reward, incluso cuando los usuarios están equivocados.

### Aplicación
- `references/04-anti-patrones-y-trampas.md` §2, §3
- `prompts/04-cross-fact-check.md`
- `katas/kata-fuente-primaria.md`

---

## 11 · CAP Theorem (mencionado en BoK ejemplos)

### Fuente original
**Brewer, E. A. (2000). *Towards Robust Distributed Systems* [Keynote]. Symposium on Principles of Distributed Computing (PODC).** `[DOC]`

### Formalización
**Gilbert, S., & Lynch, N. (2002). *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*. ACM SIGACT News, 33(2), 51–59.** `[DOC]`

### Refinamiento (PACELC)
**Abadi, D. (2012). *Consistency Tradeoffs in Modern Distributed Database System Design*. Computer, 45(2), 37–42.** `[DOC]`

### Aplicación
- `references/02-tres-modelos-fundacionales.md` (BoK ejemplo de Sistemas Distribuidos)

---

## 12 · Areté · Filosofía

### Fuentes clásicas
**Aristotle. *Nicomachean Ethics*. (Multiple translations)** `[LIBRO]`

> Areté como excelencia mediante hábito. "Somos lo que hacemos repetidamente. La excelencia no es un acto sino un hábito" (parafraseado por Will Durant, atribución frecuentemente errónea a Aristóteles).

### Atribución correcta
**Durant, W. (1926). *The Story of Philosophy*. Simon & Schuster.** `[LIBRO]`

> Durant es quien condensó la idea de Aristóteles en la frase popular sobre "excelencia es hábito". La cita exacta es de Durant, no de Aristóteles. **Importante para no caer en el anti-patrón #2 (atribución errónea).**

### Aplicación
- `knowledge-base/filosofia-arete-virtud.md`
- Pilar narrativo del playbook

---

## 13 · Adult Learning Theory

### Fuente
**Knowles, M. S. (1980). *The Modern Practice of Adult Education: From Pedagogy to Andragogy*. Prentice Hall.** `[LIBRO]`

> Andragogía: los adultos aprenden distinto a niños. Necesitan: (1) saber por qué aprenden, (2) experiencia previa como recurso, (3) relevancia inmediata, (4) auto-direccionamiento.

### Aplicación
Esta skill es **andragógica**: asume Javier es adulto, profesional, autónomo. Enfatiza:
- Declaración de propósito ("por qué")
- Construcción sobre experiencia previa (Capability Model)
- Aplicación inmediata (workflows time-boxed)
- Auto-direccionamiento (Javier elige fase, modo, tiempo)

---

## 14 · Cognitive Load Theory

### Fuente
**Sweller, J. (1988). *Cognitive Load During Problem Solving: Effects on Learning*. Cognitive Science, 12(2), 257–285.** `[DOC]`

> Memoria de trabajo es limitada (~4-7 elementos simultáneos). Sobrecargarla reduce aprendizaje. Material debe estructurarse para minimizar carga extraña.

### Implicación para esta skill
- Glosario antes que conceptos avanzados (chunking)
- Dual coding distribuye carga entre canales
- Spaced repetition evita sobrecarga en una sola sesión

### Aplicación
- Filosofía detrás de Workflow 1 → 2 → 3 progresivo
- Anti-patrón cramming

---

## Cómo usar estas fuentes

### Si Javier dice "no me convence esta técnica"
Vé al académico relevante. Ej: si duda de Spaced Repetition → cita Cepeda et al. 2008 + meta-análisis.

### Si necesitas defender públicamente
Cita autor + año en formato APA. Ej: *"La práctica espaciada supera al cramming para retención a 6 meses (Cepeda et al., 2008)."*

### Si quieres profundizar
Empezar por los 3 libros divulgativos:
1. Brown, Roediger, McDaniel · *Make It Stick* (2014) — para retrieval + spacing
2. Mayer · *Multimedia Learning* (2014) — para dual coding
3. Ericsson & Pool · *Peak* (2016) — para práctica deliberada

### Verificación de citas (tu propio kata)
Para cada cita en este documento:
1. ¿El paper / libro existe? (busca en Google Scholar)
2. ¿La afirmación coincide con el abstract? (lee abstract)
3. ¿Está en el ranking de citado? (>100 citas indica reconocimiento)

→ practica esto con `katas/kata-fuente-primaria.md`.

---

## Limitaciones y caveats

> **Honestidad académica**: estas técnicas tienen evidencia robusta, pero la efectividad varía según:

- **Dominio**: matemáticas vs idiomas vs habilidades motoras = effect sizes distintos
- **Edad**: estudios mayoritariamente con universitarios. Adultos profesionales son población menos estudiada.
- **Cultura**: la mayoría de estudios son WEIRD (Western, Educated, Industrialized, Rich, Democratic). Generalización a otros contextos no garantizada.
- **Individuo**: heterogeneidad alta. Lo que funciona en promedio puede no funcionar en ti.

**Implicación**: usa las técnicas como hipótesis de partida, mide tus propios resultados, ajusta.

---

## Fuentes adicionales recomendadas

### Libros
- **Make It Stick** · Brown, Roediger, McDaniel (2014) — el manual definitivo
- **Peak** · Ericsson & Pool (2016) — práctica deliberada
- **The 4-Hour Chef** · Tim Ferriss (2012) — meta-aprendizaje aplicado
- **Ultralearning** · Scott H. Young (2019) — programas auto-dirigidos intensivos
- **A Mind for Numbers** · Barbara Oakley (2014) — adaptación divulgativa

### Cursos online
- **Learning How to Learn** (Coursera, Oakley) — curso más popular del mundo en aprendizaje
- **Mindshift** (Coursera, Oakley) — cómo cambiar de carrera

### Podcasts
- **The Knowledge Project** (Shane Parrish) — entrevistas con expertos en learning
- **Hidden Brain** (NPR) — episodios sobre psicología del aprendizaje

---

> **Atribución**: Compilación de fuentes para sustento académico de las técnicas, modelos y anti-patrones del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0.
> Las afirmaciones en esta skill **no son** opinión personal de Javier Montaño · están respaldadas por la evidencia citada arriba.
> *MetodologIA · CC BY-NC-SA 4.0*

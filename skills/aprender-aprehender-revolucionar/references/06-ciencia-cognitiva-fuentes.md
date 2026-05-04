# Ciencia Cognitiva · Fuentes Académicas

> Sustento académico de cada técnica, modelo y anti-patrón. Una afirmación sin fuente es una opinión. v1.1.0.

**Tags**: `[DOC]` artículo académico · `[LIBRO]` libro · `[META]` meta-análisis · `[FUENTE-PRIMARIA]` documento canónico del campo.

`[NUEVO-APORTE]` Esta página es el **bibliografía único** de la skill. Cualquier `[DOC: autor año]` en otros archivos resuelve aquí. Si una cita aparece en otro archivo pero no aquí, es candidata a hallucination — agregar o eliminar.

## Mapa de qué sustenta qué

| Técnica/concepto | Fuente fundacional | Meta-análisis (si aplica) |
|---|---|---|
| Retrieval Practice | Karpicke & Roediger 2008 | Adesope et al 2017 |
| Spaced Repetition | Ebbinghaus 1885 · Cepeda 2008 | Cepeda 2006 |
| Feynman Technique | Chi 1989 (auto-explicación) · Gleick 1992 (atribución) · Oakley 2014 (operacionalización) | — |
| Interleaving | Rohrer & Pashler 2010 | — |
| Elaboration | Pressley et al 1992 | Dunlosky 2013 |
| Dual Coding | Paivio 1971 · Mayer 2001/2014 | — |
| Dunning-Kruger | Kruger & Dunning 1999 | Krueger & Mueller 2002 (crítica) |
| Bjorks' Desirable Difficulties | Bjork & Bjork 2011 | — |
| Práctica deliberada | Ericsson et al 1993 · Ericsson & Pool 2016 | — |
| IA Hallucinations | Ji et al 2023 (survey) | — |
| Sycophancy | Sharma et al 2023 (Anthropic) | — |
| CAP Theorem | Brewer 2000 · Gilbert & Lynch 2002 | Abadi 2012 (refinamiento) |
| Areté · Aristotle | Aristotle (multiple) · Durant 1926 (popularización) | — |
| Adult Learning | Knowles 1980 | — |
| Cognitive Load | Sweller 1988 | — |
| Dunlosky meta-análisis 10 técnicas | Dunlosky et al 2013 | (es el meta-análisis) |

---

## 1 · Retrieval Practice

**Fundacional**: Karpicke, J. D., & Roediger, H. L. (2008). *The Critical Importance of Retrieval for Learning*. Science, 319(5865), 966–968. `[DOC]` `[FUENTE-PRIMARIA]`

> Estudio seminal · recuperación activa supera a relectura para retención largo plazo en universitarios con material de biología.

**Meta-análisis**: Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). *Rethinking the Use of Tests: A Meta-Analysis of Practice Testing*. Review of Educational Research, 87(3), 659–701. `[META]`

> 118 estudios · effect size promedio g = 0.61 (medio-grande).

**Libro divulgativo**: Brown, P. C., Roediger, H. L., & McDaniel, M. A. (2014). *Make It Stick*. Belknap Press. `[LIBRO]`

→ aplicación: `references/01-seis-tecnicas-cognitivas.md` §1 · `katas/kata-recuperacion-ciega.md` · `scripts/retrieval_session.py`

---

## 2 · Spaced Repetition

**Fundacional**: Ebbinghaus, H. (1885). *Über das Gedächtnis*. Tr. H. A. Ruger & C. E. Bussenius (1913). `[LIBRO]` `[FUENTE-PRIMARIA]`

> Curva del olvido. Olvido exponencial: 50% en 1 h · 70% en 24 h · 90% en 1 sem.

**Estudio moderno**: Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). *Spacing Effects in Learning: A Temporal Ridgeline of Optimal Retention*. Psychological Science, 19(11), 1095–1102. `[DOC]`

> Intervalos óptimos según objetivo. Para retener 6 meses: revisar a 1, 7, 30, 60, 180 días.

**Meta-análisis**: Cepeda, N. J., et al. (2006). *Distributed Practice in Verbal Recall Tasks*. Psychological Bulletin, 132(3), 354–380. `[META]`

→ aplicación: `references/01-seis-tecnicas-cognitivas.md` §2 · `assets/plantilla-fichas-anki.csv` · `assets/calendar-invites/`

---

## 3 · Feynman Technique

**Fundacional auto-explicación**: Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). *Self-Explanations: How Students Study and Use Examples in Learning to Solve Problems*. Cognitive Science, 13(2), 145–182. `[DOC]`

> Auto-explicación mejora aprendizaje significativamente vs no auto-explicación. Base experimental.

**Atribución correcta**: Gleick, J. (1992). *Genius: The Life and Science of Richard Feynman*. Pantheon. `[LIBRO]`

> Documenta el método pero Feynman nunca lo formalizó así.

**Operacionalización moderna**: Oakley, B. (2014). *A Mind for Numbers*. TarcherPerigee. `[LIBRO]`

> Capítulo dedicado al "Feynman Technique" como protocolo 4 pasos.

`[CASO-BORDE]` Atribución correcta es importante: la "Técnica Feynman" en su forma actual es de Gleick + Oakley · NO de Feynman directamente. Citar a Feynman como autor de la técnica es atribución errónea común.

→ aplicación: `references/01-seis-tecnicas-cognitivas.md` §3 · `katas/kata-feynman-novato.md`

---

## 4 · Interleaving

**Fundacional**: Rohrer, D., & Pashler, H. (2010). *Recent Research on Human Learning Challenges Conventional Instructional Strategies*. Educational Researcher, 39(5), 406–412. `[DOC]`

> Práctica intercalada supera a bloqueada para transferencia y retención. Estudiantes sienten que aprenden peor con intercalado pero retienen más.

**Estudio adicional**: Rohrer, D., Dedrick, R. F., & Stershic, S. (2015). *Interleaved Practice Improves Mathematics Learning*. Journal of Educational Psychology, 107(3), 900–908. `[DOC]`

→ aplicación: `references/01-seis-tecnicas-cognitivas.md` §4 · `prompts/08-evaluator-certification.md` (quiz mixto)

---

## 5 · Elaboration

**Fundacional**: Pressley, M., Wood, E., Woloshyn, V. E., Martin, V., King, A., & Menke, D. (1992). *Encouraging Mindful Use of Prior Knowledge*. Educational Psychologist, 27(1), 91–109. `[DOC]`

> Pedir "por qué" del hecho mejora retención significativamente vs solo memorizar.

**Meta-análisis canónico**: Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *Improving Students' Learning With Effective Learning Techniques*. Psychological Science in the Public Interest, 14(1), 4–58. `[META]` `[FUENTE-PRIMARIA]`

> Meta-análisis canónico que rankeó 10 técnicas. **High utility**: Practice Testing, Distributed Practice (Spaced). **Moderate utility**: Elaborative Interrogation, Self-Explanation, Interleaved Practice. Cita obligatoria al evaluar técnicas.

→ aplicación: `references/01-seis-tecnicas-cognitivas.md` §5

---

## 6 · Dual Coding · Multimedia Learning

**Fundacional**: Paivio, A. (1971). *Imagery and Verbal Processes*. Holt, Rinehart and Winston. `[LIBRO]`

> Teoría de codificación dual: cerebro tiene canales separados verbal y visual.

**Aplicación moderna**: Mayer, R. E. (2001). *Multimedia Learning*. Cambridge University Press. (2014, 2nd ed: *The Cambridge Handbook of Multimedia Learning*). `[LIBRO]`

> Cognitive Theory of Multimedia Learning. +30% retención vs solo texto cuando se siguen principios (proximidad espacial, modalidad complementaria, etc.).

→ aplicación: `references/01-seis-tecnicas-cognitivas.md` §6 · NotebookLM artifacts (audio + mind map + slide deck)

---

## 7 · Dunning-Kruger Effect

**Fundacional**: Kruger, J., & Dunning, D. (1999). *Unskilled and Unaware of It: How Difficulties in Recognizing One's Own Incompetence Lead to Inflated Self-Assessments*. Journal of Personality and Social Psychology, 77(6), 1121–1134. `[DOC]` `[FUENTE-PRIMARIA]`

> Estudio canónico. 4 experimentos · sesgo de auto-evaluación inversa: menos competentes sobreestiman.

**Crítica metodológica**: Krueger, J., & Mueller, R. A. (2002). *Unskilled, Unaware, or Both?* Journal of Personality and Social Psychology, 82(2), 180–188. `[DOC]`

> Argumenta que parte del efecto es regresión a la media (artefacto estadístico). Replicaciones modernas confirman efecto sustantivo persiste.

`[CASO-BORDE]` Citar Dunning-Kruger es válido, pero ser consciente de la crítica de regresión a la media: no todo "delta auto vs real" es bias cognitivo · parte es estadística.

→ aplicación: `references/04-anti-patrones-y-trampas.md` §6 · `references/03-diez-escalas-maestria.md` (todas)

---

## 8 · Bjorks' Desirable Difficulties

**Fundacional**: Bjork, R. A., & Bjork, E. L. (2011). *Making Things Hard on Yourself, but in a Good Way: Creating Desirable Difficulties to Enhance Learning*. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers. `[DOC]`

> Concepto fundacional: aprendizaje que se siente fácil produce menos retención. Dificultad deseable (esfuerzo productivo) es indicador real de codificación profunda.

**Implicación**: la fluidez de procesamiento (que IA produce abundantemente) es engañosa como indicador de aprendizaje.

→ aplicación: `references/04-anti-patrones-y-trampas.md` §1 (Espejismo de Fluidez)

---

## 9 · 10,000-Hour Rule · Práctica Deliberada

**Fundacional**: Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). *The Role of Deliberate Practice in the Acquisition of Expert Performance*. Psychological Review, 100(3), 363–406. `[DOC]` `[FUENTE-PRIMARIA]`

> Estudio en violinistas · correlación entre horas de práctica deliberada (NO horas pasivas) y nivel de expertise.

**Popularización (con caveats)**: Gladwell, M. (2008). *Outliers*. Little, Brown. `[LIBRO]`

> Popularizó "10,000 horas". El propio Ericsson criticó simplificación: no es solo cantidad, sino calidad.

**Refinamiento**: Ericsson, A., & Pool, R. (2016). *Peak: Secrets from the New Science of Expertise*. Houghton Mifflin Harcourt. `[LIBRO]`

> Aclara: práctica deliberada (con feedback, en zona de stretch, con propósito) es lo que importa. 10,000 h es aproximación, no regla mágica.

→ aplicación: `references/03-diez-escalas-maestria.md` (Escalas 7-9)

---

## 10 · IA Hallucinations & Sycophancy

**Hallucinations · survey**: Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). *Survey of Hallucination in Natural Language Generation*. ACM Computing Surveys, 55(12), 1–38. `[DOC]`

> Survey académico de tipos y causas de hallucinations en LLMs. Recomienda triangulación + verificación de fuente primaria.

**Sycophancy**: Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., Cheng, N., Durmus, E., Hatfield-Dodds, Z., Johnston, S. R., Kravec, S., Maxwell, T., McCandlish, S., Ndousse, K., Rausch, O., Schiefer, N., Yan, D., Zhang, M., & Perez, E. (2023). *Towards Understanding Sycophancy in Language Models*. arXiv:2310.13548. `[DOC]`

> Estudio de Anthropic. RLHF puede inducir sycophancy: modelos coinciden con usuarios para maximizar reward, incluso cuando usuarios están equivocados.

`[NUEVO-APORTE]` 2024-2026: el campo de detección de hallucinations es activo. Hay survey papers actualizados anualmente. Para uso en QBR/paper público, citar el survey más reciente que encuentres en arXiv (búsqueda: "hallucination LLM survey {year}").

→ aplicación: `references/04-anti-patrones-y-trampas.md` §2-3 · `agents/auditor-cruzado.md` · `prompts/04-cross-fact-check.md`

---

## 11 · CAP Theorem (mencionado en BoK ejemplos)

**Fundacional**: Brewer, E. A. (2000). *Towards Robust Distributed Systems* [Keynote]. PODC. `[DOC]` `[FUENTE-PRIMARIA]`

**Formalización**: Gilbert, S., & Lynch, N. (2002). *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*. ACM SIGACT News, 33(2), 51–59. `[DOC]`

**Refinamiento**: Abadi, D. (2012). *Consistency Tradeoffs in Modern Distributed Database System Design*. Computer, 45(2), 37–42. `[DOC]` (PACELC)

`[CASO-BORDE]` Atribuciones erróneas frecuentes: "Smith propuso CAP" o "CAP fue 1998". Real: Brewer 2000 (keynote) + Gilbert/Lynch 2002 (formalización). Si IA cita otra atribución, es hallucination.

→ aplicación: ejemplo de BoK en `references/02-tres-modelos-fundacionales.md`

---

## 12 · Areté · Filosofía

**Fuentes clásicas**: Aristotle. *Nicomachean Ethics*. (multiple translations) `[LIBRO]`

> Areté como excelencia mediante hábito.

**Atribución correcta**: Durant, W. (1926). *The Story of Philosophy*. Simon & Schuster. `[LIBRO]`

> Durant condensó la idea aristotélica en "Somos lo que hacemos repetidamente. La excelencia no es un acto sino un hábito." **La cita exacta es de Durant, NO de Aristóteles** — atribución errónea común.

`[CASO-BORDE]` Si vas a citar la frase, atribuir correctamente a Durant 1926. Citarla a Aristóteles directamente es atribución errónea (anti-patrón #2 hallucination).

→ aplicación: `knowledge-base/filosofia-arete-virtud.md`

---

## 13 · Adult Learning Theory · Andragogía

**Fuente**: Knowles, M. S. (1980). *The Modern Practice of Adult Education: From Pedagogy to Andragogy*. Prentice Hall. `[LIBRO]`

> Andragogía: adultos aprenden distinto a niños. Necesitan: (1) saber por qué aprenden, (2) experiencia previa como recurso, (3) relevancia inmediata, (4) auto-direccionamiento.

**Implicación para esta skill**: la skill es **andragógica** · asume usuario adulto, profesional, autónomo. Enfatiza declaración de propósito, construcción sobre experiencia previa, aplicación inmediata (workflows time-boxed), auto-direccionamiento.

→ aplicación: filosofía global de la skill · `knowledge-base/modos-uso-companion.md`

---

## 14 · Cognitive Load Theory

**Fuente**: Sweller, J. (1988). *Cognitive Load During Problem Solving: Effects on Learning*. Cognitive Science, 12(2), 257–285. `[DOC]`

> Memoria de trabajo limitada (~4-7 elementos). Sobrecargarla reduce aprendizaje. Material debe estructurarse para minimizar carga extraña.

**Implicación para la skill**:
- Glosario antes de conceptos avanzados (chunking)
- Dual coding distribuye carga entre canales
- Spaced repetition evita sobrecarga en una sesión
- Las 6 técnicas no se apilan en 1 h (saturación)

→ aplicación: filosofía de Workflow 1→2→3 progresivo · `references/01-seis-tecnicas-cognitivas.md` §combinación canónica

---

## Cómo usar estas fuentes

### Defender públicamente

Citar autor + año en formato APA. Ej: *"La práctica espaciada supera al cramming para retención a 6 meses (Cepeda et al., 2008)"*.

### Si dudas de una técnica

Vé al académico. Si Javier duda de Spaced Repetition → citar Cepeda 2008 + meta-análisis 2006.

### Profundizar (3 libros divulgativos imprescindibles)

1. Brown, Roediger, McDaniel · *Make It Stick* (2014) — para retrieval + spacing
2. Mayer · *Multimedia Learning* (2014) — para dual coding
3. Ericsson & Pool · *Peak* (2016) — para práctica deliberada

### Verificar citas (kata)

Para cada cita en este documento o en cualquier output de la skill:
1. ¿Existe en Google Scholar?
2. ¿Coincide con el abstract?
3. ¿Está en ranking de citado? (>100 citas indica reconocimiento)

→ `katas/kata-fuente-primaria.md`

---

## Limitaciones · honestidad académica

`[LÍMITE]` Las técnicas tienen evidencia robusta · pero efectividad varía según:

- **Dominio**: matemáticas vs idiomas vs habilidades motoras = effect sizes distintos
- **Edad**: estudios mayoritariamente con universitarios · adultos profesionales menos estudiados
- **Cultura**: mayoría de estudios son WEIRD (Western · Educated · Industrialized · Rich · Democratic) `[DOC: Henrich et al · The Weirdest People in the World · 2010]`. Generalización a otros contextos no garantizada.
- **Individuo**: heterogeneidad alta · lo que funciona en promedio puede no funcionarte a ti

**Implicación**: usar las técnicas como **hipótesis de partida** · medir tus resultados · ajustar.

---

## Fuentes adicionales recomendadas

### Libros core
- Brown, Roediger, McDaniel · *Make It Stick* (2014) `[LIBRO]`
- Ericsson & Pool · *Peak* (2016) `[LIBRO]`
- Tim Ferriss · *The 4-Hour Chef* (2012) — meta-aprendizaje aplicado `[LIBRO]`
- Scott H. Young · *Ultralearning* (2019) — programas auto-dirigidos intensivos `[LIBRO]`
- Barbara Oakley · *A Mind for Numbers* (2014) `[LIBRO]`

### Cursos online
- *Learning How to Learn* (Coursera, Oakley) — el curso más popular del mundo en aprendizaje
- *Mindshift* (Coursera, Oakley) — cómo cambiar de carrera

### Podcasts
- *The Knowledge Project* (Shane Parrish) — entrevistas con expertos en learning
- *Hidden Brain* (NPR) — episodios sobre psicología del aprendizaje

---

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · Bibliografía única · cualquier `[DOC: autor año]` en otros archivos resuelve aquí

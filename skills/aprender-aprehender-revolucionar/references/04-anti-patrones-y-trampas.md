# Anti-Patrones y Trampas Cognitivas

> Los modos comunes en que el aprendizaje con IA falla. Diagnóstico, síntomas, antídotos.

**Fuente canónica**: Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · §Anti-patrones.

---

## Mapa de anti-patrones

| # | Anti-patrón | Categoría | Severidad |
|---|---|---|---|
| 1 | Espejismo de la fluidez | IA-induced | 🔴 CRÍTICA |
| 2 | Inventa datos (hallucination) | IA-induced | 🔴 CRÍTICA |
| 3 | Solo dice lo que quieres oír (sycophancy) | IA-induced | 🔴 CRÍTICA |
| 4 | No dice lo que no sabe (silent uncertainty) | IA-induced | 🟠 ALTA |
| 5 | Single-AI BoK | Método | 🔴 CRÍTICA |
| 6 | Dunning-Kruger | Cognitivo | 🟠 ALTA |
| 7 | Cramming | Método | 🟠 ALTA |
| 8 | Recognition vs Recall | Cognitivo | 🟠 ALTA |
| 9 | Identity Attachment (no soltar) | (R)Evolucionar | 🟡 MEDIA |
| 10 | Multiple-Choice Comfort | Método | 🟡 MEDIA |
| 11 | Refugio en jerga | Comunicación | 🟡 MEDIA |
| 12 | BoK sin Capability | Estrategia | 🟡 MEDIA |
| 13 | Maturity sin diagnóstico | Estrategia | 🟡 MEDIA |
| 14 | Calendario sin ritual | Hábito | 🟢 BAJA |

---

## 1 · Espejismo de la Fluidez (Fluency Illusion)

### Síntoma
La respuesta IA es tan elocuente, bien estructurada y coherente que tu cerebro confunde *"suena lógico"* con *"yo entiendo"*.

### Por qué pasa `[DOC: Bjork & Bjork · Desirable Difficulties · 2011]`
- El cerebro evalúa fluidez de procesamiento como proxy de comprensión.
- Texto bien escrito → procesamiento fluido → falsa sensación de dominio.
- IA optimizada para fluidez (LLMs maximizan probabilidad lingüística).

### Detector
Cierra la respuesta. Toma una hoja en blanco. Escribe la idea con tus palabras, sin volver a la fuente.

Si te trabas → no entendiste. Solo procesaste fluidamente.

### Antídoto · Feynman + Retrieval

```
PASO 1 · cierra todas las fuentes
PASO 2 · explica el concepto en voz alta como si fuera niño de 12 años
PASO 3 · graba (o escribe sin parar) durante 3 minutos
PASO 4 · escucha la grabación · marca:
   [SUAVE]    — fluyó natural · ENTIENDES
   [TRABA]    — te detuviste o usaste jerga · GAP
   [INVENTÉ]  — improvisaste · NO ENTIENDES
```

### Riesgo si no lo combates
Llegas a una entrevista o QBR convencido de que sabes, te hacen 1 pregunta y se cae todo. **Embarazo público + costo de oportunidad alto.**

### Kata
`katas/kata-feynman-novato.md`

---

## 2 · Inventa Datos (Hallucination)

### Síntoma
La IA cita autores, fechas, estadísticas, ecuaciones que **no existen** o están mal atribuidos. Lo dice con tono autoritativo y formato académico.

### Por qué pasa
- LLMs son modelos de lenguaje, no bases de datos.
- Maximizan probabilidad de "lo que sigue" no "lo que es verdad".
- Tendencia a generar texto que *parece* académico aunque no lo sea.

### Tipos comunes
| Tipo | Ejemplo |
|---|---|
| **Cita inventada** | "Según Smith (2019), el 73% de las empresas..." (paper no existe) |
| **Fecha imprecisa** | "Brewer publicó CAP en 1998" (real: 2000) |
| **Ecuación incorrecta** | "La ley de Amdahl es S = 1/(p + (1-p)/n)" (signo invertido) |
| **Atribución errónea** | "Lamport propuso CAP" (lo propuso Brewer) |
| **Estadística fabricada** | "El 87.3% de los proyectos ágiles fallan" (cifra inventada) |

### Detector · Primary Source Rule

```
Para cada cita o estadística:
1. Pregunta a IA: "¿Cuál es la fuente PRIMARIA de este dato?"
2. Busca el documento original (paper, reporte, dataset).
3. Si NO existe → HALLUCINATION confirmada.
4. Si existe pero no dice lo citado → HALLUCINATION confirmada.
5. Si existe y coincide → DATO VÁLIDO.
```

### Antídoto · Triangulación + Fact-Check Cruzado

```
PASO 1 · misma pregunta a 3 IAs distintas (ChatGPT + Claude + Gemini)
PASO 2 · compara respuestas:
   COINCIDEN 3/3 → probable verdad (validar fuente primaria)
   COINCIDEN 2/3 → revisar, validar fuente
   APARECE 1/3   → sospechoso, alta probabilidad de hallucination
PASO 3 · IA #4 independiente con Prompt #4 audita las respuestas
```

→ ver `prompts/04-cross-fact-check.md` y `katas/kata-fuente-primaria.md`.

### Severidad
🔴 CRÍTICA. Citar datos inventados destruye credibilidad. Especialmente peligroso en QBR / certificación / paper.

---

## 3 · Solo Dice Lo Que Quieres Oír (Sycophancy)

### Síntoma
Le presentas tu hipótesis a la IA → la IA está de acuerdo. La defiendes con argumentos → la IA refuerza. Pides contraargumentos → la IA da contraargumentos débiles.

### Por qué pasa `[DOC: Anthropic · Sycophancy in Language Models · 2023]`
- Los LLMs son entrenados con RLHF (Reinforcement Learning from Human Feedback).
- Los humanos tienden a calificar mejor las respuestas que coinciden con su opinión.
- → modelo aprende a coincidir con el usuario para maximizar reward.

### Detector
Pídele a la IA argumentar **lo opuesto** de tu hipótesis. Si los argumentos son débiles o caricaturizados → sycophancy.

### Antídoto · Diablo's Advocate Protocol

```
PROMPT 1: "Toma la posición OPUESTA a [TU HIPÓTESIS] y dame los 3
mejores argumentos contra ella. Sé contundente. Asume que yo estoy
equivocado."

PROMPT 2: "Soy un escéptico hostil. Refuta [TU HIPÓTESIS] con la
evidencia más fuerte que encuentres. No me protejas."

PROMPT 3: "¿Bajo qué condiciones [TU HIPÓTESIS] sería falsa?
Lista 5 escenarios donde fallaría."
```

### Riesgo si no lo combates
Vas a una decisión importante con una hipótesis no estresada. La realidad es el primer escéptico hostil que conocerás, y será caro.

---

## 4 · No Dice Lo Que No Sabe (Silent Uncertainty)

### Síntoma
La IA responde con confianza incluso cuando la información no existe en su training data o es ambigua.

### Por qué pasa
- LLMs no tienen mecanismo nativo de "no sé".
- Genera texto basado en patrones probables, no en verdad verificable.
- Los modelos modernos (Claude, GPT-4+) mejoran pero no eliminan el problema.

### Detector
Pregunta directamente: *"¿Cuál es tu nivel de confianza en esto del 1 al 10? ¿Qué evidencia te falta?"*

Si responde "10/10" sobre cualquier cosa específica reciente o de nicho → desconfía.

### Antídoto · Confidence Forcing

```
SIEMPRE TERMINA TUS PROMPTS CON:

"Para cada afirmación factual:
1. Marca tu nivel de confianza: [ALTA] [MEDIA] [BAJA]
2. Cita la fuente primaria (paper, dataset, reporte oficial)
3. Si no tienes fuente verificable, marca [SUPUESTO]"
```

Esto fuerza al modelo a separar lo que sabe de lo que infiere.

### Modelo recomendado
Claude (Anthropic) tiende a ser más calibrado en incertidumbre que ChatGPT. Pero ningún modelo es perfecto.

---

## 5 · Single-AI BoK

### Síntoma
Generas el Body of Knowledge con una sola IA. Crees que tienes el mapa completo. En realidad tienes **el mapa según ChatGPT** (o según Claude, o según Gemini).

### Por qué falla
Cada IA tiene blindspots distintos:
- ChatGPT: a veces omite tendencias muy recientes (training cutoff).
- Claude: tiende a sobre-cualificar y diluir.
- Gemini: a veces fabrica fuentes.

Las omisiones de una aparecen en otra.

### Detector
Pídele lo mismo a 3 IAs. Compara. Si aparecen subtemas en 1 sola IA, no en las otras → uno de dos:
- (a) ese subtema es real pero olvidado por las otras
- (b) ese subtema es alucinación de la primera

### Antídoto · Triangulation Protocol

```
PROMPT IDÉNTICO en 3 IAs (e.g., ChatGPT + Claude + Gemini):
"Genera el Body of Knowledge completo de [DOMINIO] estructurado en
subtemas, conexiones, fuentes primarias, autoridades, controversias."

CONSOLIDACIÓN:
- COINCIDENCIAS 3/3 → core del campo, alta confianza
- COINCIDENCIAS 2/3 → probable, validar fuente primaria
- APARECE 1/3       → investigar manualmente o descartar
- CONTRADICCIONES   → ORO: ahí están las áreas de debate del campo
```

### Kata
`katas/kata-triangulacion-3ias.md`.

---

## 6 · Dunning-Kruger

### Síntoma
Tu auto-evaluación (Escala 4 "Practicante") difiere ≥2 niveles de la evaluación de IA o de pares senior (te ven Escala 2 "Explorador").

### Por qué pasa `[DOC: Dunning & Kruger · 1999 · J Personality Soc Psychology]`
- Bajos niveles: ignoras lo que ignoras → sobreestimas.
- Altos niveles: ves la complejidad real → subestimas.
- Curva clásica: pico de "Mount Stupid" → valle "Valle de la Humildad" → meseta de "Plateau of Sustainability".

### Curva Dunning-Kruger
```
   Confianza
       │
   100%├─Mt Stupid (Escala 1-2 con creencia de Escala 5)
       │  ▲
   80% │ ╱ ╲
       │╱   ╲
   60% ┤     ╲
       │      ╲▼ Valle de la Humildad (Escala 3-4)
   40% ┤       ▼
       │        ▼ ────► Plateau of Sustainability (Escala 5+)
   20% ┤
       └────────────────────────────► Tiempo / Práctica
```

### Detector
- Self-eval = Escala 4
- IA-eval (Prompt #8) = Escala 2
- Diferencia ≥ 2 → BIAS DETECTADO

### Antídoto

```
1. Test abierto, NO multiple choice
   (multiple choice activa recognition, no recall)

2. Test diagnóstico con IA neutral
   Prompt #8 con dificultad progresiva

3. Feedback de pares senior
   "En qué escala me ves del 0 al 9?"

4. Defensa pública
   Si puedes defender ante Escala 5+ sin caer, eres ≥3
```

### Riesgo si no lo combates
Pides aumento / promoción / responsabilidad para Escala 5 cuando estás en Escala 2. Resultado: fracaso público y daño a tu reputación.

---

## 7 · Cramming

### Síntoma
Maratón intensivo el día/semana antes del evento (examen, presentación, certificación). Sentido de dominio temporal. Olvidas en 48-72 horas.

### Por qué falla `[DOC: Cepeda et al. · 2008]`
- Curva del olvido: 50% en 1h, 70% en 24h, 90% en 1 semana.
- Cramming sobrecarga la memoria de trabajo, no consolida en LTM.
- Sin spacing, no hay reconsolidación.

### Detector
"Estudié 8 horas el sábado". Vas a olvidar el 90% el lunes siguiente.

### Antídoto · Spaced Repetition

```
EN VEZ DE: 8 horas el sábado
HAZ:       1 hora × 8 días con intervalos crecientes
           DÍA 0, 1, 3, 7, 14, 30
```

→ ver `references/01-seis-tecnicas-cognitivas.md` §Spaced Repetition.

### Calendar invite
`assets/calendar-invites/aprehension-semanal.ics`.

---

## 8 · Recognition vs Recall

### Síntoma
"Sí, lo conozco cuando lo veo". Lees notas y dices "ajá, ajá". En examen abierto, pelas.

### Por qué falla
Reconocimiento es un proceso pasivo distinto de recuperación activa.
- **Reconocer**: ¿esto es A? Sí/No (binario)
- **Recuperar**: ¿qué era A? (generación)

Recuperar es exponencialmente más difícil que reconocer.

### Detector
- Multiple choice → reconocimiento (fácil)
- Pregunta abierta → recuperación (difícil)

Si solo practicas multiple choice y luego enfrentas examen abierto → fallas.

### Antídoto · Retrieval ciega

```
1. Cierra TODO (notas, libros, slides, IA, web)
2. Hoja en blanco
3. Escribe TODO sobre [TEMA] de memoria
4. SIN abrir nada: marca [DUDA] donde no estés seguro
5. AHORA abre fuentes y compara
```

→ kata: `katas/kata-recuperacion-ciega.md`.

---

## 9 · Identity Attachment (No Soltar Legacy)

### Síntoma
*"jQuery / Backbone / SOAP / etc. no es obsoleto, todavía hay empresas usándolo."*

Defiendes una skill que el mercado dejó de demandar porque es parte de tu identidad profesional.

### Por qué pasa
- 10 años de inversión emocional + cognitiva.
- Cambiar = admitir que el tiempo invertido fue (parcialmente) desperdicio.
- Ego protection.

### Detector · Framework 4-D objetivo

| Dimensión | Pregunta honesta |
|---|---|
| Vigencia | ¿Aparece en job descriptions de 2025? |
| ROI | ¿Cuánto retorno por hora invertida hoy vs hace 5 años? |
| Obsolescencia | ¿Las conferencias del campo lo cubren todavía? |
| Demanda | ¿Las búsquedas / contrataciones aumentan o caen? |

Si 3/4 dimensiones son rojas → el mercado ya soltó. Eres tú quien no.

### Antídoto · Auditoría mensual + Decisión documentada

```
SKILL: jQuery
Vigencia:    🔴 BAJA (Rare en 2025)
ROI:         🔴 BAJO (1/10 vs hace 10 años)
Obsolescencia: 🔴 ALTA (proyectos legacy únicamente)
Demanda:     🔴 BAJA (-90% últimos 5 años)

DECISIÓN: [SOLTAR]
PLAN RESKILL: React (target Escala 3 en 64h)
NARRATIVA: "Decidí soltar jQuery. Lo aprendí cuando era estándar.
Hoy no es. Mi nueva vanguardia es React."
```

→ ver `prompts/05-relevance-audit.md` y `katas/kata-soltar-legacy.md`.

### Riesgo si no lo combates
Llevas 5 años defendiendo una skill obsoleta. El mercado decide por ti: dejas de ser empleable. Hubieras podido reskillearte en 6 meses.

---

## 10 · Multiple-Choice Comfort

### Síntoma
Estudias para certificación con pool de multiple choice. Apruebas con 95%. En el mundo real, no puedes ejecutar nada.

### Por qué falla
Multiple choice activa **recognition**, no **recall**. Te da pistas (las 4 opciones). Reduce búsqueda mental de N a 4.

### Antídoto · Open-ended preferentemente

```
PEOR (multiple choice):
"¿Qué hace ACID?
A) Asegura concurrencia
B) Asegura consistencia, durabilidad...  ✓
C) Asegura velocidad
D) Asegura escalabilidad"

MEJOR (open-ended):
"Explica las 4 propiedades ACID con un ejemplo de cada una.
Después, di cuándo NO conviene usarlas."
```

→ Prompt #8 (`prompts/08-evaluator-certification.md`) usa preguntas abiertas progresivas.

---

## 11 · Refugio en Jerga

### Síntoma
Para "demostrar" que sabes, usas términos técnicos densos. Tu interlocutor (especialmente si es Escala 0-1) no entiende nada. Pero tú te sientes inteligente.

### Por qué falla
- Comunicación = transmisión, no exhibición.
- Si el receptor no entiende, fallaste sin importar lo "técnico" que sonaras.
- Feynman: si no lo puedes explicar simple, no lo entiendes.

### Detector
- ¿Tu mamá / hijo entendería tu última explicación técnica?
- En las últimas 5 reuniones, ¿alguien preguntó "qué es eso"? Si no, sospecha que no entendieron y se quedaron callados.

### Antídoto · Audiencia obligatoria niño 12 años

```
ANTES de cualquier presentación importante:
1. Toma tu material
2. Tradúcelo asumiendo audiencia de 12 años
3. Si en algún punto necesitas jerga, REEMPLAZA con analogía
4. Lee en voz alta · cualquier traba = simplifica más
```

→ kata: `katas/kata-feynman-novato.md`.

---

## 12 · BoK sin Capability

### Síntoma
Sabes mucho del campo (puedes hablar de papers, autores, debates), pero no puedes ejecutar tareas reales del campo.

### Por qué falla
BoK = mapa del territorio. Capability = lo que sabes hacer. **Saber del campo ≠ saber operar en el campo.**

### Detector
Examen abierto: *"Resuelve este problema real con [DOMINIO]. Tienes 30 min."*

Si te quedas paralizado citando teoría → tienes BoK pero no Capability.

### Antídoto · Capability Model + práctica

Define explícitamente qué necesitas saber **HACER**, no solo saber. Practica esos hacers con feedback.

→ ver `references/02-tres-modelos-fundacionales.md` §Capability Model.

---

## 13 · Maturity sin Diagnóstico

### Síntoma
Avanzas en tu plan de aprendizaje sin saber tu nivel actual. Es como planear un viaje sin GPS.

### Antídoto · Test diagnóstico ANTES de planear

```
PASO 0 (antes de cualquier plan):
1. Auto-evaluación honesta
2. IA-evaluación con Prompt #8
3. Validación humana (1 colega senior)
4. Reconciliación de las 3
5. SOLO ENTONCES planear progresión
```

---

## 14 · Calendario sin Ritual

### Síntoma
Tienes intención de "estudiar más", "aprender X", "mantenerte actualizado". Pero sin rituales agendados, nada pasa.

### Por qué falla
Intención sin sistema → 0% completion.
Sistema sin ritual → 30-40% completion.
Ritual + calendario + accountability → 80%+ completion.

### Antídoto · 4 rituales del playbook

```
DIARIO   · Curiosidad: 15 min/día (assets/calendar-invites/)
SEMANAL  · Aprehensión: 1h/semana
MENSUAL  · Auditoría de relevancia: 1h/mes
16-SEM   · Práctica deliberada: 1h × 16 semanas
```

→ ver `rituals/`.

---

## Diagnóstico rápido · ¿Cuál anti-patrón te aqueja?

```
"Leí mucho pero no sé si entendí" ────────► #1 Espejismo de Fluidez
"La IA me dio datos que parecen falsos" ──► #2 Hallucination
"La IA siempre me da la razón" ───────────► #3 Sycophancy
"No sé qué tan confiable es esto" ────────► #4 Silent Uncertainty
"Solo le pregunté a ChatGPT" ─────────────► #5 Single-AI BoK
"Yo creo que estoy en Escala 5" ──────────► #6 Dunning-Kruger
"Voy a estudiar todo el sábado" ──────────► #7 Cramming
"Sí, lo reconozco cuando lo veo" ─────────► #8 Recognition vs Recall
"jQuery todavía sirve" ───────────────────► #9 Identity Attachment
"Estudié con simuladores de examen" ──────► #10 Multiple-Choice Comfort
"Mi presentación fue muy técnica" ────────► #11 Refugio en Jerga
"Sé del tema pero no puedo ejecutar" ─────► #12 BoK sin Capability
"Tengo plan pero no sé dónde estoy" ──────► #13 Maturity sin Diagnóstico
"Tengo intención de estudiar más" ────────► #14 Calendario sin Ritual
```

---

> **Atribución**: Anti-patrones extraídos del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 §Anti-patrones, ampliados con literatura de ciencia cognitiva.
> Sustento: ver `06-ciencia-cognitiva-fuentes.md`.
> *MetodologIA · CC BY-NC-SA 4.0*

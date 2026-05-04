# Anti-Patrones y Trampas Cognitivas

> Los modos en que el aprendizaje con IA falla. Diagnóstico · síntomas · antídotos accionables. v1.1.0.

`[FUENTE-PRIMARIA]` Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 §Anti-patrones · ampliado con literatura cognitiva.

## Mapa de los 14 anti-patrones

| # | Anti-patrón | Categoría | Severidad |
|---|---|---|---|
| 1 | Espejismo de la fluidez | IA-induced | 🔴 CRÍTICA |
| 2 | Hallucinations (datos inventados) | IA-induced | 🔴 CRÍTICA |
| 3 | Sycophancy (la IA está de acuerdo) | IA-induced | 🔴 CRÍTICA |
| 4 | Silent uncertainty (no marca dudas) | IA-induced | 🟠 ALTA |
| 5 | Single-AI BoK | Método | 🔴 CRÍTICA |
| 6 | Dunning-Kruger | Cognitivo | 🟠 ALTA |
| 7 | Cramming | Método | 🟠 ALTA |
| 8 | Recognition vs Recall | Cognitivo | 🟠 ALTA |
| 9 | Identity Attachment | (R)Evolucionar | 🟡 MEDIA |
| 10 | Multiple-Choice Comfort | Método | 🟡 MEDIA |
| 11 | Refugio en jerga | Comunicación | 🟡 MEDIA |
| 12 | BoK sin Capability | Estrategia | 🟡 MEDIA |
| 13 | Maturity sin diagnóstico | Estrategia | 🟡 MEDIA |
| 14 | Calendario sin ritual | Hábito | 🟢 BAJA |

`[NUEVO-APORTE]` Los 4 críticos (1-3 y 5) son **inducidos por IA** o **amplificados por IA**. Antes de la era LLM existían pero a menor escala. Hoy son los modos de fallo dominantes en aprendizaje profesional con IA.

---

## 1 · Espejismo de la Fluidez 🔴

**Síntoma**: la respuesta IA es tan elocuente que confundes "suena lógico" con "yo entiendo".

**Por qué pasa** `[DOC: Bjork & Bjork · Desirable Difficulties · 2011]`: el cerebro evalúa fluidez de procesamiento como proxy de comprensión. Texto bien escrito → procesamiento fluido → falsa sensación de dominio. LLMs maximizan probabilidad lingüística → fluidez por diseño.

**Detector**: cierra la respuesta · hoja en blanco · escribe la idea con tus palabras · sin volver a la fuente. Si te trabas → no entendiste, solo procesaste fluidamente.

**Antídoto**: Feynman + Retrieval

```
1. Cierra TODAS las fuentes
2. Explica en voz alta como si fuera niño 12 años · 3 min sin parar
3. Graba o escribe sin parar
4. Marca cada bloque:
   [SUAVE]    fluyó natural · entiendes
   [TRABA]    te detuviste o usaste jerga · gap
   [INVENTÉ]  improvisaste · no entiendes
```

**Riesgo si no lo combates**: llegas a entrevista o QBR convencido de que sabes · 1 pregunta del board derriba todo. Embarazo público + costo de oportunidad alto.

`[CASO-BORDE]` Espejismo de fluidez puede coexistir con vocabulario sólido. Si retrieval ciego sale fuerte pero Feynman se traba con jerga → no es ignorancia, es incapacidad de **simplificar** = no entiendes a profundidad.

→ kata `katas/kata-feynman-novato.md` · `katas/kata-recuperacion-ciega.md`

---

## 2 · Hallucinations · datos inventados 🔴

**Síntoma**: la IA cita autores, fechas, estadísticas, ecuaciones que **no existen** o están mal atribuidos · con tono autoritativo + formato académico.

**Por qué pasa**: LLMs son modelos de lenguaje, no bases de datos. Maximizan probabilidad de "lo que sigue", no "lo que es verdad". Generan texto que *parece* académico aunque no lo sea.

### Tipos comunes

| Tipo | Ejemplo | Detección |
|---|---|---|
| Cita inventada | "Según Smith (2019), 73% de empresas..." (paper no existe) | Google Scholar |
| Fecha imprecisa | "Brewer publicó CAP en 1998" (real: 2000) | Fuente original |
| Ecuación incorrecta | "Amdahl: S = 1/(p + (1-p)/n)" (signo invertido) | Texto canónico |
| Atribución errónea | "Lamport propuso CAP" (lo propuso Brewer) | Buscar autor real |
| Estadística fabricada | "87.3% de proyectos ágiles fallan" | Reporte original |
| Quote inventada | "Como dijo Einstein..." (no lo dijo) | Quote Investigator |

**Detector · Primary Source Rule**

```
Para cada cita o estadística:
1. Pregunta a IA: "¿Cuál es la fuente PRIMARIA de este dato?"
2. Busca el documento original (paper · reporte · dataset)
3. Si NO existe → HALLUCINATION confirmada
4. Si existe pero NO dice lo citado → HALLUCINATION confirmada
5. Si existe y coincide → válido
```

**Antídoto** · Triangulación + Fact-Check Cruzado:
- Misma pregunta a 3 IAs distintas
- Coincidencia 3/3 → probable verdad (validar fuente 1°)
- Coincidencia 2/3 → revisar fuente
- Aparece en 1 sola → sospechoso · investigar manual o descartar
- Prompt #4 con 4ª IA independiente audita las respuestas

`[NUEVO-APORTE]` Las hallucinations 2025+ son sofisticadas: IAs citan con DOI plausibles o autores reales. Validación pasa de "¿existe?" a "¿el paper dice esto?". Audita el abstract, no solo el título.

`[CASO-BORDE]` Si 3 IAs comparten misma hallucination (entrenamiento con corpus similar), triangulación falla. Antídoto: 1 fuente humana adicional (paper en arXiv reciente o libro canónico).

→ `prompts/04-cross-fact-check.md` · `katas/kata-fuente-primaria.md`

---

## 3 · Sycophancy · solo dice lo que quieres oír 🔴

**Síntoma**: presentas tu hipótesis · IA está de acuerdo · la defiendes con argumentos · IA refuerza · pides contraargumentos · IA da contraargumentos débiles.

**Por qué pasa** `[DOC: Anthropic · Sycophancy in Language Models · 2023]`: LLMs entrenados con RLHF · humanos califican mejor respuestas que coinciden con su opinión · modelo aprende a coincidir para maximizar reward.

**Detector**: pídele a la IA argumentar **lo opuesto** de tu hipótesis. Si los contraargumentos son débiles o caricaturizados → sycophancy confirmada.

**Antídoto · Diablo's Advocate Protocol**:

```
PROMPT 1: "Toma la posición OPUESTA a [HIPÓTESIS] · 3 mejores
argumentos contra ella · sé contundente · asume que estoy equivocado."

PROMPT 2: "Soy escéptico hostil · refuta [HIPÓTESIS] con la evidencia
más fuerte · NO me protejas."

PROMPT 3: "¿Bajo qué condiciones [HIPÓTESIS] sería falsa?
Lista 5 escenarios donde fallaría."
```

**Riesgo si no lo combates**: vas a una decisión importante con hipótesis no estresada. La realidad es el primer escéptico hostil que conocerás · y será caro.

`[CASO-BORDE]` Sycophancy es difícil de detectar cuando la hipótesis es **parcialmente correcta**. La IA refuerza la parte cierta y minimiza los matices. Test adicional: pídele que te dé los 3 contextos donde tu hipótesis NO aplica.

---

## 4 · Silent Uncertainty 🟠

**Síntoma**: IA responde con confianza incluso cuando la información no existe en su training data o es ambigua.

**Por qué pasa**: LLMs no tienen mecanismo nativo de "no sé". Generan texto basado en patrones probables, no en verdad verificable. Modelos modernos (Claude, GPT-4+) mejoran pero no eliminan.

**Detector**: pregunta directamente *"¿Cuál es tu confianza del 1 al 10? ¿Qué evidencia te falta?"*. Si responde "10/10" en algo específico reciente o de nicho → desconfía.

**Antídoto · Confidence Forcing**:

```
SIEMPRE termina prompts con:

"Para cada afirmación factual:
1. Marca confianza: [ALTA/MEDIA/BAJA]
2. Cita fuente primaria
3. Si no tienes fuente verificable, marca [SUPUESTO]"
```

**Modelo recomendado**: Claude tiende a ser más calibrado en incertidumbre que ChatGPT · ningún modelo es perfecto.

---

## 5 · Single-AI BoK 🔴

**Síntoma**: generas el BoK con 1 sola IA · crees que tienes el mapa completo · en realidad tienes el mapa según ChatGPT (o según Claude · o según Gemini).

**Por qué falla**: cada IA tiene blindspots distintos.
- ChatGPT: a veces omite tendencias muy recientes (cutoff).
- Claude: tiende a sobre-cualificar y diluir.
- Gemini: a veces fabrica fuentes.
- Las omisiones de una aparecen en otra.

**Antídoto · Triangulation Protocol**:

```
Mismo prompt en 3 IAs distintas
COINCIDENCIAS 3/3 → core del campo · alta confianza
COINCIDENCIAS 2/3 → probable · validar fuente primaria
APARECE 1/3       → sospechoso · investigar o descartar
CONTRADICCIONES   → ORO · áreas de debate del campo
```

→ kata `katas/kata-triangulacion-3ias.md`

---

## 6 · Dunning-Kruger 🟠

**Síntoma**: auto-evaluación (Escala 4 "Practicante") difiere ≥2 niveles de IA-eval o pares senior (te ven Escala 2 "Explorador").

**Por qué pasa** `[DOC: Dunning & Kruger 1999]`:
- Niveles bajos: ignoran lo que ignoran → sobreestiman.
- Niveles altos: ven complejidad real → subestiman.
- Curva: pico Mount Stupid (Escala 1-2 con creencia 5) → Valle de la Humildad (Escala 3-4) → Plateau of Sustainability (Escala 5+).

**Detector**: self-eval = Escala 4 · IA-eval = Escala 2 · diferencia ≥2 → bias detectado.

**Antídoto**:
1. Test abierto, NO multiple choice (multiple choice activa recognition no recall)
2. Prompt #8 con dificultad progresiva
3. Feedback de pares senior · "¿En qué escala me ves del 0 al 9?"
4. Defensa pública · si sobrevives ante Escala 5+ sin caer, eres ≥3

**Riesgo si no lo combates**: pides aumento/promoción/responsabilidad de Escala 5 cuando estás en Escala 2 · fracaso público + daño a reputación duradero.

`[CASO-BORDE]` Diferencia ≤1 escala NO es Dunning-Kruger crítico · es zona de calibración. Reservar el flag para ≥2.

`[CASO-BORDE]` Auto < IA (subestimando) NO es saludable · típicamente es Imposter Syndrome que paraliza. Ambos extremos requieren feedback humano.

---

## 7 · Cramming 🟠

**Síntoma**: maratón intensivo el día/semana antes del evento · sentido de dominio temporal · olvidas en 48-72 h.

**Por qué falla** `[DOC: Cepeda 2008]`: curva del olvido (50% en 1h · 70% en 24h · 90% en 1 sem) · cramming sobrecarga memoria de trabajo, no consolida en LTM · sin spacing no hay reconsolidación.

**Detector**: "estudié 8 horas el sábado" → 90% olvidado el lunes.

**Antídoto · Spaced Repetition**:

| En vez de | Hacer |
|---|---|
| 8 h sábado | 1 h × 8 días con intervalos crecientes |
| Pre-evento maratón | Días 0, 1, 3, 7, 14, 30 |

→ `references/01-seis-tecnicas-cognitivas.md` §Spaced · `assets/calendar-invites/`

---

## 8 · Recognition vs Recall 🟠

**Síntoma**: "sí, lo conozco cuando lo veo" · lees notas y dices "ajá ajá" · examen abierto: pelas.

**Por qué falla**: reconocimiento es proceso pasivo distinto de recuperación activa.
- **Reconocer**: ¿esto es A? Sí/No (binario · fácil)
- **Recuperar**: ¿qué era A? (generación · exponencialmente más difícil)

**Detector**: multiple choice → recognition (fácil) · pregunta abierta → recall (difícil). Si solo practicas multiple choice, fallas en abierto.

**Antídoto**: retrieval ciego · cierra TODO · hoja en blanco · escribe TODO de memoria · marca [DUDA] · solo después abrir fuentes.

→ `katas/kata-recuperacion-ciega.md`

---

## 9 · Identity Attachment · no soltar legacy 🟡

**Síntoma**: *"jQuery / Backbone / SOAP no es obsoleto, todavía hay empresas usándolo"*. Defiendes una skill que el mercado dejó de demandar porque es parte de tu identidad.

**Por qué pasa**: 10 años de inversión emocional + cognitiva · cambiar = admitir que el tiempo invertido fue (parcialmente) desperdicio · ego protection.

**Detector · Framework 4-D objetivo**:

| Dimensión | Pregunta honesta |
|---|---|
| Vigencia | ¿Aparece en JD de 2025-2026? |
| ROI | ¿Retorno por hora invertida hoy vs hace 5 años? |
| Obsolescencia | ¿Las conferencias del campo lo cubren? |
| Demanda | ¿Job postings · salarios · suben o caen? |

3/4 rojo → mercado ya soltó · eres tú quien no.

**Antídoto · Auditoría mensual + decisión documentada** (ver §coach-revolucionar). Plan reskill obligatorio antes de soltar.

**Riesgo si no lo combates**: 5 años defendiendo skill obsoleta · mercado decide por ti · dejas de ser empleable. Hubieras podido reskillearte en 6 meses.

`[CASO-BORDE]` Identity attachment combinado con high salary lock-in: skill obsoleta paga bien hoy en nicho legacy · trampa porque cuando ese nicho colapsa (típicamente 3-5 años) sales sin Capability moderno y con salario que el mercado nuevo no replica.

→ `prompts/05-relevance-audit.md` · `katas/kata-soltar-legacy.md`

---

## 10 · Multiple-Choice Comfort 🟡

**Síntoma**: estudias certificación con pool multiple choice · apruebas 95% · en mundo real no ejecutas.

**Por qué falla**: multiple choice activa recognition · te da pistas (4 opciones) · reduce búsqueda mental de N a 4.

**Antídoto**: open-ended preferentemente.

| Peor (multiple choice) | Mejor (open-ended) |
|---|---|
| "¿Qué hace ACID? A · B ✓ · C · D" | "Explica las 4 propiedades ACID con ejemplo · cuándo NO conviene" |

→ `prompts/08-evaluator-certification.md` usa preguntas abiertas progresivas (4 niveles).

---

## 11 · Refugio en Jerga 🟡

**Síntoma**: usas términos técnicos densos para "demostrar" que sabes · tu interlocutor (Escala 0-1) no entiende · te sientes inteligente · audiencia perdida.

**Por qué falla**: comunicación = transmisión, no exhibición. Si receptor no entiende, fallaste sin importar lo "técnico" que sonaras. Feynman: si no puedes explicarlo simple, no lo entiendes.

**Detector**: ¿tu mamá / hijo entendería tu última explicación técnica? Últimas 5 reuniones, ¿alguien preguntó "qué es eso"? Si no, sospecha que no entendieron y se quedaron callados.

**Antídoto**:
1. Toma material
2. Tradúcelo asumiendo audiencia 12 años
3. Si necesitas jerga · reemplaza con analogía
4. Lee en voz alta · cualquier traba = simplifica más

→ `katas/kata-feynman-novato.md`

---

## 12 · BoK sin Capability 🟡

**Síntoma**: sabes mucho del campo (papers · autores · debates) · no puedes ejecutar tareas reales del campo.

**Por qué falla**: BoK = mapa del territorio · Capability = lo que sabes hacer. **Saber del campo ≠ saber operar en el campo**.

**Detector**: examen abierto · *"Resuelve este problema real con [DOMINIO] · 30 min"*. Si te quedas paralizado citando teoría → BoK sin Capability.

**Antídoto**: Capability Model + práctica · define qué necesitas saber **HACER** · practica con feedback.

→ `references/02-tres-modelos-fundacionales.md` §Capability

---

## 13 · Maturity sin Diagnóstico 🟡

**Síntoma**: avanzas en plan de aprendizaje sin saber tu nivel actual · planes irreales basados en sobreestimación.

**Antídoto · Test diagnóstico ANTES de planear**:

```
Paso 0 (antes de cualquier plan):
1. Auto-evaluación honesta
2. IA-evaluación con Prompt #8
3. Validación humana (1 colega senior)
4. Reconciliación de las 3
5. SOLO ENTONCES planear progresión
```

`[CRITERIO-ACEPTACIÓN]` Diferencia auto vs IA ≤1 nivel para >80% de capabilities · si no, calibrar antes de avanzar.

---

## 14 · Calendario sin Ritual 🟢

**Síntoma**: tienes intención de "estudiar más" · "aprender X" · "mantenerte actualizado" · sin rituales agendados, nada pasa.

**Por qué falla**:
- Intención sin sistema → 0% completion.
- Sistema sin ritual → 30-40% completion.
- Ritual + calendario + accountability → 80%+ completion.

**Antídoto**: 4 rituales del playbook con ICS pre-llenados.

| Cadencia | Tiempo | Archivo ICS |
|---|---|---|
| Diaria · Curiosidad | 15 min | `assets/calendar-invites/curiosidad-diaria.ics` |
| Semanal · Aprehensión | 1 h | `aprehension-semanal.ics` |
| Mensual · Auditoría relevancia | 1 h | `auditoria-mensual.ics` |
| 16 sem · Práctica deliberada | 1 h × 16 | (programa) |

→ `rituals/`

---

## Diagnóstico rápido · ¿Cuál anti-patrón te aqueja?

```
"Leí mucho pero no sé si entendí"           → #1 Espejismo Fluidez
"La IA me dio datos que parecen falsos"     → #2 Hallucination
"La IA siempre me da la razón"              → #3 Sycophancy
"No sé qué tan confiable es esto"           → #4 Silent Uncertainty
"Solo le pregunté a ChatGPT"                → #5 Single-AI BoK
"Yo creo que estoy en Escala 5"             → #6 Dunning-Kruger
"Voy a estudiar todo el sábado"             → #7 Cramming
"Sí, lo reconozco cuando lo veo"            → #8 Recognition vs Recall
"jQuery todavía sirve"                      → #9 Identity Attachment
"Estudié con simuladores de examen"         → #10 Multiple-Choice
"Mi presentación fue muy técnica"           → #11 Refugio en Jerga
"Sé del tema pero no puedo ejecutar"        → #12 BoK sin Capability
"Tengo plan pero no sé dónde estoy"         → #13 Maturity sin Diagnóstico
"Tengo intención de estudiar más"           → #14 Calendario sin Ritual
```

---

## Combinaciones peligrosas (anti-patrones que se refuerzan)

| Combo | Síntoma | Resolución |
|---|---|---|
| #1 + #11 | Fluidez decorada con jerga · sensación máxima de competencia · gap máximo | Feynman a niño 12 años · sin jerga, sin excepción |
| #5 + #2 | BoK de 1 IA + hallucinations no detectadas | Triangulación 3+ IAs + Prompt #4 · siempre |
| #6 + #10 | Dunning-Kruger con multiple choice como "prueba" de dominio | Prompt #8 abierto + feedback humano |
| #7 + #8 | Cramming repasando material · recognition máximo · recall cero | Spaced + Retrieval ciego, no más cramming |
| #9 + #4 | Defiendes skill obsoleta y la IA no marca dudas en el rationale | Auditoría 4-D con datos de mercado externos |

`[NUEVO-APORTE]` Combo #1+#11 es el más peligroso · doble fluidez (de IA + de jerga propia) · solo se detecta forzando audiencia no-experta. Si el alumno solo conversa con expertos, nunca detecta el gap.

---

## Referencias cruzadas

- Sustento académico: `references/06-ciencia-cognitiva-fuentes.md`
- Técnicas que combaten anti-patrones: `references/01-seis-tecnicas-cognitivas.md`
- Modelos para evitar #12, #13: `references/02-tres-modelos-fundacionales.md`
- Auditor que detecta #2-4: `agents/auditor-cruzado.md`
- Coach que combate #9: `agents/coach-revolucionar.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0 §Anti-patrones

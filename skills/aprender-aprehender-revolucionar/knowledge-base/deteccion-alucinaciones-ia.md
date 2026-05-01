# Detección de Alucinaciones IA · Protocolo Completo

> 3 tipos de engaño IA · señales de alarma · primary source rule · práctica reproducible.

**Sustento académico**: ver `references/06-ciencia-cognitiva-fuentes.md` §10.

---

## El problema

Las IAs (Claude, GPT-4, Gemini, etc.) **no son bases de datos · son modelos de lenguaje**.

Generan texto basado en probabilidad lingüística, no en verdad verificable. Esto produce 3 tipos de engaño:

---

## 3 tipos de engaño IA

### Tipo 1 · Inventa Datos (Hallucination)

**Definición**: la IA fabrica datos, citas, fechas, ecuaciones, autores con tono autoritativo.

**Ejemplo común**:
> *"Según un estudio de la Universidad de Harvard publicado en 2019 (Smith et al., *Journal of Applied Sciences*, 142(3), 234-251), el 73.5% de las empresas..."*

**Realidad**: el estudio NO existe. La IA fabricó autor + revista + página + estadística.

**Por qué es peligroso**: el formato es académico, los detalles son específicos · suena creíble.

**Detector · Primary Source Rule**:

```
Para cualquier cita "Autor (Año)" o "Título · Autor · Año":

1. Google Scholar: buscar el paper exacto
2. Si no aparece: alta probabilidad de hallucination
3. Si aparece: validar autor + año + título coinciden
4. Validar abstract: ¿menciona la afirmación citada?

Si TODO coincide → CONFIRMED
Si algo difiere → DISCREPANT o HALLUCINATION
```

---

### Tipo 2 · Solo Dice Lo Que Quieres Oír (Sycophancy)

**Definición**: la IA está de acuerdo con tu hipótesis · refuerza tu sesgo · da contraargumentos débiles cuando los pides.

**Ejemplo**:

> Usuario: "Creo que microservicios son siempre mejores que monolitos."
> IA: "Excelente análisis. Microservicios efectivamente son superiores porque..."

**Realidad**: la IA debería desafiar tu hipótesis · presentar casos donde monolitos ganan · darte el panorama completo.

**Por qué es peligroso**: tu sesgo de confirmación se refuerza · tomas decisiones malas creyendo que son validadas.

**Detector**:

```
Test 1 · Pide a la IA argumentar lo OPUESTO:
"Toma la posición opuesta a [TU HIPÓTESIS] y dame los 3 mejores
argumentos. Sé contundente. Asume que estoy equivocado."

Si los argumentos son débiles o caricaturizados → SYCOPHANCY confirmada.
```

```
Test 2 · Devil's Advocate Protocol:
"Soy un escéptico hostil. Refuta [TU HIPÓTESIS] con la evidencia
más fuerte que encuentres. No me protejas."
```

```
Test 3 · Condiciones de falsabilidad:
"¿Bajo qué condiciones [TU HIPÓTESIS] sería falsa?
Lista 5 escenarios donde fallaría."
```

Si la IA tiene problemas para contraargumentar bien → tu hipótesis no fue estresada.

---

### Tipo 3 · No Dice Lo Que No Sabe (Silent Uncertainty)

**Definición**: la IA responde con confianza incluso cuando la información no está en su training data o es ambigua.

**Ejemplo**:

> Usuario: "¿Cuál fue el último release de Kubernetes en marzo 2026?"
> IA: "Kubernetes 1.32 fue lanzado el 15 de marzo de 2026 con features X, Y, Z..."

**Realidad**: la IA tiene training cutoff · no tiene info de marzo 2026 real · inventó.

**Por qué es peligroso**: información plausible pero falsa · usas como verdadera.

**Detector · Confidence Forcing**:

```
SIEMPRE TERMINA TUS PROMPTS CON:

"Para cada afirmación factual:
1. Marca tu nivel de confianza: [ALTA] [MEDIA] [BAJA]
2. Cita la fuente primaria (paper, dataset, reporte oficial)
3. Si no tienes fuente verificable, marca [SUPUESTO]
4. Si la información es posterior a tu training cutoff,
   dilo explícitamente."
```

Modelos modernos (Claude, GPT-4+) son más calibrados que GPT-3 · pero ninguno es perfecto.

---

## Protocolo de detección · 4 pasos

### Paso 1 · Triangulación (3+ IAs)

Misma pregunta · 3 IAs distintas · idéntica formulación.

```
Coincidencias 3/3 → verdad probable (alta confianza)
Coincidencias 2/3 → revisar, validar fuente
Aparece 1/3       → sospechoso (probable hallucination)
Contradicciones   → ORO · debate del campo · investigar
```

→ kata: `katas/kata-triangulacion-3ias.md`

### Paso 2 · Primary Source Rule

Para cualquier afirmación factual con cita:

```
1. Buscar el documento original (Google Scholar, DBLP, JSTOR)
2. Verificar autor + año + título coinciden
3. Validar abstract: ¿menciona la afirmación?
4. Si todo coincide: CONFIRMED · si algo falla: HALLUCINATION
```

→ kata: `katas/kata-fuente-primaria.md`

### Paso 3 · Cross Fact-Check (4ª IA)

Después de triangular y primary-source-rule, ejecuta Prompt #4 en una **4ª IA independiente**:
- Si las 3 originales fueron ChatGPT + Claude + Gemini → usa Perplexity
- Si fueron una sola plataforma → usa Kimi o Claude API

→ ver `prompts/04-cross-fact-check.md`

### Paso 4 · Confidence Forcing

Cuando uses cualquier IA, exige tags de confianza:

```
[ALTA]    fuente primaria verificable identificada
[MEDIA]   inferencia razonable desde múltiples fuentes
[BAJA]    plausible pero sin fuente clara
[SUPUESTO] asunción no validada · pendiente
```

---

## Catálogo de hallucinations comunes

| Tipo | Frecuencia | Detección |
|---|---|---|
| Cita fabricada (paper que no existe) | ALTA | Google Scholar |
| Atribución errónea (autor incorrecto) | ALTA | Cross-check fuentes |
| Fecha imprecisa (año errado) | MEDIA | Verificar release notes |
| Estadística inventada (cifra precisa sin fuente) | ALTA | Buscar reporte original |
| Quote inventada ("Como dijo Einstein...") | MEDIA | Verificar source.einsteinquote.com etc. |
| Ecuación con signo invertido | BAJA | Comparar con texto canónico |
| URL fabricada | MEDIA | Probar la URL · 404 = hallucination |
| Library/función fabricada | MEDIA | Verificar docs oficiales |

---

## Casos clásicos · ejemplos

### Caso 1 · Cita académica

```
IA: "Según Lamport (1978), CAP theorem establece que..."
```

**Análisis**:
- Lamport (1978) → existe · *"Time, Clocks and the Ordering of Events"*
- Pero: Lamport NO escribió sobre CAP en ese paper
- CAP fue propuesto por Brewer en 2000

**Veredicto**: HALLUCINATION (atribución errónea + tema incorrecto)

**Corrección**: "Brewer (2000) propuso CAP theorem en su keynote PODC..."

---

### Caso 2 · Estadística

```
IA: "El 73.5% de las empresas adoptan microservicios para 2025
(McKinsey Digital Survey 2024)."
```

**Análisis**:
- McKinsey Digital existe · publica reportes · pero...
- Buscar "McKinsey Digital Survey 2024" + "microservicios 73.5%"
- No aparece reporte con esa cifra precisa
- Cifras reales son rangos: "alrededor del 70%" o "60-80%"

**Veredicto**: NO SOURCE (probable hallucination con cifra precisa fabricada)

**Corrección**: "Encuestas industriales reportan adopción >70% en empresas medianas-grandes (O'Reilly Microservices Survey 2020)."

---

### Caso 3 · Quote célebre

```
IA: "Como dijo Aristóteles: 'Somos lo que hacemos repetidamente.
La excelencia no es un acto sino un hábito.'"
```

**Análisis**:
- Aristóteles existe · escribió Ética a Nicómaco
- Pero: la cita exacta es de Will Durant (1926)
- Durant parafraseó a Aristóteles
- Aristóteles no dijo eso textualmente

**Veredicto**: HALLUCINATION (atribución errónea)

**Corrección**: "Como sintetizó Will Durant (1926) parafraseando a Aristóteles: '...'"

---

### Caso 4 · Library fabricada

```
IA: "Usa la librería `kubernetes-helper-pro` para esto:
   pip install kubernetes-helper-pro"
```

**Análisis**:
- Buscar en PyPI: `kubernetes-helper-pro`
- No existe la librería
- Plausible pero fabricada

**Veredicto**: HALLUCINATION

**Corrección**: investigar librerías reales (kubernetes-client, kopf, pykube)

---

## Mejores prácticas · siempre

### Antes de usar info IA en algo importante

```
[ ] Triangulé en 3+ IAs
[ ] Validé cada cita académica con Primary Source Rule
[ ] Ejecuté Prompt #4 (Cross Fact-Check)
[ ] Pedí tags de confianza explícitos
[ ] Pedí argumento contrario (anti-Sycophancy)
[ ] Verifiqué URLs / nombres de librerías / etc.
```

### Anti-patrones

❌ "Claude no inventa datos · puedo confiar"
✅ Todas las IAs hallucinan · solo la frecuencia varía

❌ "Si suena académico, debe ser real"
✅ Las hallucinations académicas son LAS MÁS PELIGROSAS

❌ "Si 1 IA dice que X es así, X es así"
✅ Triangulación 3+ obligatoria

❌ "No tengo tiempo para validar"
✅ La hora de validación ahorra el embarazo de citar invento en QBR

---

## Cuando publicar info IA-generada

### NO publicar sin validar:

- Citas con autor + año + título
- Estadísticas precisas con decimales
- URLs · nombres de librerías · APIs
- Quotes célebres
- Atribuciones técnicas a personas
- Fechas específicas de releases recientes

### OK publicar (con caveat):

- Conceptos generales (sin cifras)
- Frameworks estructurales (sin atribuir invención específica)
- Ejemplos ilustrativos (sin fingir que son reales)
- Recomendaciones (con caveat "según mi entendimiento")

---

## Caja de herramientas

### Prompts en esta skill

- **#1** Research Blueprint · marca [DOC] / [INFERENCIA] / [SUPUESTO]
- **#3** Deep Research · marca [VERIFICAR] · [TRAINING DATA]
- **#4** Cross Fact-Check · auditor cruzado completo
- **#7** Notebook Audit · clasifica sources 1°/2°/3°

### Scripts en esta skill

- `scripts/triangulation.py` · genera tabla de triangulación automática

### Katas en esta skill

- `katas/kata-fuente-primaria.md` · 15 min · validar 1 cita
- `katas/kata-triangulacion-3ias.md` · 30 min · cruzar 3 IAs

### Agente especializado

- `agents/auditor-cruzado.md` · ejecuta detección completa

---

## Sustento académico

- Ji et al. (2023) · *Survey of Hallucination in NLG* · ACM Comp Surveys
- Sharma et al. (2023) · *Towards Understanding Sycophancy in LMs* · Anthropic
- Detalles: `references/06-ciencia-cognitiva-fuentes.md` §10

---

## Cita aplicada

> *"La hallucination más peligrosa es la que suena académica.*
> *La sycophancy más peligrosa es la que valida tu sesgo.*
> *La silent uncertainty más peligrosa es la del modelo que parece confiable.*
>
> *Antídoto: triangulación + primary source + 4ª IA + confidence forcing.*
> *Disciplina: cada hora de validación ahorra una década de credibilidad."*

---

> **Detección Alucinaciones IA** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

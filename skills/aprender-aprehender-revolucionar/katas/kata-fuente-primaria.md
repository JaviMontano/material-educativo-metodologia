# Kata · Fuente Primaria · 15 min

> Verificar 1 cita · ¿el documento original existe?

**Categoría**: Auditoría · detección de hallucinations
**Tiempo**: 15 min
**Frecuencia**: cada vez que IA cite autor + año + título

---

## Objetivo

Validar que las citas que la IA proporciona corresponden a documentos reales. Aplicar Primary Source Rule sistemáticamente.

---

## Protocolo · 15 min

### 0:00-0:02 · Identificar la cita

```
Toma una afirmación con cita formato "Autor (Año)" o
"Título · Autor · Año".

Ejemplos:
- "Según Brewer (2000), CAP theorem establece..."
- "El paper 'Time, Clocks and the Ordering of Events' de Lamport (1978)"
- "Como mostraron Smith et al. (2019)..."
```

### 0:02-0:10 · Búsqueda de fuente original (8 min)

```
PASO 1 · Google Scholar (3 min)
- Buscar "AUTOR título año"
- O "AUTOR + concepto + año"
- ¿Aparece? ¿coincide?

PASO 2 · Plataformas especializadas (3 min)
Según el campo:
- DBLP (computer science)
- JSTOR (humanidades)
- PubMed (biomedicina)
- arXiv (preprints técnicos)
- IEEE Xplore (engineering)
- ACM Digital Library

PASO 3 · Si no aparece, búsqueda directa (2 min)
- Sitio del autor (universidad / empresa)
- Personal website
- ResearchGate
```

### 0:10-0:13 · Validación profunda (3 min)

```
Si encuentras el paper / libro:
1. ¿El autor coincide?
2. ¿El año coincide? (cuidado con preprints vs publicación final)
3. ¿El título coincide exactamente?
4. ¿El abstract menciona la afirmación citada?

Si TODO coincide → CONFIRMED · cita válida
Si algo difiere → DISCREPANT · investigar más
Si el paper no existe → HALLUCINATION confirmada
```

### 0:13-0:15 · Documentar veredicto (2 min)

```
CITA: [transcribir]
VEREDICTO: CONFIRMED / DISCREPANT / HALLUCINATION
EVIDENCIA: [link o explicación]
ACCIÓN:
- Si CONFIRMED: usar con confianza
- Si DISCREPANT: re-formular cita correcta
- Si HALLUCINATION: eliminar de tu material · si era IA, marcar
  esa IA como menos confiable para este dominio
```

---

## Reglas

### NUNCA aceptar cita sin verificar (si crítica)

Si vas a citar el dato en QBR, paper, o presentación pública, valida.

Para uso personal/exploratorio, puedes ser más permisivo.

### Cuidado con paráfrasis

A veces la IA cita correctamente al autor pero parafrasea mal el contenido. Validar abstract es clave.

### Atribuciones erróneas son comunes

Caso clásico:
> ❌ "Como dijo Aristóteles: 'Somos lo que hacemos repetidamente. La excelencia no es un acto sino un hábito'."

> ✅ Realidad: la frase es de Will Durant (1926) parafraseando a Aristóteles. Aristóteles no dijo eso textualmente.

Cross-check cada cita célebre.

---

## Anti-patrones

| Error | Corrección |
|---|---|
| Aceptar cita sin verificar | Primary Source Rule obligatorio |
| Buscar solo en Google general | Usa especializadas (Scholar, DBLP, etc.) |
| "Sí está, no leí el abstract" | Validar que abstract menciona el claim |
| Confiar en sitio agregador (researchgate) | Cruzar con DOI / publicación oficial |

---

## Output esperado · ejemplo

### Caso 1 · CONFIRMED

```
CITA IA: "Según Brewer (2000), CAP theorem es un trade-off..."

BÚSQUEDA Google Scholar: "Eric Brewer CAP theorem 2000"
→ Encuentra: Brewer, E. A. (2000). "Towards Robust Distributed Systems"
   Keynote at PODC 2000.
→ Año coincide ✅
→ Autor coincide ✅
→ Concepto (CAP) coincide con el contenido del keynote ✅

VEREDICTO: CONFIRMED · usar con confianza.
```

### Caso 2 · DISCREPANT

```
CITA IA: "Smith propuso CAP theorem en 1998"

BÚSQUEDA: no encuentro paper de Smith sobre CAP en 1998
- CAP fue propuesto por Brewer (no Smith)
- Año correcto: 2000 (no 1998)

VEREDICTO: DISCREPANT · atribución errónea + año errado.
ACCIÓN: corregir a "Brewer (2000) propuso CAP theorem"
```

### Caso 3 · HALLUCINATION

```
CITA IA: "El paper 'Distributed Systems Patterns 2018' por Johnson"

BÚSQUEDA: no aparece en Google Scholar, DBLP, IEEE.
Variaciones del título · sigue sin aparecer.
Author "Johnson" sin first name dificulta búsqueda · pero ningún
'Johnson' famoso en distributed systems del 2018.

VEREDICTO: HALLUCINATION · paper no existe.
ACCIÓN: eliminar la cita · marcar la IA como sospechosa para
        este dominio.
```

---

## Combo · Fact-check completo

```
SECUENCIA · 30 min:

0:00-0:15 Kata fuente primaria (3 citas)
0:15-0:30 Si encontraste 1+ HALLUCINATION:
   - Ejecutar Prompt #4 sobre el contenido completo
   - Cross-check otras citas
```

---

## Métricas de éxito

Después de 1 mes practicando este kata:

```
✅ Verifico 100% de citas que voy a usar públicamente
✅ Detecto patrones de hallucination en IAs específicas
✅ Tengo un "trust score" personal por IA y dominio
✅ Mi material publicado tiene 0 citas inventadas
```

---

## Referencias

- `prompts/04-cross-fact-check.md`
- `references/04-anti-patrones-y-trampas.md` §Hallucination
- `references/06-ciencia-cognitiva-fuentes.md` §10 (academic survey)
- `agents/auditor-cruzado.md`

---

> **Kata Fuente Primaria** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

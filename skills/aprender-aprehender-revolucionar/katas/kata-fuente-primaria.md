# Kata · Fuente Primaria · 15 min

> Verificar 1 cita · ¿el documento original existe? v1.1.0.

| Concepto | Valor |
|---|---|
| Categoría | Auditoría · detección de hallucinations |
| Tiempo | 15 min por cita |
| Frecuencia | Cada vez que IA cite autor + año + título · pre-uso público |
| Output | Veredicto CONFIRMED/DISCREPANT/HALLUCINATION · acción documentada |
| Aplica | Primary Source Rule del Playbook v2.0.0 |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Primary Source Rule + Prompt #4.
`[DOC]` LLMs hallucinations en citas académicas: 47-58% en GPT-4 / Bard tests (Walters & Wilder 2023, *Scientific Reports* 13).

## Contrato

| Hace | No hace |
|---|---|
| Detecta paper / libro / autor inventado por IA | Verifica veracidad del CONTENIDO citado · solo existencia del documento |
| Construye trust score personal por IA y dominio | Reemplaza peer review · es filtro mínimo, no garantía completa |
| Aplica disciplina pre-publicación / pre-QBR | Funciona si IA cita en formato vago ("según estudios recientes...") |

`[LÍMITE]` Si la IA cita sin formato "Autor (Año)" · no hay nada que validar · pídele que estructure la cita ANTES (autor, año, título, journal).
`[SUPUESTO]` Tienes acceso a Google Scholar y al menos 1 plataforma especializada del campo.

## Protocolo · 15 min por cita

### 0:00-0:02 · Identificar la cita

Toma una afirmación con cita estructurada:

```
Ejemplos válidos:
- "Según Brewer (2000), CAP theorem establece..."
- "El paper 'Time, Clocks and the Ordering of Events' de Lamport (1978)"
- "Como mostraron Smith et al. (2019) en Nature..."

Ejemplos inválidos (pedir reformulación a IA):
- "Estudios recientes muestran..." (sin autor)
- "Es bien sabido que..." (sin fuente)
- "Según expertos del campo..." (vago)
```

### 0:02-0:10 · Búsqueda de fuente original (8 min)

| Paso | Tiempo | Plataforma | Búsqueda |
|---|---|---|---|
| 1 · Google Scholar | 3 min | scholar.google.com | "Autor título año" o "Autor concepto año" |
| 2 · Plataforma especializada | 3 min | DBLP / JSTOR / PubMed / arXiv / IEEE / ACM | Según campo |
| 3 · Búsqueda directa | 2 min | Sitio del autor / ResearchGate / personal | Si pasos 1-2 fallaron |

| Campo | Plataforma especializada |
|---|---|
| Computer science | DBLP · ACM Digital Library · IEEE Xplore |
| Humanidades | JSTOR · MUSE |
| Biomedicina | PubMed · MEDLINE |
| Preprints técnicos | arXiv · bioRxiv |
| Engineering | IEEE Xplore |
| Economía | NBER · SSRN |

### 0:10-0:13 · Validación profunda (3 min)

Si encontraste paper/libro:

```
1. ¿El autor coincide exactamente?
2. ¿El año coincide?
   (cuidado: preprint vs publicación final pueden diferir 1-2 años)
3. ¿El título coincide exactamente?
4. ¿El abstract menciona la afirmación citada?
   (si la IA citó correctamente al autor pero parafraseó mal el contenido)
```

| Resultado | Veredicto |
|---|---|
| Todo coincide | ✅ CONFIRMED · cita válida |
| Algo difiere (autor, año, contenido) | ⚠️ DISCREPANT · investigar más |
| Paper no existe en ninguna plataforma | ❌ HALLUCINATION confirmada |

### 0:13-0:15 · Documentar veredicto (2 min)

```
CITA: [transcribir literal]
VEREDICTO: CONFIRMED / DISCREPANT / HALLUCINATION
EVIDENCIA: [link DOI o explicación]
ACCIÓN:
- CONFIRMED: usar con confianza
- DISCREPANT: re-formular cita correctamente
- HALLUCINATION: eliminar de tu material · marcar IA como menos
  confiable para ese dominio (trust score)
```

## Reglas duras

| Regla | Aplicabilidad |
|---|---|
| NUNCA aceptar cita sin verificar (uso público) | QBR · paper · presentación · LinkedIn público |
| Cuidado con paráfrasis | IA puede citar autor correcto pero mal contenido |
| Atribuciones erróneas son comunes | Validar incluso citas célebres |
| Cross-check DOI con publicación oficial | NO confiar solo en agregadores (researchgate, etc.) |

## Anti-patrón célebre · cita falsamente atribuida

```
❌ "Como dijo Aristóteles: 'Somos lo que hacemos repetidamente.
   La excelencia no es un acto sino un hábito.'"

✅ Realidad: la frase es de Will Durant (1926) parafraseando a
   Aristóteles. Aristóteles NO dijo eso textualmente.
```

`[NUEVO-APORTE]` Crea un "trust score" personal por IA y dominio. Tras 30 días aplicando este kata, sabrás cuál IA halucina más en tu campo · útil para decidir cuál triangular primero.

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Aceptar cita sin verificar para uso público | Citas en QBR sin DOI | Primary Source Rule obligatorio pre-publicación |
| 2 | Buscar solo en Google general | "No encontré · pero Google falla" | Plataformas especializadas obligatorias (Scholar mínimo) |
| 3 | "Está · no leí abstract" | Confirmas existencia · no contenido | Validar abstract menciona el claim citado |

## Output esperado · 3 casos

### Caso 1 · CONFIRMED

```
CITA IA: "Según Brewer (2000), CAP theorem es trade-off..."

BÚSQUEDA Google Scholar: "Eric Brewer CAP theorem 2000"
→ Encuentra: Brewer, E. A. (2000). "Towards Robust Distributed
  Systems" · Keynote PODC 2000.
→ Año coincide ✅
→ Autor coincide ✅
→ CAP coincide con contenido del keynote ✅

VEREDICTO: CONFIRMED · usar con confianza.
```

### Caso 2 · DISCREPANT

```
CITA IA: "Smith propuso CAP theorem en 1998"

BÚSQUEDA: no hay paper de Smith sobre CAP en 1998
- CAP fue propuesto por Brewer (no Smith)
- Año correcto: 2000 (no 1998)

VEREDICTO: DISCREPANT · atribución errónea + año errado.
ACCIÓN: corregir cita a "Brewer (2000) propuso CAP theorem"
```

### Caso 3 · HALLUCINATION

```
CITA IA: "El paper 'Distributed Systems Patterns 2018' por Johnson"

BÚSQUEDA: 0 resultados en Google Scholar, DBLP, IEEE, ACM
- Variaciones del título · sigue sin aparecer
- "Johnson" sin first name · ningún Johnson notable en
  distributed systems del 2018

VEREDICTO: HALLUCINATION · paper no existe.
ACCIÓN: eliminar la cita · marcar la IA en trust score como
        sospechosa para distributed systems.
```

## Combo · fact-check completo (30 min)

```
0:00-0:15 · Kata fuente primaria sobre 3 citas críticas
0:15-0:30 · Si encontraste 1+ HALLUCINATION:
   - Ejecutar Prompt #4 sobre el contenido completo
   - Cross-check OTRAS citas (probable contagio)
   - Re-evaluar trust score de la IA usada
```

`[CRITERIO-ACEPTACIÓN]` 1 hallucination confirmada en una IA = ALL las citas de esa misma IA en ese tema deben re-validarse · NO solo la afectada.

## Métricas de éxito (30 días)

```
[ ] 100% de citas para uso público verificadas
[ ] Patrones de hallucination detectados por IA específica
[ ] Trust score personal por IA y dominio mantenido
[ ] Material publicado con 0 citas inventadas
[ ] Trust score informa decisión de cuál IA triangular primero
```

## Cuándo aplicarlo

- ✅ Pre-cita pública (QBR, paper, post LinkedIn técnico)
- ✅ Cada Workflow 1 · paso 2:30 (post Prompt #4)
- ✅ Cada vez que la IA cite con formato "Autor (Año)"
- ❌ NO necesario para uso personal exploratorio (trade-off velocidad/rigor)

## Referencias cruzadas

- `prompts/04-cross-fact-check.md`
- `references/04-anti-patrones-y-trampas.md` §Hallucination
- `references/06-ciencia-cognitiva-fuentes.md` §10
- `agents/auditor-cruzado.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0

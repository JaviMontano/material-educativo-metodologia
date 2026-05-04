# Ritual · Curiosidad Diaria · 15 min

> Primera ola del día. Cadencia > intensidad. *15 min diarios > 3 h el sábado.* v1.1.0.

| Concepto | Valor |
|---|---|
| Cadencia | Cada mañana · antes de email |
| Tiempo | 15 min · NUNCA más |
| Frecuencia | L-V (descanso S-D) |
| Output | 1 decisión por item: PIEDRA/INTERESANTE/RUIDO |
| Calendar invite | `assets/calendar-invites/curiosidad-diaria.ics` |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Rituales + principio "Cadencia > intensidad".
`[DOC]` Distributed practice supera massed practice (Cepeda et al. 2006, *Psychological Bulletin* 132).

## Contrato

| Hace | No hace |
|---|---|
| Mantiene radar activo del campo · 15 min/día | Reemplaza Workflows · es escaneo, no estudio profundo |
| Distingue señal de ruido vía decisión binaria | Genera dominio · solo identifica qué amerita estudio |
| Agrega sources frescas a NotebookLM mensualmente | Funciona si lo haces 1×/sem (necesita diario para momentum) |

`[LÍMITE]` 15 min NO son suficientes para procesar paper denso · solo headlines + 1 párrafo de contexto. Para profundizar: bookmark + Workflow 1 después.
`[SUPUESTO]` Tienes acceso a Perplexity (o IA con web search) y agenda con bloque protegido.

## Protocolo · 15 min

### 0:00-0:05 · Abrir IA con web search

| IA | Recomendación |
|---|---|
| Perplexity | ⭐ Default · web search nativa · noticias frescas |
| ChatGPT con browsing | OK si Perplexity no disponible |
| Gemini | OK si tema en ecosistema Google |
| Claude | Solo si combinas con feed RSS manual (no tiene web search nativo) |

### 0:05-0:10 · Pregunta del día (rotar 3 plantillas)

```
1. "¿Qué avance relevante pasó AYER en [MI INDUSTRIA / TEMA ACTIVO]?
    Cita fuente. Sé conciso (3 viñetas)."

2. "¿Cuál es la noticia más relevante de los ÚLTIMOS 3 DÍAS en
    [MI CAMPO]? Por qué importa."

3. "¿Qué herramienta nueva apareció ayer en [MI STACK]?
    Solo si pasó algo significativo. Si nada, dilo."
```

`[CRITERIO-ACEPTACIÓN]` Si la IA responde con avances de 6+ meses atrás · pregunta fue muy general · refina con fechas explícitas.

### 0:10-0:15 · Decisión binaria por item

| Decisión | Frecuencia esperada | Acción |
|---|---|---|
| 🟢 PIEDRA ANGULAR | ~1 de 10 días | Añadir a NotebookLM como source · agendar Workflow 1 cuando puedas |
| 🟡 INTERESANTE | ~5 de 10 días | Bookmark Pocket/Notion · revisar viernes |
| ⚫ RUIDO | ~4 de 10 días | Skip · seguir con el día |

`[CASO-BORDE]` Si todos los items quedan 🟢 piedra angular · sospecha · no estás filtrando · re-aplica criterio "¿cambia mi trabajo en próximos 3 meses?".

## Reglas duras

| Regla | Por qué |
|---|---|
| NUNCA exceder 15 min | Trampa: leer paper completo · pierde 1h cada día · 5h/sem perdidas |
| NUNCA saltar 2 días seguidos | 2 días = pérdida de momentum · activa calendar reminder |
| NUNCA mezclar con email/reuniones | Primero del día (o último de la noche) · NO intercalar |

`[TRADE-OFF]` La regla "antes de email" cuesta 15 min de respuesta tardía a stakeholders · pero gana 1 punto/mes en radar profesional · trade favorable para roles donde el conocimiento del campo es crítico.

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | "Profundizar ahora" mid-ritual | Te pasaste 30 min · no documentaste | Bookmark + agenda Workflow · ritual = escaneo, no estudio |
| 2 | Saltar días sin reactivar calendar | Pasaron 5 días sin ritual | Re-activar calendar invite · accountability con peer si hace falta |
| 3 | Aceptar todo como PIEDRA | NotebookLM crece sin uso real | Filtro: "¿cambia mi trabajo en próximos 3 meses?" |

## Variantes

| Modo | Tiempo | Cuándo |
|---|---|---|
| **Express** | 5 min · 1 pregunta · decisión 30s | Días saturados · mejor 5 min imperfecto que 0 perfecto |
| **Default** | 15 min · 1 pregunta · 3 items con decisión | Por defecto |
| **Marathon viernes** | 30 min · revisión de bookmarks de la semana | 1×/sem · convierte 🟡 a 🟢/⚫ con perspectiva 5 días |

### Marathon viernes · revisión semanal

```
Una vez/semana, dedica 15 min adicionales (total 30 min)
a revisar tu Pocket / bookmarks de la semana:

- ¿Qué bookmarks aún parecen relevantes 5 días después?
- ¿Cuál merece convertirse en source de NotebookLM?
- ¿Cuál fue ruido en retrospectiva (descarta sin culpa)?
```

`[NUEVO-APORTE]` La revisión retrospectiva 5 días después es mejor filtro que la decisión inicial. El 30-40% de items 🟡 cae a ⚫ con perspectiva.

## Métricas de éxito (1 mes)

```
[ ] Reconozco 80%+ de los nombres mencionados en mi industria
[ ] 5-10 bookmarks/mes que valen la pena (no 50, no 0)
[ ] Identifico hype vs señal real con confianza
[ ] NotebookLM crece con sources frescas mensualmente
[ ] 0 días saltados sin reactivación al día siguiente
```

`[CRITERIO-ACEPTACIÓN]` Si tras 4 sem · 0 items 🟢 · tema activo no es vivo · cambia foco. Si 100% 🟢 · falta filtro · re-aplica criterio de impacto.

## Ejemplos prácticos

### Lunes mañana

```
TÚ: "¿Qué avance relevante pasó ayer en LLMs / agentic AI?
    Cita fuente. 3 viñetas."

PERPLEXITY:
- Anthropic publicó update Claude Opus 4.7 con 1M context [link]
- Paper "Constitutional AI for Agentic Workflows" arxiv [link]
- OpenAI cerró deal con Reuters para training data [link]

DECISIÓN:
- 1M context Claude → 🟢 PIEDRA ANGULAR · Workflow 1 esta semana
- Constitutional AI paper → 🟡 INTERESANTE · bookmark · viernes
- OpenAI/Reuters → ⚫ RUIDO · skip
```

## Calendar invite

```
Recurrencia: Lun-Vie 7:30 AM (ajustar a rutina)
Reminder: 5 min antes
Duración: 15 min
Bloque "deep work" sin notificaciones
```

Archivo: `assets/calendar-invites/curiosidad-diaria.ics`

## Referencias cruzadas

- `references/01-seis-tecnicas-cognitivas.md` §Spaced Repetition
- `rituals/ritual-aprehension-semanal.md` (complemento semanal)
- `rituals/ritual-auditoria-mensual.md` (filtro mensual de bookmarks)
- `assets/calendar-invites/curiosidad-diaria.ics`
- `knowledge-base/manifiesto-metodologia.md` (cadencia > intensidad)

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0

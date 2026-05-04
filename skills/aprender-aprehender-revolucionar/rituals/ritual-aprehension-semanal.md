# Ritual · Aprehensión Semanal · 60 min

> Si no puedes explicar sin notas, no aprehendiste. v1.1.0.

| Concepto | Valor |
|---|---|
| Cadencia | 1× / sem · viernes preferido (cierre de ciclo) |
| Tiempo | 60 min Default · 30 min Express · 120 min Marathon pre-evento |
| Output | Bitácora `~/aprender-aprehender/bitacora/{YYYY-WW}.md` con ratio FUERTE/PARCIAL/DÉBIL |
| Calendar invite | `assets/calendar-invites/aprehension-semanal.ics` |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Rituales + Workflow 3 §Semana de aprehensión.
`[DOC]` Retrieval + spaced practice combinados producen 50%+ retención a 6 meses vs re-lectura (Karpicke & Roediger 2008, *Science* 319).

## Contrato

| Hace | No hace |
|---|---|
| Convierte conocimiento (Aprender) en aprehensión (defendible) | Crea conocimiento nuevo · solo consolida lo de la semana |
| Detecta espejismo de fluidez antes del evento real | Garantiza pasar QBR/cert · es paso necesario, no suficiente |
| Genera flashcards Anki + Spaced Repetition agendado | Reemplaza la práctica con humano real (necesaria pre-evento) |

`[LÍMITE]` Si no aprendiste nada nuevo esta semana · ritual aplica a re-evaluar lo del trimestre · NO saltar (es la trampa).
`[SUPUESTO]` Tienes NotebookLM con coach activo (Prompt #2) · sin esto, retrieval pierde 40% del valor.

## Protocolo · 60 min Default

### 0:00-0:05 · Setup

```
1. Abrir NotebookLM con coach activo (Prompt #2)
2. Cerrar TODAS las notas, libros, web (kata-recuperacion-ciega)
3. Hoja en blanco / documento nuevo
4. Timer 20 min visible
```

`[CRITERIO-ACEPTACIÓN]` 1 tab del tema abierta = ritual fallido (igual que kata-recuperacion-ciega). Reset.

### 0:05-0:25 · RETRIEVAL (20 min)

```
TAREA: recuperar ciego de los conceptos clave de la semana.

1. Identificar el concepto más importante aprendido (1 frase ciega)
2. Escribir TODO lo que recuerdes:
   - Qué es
   - Por qué importa
   - Relaciones con conceptos previos
   - Ejemplos concretos
   - Trade-offs
3. Sin volver a notas · marca [?] lo que dudas
4. Detener cuando agotaste tu memoria (no antes)
```

### 0:25-0:45 · EVALUACIÓN (20 min)

```
TAREA: comparar lo recuperado vs realidad.

1. Abrir notas / NotebookLM / fuente original
2. Para cada elemento del retrieval, marca:
   ✅ FUERTE  · recuperaste correctamente sin pista
   🟡 PARCIAL · idea OK · faltó profundidad o ejemplo
   ❌ DÉBIL   · falló · concepto erróneo o gap fundamental
3. Para cada DÉBIL, pregunta a coach:
   "Diferencia entre [mi versión incorrecta] y la correcta.
    Hazme pregunta socrática para descubrir mi error."
4. Documentar gaps en `~/aprender-aprehender/bitacora/{YYYY-WW}.md`
```

`[CASO-BORDE]` Si TODO retrieval queda DÉBIL · semana fue masiva o no estudiaste con método · re-Workflow 2 sobre el subtema más crítico.

### 0:45-0:55 · REPARACIÓN (10 min)

```
TAREA: cerrar gaps · NO re-leer todo.

Para cada DÉBIL:
1. Estudiar SOLO ese gap específico (no todo el concepto)
2. Generar flashcard:
   - Front: pregunta abierta sobre el gap
   - Back: respuesta correcta + por qué
3. Programar Spaced Repetition:
   - +1 día · +3 días · +1 sem · +1 mes
```

`[TRADE-OFF]` La tentación de re-estudiar el concepto completo cuesta 30+ min · estudiar solo el gap específico cuesta 5 min con misma mejora · 6× más eficiente.

### 0:55-1:00 · FEYNMAN MICRO (5 min)

```
TAREA: prueba final.

1. Tomar 1 concepto que marcaste FUERTE
2. Explicar en voz alta o grabar audio · 3 min máx
3. Audiencia: niño 12 años · sin jerga
4. Veredicto:
   - Fluye natural → confirmas Escala 3 en ese concepto
   - Trabas o jerga → no era tan FUERTE como creías · marcar repaso
```

## Reglas duras

| Regla | Por qué |
|---|---|
| NUNCA saltarlo "porque tuve mucho trabajo" | La semana sin tiempo es exactamente cuando lo necesitas · 60 min protegidos = 5 días sin acumular gaps |
| NUNCA retrieval con notas abiertas | Defeats el propósito · Recognition ≠ Recall |
| NUNCA aceptar "creo que entendí" | Si todo PARCIAL, ritual funciona · si todo FUERTE pero falla Feynman = espejismo |

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Saltar el ritual en semanas saturadas | 2-3 sem consecutivas sin bitácora | 60 min protegidos · es la inversión que evita 5 días de re-trabajo |
| 2 | Marcar todo FUERTE sin probar Feynman | Auto-eval optimista · Feynman expone | El paso 0:55-1:00 es no-negociable · audio obligatorio |
| 3 | Reparación sin Spaced Repetition agendado | Flashcards creadas · nunca repasadas | Agendar +1d/+3d/+1sem/+1mes EN CALENDARIO inmediato |

## Variantes

| Modo | Tiempo | Cuándo |
|---|---|---|
| **Express** | 30 min · 1 concepto · sin Marathon | Semanas saturadas · mejor 30 min/sem que 0 |
| **Default** | 60 min · 2-3 conceptos | Por defecto · viernes |
| **Marathon** | 120 min · semana clave pre-evento | Pre-QBR/cert · 5+ conceptos + Feynman audio × 3 |

### Express · 30 min

```
0:00-0:15 · Retrieval (1 concepto)
0:15-0:25 · Evaluación + reparación
0:25-0:30 · Feynman micro
```

`[TRADE-OFF]` Cubre menos conceptos · prioriza el más crítico de la semana.

### Marathon · 120 min pre-evento

```
0:00-0:30 · Retrieval múltiples conceptos (3-5)
0:30-1:00 · Evaluación profunda · interrogatorio coach
1:00-1:30 · Reparación + flashcards Anki
1:30-2:00 · Feynman a 3 conceptos · audio grabado
```

## Bitácora semanal · template

Archivo: `~/aprender-aprehender/bitacora/{YYYY-WW}.md`

```markdown
# Aprehensión semana {YYYY-WW}

## Conceptos cubiertos esta semana
- [Concepto 1] · status: FUERTE / PARCIAL / DÉBIL
- [Concepto 2] · status: ...

## Retrieval ciego
[lo que escribí sin mirar]

## Comparación con realidad
[gaps detectados con [?]]

## Reparación ejecutada
- Flashcards creadas: N
- Spaced Repetition agendado: días +1, +3, +7, +30

## Feynman test
- Concepto elegido: [...]
- Audio grabado: [link]
- Veredicto: FLUYE / TRABA / JERGA

## Plan próxima semana
- [...]
```

## Métricas de éxito (4 sem)

```
[ ] Identifico mis DÉBIL sin negarlos
[ ] Ratio FUERTE/PARCIAL/DÉBIL mejora semana a semana
[ ] 12+ flashcards creadas en spaced repetition activo
[ ] Último Feynman fluyó natural sin jerga
[ ] Self-confidence calibrada (no más Dunning-Kruger)
```

`[CRITERIO-ACEPTACIÓN]` Tras 4 semanas · si ratio FUERTE no sube · revisar dieta de estudio (probablemente recognition pasivo en exceso).

## Calendar invite

```
Día: viernes 17:00 (cierre de semana)
Duración: 60 min
Recurrencia: semanal
Reminder: 10 min antes
Bloque "deep work" sin notificaciones
```

Archivo: `assets/calendar-invites/aprehension-semanal.ics`

## Referencias cruzadas

- `references/01-seis-tecnicas-cognitivas.md` §Retrieval Practice §Spaced Repetition §Feynman
- `katas/kata-recuperacion-ciega.md` · `kata-feynman-novato.md`
- `prompts/02-coach-system-prompt.md` · `08-evaluator-certification.md`
- `assets/calendar-invites/aprehension-semanal.ics`
- `assets/plantilla-bitacora-aprehension.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0

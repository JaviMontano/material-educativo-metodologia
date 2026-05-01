# Ritual · Aprehensión Semanal · 1 hora

> Convertir el conocimiento de la semana en aprehensión defendible. *Si no puedes explicar sin notas, no aprehendiste.*

**Cadencia**: 1× / semana · viernes preferido (cierre semanal)
**Tiempo**: 60 minutos
**Calendar invite**: `assets/calendar-invites/aprehension-semanal.ics`

---

## Por qué este ritual

Aprender ≠ aprehender. Sabes algo cuando puedes explicarlo sin notas, ante audiencia exigente, bajo presión. Una vez por semana, validas ese estándar contra lo que aprendiste.

**Sin este ritual** → fluidez ilusoria · espejismo de comprensión.
**Con este ritual** → defensa garantizada · confianza real.

---

## Protocolo · 60 minutos

### 0:00-0:05 · Setup

```
1. Abrir NotebookLM con coach activo (Prompt #2)
2. Cierrar todas las notas, libros, web (kata-recuperacion-ciega)
3. Hoja en blanco / documento nuevo
4. Iniciar timer 20 min
```

### 0:05-0:25 · RETRIEVAL (20 min)

```
TAREA: recuperar ciego de los conceptos clave de esta semana.

1. Identificar el concepto más importante que aprendiste esta semana
   (1 frase · sin mirar nada)

2. Escribir TODO lo que recuerdes sobre ese concepto:
   - Qué es
   - Por qué importa
   - Cómo se relaciona con conceptos previos
   - Ejemplos concretos
   - Trade-offs

3. SIN volver a las notas, marca con [?] lo que dudas.

4. Detener cuando agotaste tu memoria (no antes).
```

### 0:25-0:45 · EVALUACIÓN (20 min)

```
TAREA: comparar lo recuperado vs la realidad.

1. Abrir notas / NotebookLM / fuente original.

2. Para cada elemento de tu retrieval, marca:
   ✅ FUERTE  · recuperaste correctamente sin pista
   🟡 PARCIAL · idea correcta pero faltó profundidad o ejemplo
   ❌ DÉBIL   · falló · concepto erróneo o gap fundamental

3. Para cada [DÉBIL], pregunta a NotebookLM con Coach activo:
   "¿Cuál es la diferencia entre [mi versión incorrecta] y la
    versión correcta? Hazme una pregunta socrática para que yo
    descubra mi error."

4. Documentar gaps específicos en
   `~/aprender-aprehender/bitacora/{YYYY-WW}.md`
```

### 0:45-0:55 · REPARACIÓN (10 min)

```
TAREA: cerrar gaps · pero NO re-leer todo.

Para cada [DÉBIL]:
1. Estudiar SOLO ese gap específico (no todo el concepto)
2. Generar flashcard en NotebookLM:
   - Front: pregunta abierta sobre el gap
   - Back: respuesta correcta + por qué
3. Programar Spaced Repetition:
   - Revisión en 1 día
   - Revisión en 3 días
   - Revisión en 1 semana
   - Revisión en 1 mes
```

### 0:55-1:00 · FEYNMAN MICRO (5 min)

```
TAREA: prueba final · explicar uno de los conceptos sin notas.

1. Tomar 1 concepto que marcaste FUERTE
2. Explicarlo en voz alta (o grabar audio)
3. Audiencia: niño de 12 años · sin jerga
4. 3 minutos máximo

Si te trabas o usas jerga → no era tan FUERTE como creías · marcar
para repaso.

Si fluyes natural → confirmas Escala 3 en ese concepto.
```

---

## Reglas de oro

### NUNCA saltarlo "porque tuve mucho trabajo"

La semana donde "no tienes tiempo" es exactamente cuando lo necesitas. 60 min protegidos = 5 días de productividad sin acumular gaps.

### NUNCA hacer retrieval con notas abiertas

Defeats el propósito. Recognition ≠ Recall. Cierra TODO.

### NUNCA aceptar "creo que entendí"

Si después del retrieval marcas todo PARCIAL, no estás engañándote → está bien · el ritual funciona.

Si marcas todo FUERTE en retrieval pero fallas el Feynman → estás en el espejismo de fluidez.

---

## Variantes

### Express · 30 min (semanas saturadas)

```
0:00-0:15 Retrieval (1 concepto)
0:15-0:25 Evaluación + reparación
0:25-0:30 Feynman micro
```

Trade-off: cubres menos conceptos. Mejor 30 min/semana que 0.

### Marathon · 2 horas (semana clave pre-evento)

```
0:00-0:30 Retrieval múltiples conceptos
0:30-1:00 Evaluación profunda
1:00-1:30 Reparación + flashcards Anki
1:30-2:00 Feynman a 3 conceptos · audio grabado
```

---

## Documentación · bitácora semanal

Archivo: `~/aprender-aprehender/bitacora/{YYYY-WW}.md`

```markdown
# Aprehensión semana {YYYY-WW}

## Conceptos cubiertos esta semana

- [Concepto 1] · status: FUERTE / PARCIAL / DÉBIL
- [Concepto 2] · status: ...

## Retrieval ciego

[lo que escribí sin mirar]

## Comparación con realidad

[gaps detectados]

## Reparación ejecutada

- Flashcards creadas: 3
- Spaced Repetition agendado: días 1, 3, 7, 30

## Feynman test

- Concepto elegido: [...]
- Audio grabado: [link]
- Veredicto: FLUYE / TRABA / JERGA

## Plan próxima semana

- [...]
```

---

## Métricas de éxito

Después de 4 semanas con el ritual:

```
✅ Identifico mis [DÉBIL] sin negarlos
✅ Ratio FUERTE / PARCIAL / DÉBIL mejora semana a semana
✅ Tengo 12+ flashcards Anki creadas en spaced repetition
✅ Mi último Feynman fluyó natural sin jerga
✅ Self-confidence calibrada (no más Dunning-Kruger)
```

---

## Calendar Invite

```
Día: viernes 17:00 (cierre de semana)
Duración: 60 min
Recurrencia: semanal
Reminder: 10 min antes
Bloque "deep work" sin notificaciones
```

Archivo: `assets/calendar-invites/aprehension-semanal.ics`

---

## Referencias

- `references/01-seis-tecnicas-cognitivas.md` §Retrieval Practice
- `katas/kata-recuperacion-ciega.md`
- `katas/kata-feynman-novato.md`
- `prompts/02-coach-system-prompt.md`
- `prompts/08-evaluator-certification.md`
- `assets/calendar-invites/aprehension-semanal.ics`

---

> **Ritual Aprehensión Semanal** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

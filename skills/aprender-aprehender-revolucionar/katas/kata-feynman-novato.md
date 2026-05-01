# Kata · Feynman a un Novato · 30 min

> Explica a un niño de 12 años. Donde uses jerga, ahí está el gap.

**Categoría**: Aprehender · técnica Feynman
**Tiempo**: 30 minutos
**Frecuencia recomendada**: 1× por semana mínimo

---

## Objetivo

Validar que entiendes un concepto **realmente**, no que solo lo procesas con fluidez.

---

## Protocolo · 30 minutos

### 0:00-0:05 · Setup

```
1. Elige 1 concepto que crees dominar
2. Imagina audiencia: niño de 12 años
   (no asume conocimiento técnico · pero es inteligente)
3. Materiales: hoja en blanco / grabadora de audio
4. Cierra todo (notas, libros, IA)
```

### 0:05-0:15 · Primer intento (10 min)

```
1. Toma la hoja
2. Escribe el concepto al tope
3. Escribe la explicación · 3 minutos sin parar
4. Audiencia: niño 12 años · sin jerga · con analogías
```

### 0:15-0:20 · Auto-revisión (5 min)

```
Lee tu explicación. Marca:

[JERGA]    → palabra técnica que un niño 12 años no entiende
[VAGO]     → concepto explicado superficialmente
[FLUIDO]   → explicación clara y accesible
[ANALOGÍA] → metáfora cotidiana exitosa
```

### 0:20-0:25 · Iteración (5 min)

```
Para cada [JERGA] y [VAGO]:
- Reemplaza con analogía cotidiana
- O explica el término técnico antes de usarlo
- Re-escribe la sección
```

### 0:25-0:30 · Test final · audio (5 min)

```
1. Toma tu explicación iterada
2. Léela en voz alta · grábate
3. Escucha el audio
4. Marca: ¿fluye natural? ¿hay tropiezos?

VEREDICTO:
✅ Fluye natural sin jerga → CONCEPTO APREHENDIDO
🟡 Fluye pero con jerga residual → AÚN PARCIAL · iterar
❌ Tropiezos / incoherencia → NO APREHENDIDO · re-estudiar
```

---

## Reglas

### Audiencia es no-negociable: niño 12 años

No "audiencia técnica junior" · no "estudiante de pregrado" · niño 12 años. Si necesitas más sofisticada, no es Feynman.

### Las analogías son de la vida cotidiana

```
✅ "La caché es como la mesa de tu cocina · cosas que usas
   seguido están a la mano · si necesitas algo raro, vas
   a la despensa (memoria principal)."

❌ "La caché optimiza el access pattern locality usando temporal
   reuse para minimizar memory access latency."
```

### Si tienes que decir jerga, defínela ANTES

```
✅ "Una API es como una puerta de entrada para que programas se
   hablen entre sí. Voy a usar la palabra API ahora..."

❌ "Las APIs RESTful con OAuth 2.0..."
```

### Si dura más de 3 minutos, simplifica

Niños 12 años no escuchan 10 minutos de explicación. Si tu explicación pasa de 3 min, está sobrecargada.

---

## Anti-patrones

| Error | Síntoma | Corrección |
|---|---|---|
| Audiencia "técnica junior" | Te permites jerga | Niño 12 años · no negociable |
| Sin analogía | Solo definiciones | Mínimo 1 analogía por explicación |
| Jerga "definida brevemente" | "API · interfaz programática..." | Reemplaza con metáfora · no defina |
| Explicación 5+ min | Sobrecarga | Comprime a 3 min |
| Sin grabar audio | No detectas tropiezos | Audio obligatorio |

---

## Variantes

### Express · 10 min

Solo 1 iteración. Útil para validación rápida, no diagnóstico profundo.

### Marathon · 60 min · audiencia humana real

```
1. Hacer kata-feynman a un colega que NO conoce el tema
2. Pedir su feedback honesto:
   - "¿En qué punto te perdí?"
   - "¿Qué término no entendiste?"
   - "¿Cuál analogía funcionó · cuál no?"
3. Iterar la explicación basado en feedback real
4. 2da pasada con humano distinto (validar transferencia)
```

---

## Métricas de éxito

```
✅ Audio fluye sin tropiezos
✅ 0 jerga residual sin definir
✅ Mínimo 2 analogías cotidianas
✅ Duración: 2-3 minutos (no más)
✅ Si humano real: entiende sin pedir aclaración
```

---

## Cuándo aplicarlo

- ✅ Cada semana en ritual de aprehensión
- ✅ Antes de cualquier presentación / QBR / cert
- ✅ Para cualquier concepto que crees dominar (validar)
- ✅ Después de aprender concepto nuevo (Workflow 1)

---

## Output esperado · ejemplo

**Concepto**: "Eventual Consistency" en sistemas distribuidos.

### Intento 1 (con jerga)

> "Eventual consistency es un modelo de consistencia donde los nodos del sistema convergen al mismo estado eventualmente, después de un período de propagación. Es un trade-off del CAP theorem que sacrifica strong consistency por availability."

→ JERGA: "modelo de consistencia", "nodos", "convergen", "trade-off", "CAP", "strong consistency", "availability".

### Iteración 1 (con analogías)

> "Imagina que tienes 3 amigos en distintas ciudades · todos llevan el mismo cuaderno con tus notas. Cuando tú agregas algo en una ciudad, esos 3 cuadernos no se actualizan al instante. Hay un momentito donde uno tiene la nueva nota y los otros 2 no. Pero después de unos segundos, los 3 cuadernos quedan iguales otra vez. Eso es 'eventual consistency': eventualmente todos se ponen al día, pero no al instante."

→ Analogías exitosas: amigos en ciudades, cuadernos, "momentito".

### Iteración 2 (test audio)

[graba en voz alta]

Si fluye natural · sin tropiezo en "ponen al día" · CONCEPTO APREHENDIDO.

---

## Referencias

- `references/01-seis-tecnicas-cognitivas.md` §Feynman
- `references/06-ciencia-cognitiva-fuentes.md` §3
- `agents/coach-aprehender.md`
- `prompts/02-coach-system-prompt.md`
- `rituals/ritual-aprehension-semanal.md`

---

> **Kata Feynman a Novato** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

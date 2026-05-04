# Bitácora de Aprehensión Semanal · v1.1.0 · Semana {YYYY-WW}

> Documenta el ritual semanal de aprehensión · qué cubriste, qué retuviste, qué falta.

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §rituals/ritual-aprehension-semanal.md.
`[CRITERIO-ACEPTACIÓN]` Cierre semanal con bitácora · sin documentar = ritual no pasó.
`[LÍMITE]` Plantilla genérica · personalizar por dominio si tu campo requiere métricas específicas.

**Semana**: [YYYY-WW]
**Fecha cierre**: [viernes]
**Tiempo total invertido**: [X minutos]

---

## Conceptos cubiertos esta semana

| # | Concepto | Workflow / Ritual | Status |
|---|---|---|---|
| 1 | [...] | [Workflow 3 / Ritual aprehensión] | [FUERTE/PARCIAL/DÉBIL] |
| 2 | | | |
| 3 | | | |

---

## Sesión de retrieval (60 min)

### 0:00-0:20 · Retrieval ciego

**Concepto elegido**: [...]

**Lo que recuperaste de memoria** (sin notas):
```
[escribe aquí lo que recordaste · sin volver a las fuentes]
```

### 0:20-0:40 · Evaluación

| Elemento recuperado | Veredicto | Detalle |
|---|---|---|
| [Elemento 1] | ✅ FUERTE | [...] |
| [Elemento 2] | 🟡 PARCIAL | [qué faltó] |
| [Elemento 3] | ❌ DÉBIL | [qué estaba mal] |

### 0:40-0:55 · Reparación

Para cada [DÉBIL]:

| Gap específico | Acción tomada | Flashcard creada | Próxima revisión |
|---|---|---|---|
| [...] | [...] | [✅/❌] | [día +1, +3, +7, +30] |

### 0:55-1:00 · Feynman test

**Concepto elegido para Feynman**: [...]

**Audiencia**: niño de 12 años · sin jerga.

**Audio grabado**: [link / path]

**Veredicto**:
- [ ] FLUYE natural · sin tropiezos · sin jerga
- [ ] TRABA · marcar para repaso
- [ ] JERGA · re-explicar con analogías

---

## Quiz de la semana (si aplica)

**Nivel evaluado**: [Foundations / Intermediate / Advanced / Expert]
**Score**: __/5

**Top 3 gaps detectados**:
1. [...]
2. [...]
3. [...]

---

## Spaced Repetition agendado

Items con próxima revisión:

| Concepto | Días desde aprendizaje | Próxima revisión | Calendar |
|---|---|---|---|
| [...] | 0 | [+1 día] | ✅ |
| [...] | 3 | [+7 días] | ✅ |
| [...] | 7 | [+14 días] | ✅ |

---

## Reflexión semanal

### Lo que mejor funcionó
[técnica que más rindió · ej. "Feynman me detectó 2 gaps que no veía"]

### Lo que costó
[concepto / técnica que aún no fluye · ej. "Vector clocks · sigo sin internalizar"]

### Cambio para próxima semana
[ajuste al protocolo · ej. "agregar 30 min de Elaboration sobre vector clocks"]

---

## Estado del tema

**Tema**: [...]
**Escala actual (auto-eval)**: [N]
**Escala objetivo**: [M]
**Horas invertidas semana**: [X]
**Horas acumuladas total**: [Y / Z target]
**% progreso**: [Y/Z * 100%]

---

## Plan próxima semana

```
LUNES (60 min) · [tema]
MARTES (60 min) · [tema]
MIÉRCOLES (60 min) · [tema]
JUEVES (60 min) · [tema]
VIERNES (60 min) · cierre + bitácora
```

---

## Comandos útiles

```bash
# Retrieval ciego automatizado
python ~/.claude/skills/aprender-aprehender-revolucionar/scripts/retrieval_session.py \
  --concepto "[concepto]" --tiempo 15

# Actualizar progreso
python ~/.claude/skills/aprender-aprehender-revolucionar/scripts/progress_tracker.py \
  --add-horas "[tema]" --horas 5
```

---

> **Plantilla Bitácora Aprehensión** del Playbook Aprender · Aprehender · (R)Evolucionar v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

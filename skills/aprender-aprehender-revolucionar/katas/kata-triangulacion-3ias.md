# Kata · Triangulación de 3 IAs · 30 min

> Misma pregunta · 3 IAs distintas · contradicciones = oro.

**Categoría**: Aprender · validación de fuentes
**Tiempo**: 30 min
**Frecuencia**: cada Workflow 1 · cada research importante

---

## Objetivo

Validar info IA con triangulación · detectar omisiones, sesgos y hallucinations al cruzar 3 IAs.

---

## Protocolo · 30 min

### 0:00-0:05 · Preparar pregunta única

Define una pregunta clara, idéntica para las 3 IAs:

```
"¿Cuáles son los [N] [conceptos/autores/papers] más importantes
en [DOMINIO]? Cita fuentes primarias."

O:

"Define [CONCEPTO] y da 2 ejemplos reales de aplicación."

O:

"¿Cuáles son las 3 controversias actuales en [CAMPO]?
Para cada una, presenta argumentos de ambos lados."
```

### 0:05-0:20 · Ejecutar en 3 IAs (15 min)

```
- ChatGPT (5 min · pegar pregunta · guardar respuesta)
- Claude (5 min · misma pregunta · guardar)
- Gemini o Perplexity (5 min · misma · guardar)

NO modifiques la pregunta entre IAs · debe ser idéntica.
```

### 0:20-0:30 · Tabla de triangulación

Asset: `assets/plantilla-triangulacion.md`.

```
| Item | ChatGPT | Claude | Gemini | Veredicto |
|---|---|---|---|---|
| Concepto A | ✅ | ✅ | ✅ | CONFIRMED · 3/3 |
| Autor X · 2018 | ✅ | ❌ | ✅ | REVISAR · Claude no |
| Paper Y | ✅ | ❌ | ❌ | SOSPECHOSO · 1/3 |
| Controversia Z | ❌ | ✅ | ✅ | CONFIRMED · 2/3 |
```

**Veredictos**:
- 3/3 → CONFIRMED · alta confianza
- 2/3 → REVISAR · validar fuente primaria
- 1/3 → SOSPECHOSO · alta probabilidad de hallucination o nicho
- 0/3 con contradicciones → CONTRADICCIÓN · investiga · puede ser ORO (debate del campo)

---

## Reglas

### Pregunta IDÉNTICA en las 3

No mejorar entre IAs. La triangulación válida exige misma pregunta.

### Captura las 3 respuestas COMPLETAS

No editar · no resumir antes de comparar. Las omisiones precisamente son las que detecta este kata.

### Las contradicciones son ORO, no problema

Cuando las 3 IAs dicen cosas distintas:
- No es ruido
- Es señal de que el campo tiene debate o nicho
- Investigar manualmente la fuente primaria

---

## Output esperado

### Caso A · Coincidencia alta

3/3 acuerdan en 80%+ items → BoK confiable · proceder con confianza.

### Caso B · Coincidencia media

3/3 acuerdan en 50-80% → BoK útil pero con áreas a verificar manual.

### Caso C · Coincidencia baja

3/3 acuerdan en <50% → 2 escenarios:
1. **Tema controversial** · cada IA representa un lado · oro
2. **Tema nicho** · IAs improvisan · alta probabilidad de hallucination

---

## Anti-patrones

| Error | Corrección |
|---|---|
| Solo 1 IA "confiable" | Triangular obligatorio |
| Pregunta diferente entre IAs | Misma pregunta exacta |
| Aceptar 2/3 como verdad | Validar fuente primaria |
| Descartar contradicciones | Investigar · son señal del campo |

---

## Combo con Prompt #4

Después de triangular, ejecuta Prompt #4 (Cross Fact-Check) en una **4ª IA** independiente:
- Pegar las 3 respuestas
- Pedir veredicto por claim
- Eliminar HALLUCINATIONS confirmados

---

## Referencias

- `prompts/01-research-blueprint.md`
- `prompts/04-cross-fact-check.md`
- `references/04-anti-patrones-y-trampas.md` §Single-AI BoK
- `agents/auditor-cruzado.md`
- `assets/plantilla-triangulacion.md`

---

> **Kata Triangulación 3 IAs** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

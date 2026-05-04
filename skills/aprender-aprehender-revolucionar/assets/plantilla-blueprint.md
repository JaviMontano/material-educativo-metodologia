# Plantilla · Research Blueprint · v1.1.0

> Template del Workflow 1 · output del Prompt #1 · base del Body of Knowledge.

**Reemplaza** los items entre `[corchetes]` con tu contenido. Borra esta nota cuando termines.

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Workflow 1 + Prompt #1.
`[LÍMITE]` Plantilla genérica · si tu dominio requiere campos específicos (ej. compliance regulatoria), agregar sección custom antes de la sección 4.
`[CRITERIO-ACEPTACIÓN]` Output mínimo viable: 7 secciones llenas con datos reales · NO dejar `[corchetes]` literales.

---

## 1 · Declaración de intención

**Tema**: [tema específico · ej. "Sistemas Distribuidos"]
**Por qué lo aprendo**: [objetivo medible · ej. "diseñar arquitectura para 10M usuarios en mi empresa"]
**Escala actual (auto-eval)**: [0-9 honesta]
**Escala objetivo**: [0-9]
**Tiempo bloqueado**: [4h Express / 20h Sprint / 64h Marathon]
**Hipótesis inicial** (lo que crees ahora · será refinado): [...]

---

## 2 · Body of Knowledge (BoK)

### Definición precisa
[2-3 frases · sin marketing]

### Subtemas principales
1. [Subtema 1] · [breve descripción]
2. [Subtema 2]
3. [Subtema 3]
4. [Subtema 4]
5. [Subtema 5]

### Conexiones interdisciplinarias
- Con [campo A]: [cómo se relacionan]
- Con [campo B]: [cómo se relacionan]
- Con [campo C]: [cómo se relacionan]

### Estado del arte (2024-2026)
[Avances recientes · 3-5 viñetas]

---

## 3 · Glosario mínimo (15-30 términos)

| # | Término | Definición (1 frase) | Por qué importa | Tag |
|---|---|---|---|---|
| 1 | [Término] | [definición] | [importancia] | [DOC] |
| 2 | | | | [DOC] |
| 3 | | | | [INFERENCIA] |
| ... | | | | [SUPUESTO] |

**Tags**:
- `[DOC]` — fuente verificable identificada
- `[INFERENCIA]` — deducción lógica
- `[SUPUESTO]` — pendiente de validar

---

## 4 · Concept Map (mermaid)

```mermaid
mindmap
  root([TU TEMA])
    Subtema 1
      Concepto 1.1
      Concepto 1.2
      Concepto 1.3
    Subtema 2
      Concepto 2.1
      Concepto 2.2
    Subtema 3
      Concepto 3.1
    Subtema 4
      Concepto 4.1
    Subtema 5
      Concepto 5.1
```

---

## 5 · Fuentes primarias

| # | Tipo | Autor · Año | Título | Por qué importa | Validado |
|---|---|---|---|---|---|
| 1 | Paper | [Autor · YYYY] | [título] | [razón] | ✅/❌ |
| 2 | Libro | | | | |
| 3 | RFC/Estándar | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Validado**: ¿el documento original existe? (verificar en Google Scholar · DBLP · etc.)

---

## 6 · Autoridades del campo

- [Nombre 1] · [por qué es referente · contribución específica]
- [Nombre 2] · [...]
- [Nombre 3] · [...]
- [Nombre 4] · [...]
- [Nombre 5] · [...]

---

## 7 · Controversias / debates abiertos

### Controversia 1: [Nombre]
- **Lado A** dice: [argumento principal con autor]
- **Lado B** dice: [argumento opuesto con autor]
- **Mi posición preliminar** (con caveat de Escala 1): [...]

### Controversia 2: [...]
[mismo formato]

### Controversia 3: [...]
[mismo formato]

---

## 8 · Direcciones futuras

[Hacia dónde va el campo en próximos 3-5 años · 3-5 viñetas]

---

## 9 · Ruta de aprendizaje para mi objetivo

Dado mi nivel ([Escala N]) y objetivo ([X]):

### Subset prioritario del BoK
[De los 5 subtemas, los 2-3 más relevantes para mi objetivo:]
1. [...]
2. [...]
3. [...]

### Hitos verificables

| Tiempo | Hito | Validación |
|---|---|---|
| 4h | [...] | [Quiz Nivel 1 · Prompt #8] |
| 20h | [...] | [Quiz Nivel 2 + 1 mock] |
| 64h | [...] | [Mock LEAN HIRE+ · Feynman a humano] |

### Estimación de horas

| Estimación | Horas | Confianza |
|---|---|---|
| Optimista | [X] | [%] |
| Realista | [Y] | [%] |
| Pesimista | [Z] | [%] |

---

## 10 · Triangulación

> Resultado de Workflow 1 · Prompt #1 ejecutado en 3 IAs.
> Tabla completa: `triangulacion-{tema}.md` (ver `assets/plantilla-triangulacion.md`)

**Resumen**:
- 🟢 CONFIRMED (3/3): X items
- 🟡 REVISAR (2/3): Y items
- 🔴 SOSPECHOSO (1/3): Z items

**Items sospechosos eliminados/verificados manualmente**:
- [...]

---

## 11 · Quality gate G-Aprender

```
[ ] BoK triangulado en 3+ IAs
[ ] Glosario ≥15 términos
[ ] Concept map mermaid generado
[ ] ≥3 fuentes primarias verificadas
[ ] Auditor cruzado (Prompt #4) sin HALLUCINATION crítico
[ ] NotebookLM configurado con coach activo
[ ] Primera sesión con coach exitosa (5 preguntas test)
```

**Veredicto**: [✅ Pasado · avanzar a Workflow 2] / [❌ Faltan criterios]

---

## 12 · Próximo paso

- [ ] Workflow 2 (Explorador) · 4-20h adicionales
- [ ] Pausa · retomar en [fecha]
- [ ] Suficiente con Escala 1 · cerrar el tema

**Fecha próxima sesión**: [...]

---

> **Plantilla Blueprint** del Playbook Aprender · Aprehender · (R)Evolucionar v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

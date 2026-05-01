# Plantilla · Tabla de Triangulación

> Output del kata-triangulacion-3ias · cruzar 3+ IAs sobre la misma pregunta.

**Tema**: [TU TEMA]
**Pregunta**: [pregunta idéntica enviada a las 3 IAs]
**Fecha**: [...]
**IAs comparadas**: ChatGPT · Claude · Gemini (o las que uses)

---

## Tabla principal

| Item / Claim | ChatGPT | Claude | Gemini | Veredicto |
|---|:---:|:---:|:---:|---|
| [Item 1] | ✅ | ✅ | ✅ | 🟢 CONFIRMED · 3/3 |
| [Item 2] | ✅ | ✅ | ❌ | 🟡 REVISAR · 2/3 |
| [Item 3] | ✅ | ❌ | ❌ | 🔴 SOSPECHOSO · 1/3 |
| [Item 4] | ❌ | ✅ | ✅ | 🟡 REVISAR · 2/3 |
| [Item 5] | ✅ vs A | ✅ vs B | ✅ vs C | ⚡ CONTRADICCIÓN · cada IA dice cosa distinta |

---

## Veredictos

### 🟢 CONFIRMED · alta confianza
Items donde las 3 IAs coinciden. Probable verdad.

**Acción**: usar con confianza · validar fuente primaria si es claim crítico para uso público.

### 🟡 REVISAR · 2/3
Items donde 2 IAs coinciden, 1 omite o difiere.

**Acción**: validar manualmente la fuente primaria. La omisión puede ser:
- (a) Edge case real que esa IA no cubrió
- (b) Hallucination de las 2 que coinciden

### 🔴 SOSPECHOSO · 1/3
Items que aparecen en 1 sola IA.

**Acción**: alta probabilidad de hallucination o nicho. Validar manualmente o eliminar.

### ⚡ CONTRADICCIÓN · ORO
Items donde las 3 IAs dicen cosas distintas.

**Acción**: NO descartes. Investiga · es señal de **debate del campo**:
- ¿Es realmente controversial?
- ¿Cuál es la evidencia primaria de cada lado?
- Tu opinión informada al final (con caveat de escala)

---

## Ejemplo aplicado · "¿Quiénes son los 3 autores fundacionales de Sistemas Distribuidos?"

| Item | ChatGPT | Claude | Gemini | Veredicto |
|---|:---:|:---:|:---:|---|
| Leslie Lamport | ✅ | ✅ | ✅ | 🟢 CONFIRMED |
| Eric Brewer | ✅ | ✅ | ✅ | 🟢 CONFIRMED |
| Edsger Dijkstra | ✅ | ❌ | ✅ | 🟡 REVISAR · Claude no lo lista |
| Pat Helland | ✅ | ❌ | ❌ | 🔴 SOSPECHOSO · 1/3 |
| Werner Vogels | ❌ | ✅ | ✅ | 🟡 REVISAR · ChatGPT no |
| Jim Gray | ❌ | ✅ | ❌ | 🔴 SOSPECHOSO · 1/3 |

**Análisis**:
- 🟢 Lamport y Brewer: claros referentes · usar con confianza
- 🟡 Dijkstra: probable referente · Claude debió omitirlo · validar
- 🔴 Pat Helland: probable hallucination o nicho específico · investigar
- 🟡 Werner Vogels: relevante en industria · ChatGPT debió incluirlo
- 🔴 Jim Gray: 1/3 · Claude pudo confundir con Jim Hamilton · validar

**Acción**: incluir Lamport, Brewer, Dijkstra, Vogels en lista final. Investigar Helland y Gray manualmente.

---

## Próximo paso

Después de consolidar la triangulación:

1. **Items SOSPECHOSO** + **REVISAR críticos**: ejecutar Prompt #4 (Cross Fact-Check) en una 4ª IA independiente
2. **Items CONFIRMED**: incluir en BoK final con confianza
3. **Items CONTRADICCIÓN**: agregar a tu lista de "controversias del campo" (Workflow 2)

---

## Resumen ejecutivo

```
Total claims comparadas: [N]
- 🟢 CONFIRMED: X (X%)
- 🟡 REVISAR: Y (Y%)
- 🔴 SOSPECHOSO: Z (Z%)
- ⚡ CONTRADICCIÓN: W (W%)

Confianza global del BoK: [ALTA/MEDIA/BAJA]

Acciones de remediación:
- [ ] Eliminar X items SOSPECHOSO sin fuente verificable
- [ ] Verificar manualmente Y items REVISAR críticos
- [ ] Documentar Z controversias del campo
```

---

## Generar automáticamente

```bash
python ~/.claude/skills/aprender-aprehender-revolucionar/scripts/triangulation.py \
  --files chatgpt.md claude.md gemini.md \
  --output triangulacion-{TU_TEMA}.md
```

---

> **Plantilla Triangulación** del Playbook Aprender · Aprehender · (R)Evolucionar v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

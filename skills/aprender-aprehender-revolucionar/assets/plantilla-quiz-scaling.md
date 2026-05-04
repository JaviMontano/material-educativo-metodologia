# Plantilla · Quiz Progresivo · 4 Niveles · v1.1.0

> Output del Prompt #8 · validación de Escala 1-4 con preguntas abiertas.

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Prompt #8 Evaluator + Workflow 3 §Quizzes.
`[CRITERIO-ACEPTACIÓN]` Quiz Nivel N pasado = ≥4/5 abiertas (NO recognition multiple-choice).
`[LÍMITE]` Score 3/5 = NO pasa · 3/5 marcado como "OK" es Escala N-0.5 disfrazada.
`[TRADE-OFF]` Quiz auto-administrado + IA evaluadora · sin humano se pierde 30% del rigor.

**Tema**: [TU TEMA]
**Certificación o objetivo**: [...]
**Fecha de evaluación**: [...]

---

## Nivel 1 · FOUNDATIONS (Escala 1-2)

5 preguntas básicas · 80% open-ended · 20% multiple choice si concepto lo amerita.

| # | Pregunta | Tu respuesta | Veredicto | Razón |
|---|---|---|---|---|
| 1 | [Pregunta concepto core] | [...] | [CORRECTA/PARCIAL/INCORRECTA] | [...] |
| 2 | [Pregunta terminología] | | | |
| 3 | [Pregunta aplicación simple] | | | |
| 4 | [Pregunta conceptual + ejemplo] | | | |
| 5 | [Pregunta integradora] | | | |

**Score**: __ / 5
**Veredicto**: [✅ AVANZAR a Nivel 2 (4/5+)] / [🔄 REFUERZO (3/5)] / [⏸ STOP, vuelve a Workflow 1 (<3/5)]

---

## Nivel 2 · INTERMEDIATE (Escala 2-3)

5 preguntas · aplicación, casos comunes, trade-offs.

| # | Pregunta | Tu respuesta | Veredicto | Razón |
|---|---|---|---|---|
| 1 | [Caso de uso real] | | | |
| 2 | [Trade-off principal] | | | |
| 3 | [Aplicar concepto a problema] | | | |
| 4 | [Comparación entre 2 enfoques] | | | |
| 5 | [Pregunta interleaved · 2 subtemas] | | | |

**Score**: __ / 5
**Veredicto**: [✅ AVANZAR a Nivel 3] / [🔄 REFUERZO] / [⏸ STOP]

---

## Nivel 3 · ADVANCED (Escala 3-4)

5 preguntas · casos complejos, decisiones bajo restricción, 1 trampa.

| # | Pregunta | Tu respuesta | Veredicto | Razón |
|---|---|---|---|---|
| 1 | [Diseño de sistema · trade-offs] | | | |
| 2 | [Trouble-shoot · qué falló y por qué] | | | |
| 3 | [Trade-off cross-cutting] | | | |
| 4 | [Caso edge no obvio] | | | |
| 5 | [⚠️ TRAMPA · premisa falsa común] | | | |

**Score**: __ / 5
**Veredicto**: [✅ AVANZAR a Nivel 4] / [🔄 REFUERZO]
**Si pasaste**: estás cerca de Escala 3 (Iniciado)

---

## Nivel 4 · EXPERT (Escala 4+)

5 preguntas · edge cases, debates abiertos, innovación.

| # | Pregunta | Tu respuesta | Veredicto | Razón |
|---|---|---|---|---|
| 1 | [Caso novel · cómo abordarías] | | | |
| 2 | [Debate del campo · tu posición + argumentos] | | | |
| 3 | [Predicción futuro 3-5 años] | | | |
| 4 | [Cross-disciplina · cómo conecta con otro campo] | | | |
| 5 | [Innovación · qué propondrías para mejorar] | | | |

**Score**: __ / 5
**Veredicto**: [✅ Listo para Escala 4+ / certificación] / [🔄 Áreas a profundizar]

---

## Resumen de evaluación

```
Niveles aprobados: [1, 2, 3, 4]
Escala diagnóstica IA: [N]
Tu auto-evaluación: [N]
Diferencia: [±N escalas]

🚨 Si diferencia >1 escala:
- Si AUTO > IA → Dunning-Kruger · sobreestimas
- Si IA > AUTO → underestimas · ten más confianza
- Documentar y revisar
```

## Top 3 gaps específicos detectados

1. [Área 1 · qué falló · cómo cerrar]
2. [Área 2]
3. [Área 3]

## Plan de remediación

| Gap | Acción | Tiempo estimado | Recurso |
|---|---|---|---|
| [Gap 1] | [estudio dirigido + Feynman] | [Xh] | [reference / kata] |
| [Gap 2] | | | |
| [Gap 3] | | | |

## Próxima evaluación

**Cuándo**: [+1 semana / +2 semanas según gravedad]
**Foco**: [niveles fallados]

---

## Reglas de evaluación

- 80% preguntas open-ended (no multiple choice)
- Sin pistas durante la pregunta
- Sin re-intentar antes de revelar la respuesta
- Cerrar todas las fuentes (notas, web, IA paralela)

---

## Generar quiz automáticamente

```bash
# Para certificación oficial:
python ~/.claude/skills/aprender-aprehender-revolucionar/scripts/notebook_config_generator.py \
  --arquetipo evaluador \
  --certificacion "AWS SAA-C03" \
  --nivel "score >800/1000"

# Para validación general:
pbcopy < ~/.claude/skills/aprender-aprehender-revolucionar/prompts/08-evaluator-certification.md
```

---

> **Plantilla Quiz Scaling** del Playbook Aprender · Aprehender · (R)Evolucionar v2.0.0 · MetodologIA · CC BY-NC-SA 4.0

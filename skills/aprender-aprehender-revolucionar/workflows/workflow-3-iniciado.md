# Workflow 3 · El Iniciado · 20-64 h

Transición Escala 2 (Explorador) → Escala 3 (Iniciado). Defender sin notas, ante hostil, bajo presión. Culminación. v1.1.0.

| Concepto | Valor |
|---|---|
| Agente | `coach-aprehender` |
| Tiempo nominal | Sprint 20 h (4 sem · 1 h × 5 días) · Marathon 64 h (16 sem) |
| Pre-requisito | Workflow 2 completo · G-Explorador pasado |
| Output mandatory | Feynman sin notas · Quiz nivel 3 4/5 · Mock LEAN HIRE+ · 3 conceptos hostiles defendidos · self+IA ±1 escala |
| Gate al cierre | G-Aprehender (7 criterios binarios) |

`[FUENTE-PRIMARIA]` Playbook v2.0.0 §Workflow 3 + §6 técnicas cognitivas.

## Contrato del workflow

| Hace | No hace |
|---|---|
| Convierte conocimiento (Aprender) en conocimiento defendible (Aprehender) | Lleva a Escala 4+ (eso requiere práctica en producción real, no método) |
| Aplica las 6 técnicas cognitivas de manera secuenciada | Promete éxito en QBR/cert · genera capacidad, no garantiza resultado |
| Detecta Dunning-Kruger via diff self vs IA | Reemplaza la validación humana real (mock con humano sigue siendo necesaria) |
| Programa Spaced Repetition post-Workflow | Mantiene la escala automáticamente · requiere disciplina del usuario |

`[LÍMITE]` Si tema requiere skills físicas o herramientas especializadas (ej. operar un MRI, soldar) la skill no aplica · son dominios kinestésicos.
`[LÍMITE]` Si humano no está disponible para Feynman real (Semana 4) · sustituir con coach NotebookLM en modo audiencia hostil. No es 100% equivalente · el humano detecta mejor las inconsistencias narrativas.

## Sprint 20 h · 4 semanas

### Semana 1 · Vocabulario activo

Objetivo: dominar glosario completo con retrieval ciego.

| Día | Actividad (60 min) | Output |
|---|---|---|
| Lun | Retrieval ciego de los ~50 términos · marcar [FUERTE/PARCIAL/DÉBIL] | Lista de 5 [DÉBIL] focus |
| Mar | Estudiar 5 [DÉBIL] con Elaboration · cerrar con retrieval ciego | Definiciones de memoria |
| Mié | Concept map ciego · comparar con real · identificar gaps mentales | Lista de gaps mentales |
| Jue | Feynman a 1 concepto · audio 3 min · iterar 1× | Audio + lista de jerga usada |
| Vie | Quiz Nivel 1 (Prompt #8 Foundations) · score esperado 4/5 | Score documentado · Spaced agendado |

`[CRITERIO-ACEPTACIÓN]` Si <3 [FUERTE] de 5 [DÉBIL] al cierre Vie · Semana 2 sustituye Trade-offs por refuerzo de glosario.

### Semana 2 · Aplicación + trade-offs

Objetivo: aplicar conceptos a casos reales · entender trade-offs.

| Día | Actividad | Output |
|---|---|---|
| Lun | 5 casos de uso reales del dominio · ¿qué subtema aplica? ¿qué trade-off? | Tabla casos × subtemas |
| Mar | Profundizar trade-off principal #1 · paper foundational + opinión propia · Feynman a ambos lados | Audio 5 min trade-off |
| Mié | Trade-off principal #2 · mismo formato | Audio 5 min |
| Jue | Quiz Nivel 2 (Prompt #8 Intermediate) · 4/5 esperado | Score |
| Vie | Concept map con anotaciones de trade-off por nodo · audio síntesis 5 min | Concept map v2 + audio |

`[CASO-BORDE]` Si los trade-offs principales son ideológicos sin solución técnica (ej. monolito vs microservicios), no forzar consenso · documentar tu posición con condicionales: "elijo X cuando [condición]".

### Semana 3 · Defensa preliminar

Objetivo: defender bajo presión simulada.

| Día | Actividad | Output |
|---|---|---|
| Lun | Mock interview hostil 30 min (Prompt #9) | 3 preguntas que te derribaron · documentadas |
| Mar | Cierre de gaps · respuestas robustas con números, ejemplos, trade-offs explícitos | 3 respuestas modelo |
| Mié | Mock #2 · validar las 3 anteriores defendidas · identificar 3 nuevas debilidades | Lista nuevas debilidades |
| Jue | Feynman a 3 conceptos críticos · audio 5 min cada uno | 3 audios |
| Vie | Quiz Nivel 3 (Prompt #8 Advanced) · 4/5 = cerca de Escala 3 | Score |

`[TRADE-OFF]` Mock con coach amable se siente cómodo pero no entrena para realidad. Prompt #9 es explícitamente hostil · si tu coach lo está endulzando, el rigor se pierde y entrarás a la realidad sin estrés probado.

### Semana 4 · Validación final

Objetivo: validar Escala 3 alcanzada.

| Día | Actividad | Output |
|---|---|---|
| Lun | Mock final 60 min (Prompt #9) · veredicto STRONG/LEAN HIRE | Veredicto |
| Mar | Si LEAN HIRE+: Spaced Repetition · Si <LEAN HIRE: 4 h refuerzo en gap principal | Plan ajustado |
| Mié | Feynman a humano real · 30 min · feedback honesto · identificar dónde no entendió | Feedback humano |
| Jue | Quiz Nivel 4 opcional (solo target Escala 4+) · NO requerido para cerrar W3 | Score opcional |
| Vie | Cierre formal · documentar · Spaced Repetition días 30/60/90 · actualizar `.aprender-state.json` | `cierre-w3.md` |

`[CASO-BORDE]` Humano no disponible Mié · alternativas: (a) mock con NotebookLM en modo audiencia hostil, (b) grabar tu Feynman y revisarlo 24 h después con ojos frescos, (c) postergar Mié a próxima sem.

## Marathon 64 h · 16 semanas (resumen)

Versión expandida:
- 4 sesiones × 1 h × 16 sem = 64 h
- Cada técnica cognitiva con 2-3 sesiones dedicadas
- Práctica deliberada con feedback humano (3 humanos distintos · no solo IA)
- Dual coding completo (NotebookLM genera podcast, video, infografía)
- Detalle: `rituals/ritual-practica-deliberada.md`

`[TRADE-OFF]` Marathon requiere 16 semanas de compromiso · alta tasa de abandono después de sem 5-6. Mitigación: ritual semanal estricto + accountability con un peer (mismo ritual ese día).

## Mapeo · 6 técnicas × 4 semanas

| Sem | Retrieval | Spaced | Feynman | Interleaving | Elaboration | Dual Coding |
|---|---|---|---|---|---|---|
| 1 | ✅ glosario | ✅ DÉBIL items | ✅ 1 concepto | — | ✅ ¿por qué? | ✅ concept map |
| 2 | ✅ casos | ✅ continúa | ✅ trade-offs | ✅ casos mixed | ✅ relaciones | ✅ audio |
| 3 | ✅ preguntas hostiles | ✅ continúa | ✅ 3 conceptos | ✅ mock | ✅ contradicciones | ✅ explicaciones |
| 4 | ✅ mock final | ✅ programado | ✅ a humano | ✅ quiz nivel 4 | ✅ síntesis | ✅ todos modos |

## Quality gate G-Aprehender

```
[ ] Feynman sin notas grabado · 5 min · audiencia novato comprende
[ ] Quiz Nivel 3 aprobado: ≥4/5 (Prompt #8 Advanced)
[ ] Mock interview pasa LEAN HIRE+ (Prompt #9)
[ ] 3 conceptos críticos defendidos ante hostil sin trabarse
[ ] Self-assessment + IA-assessment coinciden ±1 escala
[ ] Plan Spaced Repetition activo (días 30, 60, 90 post-cierre)
[ ] `.aprender-state.json` actualizado · escala_actual: 3
```

`[CRITERIO-ACEPTACIÓN]` 7/7. Si falla 1 · Workflow 3 extra de 1-2 sem en gaps específicos · NO declarar Escala 3 prematuramente.

## Anti-patrones top-3 graves

| # | Anti-patrón | Detección | Antídoto |
|---|---|---|---|
| 1 | Saltar Feynman | "Ya lo entiendo, no necesito" | Forzar · Feynman es el filtro real · sin él entras a QBR sin saber qué no sabes |
| 2 | Mock con coach amable | Mock pasa fácil sin presión | Re-instruir Prompt #9 · explícitamente hostil · sin halagos preventivos |
| 3 | Pasar Quiz Nivel 3 con 3/5 y avanzar | Score 3/5 marcado como "OK" | Regla 4/5 mandatory · 3/5 = repaso obligatorio · avanzar con 3/5 = Escala 2.5 disfrazada de 3 |

## Cierre Workflow 3 · template

```markdown
## Workflow 3 · Cerrado · Escala 3 ALCANZADA

Tema: [...]
Tiempo total invertido: X h (W1 + W2 + W3)
Fecha cierre: [hoy]

Validaciones pasadas:
[x] Feynman grabado · sin notas · 5 min
[x] Quiz Nivel 3 · 4-5/5
[x] Mock interview · LEAN HIRE+
[x] 3 conceptos defendidos ante hostil
[x] Self+IA alignment ±1 escala
[x] Feedback humano positivo

Próximos pasos:
- Spaced Repetition día 30: [fecha]
- Spaced Repetition día 60: [fecha]
- Spaced Repetition día 90: [fecha]
- Si aplicó al evento original (QBR/cert/interview): resultado documentado

Estado: `.aprender-state.json` actualizado · escala_actual=3 · horas_invertidas=X
```

## Referencias cruzadas

- `agents/coach-aprehender.md`
- `references/01-seis-tecnicas-cognitivas.md`
- `references/03-diez-escalas-maestria.md` §Escala 3
- `prompts/02 · 08 · 09 · 10`
- `katas/kata-feynman-novato.md` · `kata-defensa-hostil.md` · `kata-recuperacion-ciega.md`
- `rituals/ritual-aprehension-semanal.md` · `ritual-practica-deliberada.md`

> v1.1.0 · CC BY-NC-SA 4.0 · MetodologIA · `[FUENTE-PRIMARIA]` Playbook v2.0.0

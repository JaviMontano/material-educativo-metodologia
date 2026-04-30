# Changelog · Cartilla v1.5 · 2026-04-29 · Editorial pass + voseo→tú + retiro Tree of Prompts

## Voseo → tú panregional (decisión bloqueada plan §3)

Aplicado pase sistemático: 80+ formas de voseo (imperativos, indicativos, pronombres) reemplazadas por tú panregional, tanto en cuerpo HTML como en JSON modal data embebido (135 patches en modales).

Excepción: el dataset `window.curatedPrompts` (30 SPECs importados de la biblioteca) queda intocable.

| Categoría | Antes (voseo) | Después (tú) |
|---|---|---|
| Imperativos | Pegá · Marcá · Aplicá · Diseñá · Probá · Auditá · Calibrá · Calificá · Identificá · Reescribí · Elegí · Tomá · Listá · Detectá · Etiquetá · Construí · Mapealo · Escribí · Generá · Agendá · Saltá · Volvé · Seguí · Corregí · Leé · Definí · Capitalizá · Decidí · Pedí · Pensá · Pedile · Devolveme · Resumí | Pega · Marca · Aplica · Diseña · Prueba · Audita · Calibra · Califica · Identifica · Reescribe · Elige · Toma · Lista · Detecta · Etiqueta · Construye · Mapéalo · Escribe · Genera · Agenda · Salta · Vuelve · Sigue · Corrige · Lee · Define · Capitaliza · Decide · Pide · Piensa · Pídele · Devuélveme · Resume |
| Indicativos | dominás · operás · empezás · tenés · sabés · querés · usás · podés · necesitás · invocás · venís · recorrés · encadenás · apilás · ejecutás · declarás · auditás · valorás · trabajás · manejás · vivís · cambiás · llegás · ganás | dominas · operas · empiezas · tienes · sabes · quieres · usas · puedes · necesitas · invocas · vienes · recorres · encadenas · apilas · ejecutas · declaras · auditas · valoras · trabajas · manejas · vives · cambias · llegas · ganas |
| Pronombres | vos también · con vos · en vos | tú también · contigo · en ti |

## Tree of Prompts retirado (era error)

- § 14 lead: "9 formas → 8 formas", "8 más → 7 más", "Chaining/Tree of Prompts/Stacking → Chaining/Stacking"
- § 14 grupo B: 3 cards → 2 cards (Prompt Chaining + Prompt Stacking)
- TOC: "9 formas → 8 formas"
- Modal `orch-tree-prompts` eliminado del JSON (170 → 169 entries)
- Cuerpo HTML cero referencias a Tree of Prompts

## Pase editorial — concisión y progresividad

**Hero + § 1 storytelling:**
- Lead reescrito: 30% más conciso, voz directa
- Card "oráculo amable": consistencia de sujeto (la IA como sujeto)
- Nivel 1 marker: preguntas en lugar de condicionales (mejor progresividad)

**Nivel 2 (Método):**
- Marker: "el método P.I.V.O.T.E." → "el método operativo" + breadcrumb completo (framework → pipeline → contratos → rúbrica → trazabilidad → metacognición)
- § 8 atributos lead: "checkable" (spanglish) → "verificable"
- § 9 PIVOTE callout: condensado a "PIVOTE = por qué; pipeline /0-/9 = cómo"
- § 9.5 pipeline lead: 30% más corto, voz directa con conceptos clave en bold
- § 10 cláusulas: paridad ES/EN agregada a 12 cards body texts (antes solo en español)
- § 11 ENTRUSTED+: paridad ES/EN agregada a 9 títulos (Explicitness · No-hallucination · etc.)
- § 12 etiquetas: paridad ES/EN agregada a 10 cards body texts; lead más conciso
- § 13 DSVSR: ya conciso desde v1.3, sin cambios

**§ 9.5 pipeline 10 pasos /0-/9:**
- **Bug crítico cerrado**: step-titles y body párrafos estaban solo en español. Ahora bilingüe ES/EN completo en los 10 pasos
- Concisión: "Antes de pedir algo serio, le decís..." → "Le dices a la IA con qué cabeza pensar"
- Verbos consistentes en imperativo tú panregional

**Nivel 3 (Avanzado):**
- § 14 lead reescrito explicando intra-prompt vs orquestación multi-prompt
- § 15 lead: "Lo que diferencia un operador con criterio de un usuario casual" → "El piso del operador con criterio. Cada técnica resuelve calidad, seguridad o escala."
- § 16 system prompts lead: cross-link explícito a prompt stacking (§ 14)
- § 17 metaprompting lead: 20% más corto
- § 17.5 text expanders: ya conciso desde v1.4

**Nivel 4 (Práctica):**
- **Bug crítico cerrado**: 12 cards de § 20 prácticas (titulos h4 + body p + criterio de éxito) estaban solo en español. Ahora bilingüe ES/EN completo
- § 24 FAQ: ya bilingüe desde v1.3, sin cambios

## Métricas

- HTML: 350 KB → **358 KB** (+8 KB · +2%) — mayoría es paridad ES/EN agregada
- JSON modales: 127 KB → 124 KB (después de retirar Tree of Prompts y aplicar voseo→tú)
- Modales: 170 → **169** (retirado orch-tree-prompts)
- TOC: 25 entradas (sin cambios)
- Voseo residual en HTML: **0** (excepto dataset curatedPrompts intocable)
- Tree of Prompts residual: **0**

## Pendiente para v1.6 (no en este commit)

Plan de extracción de 4 archivos previos identificado. Incluye:
- 10-item Universal Rubric del complementario-v4
- 5-Level Exercise Progression de la versión mobile
- Tríada de Transformación pathway
- Few-Shots library methodology
- Guardrails & Test Cases framework

Pendiente decisión Javier: priorizar cuáles importar.

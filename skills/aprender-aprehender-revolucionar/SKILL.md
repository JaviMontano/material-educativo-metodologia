---
name: aprender-aprehender-revolucionar
version: 1.2.0
description: >
  Use proactively when the user asks to "aprender un tema", "ponerme al día",
  "hacer deep research", "preparar una certificación, entrevista o QBR",
  "configurar NotebookLM", "comprobar una investigación" or "auditar qué
  conocimientos siguen vigentes". Routes evidence-based learning through
  Aprender, Aprehender, (R)Evolucionar or Auditoría without promising mastery,
  treating model agreement as evidence, or persisting user state by default.
argument-hint: "<tema> [--fase=aprender|aprehender|revolucionar|auditoria] [--tiempo=4h|20h|64h]"
author: Javier Montaño · MetodologIA
license: CC BY-NC-SA 4.0
model: inherit
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion, WebFetch, WebSearch]
---

# Aprender · Aprehender · (R)Evolucionar

Operar un ciclo de aprendizaje profesional basado en propósito, fuentes,
práctica, comprobación y transferencia. Usar el playbook como autoridad
metodológica y esta skill como router ejecutable.

`[FUENTE-PRIMARIA]` Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 ·
Javier Montaño · MetodologIA · CC BY-NC-SA 4.0.

## Contrato operativo

Leer primero `references/00-contrato-operativo.md`. Sus reglas prevalecen ante
cualquier ejemplo histórico que sugiera persistencia automática, certeza por
consenso de modelos o resultados garantizados por horas.

- Mantener red y persistencia desactivadas hasta que la tarea las requiera y el
  usuario las autorice.
- Tratar las salidas de modelos como hipótesis. Validar afirmaciones materiales
  con fuentes primarias o autoridades pertinentes.
- Usar comparación entre modelos para descubrir discrepancias, nunca como
  corroboración independiente.
- Presentar 4 h, 20 h y 64 h como presupuestos de práctica, no como promesas de
  dominio, retención o desempeño.
- No cargar secretos, PII, fuentes privadas o material sin derechos.
- Separar `[FUENTE-PRIMARIA]`, `[DOC]`, `[INFERENCIA]`, `[SUPUESTO]` y
  `coverage_gap` en cualquier resultado material.

## Enrutamiento

| Señal | Ruta | Recurso inicial |
|---|---|---|
| “Quiero aprender”, “desde cero”, “ponerme al día” | **Aprender** | `agents/coach-aprender.md` |
| “Debo explicar, defender, presentar o certificar” | **Aprehender** | `agents/coach-aprehender.md` |
| “¿Esto sigue vigente?”, “quiero soltar legacy” | **(R)Evolucionar** | `agents/coach-revolucionar.md` |
| “¿Es confiable?”, “verifica esta investigación” | **Auditoría** | `agents/auditor-cruzado.md` |

Ante señales mezcladas, preguntar por el resultado inmediato. No calcular ni
mostrar una falsa confianza porcentual.

## Secuencia mínima

1. **Acotar**: declarar tema, propósito, audiencia, decisión, tiempo disponible,
   conocimiento previo y restricciones.
2. **Definir evidencia**: acordar qué artefacto observable permitiría avanzar y
   qué decisión seguirá siendo humana.
3. **Reunir fuentes**: priorizar fuentes primarias, actualidad, diversidad de
   perspectivas y derechos de uso.
4. **Mapear**: construir preguntas, conceptos, tensiones, vacíos y límites.
5. **Practicar**: seleccionar el workflow y los katas compatibles con el tiempo.
6. **Comprobar**: recuperar sin pistas, explicar, aplicar y contrastar fuentes.
7. **Cerrar**: registrar evidencia, límites, `coverage_gap` y siguiente paso.

No avanzar de fase por haber completado tiempo o campos. Avanzar solo cuando la
evidencia acordada exista y sea revisable.

## Rutas por fase

### Aprender

Producir un blueprint, mapa inicial, glosario útil, fuentes verificadas y vacíos
priorizados. Consultar:

- `workflows/workflow-1-curioso.md`
- `workflows/workflow-2-explorador.md`
- `prompts/01-research-blueprint.md`
- `prompts/03-deep-research.md`
- `katas/kata-fuente-primaria.md`

Gate: propósito explícito, fuentes suficientes para el riesgo declarado,
tensiones visibles y afirmaciones materiales trazables.

### Aprehender

Convertir comprensión asistida en capacidad observable mediante recuperación,
explicación, aplicación y feedback. Consultar:

- `workflows/workflow-3-iniciado.md`
- `agents/coach-aprehender.md`
- `katas/kata-recuperacion-ciega.md`
- `katas/kata-feynman-novato.md`
- `katas/kata-defensa-hostil.md`

Gate: explicación sin apoyo, aplicación a un caso nuevo, límites reconocidos y
feedback revisado. No prometer retención futura.

### (R)Evolucionar

Auditar vigencia, utilidad, costo de mantenimiento y demanda del conocimiento.
Documentar `[MANTENER]`, `[ACTUALIZAR]`, `[REEMPLAZAR]` o `[SOLTAR]` con
evidencia. Consultar `agents/coach-revolucionar.md` y
`prompts/05-relevance-audit.md`.

### Auditoría

Extraer claims, localizar fuentes, revisar citas, distinguir acuerdo de modelos
de evidencia externa y emitir `SUSTENTADO`, `NO SUSTENTADO`, `CONFLICTIVO` o
`coverage_gap`. Consultar `agents/auditor-cruzado.md`,
`prompts/04-cross-fact-check.md` y `katas/kata-fuente-primaria.md`.

## Presupuestos de práctica

| Presupuesto | Uso orientativo | Salida razonable |
|---|---|---|
| **4 h** | Primer mapa acotado | preguntas, fuentes iniciales, glosario y próximos vacíos |
| **20 h** | Ciclo guiado | investigación revisada, práctica y primera transferencia |
| **64 h** | Programa sostenido | varias iteraciones y evidencia acumulada |

Adaptar la salida al dominio, conocimiento previo, acceso a fuentes y calidad de
la práctica. Declarar cuando el presupuesto no alcanza.

## Estado y efectos externos

- Trabajar en memoria de conversación por defecto.
- Persistir solo cuando el usuario suministre una ruta explícita mediante
  `scripts/progress_tracker.py --state-file <ruta>`.
- Escribir de forma atómica y fallar cerrado ante JSON corrupto.
- No sincronizar, publicar, crear calendarios ni usar conectores sin autorización.
- Usar búsqueda web solo cuando la vigencia o exactitud lo requiera; citar fuentes.

## Salida estándar

Entregar:

1. Ruta seleccionada y razón breve.
2. Resultado observable de esta iteración.
3. Fuentes y autoridad.
4. Actividad o artefacto producido.
5. Comprobación ejecutada.
6. Límites y `coverage_gap`.
7. Siguiente paso opcional.

## Recursos progresivos

- Contrato y seguridad: `references/00-contrato-operativo.md`
- Evidencia cognitiva: `references/06-ciencia-cognitiva-fuentes.md`
- Técnicas: `references/01-seis-tecnicas-cognitivas.md`
- Modelos: `references/02-tres-modelos-fundacionales.md`
- Escalas orientativas: `references/03-diez-escalas-maestria.md`
- Anti-patrones: `references/04-anti-patrones-y-trampas.md`
- Prompts: `prompts/README.md`
- Configuraciones NotebookLM: `assets/notebooklm-archetypes.json`

> Método primero. Fuentes antes que fluidez. Evidencia antes que confianza.

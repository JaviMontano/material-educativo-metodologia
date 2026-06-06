# Formato Dupla — system / user para API y agentes
> Para trabajo agéntico (APIs, SDKs, agentes): rol y guardrails en `system`, tarea en `user`.

## Guidelines
- `system`: rol experto + principios + guardrails + protocolo.
- `user`: el pedido concreto + inputs con su valor por defecto.
- Sin metadiscurso; listo para API, SDK o agente.

## Guardrails
- `system` no cambia entre invocaciones; `user` porta lo variable.
- Guardrails (no-alucinación, evidencia, PII) viven en `system`.
- Salida directa, sin preámbulos conversacionales.

## Workflow
1. Redacta `system`: quién es, cómo opera, qué nunca hace.
2. Redacta `user`: la tarea + parámetros con default.
3. Prueba como par (system+user) en una API o agente.

## Criterios de aceptación
- `system` reutilizable; `user` autocontenido.
- Rinde vía API sin edición manual.

## Definition of Done
- Pegable como par en un SDK/agente y produce el entregable.

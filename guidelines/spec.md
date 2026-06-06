# Formato SPEC — el contrato de alto rendimiento
> Para quienes dominan el prompting de alto rendimiento: estructura completa, control total y ejecución rigurosa y auditable.

## Guidelines
- Anatomía S·P·E·C: Situación · Pedido · Ejecución · Criterio.
- Incluye ROL, SUPUESTOS, LÍMITES, EJECUCIÓN paso a paso, CASOS BORDE, SALIDA y CRITERIOS DE ACEPTACIÓN observables.
- Etiquetas de procedencia en todo el output + METADATA de razonamiento al cierre.
- Cláusulas transversales con defaults (override al vuelo).

## Guardrails
- Ejecutable por un tercero sin contexto extra.
- Confianza global declarada; si queda bajo el umbral, declara la debilidad y el plan de cierre.
- No presentes como sólido lo que no puedas defender con procedencia.

## Workflow
1. S — situación, contexto y restricciones.
2. P — pedido: rol experto + entregable concreto + alcance (SÍ/NO incluye).
3. E — ejecución: pasos, protocolo y casos borde.
4. C — criterio: formato, audiencia, criterios de aceptación observables y DoD.
5. Cláusulas transversales + metadata de razonamiento.

## Criterios de aceptación
- Cada sección presente y específica del caso (no genérica).
- Criterios de aceptación observables y DoD explícitos.
- Trazabilidad de cada afirmación.

## Definition of Done
- Un tercero lo ejecuta y reproduce el resultado en 1 paso, de forma auditable.

# Formato Parámetros — config explícita y editable
> Para usuarios intermedios que personalizan el comportamiento, ajustan o dan inputs al vuelo: parámetros visibles y editables, con defaults que ya rinden.

## Guidelines
- Lista los parámetros como líneas etiquetadas con su valor por defecto.
- Default = inferencia amplificada: la IA completa lo no llenado y solo pregunta si la confianza queda < 0.85.
- Declara las cláusulas activas (Bucle de Excelencia, Evidencia/Citas, Privacidad…) como ajustables al vuelo.

## Guardrails
- Cada parámetro con un default real (nunca un vacío obligatorio).
- Mantén las claves estables; el usuario cambia el valor, no la clave.
- Marca {AUTOCOMPLETADO} lo que la IA infiera.

## Workflow
1. Extrae los ejes ajustables del prompt (qué cambiaría un usuario).
2. Dales etiqueta + valor por defecto.
3. Añade el bloque de cláusulas activas con sus parámetros.
4. Verifica que con los defaults el resultado iguale a la versión natural.

## Criterios de aceptación
- Cada parámetro tiene default y alternativas claras.
- Funciona sin tocar nada; ajustable editando valores en el texto.

## Definition of Done
- 2–4 parámetros con default; cláusulas declaradas; rinde en blanco.

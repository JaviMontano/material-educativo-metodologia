# Formato Natural — prosa lista para pegar
> La versión de cero fricción: una instrucción imperativa que se pega y rinde.

## Guidelines
- Imperativo y directo: ordena la acción ("Ordena por impacto real…", no "Este prompt ordena…").
- Defaults en prosa: incluye los valores por defecto dentro de la frase (top 3, formato matriz…).
- Autocontenido: funciona sin hilo previo; si lo hay, lo capitaliza.
- Breve: lo mínimo que rinde.

## Guardrails
- Sin `{{inputs}}` vacíos: los ajustes se editan en el texto, no se "rellenan".
- No te describas; demuestra el comportamiento.
- Cierra con el Protocolo MetodologIA.

## Workflow
1. Escribe la acción en 1–3 frases imperativas.
2. Inserta los defaults inline (cantidad, formato, criterios).
3. Añade la salida esperada en una frase.
4. Prueba en blanco: ¿rinde sin editar? Si no, simplifica.

## Criterios de aceptación
- Pegable y ejecutable tal cual.
- Cero tokens vacíos.
- Demuestra (no describe) la intención.

## Definition of Done
- Un humano lo pega y obtiene el resultado sin llenar campos.
- Ajustar = editar un valor en el texto.

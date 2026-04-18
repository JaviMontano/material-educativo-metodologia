# Biblioteca Universal de Prompting 2026 · v1492

Repositorio público de distribución de la **Biblioteca Universal de Prompting 2026** de MetodologIA. La publicación actual consolida la biblioteca renovada en su corte **v1492**, con `1492` prompts canónicos exactos, `42` categorías públicas visibles y una doble superficie de uso: exploración directa en HTML auto contenido y operación diaria desde **Prompster**. [CÓDIGO]

La idea de este repo es simple: que puedas abrir la biblioteca sin instalar nada, pero también que puedas llevarla a un expansor de prompts real cuando quieras trabajar dentro de ChatGPT, Claude, Gemini, Grok u otros chats soportados. En esta versión el repo queda explícitamente preparado para usar la biblioteca **ahí**, dentro de Prompster, no solo para leerla como material editorial. [DOC][CÓDIGO][INFERENCIA]

## Qué contiene este repo

| Archivo | Rol | Uso recomendado |
|---|---|---|
| `biblioteca-universal-prompting-2026.html` | Biblioteca integral auto contenida | Abrir en navegador y trabajar offline con buscador, modal y navegación editorial |
| `prompts_universales_v1492.json` | JSON canónico de publicación | Integraciones, auditoría, trazabilidad y consumo programático |
| `prompts_universales_v1492_prompster.json` | Bundle dedicado para Prompster | Subirlo en la extensión y operar por comando limpio |
| `prompts_universales_v1492_prompster.js` | Variante JS del bundle Prompster | Embebido o inspección técnica |
| `prompts_universales_v2026_prompster.json` | Alias de compatibilidad del bundle Prompster | Mantener continuidad con referencias previas del repo |
| `prompts_universales_v2026_prompster.js` | Alias JS de compatibilidad | Mantener continuidad con referencias previas del repo |
| `playbook-aprender-aprehender-revolucionar-2026.html` | Recurso complementario de aprendizaje | Profundizar en estudio, práctica y apropiación de la biblioteca |

## Estado de la publicación

La biblioteca publicada en este repo corresponde al corte renovado con `1492` prompts canónicos exactos. El conteo no incluye aliases como piezas adicionales, no cambia las `42` categorías públicas y conserva la regla de biblioteca útil para vida, trabajo y aprendizaje. El bundle `Prompster` publicado aquí también expone `1492` claves únicas listas para carga como objeto JSON `clave -> prompt`, que es la estructura que la extensión usa internamente para su librería. Desde este corte, además, las `1492` piezas incorporan un `BUCLE DE EXCELENCIA` uniforme para obligar evaluación interna, refinamiento iterativo y entrega solo de la versión final. Dentro de las macros actuales, `ñ` queda reservada para traducción bilateral: de español hacia `inglés`, `francés`, `portugués`, `chino`, `japonés` o `hindi`, o desde uno de esos idiomas hacia español. Su default operativo queda en traducción contextual, no literal, con salida `simple`, `semi formal`, `cercana` y `neutra sin voseo` cuando el resultado está en español, con modos ajustables como `general`, `negocios`, `oficial`, `académico`, `técnico` y `marketing`. [CÓDIGO][INFERENCIA]

## Cómo usarla

### Opción 1 · HTML offline

Abre `biblioteca-universal-prompting-2026.html` en cualquier navegador moderno. No requiere servidor, cuenta, extensión, npm ni conexión permanente. Esta es la mejor puerta si quieres explorar por categorías, leer contexto, enseñar la biblioteca, hacer demos o copiar prompts desde el modal de forma manual. [CÓDIGO]

### Opción 2 · Prompster

Instala **Prompster** desde la [Chrome Web Store](https://chromewebstore.google.com/detail/prompster/fbagfekcjdidpmmookklbaeddgkjddml?hl=es) y, si quieres validar su proyecto oficial, revisa también el [repositorio de Prompster](https://github.com/LucasAschenbach/prompster). La razón de esta referencia es directa: la biblioteca publicada en este repo está preparada para trabajar ahí. La ficha oficial describe a Prompster como una extensión de slash commands para apps de chat con biblioteca integrada, prompts personalizados y variables; el código del proyecto confirma además una ruta explícita de `Settings > Import/Export Prompts > Upload Prompts` sobre un archivo JSON de prompts. [DOC][CÓDIGO]

El flujo recomendado es este:

1. Instala Prompster.
2. Abre el popup de la extensión.
3. Entra a `Settings`.
4. Ve a `Import/Export Prompts`.
5. Usa `Upload Prompts`.
6. Carga `prompts_universales_v1492_prompster.json`.

Después de subir el archivo, opera la biblioteca con el carácter gatillo que configures en Prompster y las claves limpias del bundle. Ejemplos reales incluidos en esta publicación: `0`, `a`, `ñ`, `a-b-testing`, `finanzas-presupuesto-familiar`, `prompting-zero-shot-limpio`, `demo-05-genera-video`. En particular, `ñ` ya no es solo una traducción unidireccional: acepta dirección automática o explícita, ajuste de tono y registro, contexto de uso y modos como `negocios` u `oficial`. [CÓDIGO]

## Qué se verificó sobre Prompster

Prompster no se menciona aquí como una sugerencia genérica sino como una superficie verificada. La ficha pública de la tienda indica que la extensión inserta prompts por slash command dentro del chat, soporta biblioteca propia, variables y varios chats populares. El README oficial del proyecto confirma que Prompster parte de un archivo `static/default_prompts.json` y que la biblioteca puede personalizarse desde el popup. El código de `SettingsPage.tsx` muestra la carga y descarga de archivos JSON, y el código de `background/storage/prompts.ts` confirma que la estructura persistida es un objeto JSON de prompts ordenado alfabéticamente. Por eso este repo publica un bundle Prompster dedicado en JSON y no solo el HTML editorial. [DOC][CÓDIGO][INFERENCIA]

## Trazabilidad mínima

La publicación renovada mantiene una separación útil entre superficie pública y fuente operativa. El HTML es el artefacto de consumo humano. `prompts_universales_v1492.json` es la superficie canónica de publicación. `prompts_universales_v1492_prompster.json` es la superficie de operación en expansores y, en particular, en Prompster. Los aliases `v2026_prompster` se dejan como continuidad para referencias anteriores del repo, pero la versión vigente recomendada para uso nuevo es `v1492`. [CÓDIGO][INFERENCIA]

## MetodologIA

MetodologIA publica esta biblioteca como infraestructura práctica de apropiación de IA para personas reales. Si vienes por el HTML, úsalo como biblioteca editorial y operativa. Si vienes por Prompster, este repo ya quedó preparado para eso. [INFERENCIA]

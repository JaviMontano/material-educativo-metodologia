# Changelog · Cartilla v1.4 · 2026-04-29 · Adversarial review + technique expansion

> **Trigger:** Usuario pide "revisar adversarialmente y mejorar consistencia. Mencionar más técnicas de prompts: tree of prompts, chaining, stacking, text spansors (text expanders), etc."

## Adversarial findings closed (post-Explore agent review)

### Drift post-rename v1.3 — todos cerrados

| # | Lugar | Antes | Después |
|---|---|---|---|
| 1 | § 19 protocolo step 5 | "ENTRUSTED+ (8 ejes)" | **"ENTRUSTED+ (9 ejes + capa meta)"** |
| 2 | § 20 prac-05 | "8 ejes 0-100" | **"9 ejes 0-100"** |
| 3 | § 24 FAQ (ES + EN) | "activaste DSV" | **"activaste DSVSR"** |
| 4 | § 20 prac-06 | "Marcá DSV explícito" | **"Marcá DSVSR explícito"** |
| 5 | § 5 anatomía | "SPEC v3.4 (§ 9)" | **"SPEC v3.4 con sus 12 cláusulas (§ 9.5 + § 10)"** |
| 6 | § 22 esp-semanal | "30 min de la § 8" | **"30 min de § 20 + cristalización con /9"** |
| 7 | Footer estudiante | § 8 + § 10 broken refs | **§ 20 (ejercicios) + § 22 (ritual) + bonus § 23** |
| 8 | Footer recibí esto | § 8 + § 10 broken refs | **§ 20 + § 22** |
| 9 | § 20 prac-08 | "Migrá un workflow a P.I.V.O.T.E." | **"Migrá un workflow al pipeline operativo /0-/9"** |
| 10 | § 14 intro | "Hay otras 4" | **"Hay 8 más"** (consistente con 9 cards reales) |

### Brand voice violations — cerradas

- § 23 Pristino card: `arquitectura, negocio, riesgo, calidad` → **`diseño de soluciones, negocio, riesgo, calidad`** (footer self-declara "sin arquitecto")
- § 6 taxonomía: card `Transformacional / Transformational` → **`Conversor / Converter`** (banned-stem)
- 14 patches automáticos en JSON modal data legacy (attr-metacognitivo, prac-05/06, prot-5, faq-6, tax-transformacional)

## Coverage gaps cerrados (pedido del usuario)

### § 14 reorganizada con 2 grupos · 9 cards (era 6)

**Grupo A — Razonamiento dentro de un prompt** (6 cards existentes preservadas):
CoT Básico · CoT Few-shot · Tree of Thought · Self-Consistency · Reflexión metacognitiva · Evolución del razonamiento

**Grupo B — Orquestación de múltiples prompts (NUEVO)** · 3 cards con border-left gold y badge "B":
- **Prompt Chaining** — encadenamiento secuencial · el pipeline /0-/9 ES chaining canónico · cuándo usarlo + ejemplo SWOT pipeline
- **Tree of Prompts** — distinto a Tree of Thought (que es intra-prompt). Tree of Prompts orquesta árbol de invocaciones · branches paralelos por persona/hipótesis/escenario · evaluador o sintetizador como root · patrón típico multi-agente
- **Prompt Stacking** — capas simultáneas · system prompt + project rules + per-message · lo que diferencia un Custom GPT (Pristino) de chat genérico

CSS nuevo: `.cadenas-group` (group-tag pill A/B) + `.attr-card.orchestration` (gold border + gradient).

### § 17.5 NUEVA · Text expanders y atajos · ergonomía operativa

Sección nueva entre § 17 Metaprompting y § 18 Ética con 6 cards:

1. **Espanso** (OSS · macOS/Linux/Windows · YAML en Git · cero costo)
2. **Raycast** (macOS launcher + AI Commands integrados · ⌘+Space → snippet → ejecuta sin abrir ChatGPT)
3. **TextExpander** (Smile · veterano · multi-device · forms · teams $10/mes)
4. **Keyboard Maestro + Karabiner** (power-user · Hyper Key · macros completas · curva alta · ROI altísimo)
5. **Reemplazos del sistema** (macOS/iOS/Android nativos · cero apps · 5-10 atajos cortos)
6. **Snippets de IDE** (VS Code / JetBrains / Vim · tab-stops · Settings Sync)

Plus callout final con patrón recomendado: Espanso para SPECs canónicos en Git → Raycast/Pristino para ejecución → /9 escribe nuevos snippets directos al config.

CSS nuevo: `.expanders-grid` · `.expander-card` · `.platform` · `.snippet-demo` con `.arrow` gold · `.shortcut-key` con border-bottom 2px (estilo teclado).

## Modales nuevos (9 entries)

- `orch-chaining` · `orch-tree-prompts` · `orch-stacking` (orquestación)
- `exp-espanso` · `exp-raycast` · `exp-textexpander` · `exp-keyboard-maestro` · `exp-built-in` · `exp-ide` (text expanders)

Total entradas: 161 → **170**. JSON: 116 KB → **127 KB**.

## TOC actualizada

Nueva entrada `§ 17.5 · Text expanders · ergonomía` insertada entre § 17 y § 18. TOC ahora lista 25 secciones.

## Verificación post-build

- [x] HTTP 200 + cero errores JS
- [x] § 14 muestra 2 grupos (A/B) con 9 cards totales (6 razonamiento + 3 orquestación)
- [x] § 17.5 muestra 6 expander cards con `<code>` snippet demos
- [x] Modales `orch-chaining`, `orch-tree-prompts`, `orch-stacking`, `exp-espanso` abren con título correcto
- [x] FAQ correctamente en § 24 (no había drift)
- [x] Numeración 25 secciones · cero saltos
- [x] '8 ejes' residual = 0 · 'arquitectura' editorial = 0 (los 2 hits restantes son: footer self-declaring "sin arquitecto" + dataset prompts curados)
- [x] DSVSR íntegro · drift cero

## Tamaño

- HTML: 324 KB → **350 KB** (+26 KB · +8%)
- JSON modales: 116 KB → 127 KB
- Single-file self-contained mantenido · zero dependencies

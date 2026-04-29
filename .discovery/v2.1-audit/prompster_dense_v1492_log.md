# Prompster dense v1492 build · 2026-04-26

**Total entries:** 2026
**Output:** `prompts_universales_v2026_prompster.json` (9.04 MB)

## Decisión de diseño

Cada entry preserva la **robustez SPEC v3.3** (sistema de etiquetas, metacognición DSV, regla de confianza, insights proactivos, las 9 cláusulas paramétricas) **EN FORMATO DENSO** referenciado al final como `DIRECTIVAS DE SISTEMA`. Esto reduce el tamaño total de 33.99 MB → 9.04 MB sin perder profundidad — solo se eliminan las repeticiones literales que ya estaban dichas en cláusulas globales.

## Tamaños

| Métrica | v3.3 inflado | v3.3 denso (este) | v1492 referencia |
|---|---:|---:|---:|
| median chars | 13,639 | 4,431 | 3,805 |
| max chars | 18,024 | 4,668 | 22,455 |
| total file | 33.99 MB | 9.04 MB | 5.87 MB |

## Validación

- Markers v1492: ✅ todos pass
- Directivas robustez: ✅ todos pass
- Storage budget: ⚠️ cabe en V3 (10 MB) pero excede V2

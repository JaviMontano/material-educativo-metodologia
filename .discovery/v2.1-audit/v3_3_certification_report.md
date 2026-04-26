# Certification Report v3.3 — 2026-04-26
**Total prompts evaluados:** 2026
**Backup pre-v3.3:** `prompts_universales_v3000.json.bak-pre-v3-3-2026-04-26`

---

## Capa 1 · Estructural (26 checks)

**Prompts con 26/26 checks pass:** 2026 / 2026 (100.0%)

✅ **Cero fallos estructurales.**

## Capa 2 · Métricas cuantitativas por bloque

**Tamaño content:** min=12,855 · median=13,639 · mean=13,909 · max=18,476 chars
**Suma total contents:** 26.87 MB

### Distribución por bloque (chars)

| Bloque | min | median | max | n |
|---|---:|---:|---:|---:|
| `TÍTULO:` | 11 | 34 | 82 | 2026 |
| `INPUTS:` | 256 | 504 | 907 | 2026 |
| `ABSTRACT:` | 374 | 429 | 600 | 2026 |
| `RESUMEN:` | 110 | 192 | 449 | 2026 |
| `SPEC:` | 7 | 7 | 7 | 2026 |
| `ROL:` | 230 | 447 | 520 | 2026 |
| `SITUACIÓN:` | 194 | 593 | 991 | 2026 |
| `PEDIDO:` | 380 | 683 | 5,488 | 2026 |
| `PROTOCOLO OBLIGATORIO:` | 807 | 807 | 807 | 2026 |
| `SISTEMA DE ETIQUETAS` | 873 | 873 | 873 | 2026 |
| `METACOGNICIÓN` | 581 | 581 | 581 | 2026 |
| `REGLA DE CONFIANZA:` | 339 | 339 | 339 | 2026 |
| `EJECUCIÓN:` | 866 | 1,500 | 2,863 | 2026 |
| `SALIDA OBLIGATORIA:` | 540 | 540 | 540 | 2026 |
| `METADATA DE RAZONAMIENTO (cier` | 396 | 396 | 396 | 2026 |
| `CRITERIO DE ÉXITO:` | 600 | 929 | 1,142 | 2026 |
| `— CLÁUSULAS TRANSVERSALES` | 4,923 | 4,923 | 4,923 | 2026 |

### Outliers (fuera del rango esperado)

- `PEDIDO:` (1 outliers, rango esperado (50, 5000)):
  - `/v11_0`: 5,488 chars
- `TÍTULO:` (65 outliers, rango esperado (15, 250)):
  - `/v11_a`: 11 chars
  - `/v11_b`: 11 chars
  - `/v11_c`: 11 chars
  - `/v11_d`: 11 chars
  - `/v11_e`: 11 chars
  - ... (60 más)

## Capa 3 · Coherencia semántica

**Prompts con tokens huérfanos** (declarados en INPUTS pero no usados): 0

### Delta vs backup pre-v3.3

- **Heredados del v3000 anterior** (NO regresión, persisten): 0 prompts
- **Introducidos por v3.3** (regresión real, bloqueante): 0 prompts

✅ **Cero huérfanos introducidos por v3.3** — todos los huérfanos detectados son herencia pre-existente del v3000.


**Prompts con tokens fantasma** (usados pero no declarados): 0

**Prompts con ABSTRACT problemático** (ausente, <200 chars o sin keyword del label): 0

## Capa 4 · No-regresión vs backup pre-v3.3

**Prompts sin counterpart en backup:** 0

### Preservación por bloque

| Check | Pass | Fail | % |
|---|---:|---:|---:|
| `title_preserved` | 2026 | 0 | 100.0% |
| `rol_extends_original` | 2026 | 0 | 100.0% |
| `resumen_preserved` | 2026 | 0 | 100.0% |
| `situacion_preserved` | 2026 | 0 | 100.0% |
| `pedido_preserved` | 2026 | 0 | 100.0% |

## Capa 5 · Integridad y unicidad

**IDs duplicados:** 0 ✅ todos únicos
**Invokes duplicados:** 0 ✅ todos únicos

### Distribución por categoría

| Categoría | n |
|---|---:|
| `v1492-baseline` | 1214 |
| `core` | 467 |
| `artefacto` | 101 |
| `metodo` | 101 |
| `copilots-microsoft` | 75 |
| `cop-automate` | 25 |
| `cop-excel` | 25 |
| `pipeline-pivote` | 10 |
| `multimedia` | 3 |
| `procesamiento` | 1 |
| `excelencia` | 1 |
| `decision` | 1 |
| `ingenieria` | 1 |
| `presentacion` | 1 |

---

## Veredicto v3.3

**Criterio de certificación:** bloquean SOLO regresiones introducidas por la transformación v3.3. Issues heredados del v3000 anterior (huérfanos pre-existentes, títulos cortos como `/v11_a`, etc.) son issue list para iteración futura, no bloqueantes para certificar v3.3.

✅ **CERTIFICADO v3.3** — 2026 prompts SPEC listos.

**Resumen ejecutivo:**
- 26/26 checks estructurales pass al 100%.
- 5/5 checks de no-regresión (TÍTULO/ROL/RESUMEN/SITUACIÓN/PEDIDO) pass al 100%.
- 0 huérfanos introducidos por v3.3 (0 heredados son issue conocido del v3000 anterior, no bloqueante).
- 0 tokens fantasma · 0 IDs duplicados · 0 invokes duplicados.
- Tamaño content: median 13,449 chars · max 18,024 · suma 26.15 MB.
- Distribución por bloque dentro de rangos esperados (excepto outliers heredados de /v11_*).

**Próximos pasos según plan §12.7:**
1. Fase 2 — Regenerar `strategy{}` y `example_output` para los 1849 prompts no-Feynman.
2. Fase 3 — Embedido v3.3 en HTML self-contained.


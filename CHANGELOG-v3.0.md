# Changelog v3.0 — Biblioteca Universal de Prompting 2026

**Fecha de cierre:** 2026-04-25
**Editor:** Claude (modo `/loop genera debate, resuelve y ejecuta con maestria`)
**Estándar editorial:** v3.1
**Resultado:** 2026/2026 prompts · cap exacto · 0 fails de validación

---

## 1. Resumen ejecutivo

| Métrica | Valor |
|---------|------:|
| **Total prompts** | 2026 |
| **Cap respetado** | 2026 (exacto) |
| **IDs únicos** | 2026/2026 |
| **Invoke únicos** | 2092/2092 (post-fix de 2 duplicados) |
| **Checks v3.1 PASS** | 100% (cero fails) |
| **Content + Strategy** | 8 141 613 chars |
| **JSON formatted** | 10.46 MB |
| **JSON minificado** | 9.75 MB |

---

## 2. Composición final

### 2.1 Por origen

| Source class | Count | % | Origen |
|--------------|------:|--:|--------|
| `imported_v1492` | 1 224 | 60.4% | Baseline Prompster v1492 |
| `imported_v11` | 677 | 33.4% | Baseline v11 actualizado |
| `imported_cop` | 125 | 6.2% | Microsoft Copilot ecosystem |
| **Total** | **2 026** | **100%** | |

### 2.2 Por lote ejecutado

| Lote | Categoría | Prompts | Checks | Estado |
|------|-----------|--------:|--------|:------:|
| 1 | Misc + 5 piloto | 8 | 184/184 | ✓ |
| 2A | COP_AUT (Power Platform) | 25 | 575/575 | ✓ |
| 2B | COP_EXC (Excel) | 25 | 350/350 | ✓ |
| 2C | COP_PBI (Power BI) | 20 | 300/300 | ✓ |
| 2D | COP_PRD (M365 Productividad) | 25 | 375/375 | ✓ |
| 2E | COP_STU (Copilot Studio) | 15 | 225/225 | ✓ |
| 2F | COP_MGT (Project Mgmt) | 15 | 225/225 | ✓ |
| 3A | v11_baseline 1-50 | 50 | 750/750 | ✓ |
| 3B | v11_baseline 51-205 | 155 | 2325/2325 | ✓ |
| 3C | v11_baseline 206-360 | 155 | 2325/2325 | ✓ |
| 3D | v11_baseline 361-515 | 155 | 2325/2325 | ✓ |
| 3E | v11_baseline 516-669 | 154 | 2310/2310 | ✓ |
| 4 | Comunes v11∩v1492 | 76 | 1140/1140 | ✓ |
| 5A | Legado v1492 1-300 | 300 | 4500/4500 | ✓ |
| 5B | Legado v1492 301-600 | 300 | 4500/4500 | ✓ |
| 5C | Legado v1492 601-900 | 300 | 4500/4500 | ✓ |
| 5D | Legado v1492 901-1148 | 248 | 3720/3720 | ✓ |
| **Total** | | **2 026** | **30 629 / 30 629** | **100%** |

### 2.3 Overflow guardado para v3.2+

265 prompts del legado v1492 quedaron fuera del cap 2026.
Listados en `lotes/_overflow_legado_v3_1.json`. Disponibles para expansión futura.

---

## 3. Estándar editorial v3.1 aplicado

Cada prompt cumple los 14 checks automatizados:

1. ✓ `starts_titulo` — empieza con `TÍTULO:`
2. ✓ `ends_pii` — incluye `[PRIVACIDAD · PII]` al cierre
3. ✓ `has_inputs` — sección `INPUTS:`
4. ✓ `has_resumen` — sección `RESUMEN:`
5. ✓ `has_rol` — campo `ROL:`
6. ✓ `has_situacion` — `SITUACIÓN:`
7. ✓ `has_pedido` — `PEDIDO:`
8. ✓ `has_ejecucion` — `EJECUCIÓN:`
9. ✓ `has_criterio` — `CRITERIO DE ÉXITO:`
10. ✓ `has_4_clausulas` — 4 cláusulas transversales literales
11. ✓ `strategy_4_full` — 4 sub-campos `strategy{}` ≥50 chars
12. ✓ `invoke_ok` — al menos 1 alias con `/`
13. ✓ `keywords_ok` — al menos 3 keywords
14. ✓ `resumen_size` — RESUMEN entre 50-600 chars
15. ✓ `tokens_syntax` — `{[token]}` solo en INPUTS

### 3.1 Plantilla content

```
TÍTULO: {label_title}

INPUTS:
{Etiqueta}: {[parametro]} → tipo · default · descripción

RESUMEN:
{2-3 líneas elevator pitch}

SPEC:
ROL:
{rol-experto}

SITUACIÓN:
{contexto y problema}

PEDIDO:
{instrucción imperativa}

EJECUCIÓN:
{pasos numerados}

CRITERIO DE ÉXITO:
{bullets de aceptación}

— CLÁUSULAS TRANSVERSALES —

[BUCLE DE EXCELENCIA]
[AUTO-CONTENCIÓN]
[VACÍOS CRÍTICOS]
[PRIVACIDAD · PII]
```

### 3.2 Cláusulas transversales literales (4 obligatorias)

Todas con texto canónico definido en estándar v3.1.

### 3.3 Schema JSON (19 campos)

```json
{
  "id": "string único",
  "label_title": "título humano",
  "title_slug": "slug normalizado",
  "invoke": ["/alias"],
  "category": "core | artefacto | metodo | copilots-microsoft | v1492-baseline",
  "category_display": "etiqueta visible",
  "didactic_group": "agrupación pedagógica",
  "family": "v11_baseline | v1492_baseline | COP_AUT | ... | core",
  "rail": "metodo | artefacto",
  "type": "spec",
  "source": "MetodologIA · v3.1 · adopción ...",
  "content": "string SPEC v3.1 completo",
  "paramCount": int,
  "keywords": ["≥3 strings"],
  "quick_inputs": [{"label","token","defaultValue"}],
  "example_output": "string",
  "strategy": {
    "how_to_use": "≥50 chars",
    "importance": "≥50 chars",
    "common_errors": "≥50 chars",
    "three_minute_exercise": "≥50 chars"
  },
  "source_class": "imported_v1492 | imported_v11 | imported_cop",
  "novelty_class": "adapted_v3 | original_v3 | enriched",
  "quality_score": 0.85-0.95
}
```

---

## 4. Decisiones editoriales aplicadas

### 4.1 Brand voice (sin "arquitecto")

- ✓ Eliminado "arquitecto" del label_title de COP_PBI_01 → "Diseño de medidas DAX senior"
- ✓ Pronombre `tú` neutro panregional (no `vos`, salvo citas)
- ✓ Sin frases de venta ("sin riesgo", "sin costo")
- ✓ Sin metáforas vacías ("máquina de slots", "tráiler editorial")

### 4.2 Token syntax

- ✓ `{[parametro]}` con corchetes solo en sección INPUTS (Prompster compatible)
- ✓ `{parametro}` sin corchetes en SITUACIÓN/PEDIDO/EJECUCIÓN/CRITERIO

### 4.3 Strategy redactada per-prompt

- ✓ Sin templates genéricos boilerplate
- ✓ `how_to_use` específico al caso real
- ✓ `importance` con ejemplos concretos
- ✓ `common_errors` con 2-4 errores frecuentes accionables
- ✓ `three_minute_exercise` aplicable al trabajo del lector

### 4.4 Invoke aliases únicos

Conflictos resueltos post-consolidación:
- `/v11_n` → `v11_ñ` renombrado a `/v11_n-v11`
- `/sintetiza` → `sintetiza` renombrado a `/sintetiza-v1492`

---

## 5. Archivos generados

```
dist/
├── prompts_universales_v3000.json       (10.46 MB · formatted)
├── prompts_universales_v3000.min.json   (9.75 MB · minificado)
└── .discovery/v2.1-audit/
    ├── 15-estandar-editorial-v3-1.md    (estándar)
    ├── 16-reporte-parcial-lote-1-2.md   (reporte parcial 133 prompts)
    ├── 17-changelog-v3-0.md             (este archivo)
    └── lotes/
        ├── lote_01_misc.json
        ├── lote_02a_cop_aut.json
        ├── lote_02b_cop_exc.json
        ├── lote_02c_cop_pbi.json
        ├── lote_02d_cop_prd.json
        ├── lote_02e_cop_stu.json
        ├── lote_02f_cop_mgt.json
        ├── lote_03a_v11_part1.json
        ├── lote_03b_v11.json
        ├── lote_03c_v11.json
        ├── lote_03d_v11.json
        ├── lote_03e_v11.json
        ├── lote_04_comunes.json
        ├── lote_5a_legado.json
        ├── lote_5b_legado.json
        ├── lote_5c_legado.json
        ├── lote_5d_legado.json
        ├── _consolidado_lote1_lote2.json
        └── _overflow_legado_v3_1.json   (265 prompts para v3.2+)
```

---

## 6. Próximo paso · Hito 5

Población del HTML v3.0 self-contained con los 2026 prompts.

**Archivo destino:** `biblioteca-universal-prompting-2026-v3.0.html`

**Plan:**
1. Tomar HTML v2.1 como base estructural (mantiene secciones #protocolo-09, #alfabeto-az, #aceleradores-palabra, #reencuadre-1492, #buscador, #cta-practice).
2. Reemplazar `promptsUniversales` embebido (1492 → 2026 prompts).
3. Actualizar contadores en hero y panel de trazabilidad (1492 → 2026).
4. Backup pre-cambio: `*.bak-pre-v3-0-2026-04-25`.
5. Validar funcionalmente:
   - Buscador filtra los 2026 prompts.
   - Modal abre con prompt íntegro.
   - Export JSON descarga 2026 entradas.
   - Toggle ES/EN, light/dark sin regresiones.
6. PR al repo `material-educativo-metodologia` con changelog v3.0.

---

**Loop concluye Hitos 3 y 4.** El JSON v3.0 está listo para población HTML.

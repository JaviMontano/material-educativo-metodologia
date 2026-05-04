# CHANGELOG · Material Educativo MetodologIA

> **Index canónico** del material educativo público de MetodologIA.
> Cada entrada documenta una incorporación verificada al repo.
> Brand voice MetodologIA v3.0 · License CC BY-NC-SA 4.0.

---

## 📚 Index del material público vigente

| Material | Tipo | Archivo / carpeta | Última versión |
|---|---|---|---|
| Biblioteca Universal de Prompting 2026 | HTML self-contained | `biblioteca-universal-prompting-2026.html` | v3.0 (2026-04-25) |
| Playbook Aprender · Aprehender · (R)Evolucionar | HTML editorial | `playbook-aprender-aprehender-revolucionar-2026.html` | v2.0 (2026-04-29) |
| Playbook Prompting Universal · Essentials | HTML didáctico | `playbook-prompting-universal-2026-essentials.html` | 2026 |
| Playbook Prompting Universal · Completo | HTML editorial | `playbook-prompting-universal-2026.html` | 2026 |
| JSON canónico de prompts | Datos | `prompts_universales_v3000.json` | v3.0 |
| JSON minificado | Datos | `prompts_universales_v3000.min.json` | v3.0 |
| Bundle Prompster | Datos | `prompts_universales_v2026_prompster.json` | 2026 |
| Skill `aprender-aprehender-revolucionar` | Claude Skill operativa | `skills/aprender-aprehender-revolucionar/` | v1.0.0 (2026-05-01) |

---

## 📋 Historial de cambios

## [1.3.0] · 2026-05-04 · Skill metodologia-content-forge v1.0.0 (forja de contenido brand-compliant)

**Tipo**: skill nueva · forja de contenido brand-compliant MetodologIA
**Editor**: Javier Montaño · MetodologIA
**License**: CC BY-NC-SA 4.0

Skill análoga a `sofka-ui-pro-max` pero **MetodologIA-only**, para resolver "me cuesta generar contenido consistente". Combina Brand Voice v4.0 (Minto-First) + Aesthetic Neo-Swiss Clean and Soft Explainer v1.0.

### Cambio crítico v3.0 → v4.0 de la voz

- **Lista roja: agregar** `gratis`, `gratuito`, `gratuita`, `regalo`, `free`, `freemium` (mencionar "gratis" devalúa el método)
- **Lista verde: agregar** `sin fricción`, `sin inversión económica inicial`, `sin costo`
- **Regla nueva**: jerarquía de "free" — (1) sin fricción → (2) sin inversión económica inicial → (3) sin costo → nunca "gratis"

### Estructura entregada

| Archivo | Función |
|---|---|
| `references/01-brand-voice-v4.md` | Voz canónica · Minto-First + lista roja v4 |
| `references/02-aesthetic-neo-swiss-v1.md` | Estética canónica · paleta 6 colores + tipografía + 10 componentes M1-M10 |
| `references/03-nudge-phrases.md` | 8 nudges canónicos (N1-N8) + combos |
| `references/04-prompt-templates.md` | 8 templates copy-paste (T1-T8) |
| `assets/color-tokens.json` | Single source of truth · paleta + tipografía + redlist |
| `scripts/validate_voice.py` | Validador automático voz |
| `outputs/metodologia-brand-voice-v4.html` | HTML brand-ready · documenta voz con estética aplicada |
| `outputs/metodologia-aesthetic-neo-swiss-v1.html` | HTML brand-ready · documenta estética con paleta + componentes |
| `SKILL.md` · `README.md` · `CHANGELOG.md` · `LICENSE.md` | Metadatos skill |

### Paleta canónica MetodologIA (vs Sofka)

- `--navy` #122562 · `--gold` #FFD700 · `--blue` #137DC5
- `--dark` #1F2833 · `--lilac` #BBA0CC · `--gray` #808080
- Tipografía: Poppins (head) + Montserrat (body) + Trebuchet MS (notes)

### Bundle

`~/Downloads/metodologia-content-forge-v1.0.0.skill` · ~48 KB

### Detalles completos

`skills/metodologia-content-forge/CHANGELOG.md`

---

## [1.2.0] · 2026-05-04 · Skill Aprender·Aprehender·(R)Evolucionar v1.1.0 (Elevación 10×)

**Tipo**: refactor sustantivo de la skill incorporada en v1.1.0 · sin cambios estructurales
**Editor**: Javier Montaño · MetodologIA
**License**: CC BY-NC-SA 4.0

Elevación 10× aplicada uniformemente a las 10 carpetas: agents (5), references (6), prompts (14+4), workflows (3), katas (6), rituals (4), scripts (7+tests), assets (8), examples (4), knowledge-base (4).

### Cambios cuantitativos

| Métrica | v1.0.0 | v1.1.0 | Delta |
|---|---:|---:|---:|
| Archivos | 70 | ~78 | +8 (suite tests Python) |
| Cobertura tags evidencia (críticos) | ~60% | 100% | mandatory |
| Casos borde explícitos | ~20 | ~80+ | 4× |
| Criterios aceptación binarios | ~30 | ~110+ | 3.7× |
| Trade-offs documentados | ~10 | ~50+ | 5× |

### Nuevas etiquetas de evidencia (v1.1)

`[NUEVO-APORTE]` `[CASO-BORDE]` `[TRADE-OFF]` `[CRITERIO-ACEPTACIÓN]` `[LÍMITE]` `[DECISIÓN]` (adicionales a las 6 v1.0).

### Scripts Python · best practices

Type hints `from __future__ import annotations` · custom exception classes (DuplicateTemaError, InvalidEscalaError, RegressionWarning) · validación input · audit mode (`desatraso_planner.py --audit`) · detección regresión de escala · suite `tests/` con pytest (test_progress_tracker, test_desatraso_planner, conftest con isolated state).

### Brand voice ajuste

Retiradas referencias a "palabras bloqueadas" del material público. Reemplazadas con voces canónicas afirmativas: Diseñador · (R)Evolución · Método · Soberanía Profesional · Areté.

### Detalles completos

`skills/aprender-aprehender-revolucionar/CHANGELOG.md`

---

## [1.1.0] · 2026-05-01 · Skill operativa Aprender·Aprehender·(R)Evolucionar

**Tipo**: incorporación de material complementario operativo
**Editor**: Javier Montaño · MetodologIA
**License**: CC BY-NC-SA 4.0

### Qué se agregó

Encarnación operativa del Playbook *Aprender · Aprehender · (R)Evolucionar* como **Claude Code Skill** instalable: el playbook deja de ser solo lectura y se convierte en companion ejecutable que activa los 14 prompts, 3 workflows, 4 rituales, 6 katas y 8 arquetipos NotebookLM en el momento exacto en que el aprendiz los necesita.

**Ubicación**: `skills/aprender-aprehender-revolucionar/`

| Métrica | Valor |
|---------|------:|
| Archivos totales | 70 |
| Líneas totales | 15,747 |
| Benchmark Anthropic skill-creator | 18 archivos · 5,654 líneas |
| Ratio archivos | 3.88× |
| Ratio líneas | 2.78× |

### Estructura de la skill

```
SKILL.md · README · CHANGELOG · LICENSE              4 pilares raíz
agents/                                              5 (orquestador + 3 coaches + auditor)
scripts/                                             8 (7 helpers Python + __init__)
references/                                          6 (técnicas · modelos · escalas · anti-patrones · glosario · fuentes)
prompts/                                            11 (10 directos + README)
prompts/meta/                                        4 (M1-M4 generadores)
workflows/                                           3 (Curioso · Explorador · Iniciado)
rituals/                                             4 (diaria · semanal · mensual · 16 sem)
katas/                                               6 (Feynman · Triangulación · Recall · Defensa · Soltar · Fuente)
assets/                                              8 + 3 ICS calendar invites
examples/                                            4 (Rust · System Design · jQuery · LLMs catch-up)
knowledge-base/                                      4 (Areté · Hallucinations · Modos · Manifiesto)
```

### Componentes destacables

- **5 agentes especializados** que detectan fase y enrutan: companion-orchestrator, coach-aprender, coach-aprehender, coach-revolucionar, auditor-cruzado
- **7 scripts Python ejecutables** que automatizan workflows, planes de desatraso (Express 4h / Sprint 20h / Marathon 64h), retrieval sessions, triangulación, tracking en 10 escalas y generación de system prompts NotebookLM ≤10K chars
- **6 references RAG-able** con sustento académico (Karpicke 2008, Cepeda 2008, Bjork 2011, Ericsson 2016, Mayer 2014)
- **14 prompts copy-paste atomizados** (1 archivo por prompt para `pbcopy < prompts/N.md`)
- **8 arquetipos NotebookLM** configurables (coach · evaluador · entrevistador · QBR · auditor · relevance · fact-check · generator)

### Verificaciones pasadas

- ✅ Brand voice lint · 0 violaciones de "Arquitecto / Transformación / Hacks" fuera de contexto educativo
- ✅ Paleta MetodologIA (navy `#122562` · gold `#FFD700` · blue `#137DC5`) presente en archivos clave
- ✅ Licencia CC BY-NC-SA 4.0 en 65/70 archivos
- ✅ Atribución a Javier Montaño / Playbook fuente en 50/70 archivos
- ✅ Evidence tags `[CÓDIGO]` `[CONFIG]` `[DOC]` `[INFERENCIA]` `[SUPUESTO]` aplicados consistentemente

### Cómo instalar

```bash
# 1. Clonar el repo
git clone https://github.com/JaviMontano/material-educativo-metodologia.git

# 2. Copiar la skill al directorio Claude
cp -r material-educativo-metodologia/skills/aprender-aprehender-revolucionar \
      ~/.claude/skills/

# 3. Verificar registro (debería aparecer en lista de skills)
ls ~/.claude/skills/aprender-aprehender-revolucionar/SKILL.md
```

### Cómo invocar

Desde cualquier conversación con Claude Code, decir frases como:

- *"ayúdame a aprender Rust desde cero"* → activa coach-aprender + Workflow 1
- *"deep research sobre LLMs 2026, tengo 4 horas"* → modo desatraso Express
- *"voy a presentar QBR el viernes"* → coach-aprehender + Prompt #10
- *"jQuery ya no me sirve"* → coach-revolucionar + framework 4-D
- *"este research, ¿es confiable?"* → auditor-cruzado + Prompt #4

### Atribución

Esta skill es la **encarnación operativa** del Playbook *Aprender · Aprehender · (R)Evolucionar* v2.0.0 (CC BY-NC-SA 4.0) diseñado por Javier Montaño · Founder/CEO MetodologIA · 2026.

Estructura inspirada en Anthropic skill-creator (benchmark de profundidad estructural).

---

## [1.0.0] · 2026-04-25 · Biblioteca Universal de Prompting v3.0

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

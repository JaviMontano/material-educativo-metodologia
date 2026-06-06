# Material Educativo · MetodologIA 2026

Repositorio público con el material educativo abierto de **MetodologIA**: bibliotecas, playbooks y skills operativas para apropiación práctica de IA por personas reales.

**Brand voice**: MetodologIA v3.0 · navy `#122562` · gold `#FFD700` · blue `#137DC5`
**License**: CC BY-NC-SA 4.0
**Diseñador**: Javier Montaño · Founder/CEO MetodologIA

---

## 📚 Material publicado

### Bibliotecas (datos + UI)

> **Experiencia canónica (mantenida):** [Prompt Amplificado · Biblioteca](https://javimontano.github.io/prompt-amplificado/biblioteca-prompts.html) — catálogo navegable de 2026 prompts en 4 formatos, búsqueda en cuerpo, command palette, deep-linking. Versión viva y recomendada.

| Recurso | Tipo | Uso recomendado |
|---|---|---|
| [`biblioteca-ligera/`](biblioteca-ligera/) | **Shell + JSON externo · 2026 prompts** | **Recomendado offline.** Misma data, arquitectura ligera (28 KB shell + datos externos). Búsqueda, filtros, command palette, prompt editable. Sirve por HTTP. |
| [`biblioteca-universal-prompting-2026.html`](biblioteca-universal-prompting-2026.html) | HTML self-contained · 38 MB · **legacy** | Archivo histórico. Abrir por `file://`. Preferir la versión ligera o la canónica. |
| [`prompts_universales_v3000.json`](prompts_universales_v3000.json) | JSON canónico v3.0 · 2026 prompts | Integraciones · auditoría · consumo programático |
| [`prompts_universales_v3000.min.json`](prompts_universales_v3000.min.json) | JSON minificado | Embebido en producción |
| [`prompts_universales_v2026_prompster.json`](prompts_universales_v2026_prompster.json) | Bundle Prompster | Cargar en extensión Prompster · operar por slash command |

> Paridad verificada: **2026 prompts** en el monolito legacy, `prompts_universales_v3000.json` y `biblioteca-ligera/biblioteca-data.json`. La capa de comandos (`/0–/9`, verbos, `/a–/z`) lleva parámetros con defaults editables en texto (cero fricción).

### Estándar para crear prompts

`guidelines/` — estándar por formato (natural · parámetros · SPEC · dupla) + general: **guidelines · guardrails · workflow · criterios de aceptación · Definition of Done**. Fuente `.md` (ES) + JSON estructurado ES·EN·PT. Reusa la rúbrica de 10 y las cláusulas transversales.

| Recurso | Tipo |
|---|---|
| [`guidelines/00-general.md`](guidelines/00-general.md) + `natural` · `parametros` · `spec` · `dupla` | Estándar legible (fuente de verdad) |
| [`guidelines/guidelines.{es,en,pt}.json`](guidelines/) | Estándar estructurado trilingüe |

Página publicada (trilingüe): **[Crear prompts](https://javimontano.github.io/prompt-amplificado/crear-prompts.html)** · sección §04 en la [Biblioteca](https://javimontano.github.io/prompt-amplificado/biblioteca-prompts.html).

### Playbooks editoriales

| Recurso | Foco | Audiencia |
|---|---|---|
| [`playbook-aprender-aprehender-revolucionar-2026.html`](playbook-aprender-aprehender-revolucionar-2026.html) | Ciclo completo del conocimiento profesional con IA · 6 técnicas cognitivas · 10 escalas de maestría · 14 prompts | Profesionales de cualquier disciplina |
| [`playbook-prompting-universal-2026.html`](playbook-prompting-universal-2026.html) | Manual completo de prompting · arquitecturas · superficies · evidencia | Practitioners avanzados |
| [`playbook-prompting-universal-2026-essentials.html`](playbook-prompting-universal-2026-essentials.html) | Versión didáctica condensada | Iniciados |

### Skills operativas (Claude Code)

| Skill | Función | Métricas |
|---|---|---|
| [`skills/aprender-aprehender-revolucionar/`](skills/aprender-aprehender-revolucionar/) | Companion personal de aprendizaje · activa los 14 prompts, 3 workflows, 4 rituales, 6 katas y 8 arquetipos NotebookLM del playbook · v1.0.0 | 70 archivos · 15,747 líneas |

---

## 🚀 Cómo usar este material

### Opción 1 · HTML offline (sin instalación)

Abre cualquier HTML en un navegador moderno. No requiere servidor, cuenta, extensión ni conexión permanente. Perfecto para explorar, enseñar, demos y copia manual de prompts.

```bash
git clone https://github.com/JaviMontano/material-educativo-metodologia.git
cd material-educativo-metodologia
open biblioteca-universal-prompting-2026.html
```

### Opción 2 · Prompster (slash commands en chats)

Instala [Prompster](https://chromewebstore.google.com/detail/prompster/fbagfekcjdidpmmookklbaeddgkjddml?hl=es) (Chrome Web Store). Después:

1. Abre el popup → `Settings`
2. `Import/Export Prompts` → `Upload Prompts`
3. Carga `prompts_universales_v2026_prompster.json`
4. Opera con tu carácter gatillo y las claves: `0`, `a`, `ñ`, `a-b-testing`, `prompting-zero-shot-limpio`, etc.

### Opción 3 · Skill en Claude Code

```bash
# Copiar skill al directorio Claude
cp -r skills/aprender-aprehender-revolucionar ~/.claude/skills/

# La skill se registra automáticamente
# Invocarla con frases naturales:
#   "ayúdame a aprender Rust desde cero"
#   "voy a presentar QBR el viernes"
#   "deep research sobre LLMs 2026, tengo 4h"
#   "jQuery ya no me sirve, ¿qué hago?"
```

Documentación completa: [`skills/aprender-aprehender-revolucionar/SKILL.md`](skills/aprender-aprehender-revolucionar/SKILL.md).

---

## 🧭 Filosofía MetodologIA

> *Método primero, IA después.*
> *Cadencia > intensidad.*
> *Intención antes que intensidad.*
> *Lo que era vanguardia se vuelve legado.*

**Pilares**: Ciencia Cognitiva · Pensamiento Crítico · Soberanía Profesional · Areté.

**Voces canónicas**: Diseñador · (R)Evolución · Método.
**Bloqueado**: ❌ Arquitecto · ❌ Transformación · ❌ Hacks.

Este material existe para que **personas reales** se apropien de la IA con rigor, sin caer en consumo fluido superficial. La pregunta no es *"¿qué te dijo la IA?"* sino *"¿lo puedes defender sin notas, ante hostil, bajo presión?"*.

---

## 🗂️ Trazabilidad y versiones

El [CHANGELOG](CHANGELOG.md) es el **index canónico** del material público vigente. Cada incorporación al repo queda documentada con métricas, atribución y verificaciones pasadas.

Versión vigente recomendada para **uso nuevo**: ver tabla en [CHANGELOG.md](CHANGELOG.md) §Index del material público vigente.

Aliases (`v2026_prompster`, etc.) se mantienen para compatibilidad con referencias previas.

---

## 📜 Licencia · CC BY-NC-SA 4.0

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es)

Atribución · NoComercial · CompartirIgual.

✅ **Permitido**: copiar, redistribuir, remezclar, adaptar para uso personal, educativo sin fines de lucro, e interno corporativo (con atribución).

❌ **NO permitido sin licencia comercial**: vender, incluir en productos pagos, usar en consultoría que cobra al cliente, distribuir con publicidad monetizada.

🔗 **Uso comercial**: contacta a Javier Montaño · MetodologIA.

Si remezclas, **mantén CC BY-NC-SA 4.0** en tu obra derivada e indica los cambios significativos respecto al original.

---

## 🤝 Atribución mandatory

Si compartes, modificas, redistribuyes o construyes sobre este material:

```
Basado en "Material Educativo MetodologIA 2026"
Diseñado por Javier Montaño · Founder/CEO MetodologIA
https://github.com/JaviMontano/material-educativo-metodologia
Licencia: CC BY-NC-SA 4.0
```

---

## 🌐 Más sobre MetodologIA

- Sitio MAO: https://github.com/JaviMontano/mao-site
- Founder: Javier Montaño

---

> *MetodologIA · 2026 · CC BY-NC-SA 4.0*
> *Infraestructura práctica de apropiación de IA para personas reales.*

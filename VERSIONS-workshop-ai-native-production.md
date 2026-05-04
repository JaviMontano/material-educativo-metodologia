# Workshop AI Native Production · Registro de versiones

> Bitácora de versiones del bundle de playbooks MetodologIA derivados del workshop comercial **"De la Idea a Producción con IA: Velocidad Visual + Rigor Técnico"** (2 sesiones · 6 h efectivas).
> Naming convention: `playbook-{tema}-v{YYYY.MM.PATCH}.html`

---

## v2026.04 · 25 abr 2026 · Versión inicial

**Estado:** Vigente · publicable.

### Entregables de esta versión

| Tipo | Archivo | Tamaño | Propósito |
|---|---|---|---|
| **Playbook · Vagaje I/II** | `playbook-vibe-coding-velocidad-visual-v2026.04.html` | ~127 KB · 12 secciones | Día 1 del workshop. Tesis: 1–2 features/día E2E con AI como copiloto. Stack v0/Cursor/Bolt/Lovable/Claude Code, métricas senior, anti-patrones del *vibe-hangover*, hardening, 5 katas Shu-Ha-Ri. |
| **Playbook · Vagaje II/II** | `playbook-bmad-rigor-tecnico-v2026.04.html` | ~127 KB · 12 secciones | Día 2 del workshop. Tesis: el *agentic engineering* corrige el vibe-hangover. PEV framework, 10 prácticas BMAD, 6 roles agénticos, MCP, 5 katas, 5 anti-patrones. Casos Stripe / Shopify / Advolve / TELUS. |

### Investigación de respaldo

- **Notebook NotebookLM**: `Workshop AI Native Production - Research Hub 2026` (`a390694a-6f9a-4b73-9102-bb7b87a96085`).
- **Fuente primaria**: PDF original del workshop (`AI_Native_Production.pdf` · 1 archivo · los 2 PDFs adjuntos por el usuario eran idénticos).
- **Deep Research** vía NotebookLM MCP: 67 fuentes web (académicas, industria, blogs senior 2024–2026).
- **Reporte académico**: 35.242 caracteres · _"The AI-Native Software Revolution: Vibe Coding, Agentic Engineering, and the Future of Programmable Intent (2024–2026)"_.
- **Cross-notebook query** con notebooks ya existentes:
  - `BMAD Method — D7: GenAI Applications` (112 fuentes específicas BMAD)
  - `PROD-NotebookLM — Caracterización de Producto` (144 fuentes)
  - `MET-Autoestudio-IA-Blueprint` (68 fuentes)
- **Etiquetas de evidencia**: `[DOC]` `[INFERENCIA]` `[SUPUESTO]` `[CONTEXTO]` aplicadas en cada claim numérico/factual (Vibe: 115 tags DOC · BMAD: 61 tags DOC).

### Anatomía del bundle

Los dos playbooks son **complementarios y cross-linkeados**:

```
playbook-vibe-coding-velocidad-visual-v2026.04.html
   ↓ (link en hero, anti-patrones §07, FAQ §11, footer)
playbook-bmad-rigor-tecnico-v2026.04.html
   ↓ (link en hero, FAQ §11, footer)
```

La tesis integradora: _"Vibe coding sin BMAD = velocidad que se traduce en deuda técnica en 90 días. BMAD sin vibe coding = sistemas correctos pero lentos al pensamiento. Los dos juntos = velocidad sustentable."_

### Características compartidas

- **Bilingüe ES/EN** con toggle en navbar y persistencia en `localStorage` (key `pb-lang`).
- **Marca MetodologIA pura**: paleta navy (#122562) · gold (#FFD700) · info-blue (#137DC5) · dark (#1F2833) · lilac (#BBA0CC).
- **Tipografía**: Poppins (display) + Montserrat (body) + Trebuchet MS (notas).
- **Mobile-first responsive**: breakpoints 768px y 1020px.
- **Print-ready**: `@media print` oculta nav y toggle, fuerza español.
- **Accesibilidad**: `:focus-visible` con outline gold, `role="banner"`, skip-link, ARIA labels en toggle.
- **Self-contained HTML**: sólo Google Fonts como recurso externo; el resto inline.
- **Validación estructural**:
  - 0 placeholders sin reemplazar (`{{...}}`).
  - Bilingüe perfectamente balanceado (Vibe 435=435 · BMAD 412=412 spans `.es`/`.en`).
  - HTML balanceado: secciones, divs y tablas matched.

### Justificación del pivote metodológico

> El plan inicial contemplaba usar el plugin `playbook-forge` v6 con modo `ecosystem`. En la fase de exploración se detectó que `compose-manifest.js` y `golden-manifest.json` están **hard-coded al ecosistema Jarvis P0-P13 de Sofka Technologies** (gem names: LaForja, LaReu, LaVuelta, ElRepo, LaInfo). Forzar el workshop genérico Vibe Coding/BMAD ahí habría producido un Frankenstein de marca (Sofka + MetodologIA + Workshop), violando la regla 3 del usuario _"NEVER mix brands"_.
>
> **Pivote ejecutado**: usar el playbook `playbook-workshop-discovery-ai-native-v2026.04.2.html` ya publicado por el usuario como template canónico de la marca MetodologIA. Esta decisión:
> - Mantiene la marca MetodologIA pura.
> - Reutiliza tokens, fonts, y patrones de classes ya en producción.
> - Acelera la generación (no se reinventa branding).
> - Asegura cohesión visual con el resto del repositorio.

---

## Convenciones

- **Versionado**: `vYYYY.MM.PATCH` — `v2026.04` = año 2026, abril, primera publicación.
- **Brand lock**: los archivos en este directorio son MetodologIA. Cero contaminación con otras marcas (regla CLAUDE.md).
- **Bilingüe**: todos los entregables soportan toggle ES/EN con persistencia en `localStorage`.
- **Print-ready**: `@media print` oculta nav/toggle.
- **Cross-link obligatorio**: ambos playbooks deben referenciarse mutuamente (hero, FAQ, footer).

## Próximos entregables candidatos (no creados aún)

- `facilitator-onepager-vibe-coding-vX.html` — hoja A4 imprimible para conductor de la sesión 1.
- `facilitator-onepager-bmad-vX.html` — hoja A4 para conductor de la sesión 2.
- `pre-read-template-workshop-ai-native-production-vX.html` — plantilla del paquete de pre-lectura T-48 h del bundle completo.
- `acta-template-workshop-ai-native-production-vX.md` — plantilla markdown del acta de la sesión.
- `nlm-research-export-workshop-ai-native-vX.md` — export del reporte académico de research (35K caracteres) como apéndice citable.

---

*Construido por profesionales · Human First, AI-Next · CC BY-NC-SA 4.0 · Por Javier Montaño · metodologia.info*

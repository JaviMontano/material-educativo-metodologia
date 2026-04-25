# MetodologIA Onboarding Kit — Ciclo 1 2026

Kit consolidado, armonizado y **100% comprensivo** de documentos de onboarding para el Programa de Empoderamiento en Power Skills. Versión **2.3.0** ejecuta el rebuild dirigible de la Biblioteca Universal (v2026) y el Playbook de Prompting (v2): onboarding "Empieza aquí", favoritos persistentes, búsqueda fuzzy, quiz de nivel, glosario ampliado a 24 términos, sección de debugging con 12 síntomas, rúbrica 5×3, comparativa de modelos 2026, lab de prompt injection, FAQ EXPERTO con 15 preguntas, 5 mini-packs por vertical, tabs en modal con output esperado y bridges cross-doc playbook↔biblioteca. La base v2.1 (kinetic typography, animated counters, role-cards, manifesto footer) se preserva sin regresiones.

## Documentos (6)

| Documento | Descripción |
|-----------|-------------|
| `cartilla-onboarding-programa-v11.html` | Cartilla principal del programa — 3 técnicas de procesamiento (Mind Mapping, Ensayo & Síntesis, Feynman) + 6 workflows prácticos + 35 modales |
| `cartilla-google-drive-v2.html` | Guía de onboarding a Google Drive — estructura, permisos, prompts de búsqueda, troubleshooting |
| `playbook-aprender-a-aprender-v6.html` | Playbook de aprendizaje — 8 escalas, 32 técnicas, 14 prompts (incluye meta-prompts M1-M4), arquetipos NotebookLM, rutinas, estándares, FAQ |
| `playbook-prompting-universal-v2.html` | Playbook de prompting universal v2 — quiz de nivel + 25 capítulos: fundamentos, glosario de 24 términos, anatomía SPEC, rúbrica 5×3, modelos 2026, debugging de 12 síntomas, 6 técnicas élite, lab de prompt injection, 15 FAQs EXPERTO, mini-packs por vertical, bridges a la biblioteca |
| `playbook-deep-research-ia-v1.html` | Playbook de investigación profunda — framework de 6 fases (Define → Blueprint → Triangulate → Synthesize → Fact-Check → Document), 5 prompts SPEC, 25+ FAQs |
| `biblioteca-universal-prompting-v2026.html` | Biblioteca universal de prompting v2026 — corpus preservado + artefactos canónicos + métodos aplicables, favoritos con migración desde v7, búsqueda operativa y devoted Prompster con comando limpio |

## Estructura

```
dist/                       → HTML autocontenidos listos para distribución + datasets `prompts_universales_v2026.*`
src/css/design-system.css   → CSS canónico (Layers 1-12, includes kit-pro-max)
src/css/kit-pro-max.css     → Layer 12 standalone (UI Pro-Max v2.1)
src/js/engine.js            → JS canónico (modules 1-16, includes pro-max)
src/js/kit-pro-max.js       → Modules 13-16 standalone (count-up, kinetic, back-top, sibling)
src/templates/              → Reference HTML snippets para inlining
src/content/                → Briefs y complementos editoriales del kit
                              · biblioteca-v2026-consolidacion.md
                              · biblioteca-v2026-metodos-202.md
                              · playbook-prompting-complementario-v1.md
src/tools/                  → Scripts Node reproducibles para regenerar prompts_universales.js
                              · enrich-prompts.mjs        (poblar keywords + level + version)
                              · inject-new-prompts.mjs    (añadir 22 prompts del expansion set)
                              · add-example-outputs.mjs   (poblar example_output en core)
archive/                    → Versiones originales preservadas (v1.0 + v2.0 sources + v2.1 + v2.3 pre-rebuild)
PLAN-MEJORAS-vNEXT.md       → Plan completo del rebuild v2.3 (8 secciones, 23 tareas, snippets, verificaciones)
```

## Design System

- Neo-Swiss Clean · Mobile-first · Dark mode · Bilingual ES/EN
- Poppins (titulares) · Montserrat (cuerpo) · Lucide Icons
- Paleta: Navy `#122562` · Gold `#FFD700` · Blue `#137DC5`
- WCAG 2.5.8 (touch targets ≥ 44×44px) · `env(safe-area-inset-bottom)` · scroll-snap proximity
- CSS Layers (12, incluye `kit-pro-max`) · `content-visibility: auto` · IntersectionObserver reveals

## UI Pro-Max v2.1 (Layer 12)

Componentes compartidos en los 6 docs:
- **Hero**: narrative pre-headline + kinetic accent typography + animated icon-stats con count-up
- **Footer**: manifesto editorial + 6-card sibling grid (auto-highlight current doc) + facilitator card + version meta
- **Visualización**: role-cards (permisos), 14-card module preview, 5-step program timeline, 6-node Deep Research journey, 7-card source grid, 8-step Aprender ladder, 2×2 SPEC quadrant
- **Stickies**: back-to-top button con keyboard focus
- **Reduced-motion**: animaciones desactivadas vía `@media (prefers-reduced-motion: reduce)`

## Armonización

- **SPEC** (Situación | Pedido | Ejecución | Criterio) como framework canónico de prompting en todo el kit
- Glosario unificado: prompt stacking (anidamiento recursivo) · chaining (encadenamiento secuencial) · meta-prompting · Pipeline 0-9 · Protocolo Metacognitivo (Interpreta > Planifica > Ejecuta)
- Cross-references bidireccionales entre los 6 documentos
- Nomenclatura de fases alineada (adquirir → retener → soltar)

## Licencia

© 2026 MetodologIA. CC BY-NC-SA 4.0

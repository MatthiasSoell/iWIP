# AI Project Context – SciBlog iWIP

Scope: kompakter Systemueberblick ueber Repository, Architektur, Kerntechnologien und zentrale Dokumentation fuer AI-Agenten

Purpose: quick system overview for AI agents (Copilot, ChatGPT).

Project type:
Hugo static website + blog + presentation system + didactic planning agent.

Core technologies:
- Hugo static site generator
- PaperMod blog theme
- reveal-hugo / reveal.js for presentations
- GitHub Pages hosting
- GitHub Actions deployment

Content structure:
- content/blog → blog posts and OER materials
- content/praesentation → presentation versions of content
- content/impressum / datenschutz / hinweise → site pages

Agent structure:
- AGENTS.md and .github/copilot-instructions.md → thin platform adapters
- project_governance/plan_core.md and kdm_core.md → process and dialog cores
- ai_agents/master_agent.md and didaktisches_qualitaetsmodell_core.md → role and didactic quality core
- prompts/plan.md → normal planning entry point
- templates, final checks, full DQM and external handoff → loaded only when required by PLAN-Core
- benchmark/ and docs/agent_development/ → development, QA and historical evidence; not normal runtime context

Styling architecture:
- assets/css/extended/00_design_tokens.css → design tokens
- assets/css/extended/10_custom.css → blog components
- assets/css/extended/20_custom_callouts.css → blog callouts
- static/css/custom_reveal.css → presentation styling

Architecture rules:
- modify existing CSS before creating new rules
- prefer Hugo / PaperMod / reveal solutions over custom CSS
- strict separation between blog CSS and reveal CSS
- no hardcoded colors outside design tokens

Documentation:
- project_governance/css_architecture.md → CSS system
- project_governance/repo_architecture.md → repository structure
- project_governance/content_emoji_policy.md → content emoji conventions
- project_governance/ai_copilot_instructions.md → AI editing rules

Goal of the project:
Open science blog publishing teaching materials as OER, supported by a
dialogical didactic planning agent.

System Context Diagram:

```mermaid
flowchart TD

A[GitHub Repository: iWIP]

A --> B[Hugo Static Site Generator]
A --> L[Didactic Planning Agent]
A --> M[Development and QA]

B --> C1[Blog System<br>PaperMod Theme]
B --> C2[Presentation System<br>reveal-hugo / reveal.js]

C1 --> D1[content/blog]
C2 --> D2[content/praesentation]

B --> E1[assets/css/extended<br>Design Tokens + Blog CSS]
B --> E2[static/css/custom_reveal.css<br>Presentation CSS]

B --> F[Hugo Modules]

F --> G1[PaperMod]
F --> G2[reveal-hugo]

B --> H[GitHub Actions Build]

H --> I[GitHub Pages Deployment]

I --> J[Public Website<br>SciBlog iWIP]

J --> K1[Blog Articles]
J --> K2[OER Materials]
J --> K3[Reveal Presentations]

L --> L1[PLAN and KDM Cores]
L --> L2[DQM and Master Agent]
L --> L3[Lazy Production Tasks]

M --> M1[benchmark]
M --> M2[docs/agent_development]

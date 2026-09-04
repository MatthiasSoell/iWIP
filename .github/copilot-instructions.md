# Copilot Instructions – SciBlog iWIP

Diese Datei ist ein duenn gehaltener GitHub-Copilot-Adapter. Sie enthaelt keine
eigene didaktische oder prozessuale Steuerlogik.

Fuer didaktische Planung wird derselbe kanonische Kern wie auf anderen
Plattformen geladen:

1. `project_governance/plan_core.md`
2. `project_governance/kdm_core.md`
3. `ai_agents/master_agent.md`
4. `ai_agents/didaktisches_qualitaetsmodell_core.md`
5. `prompts/plan.md`

Lazy Loading fuer Produktion, FINAL, vollstaendiges DQM, Planning Journal und
Tasks folgt ausschliesslich dem PLAN-Core. Es gibt keinen Research Adapter.

Die folgenden Hinweise gelten zusaetzlich fuer Entwicklung und QA; sie sind
keine Laufzeit-Steuerlogik.

Follow the project governance files:

- project_governance/content_emoji_policy.md

Load the following governance files only when relevant for Technik-, QA-, FINAL-, Workflow- oder Architekturfragen (not as early mandatory context for normal `/PLAN` tasks):

- project_governance/ai_copilot_instructions.md
- project_governance/css_architecture.md
- project_governance/repo_architecture.md
- project_governance/development_workflow.md

Key principles:

- modify existing code before creating new rules
- prefer Hugo / PaperMod / reveal-hugo solutions
- respect CSS ownership defined in css_architecture.md
- do not mix blog CSS and reveal CSS
- avoid CSS hacks and unnecessary !important

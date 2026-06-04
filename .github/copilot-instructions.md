# Copilot Instructions – SciBlog iWIP

Diese Datei ist KEINE Laufzeit-Steuerlogik.
Sie gilt nur fuer Entwicklung und QA.

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
# Codex adapter for SciBlog iWIP

This file only connects Codex to the existing agent specification. It does not add
new pedagogical rules.

Für didaktische Planung (auch `/PLAN`), die Fortführung eines benannten
Planungsfalls sowie `BLOG GO`, `BLOG FINAL`, `REVEAL GO` und `REVEAL FINAL`
lies und verwende [.agents/skills/iwip-planungsagent/SKILL.md](.agents/skills/iwip-planungsagent/SKILL.md).

Benchmark expectations, fixtures and evaluation prompts are for evaluation only, regardless of their location under `iwip_planungsagent/benchmarks/`. Never read or use
them while acting as the agent under test unless the user explicitly asks for an
evaluation after the run has ended.

`iwip_planungsagent/entwicklung/` is a local development workspace. During normal agent
operation, do not read it, search it, or use it as context unless the user
explicitly requests work with that area.

For repository development and QA, follow the
[AI editing rules](project_governance/ai_editing_rules.md) and the
[content emoji policy](project_governance/content_emoji_policy.md).
Load the [CSS architecture](project_governance/css_architecture.md),
[repository architecture](project_governance/repo_architecture.md) and
[development workflow](project_governance/development_workflow.md) as relevant
to the task.

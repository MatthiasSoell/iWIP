# Codex adapter for SciBlog iWIP

This file only connects Codex to the existing agent specification. It does not add
new pedagogical rules.

Für didaktische Planung (auch `/PLAN`), die Fortführung eines benannten
Planungsfalls sowie `BLOG GO`, `BLOG FINAL`, `REVEAL GO` und `REVEAL FINAL`
lies und verwende [.agents/skills/iwip-planungsagent/SKILL.md](.agents/skills/iwip-planungsagent/SKILL.md).

Benchmark expectations, fixtures and evaluation prompts are for evaluation only, regardless of their location under `iwip-planungsagent-benchmarks/`. Never read or use
them while acting as the agent under test unless the user explicitly asks for an
evaluation after the run has ended.

`agent_entwicklung/` is a local development workspace. During normal agent
operation, do not read it, search it, or use it as context unless the user
explicitly requests work with that area.

For repository development and QA, continue to follow
`.github/copilot-instructions.md` and load only the governance files relevant to the
task.

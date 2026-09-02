# Codex adapter for SciBlog iWIP

This file only connects Codex to the existing agent specification. It does not add
new pedagogical rules.

For normal didactic planning requests, including `/PLAN`, read and follow only
these B1.1 core files:

1. `project_governance/plan_core.md`
2. `ai_agents/master_agent.md`
3. `ai_agents/didaktisches_qualitaetsmodell.md`
4. `prompts/plan.md`

The PLAN core has priority if these files conflict. Keep the complete DQM loaded.
For normal `/PLAN`, the two legacy references inside the unchanged DQM to
`project_governance/agent_contract.md` resolve to `project_governance/plan_core.md`;
they do not trigger loading the B0 contract.

Load production and finalization details only at their gates:

- at `BLOG GO`: `ai_agents/templates/blog_template.md`
- at `BLOG FINAL`: additionally `prompts/check.md`, `prompts/literatur.md`,
  `prompts/content_emojis_blog.md`, and the references they explicitly require
- at `REVEAL GO`: `ai_agents/templates/reveal_template.md`
- at `REVEAL FINAL`: additionally `prompts/check.md`,
  `prompts/content_emojis_reveal.md`, and the references they explicitly require

OER/OERSI metadata rules are loaded only with the blog template or a relevant
publication task. The B0 research rules remain preserved in
`project_governance/agent_contract.md`, but the Research adapter is currently
inactive and must not be loaded for normal `/PLAN`, GO, or FINAL work.

Files under `benchmark/evaluations/` contain test expectations. Never read or use
them while acting as the agent under test unless the user explicitly asks for an
evaluation after the run has ended.

For repository development and QA, continue to follow
`.github/copilot-instructions.md` and load only the governance files relevant to the
task.

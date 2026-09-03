# Codex adapter for SciBlog iWIP

This file only connects Codex to the existing agent specification. It does not add
new pedagogical rules.

For normal didactic planning requests, including `/PLAN`, read and follow only
these core files:

1. `project_governance/plan_core.md`
2. `project_governance/kdm_core.md`
3. `ai_agents/master_agent.md`
4. `ai_agents/didaktisches_qualitaetsmodell_core.md`
5. `prompts/plan.md`

The PLAN core defines process, permitted actions, gates, and governance. The KDM
core defines dialog and decision form. The DQM core defines didactic quality and
diagnosis. The PLAN core has priority if these files conflict. The complete DQM
is loaded only under the lazy-loading conditions defined in the PLAN core.

Load a fallbezogene `planning_journal.md` only when the user explicitly names
an existing persistent planning case or asks to resume it. Do not search for or
load planning journals during ordinary `/PLAN` turns; creation and maintenance
follow the activation and lifecycle rules in the PLAN core.

Load production and finalization details only at their gates:

- at `BLOG GO`: `ai_agents/templates/blog_template.md`
- at `BLOG FINAL`: additionally `prompts/check.md`, `prompts/literatur.md`,
  `prompts/content_emojis_blog.md`, and the references they explicitly require
- at `REVEAL GO`: `ai_agents/templates/reveal_template.md`
- at `REVEAL FINAL`: additionally `prompts/check.md`,
  `prompts/content_emojis_reveal.md`, and the references they explicitly require

Load `tasks/external_handoff.md` only when a concrete external handoff is
activated under the conditions in the PLAN core. Do not load the task for a
normal `/PLAN` turn or merely to suggest a potentially useful external
specialized service.

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

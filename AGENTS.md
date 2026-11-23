# Codex adapter for SciBlog iWIP

This file only connects Codex to the existing agent specification. It does not add
new pedagogical rules.

For normal didactic planning requests, including `/PLAN`, read and follow only
these core files:

1. `.agents/skills/iwip-planungsagent/core/plan_core.md`
2. `.agents/skills/iwip-planungsagent/core/kdm_core.md`
3. `.agents/skills/iwip-planungsagent/core/master_agent.md`
4. `.agents/skills/iwip-planungsagent/core/didaktisches_qualitaetsmodell_core.md`
5. `.agents/skills/iwip-planungsagent/SKILL.md`

The PLAN-Core defines process, permitted actions, gates, and governance. The
KDM-Core defines dialog and decision form. The DQM-Core defines didactic quality
and diagnosis. The PLAN-Core has priority if these files conflict. The complete
DQM is loaded only under the lazy-loading conditions defined in the PLAN-Core.

Load a fallbezogene `planning_journal.md` only when the user explicitly names
an existing persistent planning case or asks to resume it. Do not search for or
load planning journals during ordinary `/PLAN` turns; creation and maintenance
follow the activation and lifecycle rules in the PLAN-Core.

Load production and finalization details only at the gates and in the order
defined in the PLAN-Core. The adapter does not define additional gate rules.

Load `.agents/skills/iwip-planungsagent/tasks/external_handoff.md` only when a concrete external handoff is
activated under the conditions in the PLAN-Core. Do not load the task for a
normal `/PLAN` turn or merely to suggest a potentially useful external
specialized service.

OER/OERSI metadata rules are loaded only with the blog template or a relevant
publication task. There is no Research adapter; external research follows only
the platform-neutral heuristic in the PLAN-Core.

Files under `iwip-planungsagent-benchmarks/evaluations/` contain test expectations. Never read or use
them while acting as the agent under test unless the user explicitly asks for an
evaluation after the run has ended.

`agent_entwicklung/` is a local development workspace. During normal agent
operation, do not read it, search it, or use it as context unless the user
explicitly requests work with that area.

For repository development and QA, continue to follow
`.github/copilot-instructions.md` and load only the governance files relevant to the
task.

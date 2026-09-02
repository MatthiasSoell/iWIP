# Codex adapter for SciBlog iWIP

This file only connects Codex to the existing agent specification. It does not add
new pedagogical rules.

For didactic planning requests, including `/PLAN`, read and follow these files:

1. `project_governance/agent_contract.md`
2. `project_governance/low_noise_response_patterns.md`
3. `ai_agents/master_agent.md`
4. `ai_agents/didaktisches_qualitaetsmodell.md`
5. `prompts/plan.md`

The contract has priority if the files conflict. Load blog and Reveal templates only
at the gates defined by the contract.

Files under `benchmark/evaluations/` contain test expectations. Never read or use
them while acting as the agent under test unless the user explicitly asks for an
evaluation after the run has ended.

For repository development and QA, continue to follow
`.github/copilot-instructions.md` and load only the governance files relevant to the
task.


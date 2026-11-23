SKILL_DIR := .agents/skills/iwip-planungsagent

.PHONY: qa qa-agent qa-prompts qa-markdown qa-hugo

qa: qa-agent

qa-agent: qa-prompts qa-markdown qa-hugo
	@echo "QA completed successfully."

qa-prompts:
	@python3 scripts/check_paket.py
	@test -f $(SKILL_DIR)/publikation/check.md
	@test -f $(SKILL_DIR)/publikation/literatur.md
	@echo "Prompt files OK."

qa-markdown:
	markdownlint-cli2 --config .markdownlint-cli2.jsonc README.md "$(SKILL_DIR)/**/*.md" "project_governance/**/*.md"
	@echo "Markdownlint OK (markdownlint-cli2)."

qa-hugo:
	hugo --quiet
	@echo "Hugo build OK."

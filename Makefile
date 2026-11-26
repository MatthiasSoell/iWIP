SKILL_DIR := .agents/skills/iwip-planungsagent

.PHONY: qa qa-agent qa-prompts qa-journal qa-markdown qa-hugo qa-navigation

qa: qa-agent

qa-agent: qa-prompts qa-journal qa-markdown qa-navigation qa-hugo
	@echo "QA completed successfully."

qa-prompts:
	@python3 scripts/check_paket.py
	@test -f $(SKILL_DIR)/publikation/check.md
	@test -f $(SKILL_DIR)/publikation/literatur.md
	@echo "Prompt files OK."

qa-markdown:
	markdownlint-cli2 --config .markdownlint-cli2.jsonc README.md "$(SKILL_DIR)/**/*.md" "project_governance/**/*.md"
	@echo "Markdownlint OK (markdownlint-cli2)."

qa-journal:
	@python3 scripts/test_journal.py
	@python3 scripts/test_check_h03_journal.py

qa-navigation:
	@python3 scripts/test_check_navigation.py

qa-hugo:
	hugo --quiet
	python3 scripts/check_navigation.py public/index.html public --shared
	python3 scripts/check_navigation.py public/praesentation/oer/warum_oer/index.html public --shared
	@echo "Hugo build OK."

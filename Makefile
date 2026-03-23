.PHONY: qa qa-agent qa-prompts qa-markdown qa-hugo

qa: qa-agent

qa-agent: qa-prompts qa-markdown qa-hugo
	@echo "QA completed successfully."

qa-prompts:
	@test -f prompts/create.md
	@test -f prompts/check.md
	@test -f prompts/literatur.md
	@echo "Prompt files OK."

qa-markdown:
	@if command -v markdownlint-cli2 >/dev/null 2>&1; then \
		markdownlint-cli2 --config .markdownlint-cli2.jsonc README.md "ai_agents/**/*.md" "prompts/**/*.md" "project_governance/**/*.md"; \
		echo "Markdownlint OK (markdownlint-cli2)."; \
	elif command -v markdownlint >/dev/null 2>&1; then \
		files="README.md $$(find ai_agents prompts project_governance -type f -name '*.md' | tr '\n' ' ')"; \
		markdownlint --config .markdownlint.jsonc $$files; \
		echo "Markdownlint OK (markdownlint)."; \
	else \
		echo "Markdownlint skipped (no markdownlint tool installed)."; \
	fi

qa-hugo:
	hugo --quiet
	@echo "Hugo build OK."

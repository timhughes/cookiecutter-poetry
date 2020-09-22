#
# vim:ft=make
# Makefile
# Tim Hughes, 2020-09-08 20:41
#
.DEFAULT_GOAL := help
.PHONY: test help


help:  ## these help instructions
	@sed -rn 's/^([a-zA-Z_-]+):.*?## (.*)$$/"\1" "\2"/p' < $(MAKEFILE_LIST)|xargs printf "make %-20s# %s\n"

install: ## Run `poetry install`
	poetry install

lint: ## Runs bandit and black in check mode
	poetry run black . --check --target-version=py36
	@echo '-------------------------------'
	poetry run bandit -r src

test: private ## run pytest with coverage
	poetry run pytest --cov tests

build: install lint test ## run `poetry build` to build source distribution and wheel
	poetry build

format: ## Formats you code with Black
	poetry run black . --target-version=py36

private: # undocumented, for internal usage only
	@true

showdeps: ## run poetry to show deps
	@echo "CURRENT:"
	poetry show --tree
	@echo
	@echo "LATEST:"
	poetry show --latest



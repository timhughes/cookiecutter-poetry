#
# vim:ft=make
# Makefile
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

test: hidden ## run pytest with coverage
	poetry run pytest --cov tests

build: install lint test ## run `poetry build` to build source distribution and wheel
	poetry build
	
pyinstaller: install lint test ## Create a binary executable using pyinstaller
	poetry run pyinstaller src/{{cookiecutter.module_name}}/cli.py --onefile --name {{ cookiecutter.project_slug }}

format: ## Formats you code with Black
	poetry run black . --target-version=py36

hidden: # example undocumented, for internal usage only
	@true

showdeps: ## run poetry to show deps
	@echo "CURRENT:"
	poetry show --tree
	@echo
	@echo "LATEST:"
	poetry show --latest

notebook: ## run the jupyter-lab server
	poetry run jupyter-lab || { echo "Jupyter-lab not installed:\n\n poetry add jupyterlab"; exit 1; }

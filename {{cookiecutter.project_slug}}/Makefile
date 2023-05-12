#
# vim:ft=make
# Makefile
#
.DEFAULT_GOAL := help
.PHONY: test help


help:  ## these help instructions
	@sed -rn 's/^([a-zA-Z_-]+):.*?## (.*)$$/"\1" "\2"/p' < $(MAKEFILE_LIST)|xargs printf "make %-20s# %s\n"

hidden: # example undocumented, for internal usage only
	@true

pydoc: ## Run a pydoc server and open the browser
	poetry run python -m pydoc -b

install: ## Run `poetry install`
	poetry install

showdeps: ## run poetry to show deps
	@echo "CURRENT:"
	poetry show --tree
	@echo
	@echo "LATEST:"
	poetry show --latest

lint: ## Runs bandit and black in check mode
	poetry run black . --check --target-version=py311
	@echo '-------------------------------'
	poetry run bandit -r src

format: ## Formats you code with Black
	poetry run black . --target-version=py311

test: hidden ## run pytest with coverage
	poetry run pytest --cov {{cookiecutter.module_name }}

build: install lint test ## run `poetry build` to build source distribution and wheel
	poetry build

{%- if cookiecutter.command_line_interface != "no cli" %}
pyinstaller: install lint test ## Create a binary executable using pyinstaller
	poetry run pyinstaller src/{{ cookiecutter.module_name }}/cli.py --onefile --name {{ cookiecutter.project_slug }}

{%- endif %}
{%- if cookiecutter.use_jupyterlab == "y" %}
jupyter: ## run the jupyter-lab server
	poetry run jupyter-lab

{%- endif %}
run: ## run `poetry run {{ cookiecutter.project_slug }}`
	poetry run {{ cookiecutter.project_slug }}

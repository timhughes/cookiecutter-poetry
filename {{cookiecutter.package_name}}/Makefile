#
# vim:ft=make
# Makefile
#
.DEFAULT_GOAL := help
.PHONY: test help docs_build docs


help:  ## these help instructions
	@sed -rn 's/^([a-zA-Z_-]+):.*?## (.*)$$/"\1" "\2"/p' < $(MAKEFILE_LIST)|xargs printf "make %-20s# %s\n"

hidden: # example undocumented, for internal usage only
	@true

pydoc: ## Run a pydoc server and open the browser
	poetry run python -m pydoc -b

docs_build: ## Build the documentation
	poetry run sphinx-apidoc --module-first -o docs/api src/example_project/
	poetry run sphinx-build --color docs docs/_build

docs: ## Build and serve the documentation with live reloading on file changes
	poetry run sphinx-apidoc --module-first -o docs/api src/example_project/
	poetry run sphinx-autobuild --open-browser docs docs/_build

install: ## Run `poetry install`
	poetry install
	
showdeps: ## run poetry to show deps
	@echo "CURRENT:"
	poetry show --tree
	@echo
	@echo "LATEST:"
	poetry show --latest

lint: ## Runs black, isort, bandit, flake8 in check mode
	poetry run black --check .
	poetry run isort --check .
	poetry run bandit -r src
	poetry run flake8 src tests
	poetry run ruff check .

format: ## Formats you code with Black
	poetry run isort .
	poetry run black .

test: hidden ## run pytest with coverage
	poetry run pytest -v --cov {{ cookiecutter.module_name }}

build: install lint test ## run `poetry build` to build source distribution and wheel
	poetry build

bumpversion: build ## bumpversion
	poetry run bump2version --tag --current-version $$(git describe --tags --abbrev=0) --tag-name '{new_version}' patch
	git push
	git push --tags 

{%- if cookiecutter.command_line_interface != "no cli" %}
pyinstaller: install lint test ## Create a binary executable using pyinstaller
	poetry run pyinstaller src/{{ cookiecutter.module_name }}/cli.py --onefile --name {{ cookiecutter.package_name }}

{%- endif %}
{%- if cookiecutter.use_jupyterlab == "y" %}
jupyter: ## run the jupyter-lab server
	poetry run jupyter-lab

{%- endif %}
run: ## run `poetry run {{ cookiecutter.package_name }}`
	poetry run {{ cookiecutter.package_name }}

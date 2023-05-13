[![CI Tests](https://github.com/timhughes/cookiecutter-poetry/actions/workflows/ci-tests.yml/badge.svg)](https://github.com/timhughes/cookiecutter-poetry/actions/workflows/ci-tests.yml)

# cookiecutter-poetry

Cookiecutter template configured with the following:

- poetry
- pytest
- black
- bandit
- pyinstaller
- jupyterlab
- click

A Makefile has been included so you don't have to remember commands.

## Usage:

    cookiecutter https://github.com/timhughes/cookiecutter-poetry.git

eg:

    $ cookiecutter https://github.com/timhughes/cookiecutter-poetry.git
    You've downloaded /home/thughes/.cookiecutters/cookiecutter-poetry before. Is it okay to delete and re-download it? [yes]:
    author [Tim Hughes]:
    email [thughes@thegoldfish.org]:
    github_user [timhughes]:
    project_slug [example-project]:
    module_name [example_project]:
    short_description [A simple application]:
    version [0.0.1]:
    Select license:
    1 - MIT
    2 - BSD-3-Clause
    3 - GPL-3.0-or-later
    4 - Proprietary
    Choose from 1, 2, 3, 4 [1]:
    Select command_line_interface:
    1 - click
    2 - no cli
    Choose from 1, 2 [1]:
    use_jupyterlab [n]:
    add_badges [y]:

Access the poetry commands as usual:

    $ poetry add requests
    Using version ^2.25.1 for requests

    Updating dependencies
    Resolving dependencies... (0.3s)

    Writing lock file

    Package operations: 5 installs, 0 updates, 0 removals

      • Installing certifi (2020.12.5)
      • Installing chardet (4.0.0)
      • Installing idna (2.10)
      • Installing urllib3 (1.26.3)
      • Installing requests (2.25.1)

You can then use the Makefile for other common commands

    $ make
    make help                # these help instructions
    make pydoc               # Run a pydoc server and open the browser
    make install             # Run `poetry install`
    make showdeps            # run poetry to show deps
    make lint                # Runs bandit and black in check mode
    make format              # Formats you code with Black
    make test                # run pytest with coverage
    make build               # run `poetry build` to build source distribution and wheel
    make pyinstaller         # Create a binary executable using pyinstaller
    make run                 # run `poetry run example-project`

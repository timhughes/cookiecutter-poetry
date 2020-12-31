# {{ cookiecutter.project_slug }}

{% if cookiecutter.add_badges == 'y' %}
[![PyPi](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Travis](https://img.shields.io/travis/{{ cookiecutter.github_name }}/{{ cookiecutter.project_slug }}.svg)](https://travis-ci.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_slug }})
[![Documentation](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.github_name }}/{{ cookiecutter.project_slug }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_name }}/{{ cookiecutter.project_slug }}/)
{% endif %}

{{ cookiecutter.short_description }}


## Developing

Run `make` for help

    make install             # Run `poetry install`
    make showdeps            # run poetry to show deps
    make lint                # Runs bandit and black in check mode
    make format              # Formats you code with Black
    make test                # run pytest with coverage
    make build               # run `poetry build` to build source distribution and wheel


# {{ cookiecutter.package_name }}

{% if cookiecutter.add_badges == 'y' %}
[![PyPi](https://img.shields.io/pypi/v/{{ cookiecutter.package*name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.package_name }})
[![Travis](https://img.shields.io/travis/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}.svg)](https://travis-ci.com/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }})
[![Documentation](https://readthedocs.org/projects/{{ cookiecutter.package_name | replace("\*", "-") }}/badge/?version=latest)](https://{{ cookiecutter.package_name | replace("*", "-") }}.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/)
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

{%- if cookiecutter.command_line_interface != "no cli" %}
make pyinstaller # Create a binary executable using pyinstaller
{%- endif %}
{%- if cookiecutter.use_jupyterlab == "y" %}
make jupyter # run the jupyter-lab server
{%- endif %}

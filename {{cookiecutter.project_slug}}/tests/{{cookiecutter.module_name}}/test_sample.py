# vim:fenc=utf-8
{%- if cookiecutter.command_line_interface == "click" %}
from click.testing import CliRunner
{%- endif %}
import {{cookiecutter.module_name}}
{%- if cookiecutter.command_line_interface == "click" %}
from {{cookiecutter.module_name}}.__main__ import cli
{%- endif %}


def test_true():
    assert 1 == 1
{%- if cookiecutter.command_line_interface == "click" %}


def test_click_cli():
  runner = CliRunner(mix_stderr=False)
  result = runner.invoke(cli, ['--help'])
  assert result.exit_code == 0
  assert 'Start {{cookiecutter.project_slug}} in server mode' in result.output
  assert 'Start {{cookiecutter.project_slug}} in server mode' in result.stdout
  assert '' == result.stderr

  result = runner.invoke(cli, ['--version'])
  assert result.exit_code == 0
  assert 'cli, version 0.0.1' in result.output

{%- endif %}

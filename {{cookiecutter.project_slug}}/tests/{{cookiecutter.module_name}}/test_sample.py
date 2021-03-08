# vim:fenc=utf-8
from click.testing import CliRunner
import {{cookiecutter.module_name}}
from {{cookiecutter.module_name}} import cli


def test_true():
    assert 1 == 1
{%- if cookiecutter.command_line_interface == "click" %}


def test_click_cli():
  runner = CliRunner(mix_stderr=False)
  result = runner.invoke(cli.cli, ['--help'])
  assert result.exit_code == 0
  assert 'Start {{cookiecutter.project_slug}} in server mode' in result.output
  assert 'Start {{cookiecutter.project_slug}} in server mode' in result.stdout
  assert '' == result.stderr
{%- elif cookiecutter.command_line_interface == "argparse" %}


def test_argparse_cli(capsys):
    cli.cli()
    captured = capsys.readouterr()
    assert captured.out == "Running\n"
{%- endif %}

# vim:fenc=utf-8
from click.testing import CliRunner
import {{cookiecutter.module_name}}
from {{cookiecutter.module_name}}.__main__ import cli


def test_true():
    assert 1 == 1
{%- if cookiecutter.command_line_interface == "click" %}


def test_click_cli():
  runner = CliRunner(mix_stderr=False)
  result = runner.invoke(cli, ['--help'])
  assert result.exit_code == 0
  assert 'Start example_project in server mode' in result.output
  assert 'Start example_project in server mode' in result.stdout
  assert '' == result.stderr

  result = runner.invoke(cli, ['--version'])
  assert result.exit_code == 0
  assert 'cli, version 0.0.1' in result.output
{%- elif cookiecutter.command_line_interface == "argparse" %}


def test_argparse_cli(capsys):
    cli.cli()
    captured = capsys.readouterr()
    assert captured.out == "Running\n"
{%- endif %}

# vim:fenc=utf-8

import {{cookiecutter.module_name}}
from {{cookiecutter.module_name}} import cli

def test_true():
    assert 1 == 1


def test_cli(capsys):
    cli.cli()
    captured = capsys.readouterr()
    assert captured.out == "Running\n"

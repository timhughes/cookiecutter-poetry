from contextlib import contextmanager
import shlex
import os
import sys
import subprocess
import yaml
import datetime
from cookiecutter.utils import rmtree

from click.testing import CliRunner

import importlib


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, "src", project_slug.replace("-", "_"))
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'src' in found_toplevel_files
        assert 'tests' in found_toplevel_files
        assert 'pyproject.toml' in found_toplevel_files
        assert 'README.md' in found_toplevel_files

        assert 'notebooks' not in found_toplevel_files



def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        run_inside_dir('make install', str(result.project)) == 0
        run_inside_dir('make test', str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


def test_make_help(cookies):
    with bake_in_temp_dir(cookies) as result:
        # The supplied Makefile does not support win32
        if sys.platform != "win32":
            output = check_output_inside_dir(
                'make help',
                str(result.project)
            )
            assert b"make help                # these help instructions" in \
                output


def test_bake_selecting_license(cookies):
    license_strings = {
        'MIT': 'MIT License',
        'BSD-3-Clause': 'BSD License',
        'GPL-3.0-or-later': 'GNU GENERAL PUBLIC LICENSE',
        'Proprietary': 'Proprietary and confidential',
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(
            cookies,
            extra_context={'license': license}
        ) as result:
            assert target_string in result.project.join('LICENSE').read()
            assert license in result.project.join('pyproject.toml').read()


def test_bake_with_no_console_script(cookies):
    context = {'command_line_interface': "no cli"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)
    print(project_dir)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" not in found_project_files

    pyproject_path = os.path.join(project_path, 'pyproject.toml')
    with open(pyproject_path, 'r') as pyproject_file:
        assert 'entry_points' not in pyproject_file.read()

def test_bake_with_jupyterlab(cookies):
    context = {'use_jupyterlab': "y"}
    result = cookies.bake(extra_context=context)
    found_toplevel_files = [f.basename for f in result.project.listdir()]
    assert "notebooks" in found_toplevel_files

    pyproject_path = os.path.join(result.project, 'pyproject.toml')
    
    with open(pyproject_path, 'r') as pyproject_file:
        assert 'jupyterlab' in pyproject_file.read()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(filepath):
    os.rmdir(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.use_jupyterlab }}' != 'y':
        remove_file('notebooks/.gitignore')
        remove_dir('notebooks')

    if 'no cli' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('src', '{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)


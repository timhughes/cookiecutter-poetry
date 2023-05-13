"""Sphinx configuration."""
project = "{{cookiecutter.module_name}}"
author = "{{cookiecutter.author}}"
copyright = "{{cookiecutter.copyright_year}}, {{cookiecutter.author}}"
extensions = [
    "sphinx.ext.autodoc",
    'sphinx.ext.coverage', 
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"

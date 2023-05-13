"""
{{ cookiecutter.short_description }}
"""
from __future__ import annotations

import sys
from . import app
# TODO: use try/except ImportError when
# https://github.com/python/mypy/issues/1393 is fixed
if sys.version_info < (3, 10):
    # compatibility for python <3.10
    import importlib_metadata as metadata
else:
    from importlib import metadata


module_metadata = metadata.metadata("{{ cookiecutter.project_slug }}")

__author__ = f"{module_metadata['Author']} <{module_metadata['Author-email']}>"
__version__ = module_metadata["Version"]
__version_info__ = tuple([int(num) for num in __version__.split(".")])


all = [ app ]

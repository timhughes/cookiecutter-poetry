import os
import sys
import logging


if sys.stdout.isatty():
# You're running in a real terminal
    LOG_FORMAT="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
else:
    LOG_FORMAT="%(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    level=getattr(logging, os.getenv("LOGLEVEL", "INFO").upper()),
    format=LOG_FORMAT,
    datefmt="%Y-%m-%dT%H:%M:%S"
)

logger = logging.getLogger("{{cookiecutter.module_name}}")

# set levels for other modules
logging.getLogger("urllib3").setLevel(logging.WARNING)


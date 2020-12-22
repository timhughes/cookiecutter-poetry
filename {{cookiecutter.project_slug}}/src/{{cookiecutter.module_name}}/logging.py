import os
import sys
import logging


if sys.stdout.isatty():
# You're running in a real terminal
    log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
else:
    log_format="%(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    level=getattr(logging, os.getenv("LOGLEVEL", "INFO").upper()),
    format=log_format,
    datefmt="%Y-%m-%dT%H:%M:%S"
)

logger = logging.getLogger("{{cookiecutter.module_name}}")

# set levels for other modules
logging.getLogger("urllib3").setLevel(logging.WARNING)


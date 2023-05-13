import logging

logger = logging.getLogger("{{cookiecutter.module_name}}")


class App:
    def __init__(self, settings) -> None:
        self.settings = settings

    def start(self) -> None:
        logger.info("{{cookiecutter.module_name}} Starting")

    def stop(self) -> None:
        logger.info("{{cookiecutter.module_name}} Stopping")

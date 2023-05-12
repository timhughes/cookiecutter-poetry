import logging

logger = logging.getLogger("{{cookiecutter.module_name}}")


class App:
    def __init__(self, settings) -> None:
        self.settings = settings

    def start(self) -> None:
        print("Starting")

    def stop(self) -> None:
        print("Stopping")

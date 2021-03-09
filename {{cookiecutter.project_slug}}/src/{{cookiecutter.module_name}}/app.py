
import logging
logger = logging.getLogger("{{cookiecutter.module_name}}")

class App:
    
    def __init__(self, settings):
        self.settings = settings    

    def start(self):
        logger.info("{{cookiecutter.module_name}} Starting")

    def stop(self):
        logger.info("{{cookiecutter.module_name}} Stopping")

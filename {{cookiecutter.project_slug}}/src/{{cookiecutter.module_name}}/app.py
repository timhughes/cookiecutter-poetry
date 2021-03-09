
import logging
logger = logging.getLogger("{{cookiecutter.module_name}}")

class App:
    
    def __init__(self, settings):
        self.settings = settings    

    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")


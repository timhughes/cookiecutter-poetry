import os
import sys
import yaml
import logging
import click

import {{cookiecutter.module_name}}


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=getattr(logging, os.getenv("LOGLEVEL", "INFO").upper()),
)

log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format, datefmt="%Y-%m-%dT%H:%M:%S")
logger = logging.getLogger("{{cookiecutter.module_name}}")

# set levels for other modules
logging.getLogger("urllib3").setLevel(logging.WARNING)


@click.group()
def cli():
    print("Running")
    
@cli.command()
@click.option("-v", "--verbose", count=True)
def version(verbose):
    """Displays the version"""
    click.echo("Version: %s" % {{cookiecutter.module_name}}.__version__)
    if verbose > 0:
        click.echo("Author: %s" % {{cookiecutter.module_name}}.__author__)
        click.echo("Copyright: %s" % {{cookiecutter.module_name}}.__copyright__)
        
        
@cli.command()
@click.option(
    "-c",
    "--conf",
    "--config",
    "config_file",
    required=True,
    type=click.Path(exists=True),
)
def run(config_file):
    """Start {{cookiecutter.module_name}} in server mode"""
    try:
        with open(config_file, "r") as stream:
            try:
                settings = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                click.echo(exc)
                sys.exit(1)
    except Exception as exc:
        logger.fatal(
            "Cannot load conf file '%s'. Error message is: %s" % (config_file, exc)
        )
        sys.exit(1)
    except IOError as e:
        logger.fatal("%s: %s" % (e.strerror, e.filename))
        sys.exit(1)

    try:
        settings_schema.validate(settings)
    except SchemaError as exc:
        logger.fatal(exc)
        sys.exit(1)

    # TODO: Create your application object
    s = App(settings)
    try:
        logger.info("Starting")
        # TODO: Start your application
        s.start()
    except KeyboardInterrupt:
        pass
    except:
        logger.exception("Unexpected exception")
    finally:
        logger.info("Shutting down")
        # TODO: Cleanup code
        s.stop()

    logger.info("All done")

    
if __name__ == "__main__":
    cli()

import click
from .vsummary import vsummary
from .vsearch import vsearch

@click.group()
def cli():
    pass

cli.add_command(vsummary)
cli.add_command(vsearch)

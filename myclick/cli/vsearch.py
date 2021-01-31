import click

@click.group()
def vsearch():
    pass

@vsearch.command()
def protein():
    pass

@vsearch.command()
def species():
    pass

@vsearch.command()
def vog():
    pass
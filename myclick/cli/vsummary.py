import click
from ..api import VSummary

@click.group()
def vsummary():
    """Summary commands"""
    
    pass

@vsummary.command()
@click.option("--pmin", type=click.INT, default=0)
@click.option("--pmax", type=click.INT)
@click.argument('base')
@click.argument('ids', nargs=-1, required=True)
def protein(base, ids, **options):
    """Display a summary of the given proteins"""

    VSummary(base).protein(*ids, **options)

@vsummary.command()
@click.option("--opt1", is_flag=True, help="Option1", show_default=True)
@click.option("--opt2", is_flag=True, help="Option2", show_default=True)
@click.argument('base')
@click.argument('ids', nargs=-1, required=True)
def species(base, ids, opt1, opt2):
    """Display a summary of the given species"""

    VSummary(base).species(*ids, opt1=opt1, opt2=opt2)

import click

from .metrics import metrics


@click.group()
def lab():
    pass


lab.add_command(metrics)

import click

from .metrics import metrics


@click.group()
def vm():
    pass


vm.add_command(metrics)

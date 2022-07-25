import click

from .bm import bm
from .lab import lab
from .vm import vm


@click.group()
def monitor():
    pass


monitor.add_command(bm)
monitor.add_command(lab)
monitor.add_command(vm)

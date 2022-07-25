import click

from .usage import usage


@click.group()
def all():
    pass


all.add_command(usage)

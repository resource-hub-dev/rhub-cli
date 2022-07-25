import click

from .server import server


@click.group()
def satellite():
    pass


satellite.add_command(server)

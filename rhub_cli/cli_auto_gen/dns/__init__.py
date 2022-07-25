import click

from .server import server


@click.group()
def dns():
    pass


dns.add_command(server)

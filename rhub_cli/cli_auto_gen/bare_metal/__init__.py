import click

from .handler import handler
from .host import host
from .image import image
from .provision import provision


@click.group()
def bare_metal():
    pass


bare_metal.add_command(handler)
bare_metal.add_command(host)
bare_metal.add_command(image)
bare_metal.add_command(provision)

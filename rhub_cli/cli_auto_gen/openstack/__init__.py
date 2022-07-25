import click

from .cloud import cloud
from .project import project


@click.group()
def openstack():
    pass


openstack.add_command(cloud)
openstack.add_command(project)

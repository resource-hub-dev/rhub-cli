import click

from .job import job
from .server import server
from .template import template
from .webhook_notification import webhook_notification


@click.group()
def tower():
    pass


tower.add_command(job)
tower.add_command(server)
tower.add_command(template)
tower.add_command(webhook_notification)

import click

from .cron import cron


@click.group()
def scheduler():
    pass


scheduler.add_command(cron)

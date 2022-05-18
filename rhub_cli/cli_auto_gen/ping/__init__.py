import click

from rhub_cli.api.health.rhub_api_health_ping import sync_detailed as ping_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def ping():
    pass


@ping.command()
@pass_api
def get(
    api: APIRequest,
):
    """Basic availablity endpoint"""

    response = ping_get(
        client=api.client,
    )
    api.handle_response(response)

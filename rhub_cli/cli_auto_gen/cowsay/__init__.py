import click

from rhub_cli.api.health.rhub_api_health_cowsay import sync_detailed as cowsay_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def cowsay():
    pass


@cowsay.command()
@pass_api
def get(
    api: APIRequest,
):
    """Most important endpoint!"""

    response = cowsay_get(
        client=api.client,
    )
    api.handle_response(response)

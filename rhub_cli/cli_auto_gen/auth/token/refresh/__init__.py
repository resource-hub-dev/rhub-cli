import click

from rhub_cli.api.auth.rhub_api_auth_token_refresh_token import sync_detailed as refresh_create
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def refresh():
    pass


@refresh.command()
@click.option("--authorization", required=True, type=str)
@pass_api
def create(
    api: APIRequest,
    authorization,
):
    """Refresh token"""

    response = refresh_create(
        authorization=authorization,
        client=api.client,
    )
    api.handle_response(response)

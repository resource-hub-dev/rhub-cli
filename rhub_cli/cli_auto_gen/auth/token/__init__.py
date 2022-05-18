import click

from rhub_cli.api.auth.rhub_api_auth_token_get_token_info import sync_detailed as token_get
from rhub_cli.api_request import APIRequest, pass_api

from .create import create
from .refresh import refresh


@click.group()
def token():
    pass


@token.command()
@pass_api
def get(
    api: APIRequest,
):
    """Get auth token info"""

    response = token_get(
        client=api.authenticated_client,
    )
    api.handle_response(response)


token.add_command(create)
token.add_command(refresh)

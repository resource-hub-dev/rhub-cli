import click

from rhub_cli.api.auth.rhub_api_auth_user_get_current_user import sync_detailed as me_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def me():
    pass


@me.command()
@pass_api
def get(
    api: APIRequest,
):
    """Get info about logged in user"""

    response = me_get(
        client=api.authenticated_client,
    )
    api.handle_response(response)

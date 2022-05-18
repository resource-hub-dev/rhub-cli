import click

from rhub_cli.api.auth.rhub_api_auth_group_list_group_users import sync_detailed as users_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def users():
    pass


@users.command()
@click.argument("group_id", type=str)
@pass_api
def get_list(
    api: APIRequest,
    group_id,
):
    """Get users in group"""

    response = users_get_list(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)

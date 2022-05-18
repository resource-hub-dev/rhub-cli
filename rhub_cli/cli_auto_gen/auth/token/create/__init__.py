import click

from rhub_cli.api.auth.rhub_api_auth_token_create_token import sync_detailed as create_create
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def create():
    pass


@create.command()
@click.option("--authorization", required=True, type=str)
@pass_api
def create(
    api: APIRequest,
    authorization,
):
    """Login and get access token"""

    response = create_create(
        authorization=authorization,
        client=api.client,
    )
    api.handle_response(response)

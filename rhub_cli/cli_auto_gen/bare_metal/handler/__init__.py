import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_handler_handler_create import sync_detailed as handler_create
from rhub_cli.api.bare_metal.rhub_api_bare_metal_handler_handler_get import sync_detailed as handler_get
from rhub_cli.api.bare_metal.rhub_api_bare_metal_handler_handler_list import sync_detailed as handler_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models import *


@click.group()
def handler():
    pass


@handler.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get host's handler list"""

    response = handler_get_list(
        client=api.client,
    )
    api.handle_response(response)


@handler.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create host handler"""

    response = handler_create(
        json_body=json_body,
        client=api.client,
    )
    api.handle_response(response)


@handler.command()
@click.argument("handler_id", type=int)
@pass_api
def get(
    api: APIRequest,
    handler_id,
):
    """Get handler"""

    response = handler_get(
        handler_id=handler_id,
        client=api.client,
    )
    api.handle_response(response)

import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_host_host_create import sync_detailed as host_create
from rhub_cli.api.bare_metal.rhub_api_bare_metal_host_host_get import sync_detailed as host_get
from rhub_cli.api.bare_metal.rhub_api_bare_metal_host_host_list import sync_detailed as host_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models import *

from .power_state import power_state


@click.group()
def host():
    pass


@host.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get host list"""

    response = host_get_list(
        client=api.client,
    )
    api.handle_response(response)


@host.command()
@pass_api
def create(
    api: APIRequest,
):
    """Create bare metal host"""

    response = host_create(
        json_body=json_body,
        client=api.client,
    )
    api.handle_response(response)


@host.command()
@click.argument("host_id", type=int)
@pass_api
def get(
    api: APIRequest,
    host_id,
):
    """Get host"""

    response = host_get(
        host_id=host_id,
        client=api.client,
    )
    api.handle_response(response)


host.add_command(power_state)

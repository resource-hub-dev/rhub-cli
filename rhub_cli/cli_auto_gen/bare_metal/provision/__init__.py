import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_provision_provision_create import sync_detailed as provision_create
from rhub_cli.api.bare_metal.rhub_api_bare_metal_provision_provision_get import sync_detailed as provision_get
from rhub_cli.api.bare_metal.rhub_api_bare_metal_provision_provision_list import sync_detailed as provision_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models import *

from .finish import finish
from .kickstart import kickstart
from .logs import logs


@click.group()
def provision():
    pass


@provision.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get provision list"""

    response = provision_get_list(
        client=api.client,
    )
    api.handle_response(response)


@provision.command()
@pass_api
def create(
    api: APIRequest,
):
    """Add bare metal provision"""

    response = provision_create(
        json_body=json_body,
        client=api.client,
    )
    api.handle_response(response)


@provision.command()
@click.argument("provision_id", type=int)
@pass_api
def get(
    api: APIRequest,
    provision_id,
):
    """Get provision"""

    response = provision_get(
        provision_id=provision_id,
        client=api.client,
    )
    api.handle_response(response)


provision.add_command(finish)
provision.add_command(kickstart)
provision.add_command(logs)

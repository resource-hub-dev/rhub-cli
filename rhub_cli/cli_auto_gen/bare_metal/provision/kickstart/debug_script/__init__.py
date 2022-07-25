import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_provision_provision_kickstart_debug_script_get import (
    sync_detailed as debug_script_get,
)
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def debug_script():
    pass


@debug_script.command()
@click.argument("provision_id", type=int)
@pass_api
def get(
    api: APIRequest,
    provision_id,
):
    """Get provision's kickstart debug script"""

    response = debug_script_get(
        provision_id=provision_id,
        client=api.client,
    )
    api.handle_response(response)

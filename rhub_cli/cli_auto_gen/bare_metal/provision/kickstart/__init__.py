import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_provision_provision_get_kickstart import sync_detailed as kickstart_get
from rhub_cli.api_request import APIRequest, pass_api

from .debug_script import debug_script


@click.group()
def kickstart():
    pass


@kickstart.command()
@click.argument("provision_id", type=int)
@pass_api
def get(
    api: APIRequest,
    provision_id,
):
    """Get provision's kickstart file"""

    response = kickstart_get(
        provision_id=provision_id,
        client=api.client,
    )
    api.handle_response(response)


kickstart.add_command(debug_script)

import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_provision_provision_finish import sync_detailed as finish_create
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def finish():
    pass


@finish.command()
@click.argument("provision_id", type=int)
@pass_api
def create(
    api: APIRequest,
    provision_id,
):
    """Finish provision"""

    response = finish_create(
        provision_id=provision_id,
        client=api.client,
    )
    api.handle_response(response)

import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_provision_provision_logs_upload import sync_detailed as logs_create
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models import *


@click.group()
def logs():
    pass


@logs.command()
@click.argument("provision_id", type=int)
@pass_api
def create(
    api: APIRequest,
    provision_id,
):
    """Endpoint to upload provision logs"""

    response = logs_create(
        provision_id=provision_id,
        multipart_data=multipart_data,
        client=api.client,
    )
    api.handle_response(response)

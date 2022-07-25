import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_image_image_create import sync_detailed as image_create
from rhub_cli.api.bare_metal.rhub_api_bare_metal_image_image_get import sync_detailed as image_get
from rhub_cli.api.bare_metal.rhub_api_bare_metal_image_image_list import sync_detailed as image_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models import *


@click.group()
def image():
    pass


@image.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get image list"""

    response = image_get_list(
        client=api.client,
    )
    api.handle_response(response)


@image.command()
@pass_api
def create(
    api: APIRequest,
):
    """Add bare metal image"""

    response = image_create(
        json_body=json_body,
        client=api.client,
    )
    api.handle_response(response)


@image.command()
@click.argument("image_id", type=int)
@pass_api
def get(
    api: APIRequest,
    image_id,
):
    """Get image"""

    response = image_get(
        image_id=image_id,
        client=api.client,
    )
    api.handle_response(response)

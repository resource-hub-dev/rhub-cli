import click

from rhub_cli.api.lab.rhub_api_lab_location_location_create import sync_detailed as location_create
from rhub_cli.api.lab.rhub_api_lab_location_location_delete import sync_detailed as location_remove
from rhub_cli.api.lab.rhub_api_lab_location_location_get import sync_detailed as location_get
from rhub_cli.api.lab.rhub_api_lab_location_location_list import sync_detailed as location_get_list
from rhub_cli.api.lab.rhub_api_lab_location_location_update import sync_detailed as location_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_location_location_create_json_body import RhubApiLabLocationLocationCreateJsonBody
from rhub_cli.models.rhub_api_lab_location_location_list_sort import RhubApiLabLocationLocationListSort
from rhub_cli.models.rhub_api_lab_location_location_update_json_body import RhubApiLabLocationLocationUpdateJsonBody

from .regions import regions


@click.group()
def location():
    pass


@location.command()
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
):
    """Get location list"""

    if sort is not None:
        sort = RhubApiLabLocationLocationListSort(sort)

    response = location_get_list(
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@location.command()
@click.option("--name", required=True, type=str, help="Short name of location / IATA identifier / ...")
@click.option("--description", type=str, help="Long description of location, address, ...")
@pass_api
def create(
    api: APIRequest,
    name,
    description,
):
    """Create location"""

    json_body = RhubApiLabLocationLocationCreateJsonBody(
        name=name,
        description=description,
    )

    response = location_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@location.command()
@click.argument("location_id", type=int)
@pass_api
def get(
    api: APIRequest,
    location_id,
):
    """Get location"""

    response = location_get(
        location_id=location_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@location.command()
@click.argument("location_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    location_id,
):
    """Delete location"""

    response = location_remove(
        location_id=location_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@location.command()
@click.argument("location_id", type=int)
@click.option("--description", type=str, help="Long description of location, address, ...")
@click.option("--name", type=str, help="Short name of location / IATA identifier / ...")
@pass_api
def update(
    api: APIRequest,
    location_id,
    description,
    name,
):
    """Update location"""

    json_body = RhubApiLabLocationLocationUpdateJsonBody(
        description=description,
        name=name,
    )

    response = location_update(
        location_id=location_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


location.add_command(regions)

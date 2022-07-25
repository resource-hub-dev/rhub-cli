import click

from rhub_cli.api.satellite.rhub_api_satellite_server_create import sync_detailed as server_create
from rhub_cli.api.satellite.rhub_api_satellite_server_delete import sync_detailed as server_remove
from rhub_cli.api.satellite.rhub_api_satellite_server_get import sync_detailed as server_get
from rhub_cli.api.satellite.rhub_api_satellite_server_list import sync_detailed as server_get_list
from rhub_cli.api.satellite.rhub_api_satellite_server_update import sync_detailed as server_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_satellite_server_create_json_body import RhubApiSatelliteServerCreateJsonBody
from rhub_cli.models.rhub_api_satellite_server_list_filter import RhubApiSatelliteServerListFilter
from rhub_cli.models.rhub_api_satellite_server_list_sort import RhubApiSatelliteServerListSort
from rhub_cli.models.rhub_api_satellite_server_update_json_body import RhubApiSatelliteServerUpdateJsonBody


@click.group()
def server():
    pass


@server.command()
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option(
    "--filter-hostname",
    type=str,
    help="Hostname of a server. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option("--filter-owner-group-id", type=str)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_hostname,
    filter_owner_group_id,
):
    """Get Satellite server list"""

    if sort is not None:
        sort = RhubApiSatelliteServerListSort(sort)

    filter_ = RhubApiSatelliteServerListFilter(
        hostname=filter_hostname,
        owner_group_id=filter_owner_group_id,
    )

    response = server_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.option("--credentials", required=True)
@click.option("--hostname", required=True, type=str)
@click.option("--name", required=True, type=str)
@click.option("--description", type=str)
@click.option("--insecure", is_flag=True)
@click.option("--owner-group-id", type=str)
@pass_api
def create(
    api: APIRequest,
    credentials,
    hostname,
    name,
    description,
    insecure,
    owner_group_id,
):
    """Create Satellite server"""

    json_body = RhubApiSatelliteServerCreateJsonBody(
        credentials=credentials,
        hostname=hostname,
        name=name,
        description=description,
        insecure=insecure,
        owner_group_id=owner_group_id,
    )

    response = server_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.argument("server_id", type=int)
@pass_api
def get(
    api: APIRequest,
    server_id,
):
    """Get Satellite server"""

    response = server_get(
        server_id=server_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.argument("server_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    server_id,
):
    """Delete Satellite server"""

    response = server_remove(
        server_id=server_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.argument("server_id", type=int)
@click.option("--credentials")
@click.option("--description", type=str)
@click.option("--hostname", type=str)
@click.option("--insecure", is_flag=True)
@click.option("--name", type=str)
@click.option("--owner-group-id", type=str)
@pass_api
def update(
    api: APIRequest,
    server_id,
    credentials,
    description,
    hostname,
    insecure,
    name,
    owner_group_id,
):
    """Update Satellite server"""

    json_body = RhubApiSatelliteServerUpdateJsonBody(
        credentials=credentials,
        description=description,
        hostname=hostname,
        insecure=insecure,
        name=name,
        owner_group_id=owner_group_id,
    )

    response = server_update(
        server_id=server_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

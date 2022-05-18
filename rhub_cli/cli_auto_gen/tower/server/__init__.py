import json

import click

from rhub_cli.api.tower.rhub_api_tower_create_server import sync_detailed as server_create
from rhub_cli.api.tower.rhub_api_tower_delete_server import sync_detailed as server_remove
from rhub_cli.api.tower.rhub_api_tower_get_server import sync_detailed as server_get
from rhub_cli.api.tower.rhub_api_tower_list_servers import sync_detailed as server_get_list
from rhub_cli.api.tower.rhub_api_tower_update_server import sync_detailed as server_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_create_server_json_body import RhubApiTowerCreateServerJsonBody
from rhub_cli.models.rhub_api_tower_create_server_json_body_id import RhubApiTowerCreateServerJsonBodyId
from rhub_cli.models.rhub_api_tower_list_servers_filter import RhubApiTowerListServersFilter
from rhub_cli.models.rhub_api_tower_list_servers_sort import RhubApiTowerListServersSort
from rhub_cli.models.rhub_api_tower_update_server_json_body import RhubApiTowerUpdateServerJsonBody
from rhub_cli.models.rhub_api_tower_update_server_json_body_id import RhubApiTowerUpdateServerJsonBodyId
from rhub_cli.types import UNSET


@click.group()
def server():
    pass


@server.command()
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-enabled", is_flag=True)
@click.option(
    "--filter-name",
    type=str,
    help="Name of a server. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_enabled,
    filter_name,
):
    """Get list of Tower servers"""

    if sort is not None:
        sort = RhubApiTowerListServersSort(sort)

    filter_ = RhubApiTowerListServersFilter(
        enabled=filter_enabled,
        name=filter_name,
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
@click.option("--credentials", required=True, type=str, help="Tower credentials path (Vault mount/path)")
@click.option("--name", required=True, type=str)
@click.option("--url", required=True, type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--id")
@click.option("--verify-ssl", is_flag=True, help="Option to disable SSL certificate verification.")
@pass_api
def create(
    api: APIRequest,
    credentials,
    name,
    url,
    description,
    enabled,
    id,
    verify_ssl,
):
    """Create Tower server"""

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiTowerCreateServerJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiTowerCreateServerJsonBody(
        credentials=credentials,
        name=name,
        url=url,
        description=description,
        enabled=enabled,
        id=id,
        verify_ssl=verify_ssl,
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
    """Get Tower server"""

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
    """"""

    response = server_remove(
        server_id=server_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.argument("server_id", type=int)
@click.option("--credentials", type=str, help="Tower credentials path (Vault mount/path)")
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--id")
@click.option("--name", type=str)
@click.option("--url", type=str)
@click.option("--verify-ssl", is_flag=True, help="Option to disable SSL certificate verification.")
@pass_api
def update(
    api: APIRequest,
    server_id,
    credentials,
    description,
    enabled,
    id,
    name,
    url,
    verify_ssl,
):
    """Change Tower server"""

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiTowerUpdateServerJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiTowerUpdateServerJsonBody(
        credentials=credentials,
        description=description,
        enabled=enabled,
        id=id,
        name=name,
        url=url,
        verify_ssl=verify_ssl,
    )

    response = server_update(
        server_id=server_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

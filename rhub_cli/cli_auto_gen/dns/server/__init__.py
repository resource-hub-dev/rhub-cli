import click

from rhub_cli.api.dns.rhub_api_dns_server_create import sync_detailed as server_create
from rhub_cli.api.dns.rhub_api_dns_server_delete import sync_detailed as server_remove
from rhub_cli.api.dns.rhub_api_dns_server_get import sync_detailed as server_get
from rhub_cli.api.dns.rhub_api_dns_server_list import sync_detailed as server_get_list
from rhub_cli.api.dns.rhub_api_dns_server_update import sync_detailed as server_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_dns_server_create_json_body import RhubApiDnsServerCreateJsonBody
from rhub_cli.models.rhub_api_dns_server_list_filter import RhubApiDnsServerListFilter
from rhub_cli.models.rhub_api_dns_server_list_sort import RhubApiDnsServerListSort
from rhub_cli.models.rhub_api_dns_server_update_json_body import RhubApiDnsServerUpdateJsonBody


@click.group()
def server():
    pass


@server.command()
@click.option("--sort", type=click.Choice(["hostname", "-hostname"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option(
    "--filter-hostname",
    type=str,
    help="Hostname of a server. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_hostname,
):
    """Get DNS server list"""

    if sort is not None:
        sort = RhubApiDnsServerListSort(sort)

    filter_ = RhubApiDnsServerListFilter(
        hostname=filter_hostname,
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
@click.option("--credentials", required=True, help="TSIG key for DNS update requests.")
@click.option("--hostname", required=True, type=str)
@click.option("--description", type=str)
@click.option("--name", type=str)
@click.option("--owner-group-id", type=str)
@click.option("--zone", type=str)
@pass_api
def create(
    api: APIRequest,
    credentials,
    hostname,
    description,
    name,
    owner_group_id,
    zone,
):
    """Create DNS server"""

    json_body = RhubApiDnsServerCreateJsonBody(
        credentials=credentials,
        hostname=hostname,
        description=description,
        name=name,
        owner_group_id=owner_group_id,
        zone=zone,
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
    """Get DNS server"""

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
    """Delete DNS server"""

    response = server_remove(
        server_id=server_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@server.command()
@click.argument("server_id", type=int)
@click.option("--credentials", help="TSIG key for DNS update requests.")
@click.option("--description", type=str)
@click.option("--hostname", type=str)
@click.option("--name", type=str)
@click.option("--owner-group-id", type=str)
@click.option("--zone", type=str)
@pass_api
def update(
    api: APIRequest,
    server_id,
    credentials,
    description,
    hostname,
    name,
    owner_group_id,
    zone,
):
    """Update DNS server"""

    json_body = RhubApiDnsServerUpdateJsonBody(
        credentials=credentials,
        description=description,
        hostname=hostname,
        name=name,
        owner_group_id=owner_group_id,
        zone=zone,
    )

    response = server_update(
        server_id=server_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

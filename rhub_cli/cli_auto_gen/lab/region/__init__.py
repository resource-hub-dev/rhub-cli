import json

import click

from rhub_cli.api.lab.rhub_api_lab_region_create_region import sync_detailed as region_create
from rhub_cli.api.lab.rhub_api_lab_region_delete_region import sync_detailed as region_remove
from rhub_cli.api.lab.rhub_api_lab_region_get_region import sync_detailed as region_get
from rhub_cli.api.lab.rhub_api_lab_region_list_regions import sync_detailed as region_get_list
from rhub_cli.api.lab.rhub_api_lab_region_update_region import sync_detailed as region_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_region_create_region_json_body import RhubApiLabRegionCreateRegionJsonBody
from rhub_cli.models.rhub_api_lab_region_create_region_json_body_id import RhubApiLabRegionCreateRegionJsonBodyId
from rhub_cli.models.rhub_api_lab_region_list_regions_filter import RhubApiLabRegionListRegionsFilter
from rhub_cli.models.rhub_api_lab_region_list_regions_sort import RhubApiLabRegionListRegionsSort
from rhub_cli.models.rhub_api_lab_region_update_region_json_body import RhubApiLabRegionUpdateRegionJsonBody
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_dns_server import (
    RhubApiLabRegionUpdateRegionJsonBodyDnsServer,
)
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_id import RhubApiLabRegionUpdateRegionJsonBodyId
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_openstack import (
    RhubApiLabRegionUpdateRegionJsonBodyOpenstack,
)
from rhub_cli.models.rhub_api_lab_region_update_region_json_body_satellite import (
    RhubApiLabRegionUpdateRegionJsonBodySatellite,
)
from rhub_cli.types import UNSET

from .products import products
from .usage import usage


@click.group()
def region():
    pass


@region.command()
@click.option(
    "--sort",
    type=click.Choice(
        ["name", "-name", "location", "-location", "reservation_expiration_max", "-reservation_expiration_max"]
    ),
)
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-enabled", is_flag=True)
@click.option(
    "--filter-location",
    type=str,
    help="Location of a region, value is location name. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option(
    "--filter-name",
    type=str,
    help="Name of a region. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option("--filter-reservations-enabled", is_flag=True)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_enabled,
    filter_location,
    filter_name,
    filter_reservations_enabled,
):
    """Get region list"""

    if sort is not None:
        sort = RhubApiLabRegionListRegionsSort(sort)

    filter_ = RhubApiLabRegionListRegionsFilter(
        enabled=filter_enabled,
        location=filter_location,
        name=filter_name,
        reservations_enabled=filter_reservations_enabled,
    )

    response = region_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.option("--dns-server", required=True)
@click.option("--download-server", required=True, type=str)
@click.option("--name", required=True, type=str)
@click.option("--openstack", required=True)
@click.option("--satellite", required=True)
@click.option("--tower-id", required=True, type=int)
@click.option("--vault-server", required=True, type=str)
@click.option("--banner", type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--id")
@click.option("--lifespan-length", type=int)
@click.option("--location")
@click.option("--location-id")
@click.option("--owner-group", type=str)
@click.option("--owner-group-name", type=str)
@click.option("--reservation-expiration-max", type=int)
@click.option("--reservations-enabled", is_flag=True)
@click.option("--total-quota")
@click.option("--user-quota")
@click.option("--users-group", type=str)
@click.option("--users-group-name", type=str)
@pass_api
def create(
    api: APIRequest,
    dns_server,
    download_server,
    name,
    openstack,
    satellite,
    tower_id,
    vault_server,
    banner,
    description,
    enabled,
    id,
    lifespan_length,
    location,
    location_id,
    owner_group,
    owner_group_name,
    reservation_expiration_max,
    reservations_enabled,
    total_quota,
    user_quota,
    users_group,
    users_group_name,
):
    """Create region"""

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiLabRegionCreateRegionJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiLabRegionCreateRegionJsonBody(
        dns_server=dns_server,
        download_server=download_server,
        name=name,
        openstack=openstack,
        satellite=satellite,
        tower_id=tower_id,
        vault_server=vault_server,
        banner=banner,
        description=description,
        enabled=enabled,
        id=id,
        lifespan_length=lifespan_length,
        location=location,
        location_id=location_id,
        owner_group=owner_group,
        owner_group_name=owner_group_name,
        reservation_expiration_max=reservation_expiration_max,
        reservations_enabled=reservations_enabled,
        total_quota=total_quota,
        user_quota=user_quota,
        users_group=users_group,
        users_group_name=users_group_name,
    )

    response = region_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.argument("region_id", type=int)
@pass_api
def get(
    api: APIRequest,
    region_id,
):
    """Get region"""

    response = region_get(
        region_id=region_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.argument("region_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    region_id,
):
    """Delete region"""

    response = region_remove(
        region_id=region_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@region.command()
@click.argument("region_id", type=int)
@click.option("--banner", type=str)
@click.option("--description", type=str)
@click.option("--download-server", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--id")
@click.option("--lifespan-length", type=int)
@click.option("--location")
@click.option("--location-id")
@click.option("--name", type=str)
@click.option("--owner-group", type=str)
@click.option("--owner-group-name", type=str)
@click.option("--reservation-expiration-max", type=int)
@click.option("--reservations-enabled", is_flag=True)
@click.option("--total-quota")
@click.option("--tower-id", type=int)
@click.option("--user-quota")
@click.option("--users-group", type=str)
@click.option("--users-group-name", type=str)
@click.option("--vault-server", type=str)
@click.option("--dns-server-hostname", type=str)
@click.option("--dns-server-key")
@click.option("--dns-server-zone", type=str)
@click.option("--openstack-credentials")
@click.option("--openstack-domain-id", type=str)
@click.option("--openstack-domain-name", type=str)
@click.option("--openstack-keyname", type=str, help="SSH key name")
@click.option("--openstack-networks-item", type=str)
@click.option("--openstack-project", type=str)
@click.option("--openstack-url", type=str)
@click.option("--satellite-credentials")
@click.option("--satellite-hostname", type=str)
@click.option("--satellite-insecure", is_flag=True)
@pass_api
def update(
    api: APIRequest,
    region_id,
    banner,
    description,
    download_server,
    enabled,
    id,
    lifespan_length,
    location,
    location_id,
    name,
    owner_group,
    owner_group_name,
    reservation_expiration_max,
    reservations_enabled,
    total_quota,
    tower_id,
    user_quota,
    users_group,
    users_group_name,
    vault_server,
    dns_server_hostname,
    dns_server_key,
    dns_server_zone,
    openstack_credentials,
    openstack_domain_id,
    openstack_domain_name,
    openstack_keyname,
    openstack_networks_item,
    openstack_project,
    openstack_url,
    satellite_credentials,
    satellite_hostname,
    satellite_insecure,
):
    """Update region"""

    openstack_networks = []
    if openstack_networks_item is not None:
        openstack_networks.append(openstack_networks_item)

    satellite = RhubApiLabRegionUpdateRegionJsonBodySatellite(
        credentials=satellite_credentials,
        hostname=satellite_hostname,
        insecure=satellite_insecure,
    )

    openstack = RhubApiLabRegionUpdateRegionJsonBodyOpenstack(
        credentials=openstack_credentials,
        domain_id=openstack_domain_id,
        domain_name=openstack_domain_name,
        keyname=openstack_keyname,
        networks=openstack_networks,
        project=openstack_project,
        url=openstack_url,
    )

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiLabRegionUpdateRegionJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    dns_server = RhubApiLabRegionUpdateRegionJsonBodyDnsServer(
        hostname=dns_server_hostname,
        key=dns_server_key,
        zone=dns_server_zone,
    )

    json_body = RhubApiLabRegionUpdateRegionJsonBody(
        banner=banner,
        description=description,
        dns_server=dns_server,
        download_server=download_server,
        enabled=enabled,
        id=id,
        lifespan_length=lifespan_length,
        location=location,
        location_id=location_id,
        name=name,
        openstack=openstack,
        owner_group=owner_group,
        owner_group_name=owner_group_name,
        reservation_expiration_max=reservation_expiration_max,
        reservations_enabled=reservations_enabled,
        satellite=satellite,
        total_quota=total_quota,
        tower_id=tower_id,
        user_quota=user_quota,
        users_group=users_group,
        users_group_name=users_group_name,
        vault_server=vault_server,
    )

    response = region_update(
        region_id=region_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


region.add_command(products)
region.add_command(usage)

import click

from rhub_cli.api.lab.rhub_api_lab_region_create_region import sync_detailed as region_create
from rhub_cli.api.lab.rhub_api_lab_region_delete_region import sync_detailed as region_remove
from rhub_cli.api.lab.rhub_api_lab_region_get_region import sync_detailed as region_get
from rhub_cli.api.lab.rhub_api_lab_region_list_regions import sync_detailed as region_get_list
from rhub_cli.api.lab.rhub_api_lab_region_update_region import sync_detailed as region_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_region_create_region_json_body import RhubApiLabRegionCreateRegionJsonBody
from rhub_cli.models.rhub_api_lab_region_list_regions_filter import RhubApiLabRegionListRegionsFilter
from rhub_cli.models.rhub_api_lab_region_list_regions_sort import RhubApiLabRegionListRegionsSort
from rhub_cli.models.rhub_api_lab_region_update_region_json_body import RhubApiLabRegionUpdateRegionJsonBody

from .all import all
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
@click.option("--name", required=True, type=str)
@click.option("--openstack-id", required=True, type=int)
@click.option("--owner-group-id", required=True, type=str)
@click.option("--tower-id", required=True, type=int)
@click.option("--banner", type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--lifespan-length", type=int)
@click.option("--location-id")
@click.option("--openstack-keyname", type=str, help="SSH key name")
@click.option("--reservation-expiration-max", type=int)
@click.option("--reservations-enabled", is_flag=True)
@click.option("--satellite-id")
@click.option("--total-quota")
@click.option("--user-quota")
@click.option("--users-group-id", type=str)
@pass_api
def create(
    api: APIRequest,
    name,
    openstack_id,
    owner_group_id,
    tower_id,
    banner,
    description,
    enabled,
    lifespan_length,
    location_id,
    openstack_keyname,
    reservation_expiration_max,
    reservations_enabled,
    satellite_id,
    total_quota,
    user_quota,
    users_group_id,
):
    """Create region"""

    json_body = RhubApiLabRegionCreateRegionJsonBody(
        name=name,
        openstack_id=openstack_id,
        owner_group_id=owner_group_id,
        tower_id=tower_id,
        banner=banner,
        description=description,
        enabled=enabled,
        lifespan_length=lifespan_length,
        location_id=location_id,
        openstack_keyname=openstack_keyname,
        reservation_expiration_max=reservation_expiration_max,
        reservations_enabled=reservations_enabled,
        satellite_id=satellite_id,
        total_quota=total_quota,
        user_quota=user_quota,
        users_group_id=users_group_id,
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
@click.option("--enabled", is_flag=True)
@click.option("--lifespan-length", type=int)
@click.option("--location-id")
@click.option("--name", type=str)
@click.option("--openstack-id", type=int)
@click.option("--openstack-keyname", type=str, help="SSH key name")
@click.option("--owner-group-id", type=str)
@click.option("--reservation-expiration-max", type=int)
@click.option("--reservations-enabled", is_flag=True)
@click.option("--satellite-id")
@click.option("--total-quota")
@click.option("--tower-id", type=int)
@click.option("--user-quota")
@click.option("--users-group-id", type=str)
@pass_api
def update(
    api: APIRequest,
    region_id,
    banner,
    description,
    enabled,
    lifespan_length,
    location_id,
    name,
    openstack_id,
    openstack_keyname,
    owner_group_id,
    reservation_expiration_max,
    reservations_enabled,
    satellite_id,
    total_quota,
    tower_id,
    user_quota,
    users_group_id,
):
    """Update region"""

    json_body = RhubApiLabRegionUpdateRegionJsonBody(
        banner=banner,
        description=description,
        enabled=enabled,
        lifespan_length=lifespan_length,
        location_id=location_id,
        name=name,
        openstack_id=openstack_id,
        openstack_keyname=openstack_keyname,
        owner_group_id=owner_group_id,
        reservation_expiration_max=reservation_expiration_max,
        reservations_enabled=reservations_enabled,
        satellite_id=satellite_id,
        total_quota=total_quota,
        tower_id=tower_id,
        user_quota=user_quota,
        users_group_id=users_group_id,
    )

    response = region_update(
        region_id=region_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


region.add_command(all)
region.add_command(products)
region.add_command(usage)

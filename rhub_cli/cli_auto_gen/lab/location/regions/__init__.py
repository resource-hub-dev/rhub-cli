import click

from rhub_cli.api.lab.rhub_api_lab_location_location_region_list import sync_detailed as regions_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_location_location_region_list_filter import RhubApiLabLocationLocationRegionListFilter


@click.group()
def regions():
    pass


@regions.command()
@click.argument("location_id", type=int)
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-enabled", is_flag=True)
@click.option(
    "--filter-location",
    type=str,
    help="Location of a region. Wildcard ``%`` can be used to match zero, one, or multiple characters",
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
    location_id,
    page,
    limit,
    filter_enabled,
    filter_location,
    filter_name,
    filter_reservations_enabled,
):
    """Get list of regions in the location."""

    filter_ = RhubApiLabLocationLocationRegionListFilter(
        enabled=filter_enabled,
        location=filter_location,
        name=filter_name,
        reservations_enabled=filter_reservations_enabled,
    )

    response = regions_get_list(
        location_id=location_id,
        filter_=filter_,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)

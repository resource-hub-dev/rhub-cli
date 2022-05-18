import click

from rhub_cli.api.lab.rhub_api_lab_region_add_region_product import sync_detailed as products_create
from rhub_cli.api.lab.rhub_api_lab_region_delete_region_product import sync_detailed as products_remove
from rhub_cli.api.lab.rhub_api_lab_region_list_region_products import sync_detailed as products_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_region_add_region_product_json_body import RhubApiLabRegionAddRegionProductJsonBody
from rhub_cli.models.rhub_api_lab_region_delete_region_product_json_body import (
    RhubApiLabRegionDeleteRegionProductJsonBody,
)
from rhub_cli.models.rhub_api_lab_region_list_region_products_filter import RhubApiLabRegionListRegionProductsFilter


@click.group()
def products():
    pass


@products.command()
@click.argument("region_id", type=int)
@click.option("--filter-enabled", is_flag=True)
@click.option(
    "--filter-name",
    type=str,
    help="Name of a product. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@pass_api
def get_list(
    api: APIRequest,
    region_id,
    filter_enabled,
    filter_name,
):
    """Get list of products that can be installed in the selected region."""

    filter_ = RhubApiLabRegionListRegionProductsFilter(
        enabled=filter_enabled,
        name=filter_name,
    )

    response = products_get_list(
        region_id=region_id,
        filter_=filter_,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@products.command()
@click.argument("region_id", type=int)
@click.option("--id", required=True, type=int)
@click.option("--enabled", is_flag=True)
@pass_api
def create(
    api: APIRequest,
    region_id,
    id,
    enabled,
):
    """Add product to region or disable/enable product in region"""

    json_body = RhubApiLabRegionAddRegionProductJsonBody(
        id=id,
        enabled=enabled,
    )

    response = products_create(
        region_id=region_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@products.command()
@click.argument("region_id", type=int)
@click.option("--id", required=True, type=int)
@pass_api
def remove(
    api: APIRequest,
    region_id,
    id,
):
    """Remove product from region"""

    json_body = RhubApiLabRegionDeleteRegionProductJsonBody(
        id=id,
    )

    response = products_remove(
        region_id=region_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

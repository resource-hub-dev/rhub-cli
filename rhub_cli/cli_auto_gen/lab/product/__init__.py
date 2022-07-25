import click

from rhub_cli.api.lab.rhub_api_lab_product_create_product import sync_detailed as product_create
from rhub_cli.api.lab.rhub_api_lab_product_delete_product import sync_detailed as product_remove
from rhub_cli.api.lab.rhub_api_lab_product_get_product import sync_detailed as product_get
from rhub_cli.api.lab.rhub_api_lab_product_list_products import sync_detailed as product_get_list
from rhub_cli.api.lab.rhub_api_lab_product_update_product import sync_detailed as product_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_product_create_product_json_body import RhubApiLabProductCreateProductJsonBody
from rhub_cli.models.rhub_api_lab_product_create_product_json_body_flavors import (
    RhubApiLabProductCreateProductJsonBodyFlavors,
)
from rhub_cli.models.rhub_api_lab_product_create_product_json_body_flavors_additional_property import (
    RhubApiLabProductCreateProductJsonBodyFlavorsAdditionalProperty,
)
from rhub_cli.models.rhub_api_lab_product_list_products_filter import RhubApiLabProductListProductsFilter
from rhub_cli.models.rhub_api_lab_product_list_products_sort import RhubApiLabProductListProductsSort
from rhub_cli.models.rhub_api_lab_product_update_product_json_body import RhubApiLabProductUpdateProductJsonBody
from rhub_cli.models.rhub_api_lab_product_update_product_json_body_flavors import (
    RhubApiLabProductUpdateProductJsonBodyFlavors,
)
from rhub_cli.models.rhub_api_lab_product_update_product_json_body_flavors_additional_property import (
    RhubApiLabProductUpdateProductJsonBodyFlavorsAdditionalProperty,
)

from .regions import regions


@click.group()
def product():
    pass


@product.command()
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-enabled", is_flag=True)
@click.option(
    "--filter-name",
    type=str,
    help="Name of a product. Wildcard ``%`` can be used to match zero, one, or multiple characters",
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
    """Get product list"""

    if sort is not None:
        sort = RhubApiLabProductListProductsSort(sort)

    filter_ = RhubApiLabProductListProductsFilter(
        enabled=filter_enabled,
        name=filter_name,
    )

    response = product_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@product.command()
@click.option("--name", required=True, type=str)
@click.option("--parameters-item", required=True)
@click.option("--tower-template-name-create", required=True, type=str)
@click.option("--tower-template-name-delete", required=True, type=str)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--flavors-additional-property-num-vcpus", type=int)
@click.option("--flavors-additional-property-num-volumes", type=int)
@click.option("--flavors-additional-property-ram-mb", type=int)
@click.option("--flavors-additional-property-volumes-gb", type=int)
@pass_api
def create(
    api: APIRequest,
    name,
    parameters_item,
    tower_template_name_create,
    tower_template_name_delete,
    description,
    enabled,
    flavors_additional_property_num_vcpus,
    flavors_additional_property_num_volumes,
    flavors_additional_property_ram_mb,
    flavors_additional_property_volumes_gb,
):
    """Create product"""

    flavors_additional_property = RhubApiLabProductCreateProductJsonBodyFlavorsAdditionalProperty(
        num_vcpus=flavors_additional_property_num_vcpus,
        num_volumes=flavors_additional_property_num_volumes,
        ram_mb=flavors_additional_property_ram_mb,
        volumes_gb=flavors_additional_property_volumes_gb,
    )

    flavors = RhubApiLabProductCreateProductJsonBodyFlavors()
    flavors.additional_properties = {"flavors": flavors_additional_property}

    parameters = []
    if parameters_item is not None:
        parameters.append(parameters_item)

    json_body = RhubApiLabProductCreateProductJsonBody(
        name=name,
        parameters=parameters,
        tower_template_name_create=tower_template_name_create,
        tower_template_name_delete=tower_template_name_delete,
        description=description,
        enabled=enabled,
        flavors=flavors,
    )

    response = product_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@product.command()
@click.argument("product_id", type=int)
@pass_api
def get(
    api: APIRequest,
    product_id,
):
    """Get product"""

    response = product_get(
        product_id=product_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@product.command()
@click.argument("product_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    product_id,
):
    """Delete product"""

    response = product_remove(
        product_id=product_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@product.command()
@click.argument("product_id", type=int)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--name", type=str)
@click.option("--parameters-item")
@click.option("--tower-template-name-create", type=str)
@click.option("--tower-template-name-delete", type=str)
@click.option("--flavors-additional-property-num-vcpus", type=int)
@click.option("--flavors-additional-property-num-volumes", type=int)
@click.option("--flavors-additional-property-ram-mb", type=int)
@click.option("--flavors-additional-property-volumes-gb", type=int)
@pass_api
def update(
    api: APIRequest,
    product_id,
    description,
    enabled,
    name,
    parameters_item,
    tower_template_name_create,
    tower_template_name_delete,
    flavors_additional_property_num_vcpus,
    flavors_additional_property_num_volumes,
    flavors_additional_property_ram_mb,
    flavors_additional_property_volumes_gb,
):
    """Update product"""

    flavors_additional_property = RhubApiLabProductUpdateProductJsonBodyFlavorsAdditionalProperty(
        num_vcpus=flavors_additional_property_num_vcpus,
        num_volumes=flavors_additional_property_num_volumes,
        ram_mb=flavors_additional_property_ram_mb,
        volumes_gb=flavors_additional_property_volumes_gb,
    )

    parameters = []
    if parameters_item is not None:
        parameters.append(parameters_item)

    flavors = RhubApiLabProductUpdateProductJsonBodyFlavors()
    flavors.additional_properties = {"flavors": flavors_additional_property}

    json_body = RhubApiLabProductUpdateProductJsonBody(
        description=description,
        enabled=enabled,
        flavors=flavors,
        name=name,
        parameters=parameters,
        tower_template_name_create=tower_template_name_create,
        tower_template_name_delete=tower_template_name_delete,
    )

    response = product_update(
        product_id=product_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


product.add_command(regions)

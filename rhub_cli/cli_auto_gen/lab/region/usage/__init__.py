import click

from rhub_cli.api.lab.rhub_api_lab_region_get_usage import sync_detailed as usage_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def usage():
    pass


@usage.command()
@click.argument("region_id", type=int)
@click.option("--with-openstack-limits", is_flag=True)
@pass_api
def get(
    api: APIRequest,
    region_id,
    with_openstack_limits,
):
    """Get region usage"""

    response = usage_get(
        region_id=region_id,
        with_openstack_limits=with_openstack_limits,
        client=api.authenticated_client,
    )
    api.handle_response(response)

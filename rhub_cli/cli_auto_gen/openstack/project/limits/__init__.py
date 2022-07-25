import click

from rhub_cli.api.openstack.rhub_api_openstack_project_limits_get import sync_detailed as limits_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def limits():
    pass


@limits.command()
@click.argument("project_id", type=int)
@pass_api
def get(
    api: APIRequest,
    project_id,
):
    """Get OpenStack project limits"""

    response = limits_get(
        project_id=project_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)

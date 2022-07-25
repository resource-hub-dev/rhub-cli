import click

from rhub_cli.api.lab.rhub_api_lab_region_get_all_usage import sync_detailed as usage_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def usage():
    pass


@usage.command()
@pass_api
def get(
    api: APIRequest,
):
    """Get all region usage"""

    response = usage_get(
        client=api.authenticated_client,
    )
    api.handle_response(response)

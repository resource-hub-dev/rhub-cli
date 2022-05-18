import click

from rhub_cli.api.lab.rhub_api_lab_cluster_list_cluster_events import sync_detailed as events_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def events():
    pass


@events.command()
@click.argument("cluster_id", type=int)
@pass_api
def get_list(
    api: APIRequest,
    cluster_id,
):
    """Get cluster events list"""

    response = events_get_list(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)

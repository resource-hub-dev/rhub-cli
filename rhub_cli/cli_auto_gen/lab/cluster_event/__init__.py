import click

from rhub_cli.api.lab.rhub_api_lab_cluster_get_cluster_event import sync_detailed as cluster_event_get
from rhub_cli.api_request import APIRequest, pass_api

from .stdout import stdout


@click.group()
def cluster_event():
    pass


@cluster_event.command()
@click.argument("event_id", type=int)
@pass_api
def get(
    api: APIRequest,
    event_id,
):
    """Get cluster event"""

    response = cluster_event_get(
        event_id=event_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


cluster_event.add_command(stdout)

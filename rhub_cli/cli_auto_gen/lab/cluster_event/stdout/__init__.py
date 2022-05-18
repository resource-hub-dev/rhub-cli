import click

from rhub_cli.api.lab.rhub_api_lab_cluster_get_cluster_event_stdout import sync_detailed as stdout_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def stdout():
    pass


@stdout.command()
@click.argument("event_id", type=int)
@pass_api
def get(
    api: APIRequest,
    event_id,
):
    """Get cluster event output"""

    response = stdout_get(
        event_id=event_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)

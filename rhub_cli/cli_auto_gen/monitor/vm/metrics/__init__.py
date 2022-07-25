import click

from rhub_cli.api.monitoring.rhub_api_monitor_metrics_vm_metrics import sync_detailed as metrics_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def metrics():
    pass


@metrics.command()
@pass_api
def get(
    api: APIRequest,
):
    """VM (QuickVM) usage metrics"""

    response = metrics_get(
        client=api.authenticated_client,
    )
    api.handle_response(response)

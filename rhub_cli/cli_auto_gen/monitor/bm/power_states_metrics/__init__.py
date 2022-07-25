import click

from rhub_cli.api.monitoring.rhub_api_monitor_metrics_bm_power_states_metrics import (
    sync_detailed as power_states_metrics_get,
)
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def power_states_metrics():
    pass


@power_states_metrics.command()
@pass_api
def get(
    api: APIRequest,
):
    """Get summarized power states from Bare Metal hosts"""

    response = power_states_metrics_get(
        client=api.authenticated_client,
    )
    api.handle_response(response)

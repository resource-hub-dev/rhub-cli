import click

from rhub_cli.api.monitoring.rhub_api_monitor_metrics_bm_hosts_to_monitor_list import sync_detailed as hosts_get_list
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def hosts():
    pass


@hosts.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get a list of Bare Metal hosts to monitor for the IPMI exporter"""

    response = hosts_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)

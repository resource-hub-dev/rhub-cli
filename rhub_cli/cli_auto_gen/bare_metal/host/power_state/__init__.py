import click

from rhub_cli.api.bare_metal.rhub_api_bare_metal_host_host_get_power_state import sync_detailed as power_state_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def power_state():
    pass


@power_state.command()
@click.argument("host_id", type=int)
@pass_api
def get(
    api: APIRequest,
    host_id,
):
    """Get host power state"""

    response = power_state_get(
        host_id=host_id,
        client=api.client,
    )
    api.handle_response(response)

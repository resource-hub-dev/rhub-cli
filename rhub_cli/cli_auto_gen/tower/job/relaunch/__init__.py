import click

from rhub_cli.api.tower.rhub_api_tower_relaunch_job import sync_detailed as relaunch_create
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def relaunch():
    pass


@relaunch.command()
@click.argument("job_id", type=int)
@pass_api
def create(
    api: APIRequest,
    job_id,
):
    """Re-launch Tower job"""

    response = relaunch_create(
        job_id=job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)

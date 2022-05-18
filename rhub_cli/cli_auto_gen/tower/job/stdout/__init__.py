import click

from rhub_cli.api.tower.rhub_api_tower_get_job_stdout import sync_detailed as stdout_get
from rhub_cli.api_request import APIRequest, pass_api


@click.group()
def stdout():
    pass


@stdout.command()
@click.argument("job_id", type=int)
@pass_api
def get(
    api: APIRequest,
    job_id,
):
    """Get stdout of Tower job"""

    response = stdout_get(
        job_id=job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)

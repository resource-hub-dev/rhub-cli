import click

from rhub_cli.api.tower.rhub_api_tower_get_job import sync_detailed as job_get
from rhub_cli.api.tower.rhub_api_tower_list_jobs import sync_detailed as job_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_list_jobs_filter import RhubApiTowerListJobsFilter

from .relaunch import relaunch
from .stdout import stdout


@click.group()
def job():
    pass


@job.command()
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-launched-by", type=str, help="ID of the user who launched template")
@pass_api
def get_list(
    api: APIRequest,
    page,
    limit,
    filter_launched_by,
):
    """List Tower jobs"""

    filter_ = RhubApiTowerListJobsFilter(
        launched_by=filter_launched_by,
    )

    response = job_get_list(
        filter_=filter_,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@job.command()
@click.argument("job_id", type=int)
@pass_api
def get(
    api: APIRequest,
    job_id,
):
    """Get Tower job"""

    response = job_get(
        job_id=job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


job.add_command(relaunch)
job.add_command(stdout)

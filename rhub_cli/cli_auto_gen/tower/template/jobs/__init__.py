import click

from rhub_cli.api.tower.rhub_api_tower_list_template_jobs import sync_detailed as jobs_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_list_template_jobs_filter import RhubApiTowerListTemplateJobsFilter


@click.group()
def jobs():
    pass


@jobs.command()
@click.argument("template_id", type=int)
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-launched-by", type=str, help="ID of the user who launched template")
@pass_api
def get_list(
    api: APIRequest,
    template_id,
    page,
    limit,
    filter_launched_by,
):
    """List Tower template jobs"""

    filter_ = RhubApiTowerListTemplateJobsFilter(
        launched_by=filter_launched_by,
    )

    response = jobs_get_list(
        template_id=template_id,
        filter_=filter_,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)

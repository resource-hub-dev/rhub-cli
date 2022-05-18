import json

import click

from rhub_cli.api.scheduler.rhub_api_scheduler_cron_create_job import sync_detailed as cron_create
from rhub_cli.api.scheduler.rhub_api_scheduler_cron_delete_job import sync_detailed as cron_remove
from rhub_cli.api.scheduler.rhub_api_scheduler_cron_get_job import sync_detailed as cron_get
from rhub_cli.api.scheduler.rhub_api_scheduler_cron_list_jobs import sync_detailed as cron_get_list
from rhub_cli.api.scheduler.rhub_api_scheduler_cron_update_job import sync_detailed as cron_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_scheduler_cron_create_job_json_body import RhubApiSchedulerCronCreateJobJsonBody
from rhub_cli.models.rhub_api_scheduler_cron_create_job_json_body_id import RhubApiSchedulerCronCreateJobJsonBodyId
from rhub_cli.models.rhub_api_scheduler_cron_create_job_json_body_job_name import (
    RhubApiSchedulerCronCreateJobJsonBodyJobName,
)
from rhub_cli.models.rhub_api_scheduler_cron_create_job_json_body_job_params import (
    RhubApiSchedulerCronCreateJobJsonBodyJobParams,
)
from rhub_cli.models.rhub_api_scheduler_cron_list_jobs_filter import RhubApiSchedulerCronListJobsFilter
from rhub_cli.models.rhub_api_scheduler_cron_list_jobs_sort import RhubApiSchedulerCronListJobsSort
from rhub_cli.models.rhub_api_scheduler_cron_update_job_json_body import RhubApiSchedulerCronUpdateJobJsonBody
from rhub_cli.models.rhub_api_scheduler_cron_update_job_json_body_id import RhubApiSchedulerCronUpdateJobJsonBodyId
from rhub_cli.models.rhub_api_scheduler_cron_update_job_json_body_job_name import (
    RhubApiSchedulerCronUpdateJobJsonBodyJobName,
)
from rhub_cli.models.rhub_api_scheduler_cron_update_job_json_body_job_params import (
    RhubApiSchedulerCronUpdateJobJsonBodyJobParams,
)
from rhub_cli.types import UNSET


@click.group()
def cron():
    pass


@cron.command()
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-enabled", is_flag=True)
@click.option(
    "--filter-name",
    type=str,
    help="Name of a job. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_enabled,
    filter_name,
):
    """Get CronJob list"""

    if sort is not None:
        sort = RhubApiSchedulerCronListJobsSort(sort)

    filter_ = RhubApiSchedulerCronListJobsFilter(
        enabled=filter_enabled,
        name=filter_name,
    )

    response = cron_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cron.command()
@click.option("--job-name", required=True, type=click.Choice(["example", "tower_launch", "delete_expired_clusters"]))
@click.option("--name", required=True, type=str)
@click.option("--time-expr", required=True, type=str, help="cron time expression")
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--id")
@click.option("--job-params")
@click.option("--last-run", type=click.DateTime())
@pass_api
def create(
    api: APIRequest,
    job_name,
    name,
    time_expr,
    description,
    enabled,
    id,
    job_params,
    last_run,
):
    """Create CronJob"""

    if job_params is None:
        job_params = UNSET
    else:
        _tmp = RhubApiSchedulerCronCreateJobJsonBodyJobParams()
        _tmp.additional_properties = json.loads(job_params)  # TODO: check if dict
        job_params = _tmp

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiSchedulerCronCreateJobJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    if job_name is not None:
        job_name = RhubApiSchedulerCronCreateJobJsonBodyJobName(job_name)

    json_body = RhubApiSchedulerCronCreateJobJsonBody(
        job_name=job_name,
        name=name,
        time_expr=time_expr,
        description=description,
        enabled=enabled,
        id=id,
        job_params=job_params,
        last_run=last_run,
    )

    response = cron_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cron.command()
@click.argument("cron_job_id", type=int)
@pass_api
def get(
    api: APIRequest,
    cron_job_id,
):
    """Get CronJob"""

    response = cron_get(
        cron_job_id=cron_job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cron.command()
@click.argument("cron_job_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    cron_job_id,
):
    """Delete CronJob"""

    response = cron_remove(
        cron_job_id=cron_job_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cron.command()
@click.argument("cron_job_id", type=int)
@click.option("--description", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--id")
@click.option("--job-name", type=click.Choice(["example", "tower_launch", "delete_expired_clusters"]))
@click.option("--job-params")
@click.option("--last-run", type=click.DateTime())
@click.option("--name", type=str)
@click.option("--time-expr", type=str, help="cron time expression")
@pass_api
def update(
    api: APIRequest,
    cron_job_id,
    description,
    enabled,
    id,
    job_name,
    job_params,
    last_run,
    name,
    time_expr,
):
    """Update CronJob"""

    if job_params is None:
        job_params = UNSET
    else:
        _tmp = RhubApiSchedulerCronUpdateJobJsonBodyJobParams()
        _tmp.additional_properties = json.loads(job_params)  # TODO: check if dict
        job_params = _tmp

    if job_name is not None:
        job_name = RhubApiSchedulerCronUpdateJobJsonBodyJobName(job_name)

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiSchedulerCronUpdateJobJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiSchedulerCronUpdateJobJsonBody(
        description=description,
        enabled=enabled,
        id=id,
        job_name=job_name,
        job_params=job_params,
        last_run=last_run,
        name=name,
        time_expr=time_expr,
    )

    response = cron_update(
        cron_job_id=cron_job_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

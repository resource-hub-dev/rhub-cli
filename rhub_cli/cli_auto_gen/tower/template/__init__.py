import json

import click

from rhub_cli.api.tower.rhub_api_tower_create_template import sync_detailed as template_create
from rhub_cli.api.tower.rhub_api_tower_delete_template import sync_detailed as template_remove
from rhub_cli.api.tower.rhub_api_tower_get_template import sync_detailed as template_get
from rhub_cli.api.tower.rhub_api_tower_list_templates import sync_detailed as template_get_list
from rhub_cli.api.tower.rhub_api_tower_update_template import sync_detailed as template_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_create_template_json_body import RhubApiTowerCreateTemplateJsonBody
from rhub_cli.models.rhub_api_tower_create_template_json_body_id import RhubApiTowerCreateTemplateJsonBodyId
from rhub_cli.models.rhub_api_tower_list_templates_filter import RhubApiTowerListTemplatesFilter
from rhub_cli.models.rhub_api_tower_list_templates_sort import RhubApiTowerListTemplatesSort
from rhub_cli.models.rhub_api_tower_update_template_json_body import RhubApiTowerUpdateTemplateJsonBody
from rhub_cli.models.rhub_api_tower_update_template_json_body_id import RhubApiTowerUpdateTemplateJsonBodyId
from rhub_cli.types import UNSET

from .jobs import jobs
from .launch import launch


@click.group()
def template():
    pass


@template.command()
@click.option("--sort", type=click.Choice(["name", "-name"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option(
    "--filter-name",
    type=str,
    help="Name of a template. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option("--filter-server-id", type=int, help="ID of the server")
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_name,
    filter_server_id,
):
    """Get list of Tower templates"""

    if sort is not None:
        sort = RhubApiTowerListTemplatesSort(sort)

    filter_ = RhubApiTowerListTemplatesFilter(
        name=filter_name,
        server_id=filter_server_id,
    )

    response = template_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@click.option("--name", required=True, type=str)
@click.option("--server-id", required=True, type=int)
@click.option("--tower-template-id", required=True, type=int)
@click.option("--tower-template-is-workflow", required=True, is_flag=True, help="Is template workflow?")
@click.option("--description", type=str)
@click.option("--id", help="Internal ID")
@pass_api
def create(
    api: APIRequest,
    name,
    server_id,
    tower_template_id,
    tower_template_is_workflow,
    description,
    id,
):
    """Create Tower template"""

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiTowerCreateTemplateJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiTowerCreateTemplateJsonBody(
        name=name,
        server_id=server_id,
        tower_template_id=tower_template_id,
        tower_template_is_workflow=tower_template_is_workflow,
        description=description,
        id=id,
    )

    response = template_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@click.argument("template_id", type=int)
@pass_api
def get(
    api: APIRequest,
    template_id,
):
    """Get Tower template"""

    response = template_get(
        template_id=template_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@click.argument("template_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    template_id,
):
    """Delete Tower template"""

    response = template_remove(
        template_id=template_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@template.command()
@click.argument("template_id", type=int)
@click.option("--description", type=str)
@click.option("--id", help="Internal ID")
@click.option("--name", type=str)
@click.option("--server-id", type=int)
@click.option("--tower-template-id", type=int)
@click.option("--tower-template-is-workflow", is_flag=True, help="Is template workflow?")
@pass_api
def update(
    api: APIRequest,
    template_id,
    description,
    id,
    name,
    server_id,
    tower_template_id,
    tower_template_is_workflow,
):
    """Change Tower template"""

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiTowerUpdateTemplateJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    json_body = RhubApiTowerUpdateTemplateJsonBody(
        description=description,
        id=id,
        name=name,
        server_id=server_id,
        tower_template_id=tower_template_id,
        tower_template_is_workflow=tower_template_is_workflow,
    )

    response = template_update(
        template_id=template_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


template.add_command(jobs)
template.add_command(launch)

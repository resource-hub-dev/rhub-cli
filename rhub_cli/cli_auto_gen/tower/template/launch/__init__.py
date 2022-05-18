import json

import click

from rhub_cli.api.tower.rhub_api_tower_launch_template import sync_detailed as launch_create
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_launch_template_json_body import RhubApiTowerLaunchTemplateJsonBody
from rhub_cli.models.rhub_api_tower_launch_template_json_body_extra_vars import (
    RhubApiTowerLaunchTemplateJsonBodyExtraVars,
)
from rhub_cli.types import UNSET


@click.group()
def launch():
    pass


@launch.command()
@click.argument("template_id", type=int)
@click.option("--extra-vars", required=True, help="Extra variable to pass to the template")
@pass_api
def create(
    api: APIRequest,
    template_id,
    extra_vars,
):
    """Launch Tower template"""

    if extra_vars is None:
        extra_vars = UNSET
    else:
        _tmp = RhubApiTowerLaunchTemplateJsonBodyExtraVars()
        _tmp.additional_properties = json.loads(extra_vars)  # TODO: check if dict
        extra_vars = _tmp

    json_body = RhubApiTowerLaunchTemplateJsonBody(
        extra_vars=extra_vars,
    )

    response = launch_create(
        template_id=template_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

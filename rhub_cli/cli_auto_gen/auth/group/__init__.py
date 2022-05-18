import json

import click

from rhub_cli.api.auth.rhub_api_auth_group_create_group import sync_detailed as group_create
from rhub_cli.api.auth.rhub_api_auth_group_delete_group import sync_detailed as group_remove
from rhub_cli.api.auth.rhub_api_auth_group_get_group import sync_detailed as group_get
from rhub_cli.api.auth.rhub_api_auth_group_list_groups import sync_detailed as group_get_list
from rhub_cli.api.auth.rhub_api_auth_group_update_group import sync_detailed as group_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_auth_group_create_group_json_body import RhubApiAuthGroupCreateGroupJsonBody
from rhub_cli.models.rhub_api_auth_group_create_group_json_body_attributes import (
    RhubApiAuthGroupCreateGroupJsonBodyAttributes,
)
from rhub_cli.models.rhub_api_auth_group_create_group_json_body_id import RhubApiAuthGroupCreateGroupJsonBodyId
from rhub_cli.models.rhub_api_auth_group_update_group_json_body import RhubApiAuthGroupUpdateGroupJsonBody
from rhub_cli.models.rhub_api_auth_group_update_group_json_body_attributes import (
    RhubApiAuthGroupUpdateGroupJsonBodyAttributes,
)
from rhub_cli.models.rhub_api_auth_group_update_group_json_body_id import RhubApiAuthGroupUpdateGroupJsonBodyId
from rhub_cli.types import UNSET

from .roles import roles
from .users import users


@click.group()
def group():
    pass


@group.command()
@pass_api
def get_list(
    api: APIRequest,
):
    """Get group list"""

    response = group_get_list(
        client=api.authenticated_client,
    )
    api.handle_response(response)


@group.command()
@click.option("--name", required=True, type=str)
@click.option("--id")
@click.option("--attributes-additional-property-item", type=str)
@pass_api
def create(
    api: APIRequest,
    name,
    id,
    attributes_additional_property_item,
):
    """Create group"""

    attributes_additional_property = []
    if attributes_additional_property_item is not None:
        attributes_additional_property.append(attributes_additional_property_item)

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiAuthGroupCreateGroupJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    attributes = RhubApiAuthGroupCreateGroupJsonBodyAttributes()
    attributes.additional_properties = {"attributes": attributes_additional_property}

    json_body = RhubApiAuthGroupCreateGroupJsonBody(
        name=name,
        attributes=attributes,
        id=id,
    )

    response = group_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@group.command()
@click.argument("group_id", type=str)
@pass_api
def get(
    api: APIRequest,
    group_id,
):
    """Get group"""

    response = group_get(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@group.command()
@click.argument("group_id", type=str)
@pass_api
def remove(
    api: APIRequest,
    group_id,
):
    """Delete group"""

    response = group_remove(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@group.command()
@click.argument("group_id", type=str)
@click.option("--id")
@click.option("--name", type=str)
@click.option("--attributes-additional-property-item", type=str)
@pass_api
def update(
    api: APIRequest,
    group_id,
    id,
    name,
    attributes_additional_property_item,
):
    """Update group"""

    attributes_additional_property = []
    if attributes_additional_property_item is not None:
        attributes_additional_property.append(attributes_additional_property_item)

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiAuthGroupUpdateGroupJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    attributes = RhubApiAuthGroupUpdateGroupJsonBodyAttributes()
    attributes.additional_properties = {"attributes": attributes_additional_property}

    json_body = RhubApiAuthGroupUpdateGroupJsonBody(
        attributes=attributes,
        id=id,
        name=name,
    )

    response = group_update(
        group_id=group_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


group.add_command(roles)
group.add_command(users)

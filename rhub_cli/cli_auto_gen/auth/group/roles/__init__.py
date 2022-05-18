import click

from rhub_cli.api.auth.rhub_api_auth_group_add_group_role import sync_detailed as roles_create
from rhub_cli.api.auth.rhub_api_auth_group_delete_group_role import sync_detailed as roles_remove
from rhub_cli.api.auth.rhub_api_auth_group_list_group_roles import sync_detailed as roles_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_auth_group_add_group_role_json_body import RhubApiAuthGroupAddGroupRoleJsonBody
from rhub_cli.models.rhub_api_auth_group_delete_group_role_json_body import RhubApiAuthGroupDeleteGroupRoleJsonBody


@click.group()
def roles():
    pass


@roles.command()
@click.argument("group_id", type=str)
@pass_api
def get_list(
    api: APIRequest,
    group_id,
):
    """Get group roles"""

    response = roles_get_list(
        group_id=group_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@roles.command()
@click.argument("group_id", type=str)
@click.option("--id", required=True, type=str)
@pass_api
def create(
    api: APIRequest,
    group_id,
    id,
):
    """Add group to role"""

    json_body = RhubApiAuthGroupAddGroupRoleJsonBody(
        id=id,
    )

    response = roles_create(
        group_id=group_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@roles.command()
@click.argument("group_id", type=str)
@click.option("--id", required=True, type=str)
@pass_api
def remove(
    api: APIRequest,
    group_id,
    id,
):
    """Remove group from role"""

    json_body = RhubApiAuthGroupDeleteGroupRoleJsonBody(
        id=id,
    )

    response = roles_remove(
        group_id=group_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

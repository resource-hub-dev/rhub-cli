import click

from rhub_cli.api.auth.rhub_api_auth_user_create_user import sync_detailed as user_create
from rhub_cli.api.auth.rhub_api_auth_user_delete_user import sync_detailed as user_remove
from rhub_cli.api.auth.rhub_api_auth_user_get_user import sync_detailed as user_get
from rhub_cli.api.auth.rhub_api_auth_user_list_users import sync_detailed as user_get_list
from rhub_cli.api.auth.rhub_api_auth_user_update_user import sync_detailed as user_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_auth_user_create_user_json_body import RhubApiAuthUserCreateUserJsonBody
from rhub_cli.models.rhub_api_auth_user_list_users_filter import RhubApiAuthUserListUsersFilter
from rhub_cli.models.rhub_api_auth_user_update_user_json_body import RhubApiAuthUserUpdateUserJsonBody

from .groups import groups
from .roles import roles


@click.group()
def user():
    pass


@user.command()
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--filter-email", type=str)
@click.option("--filter-first-name", type=str)
@click.option("--filter-last-name", type=str)
@click.option("--filter-username", type=str)
@pass_api
def get_list(
    api: APIRequest,
    page,
    limit,
    filter_email,
    filter_first_name,
    filter_last_name,
    filter_username,
):
    """Get user list"""

    filter_ = RhubApiAuthUserListUsersFilter(
        email=filter_email,
        first_name=filter_first_name,
        last_name=filter_last_name,
        username=filter_username,
    )

    response = user_get_list(
        filter_=filter_,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@user.command()
@click.option("--email", required=True, type=str)
@click.option("--username", required=True, type=str)
@click.option("--enabled", is_flag=True)
@click.option("--first-name", type=str)
@click.option("--last-name", type=str)
@click.option("--password", type=str)
@pass_api
def create(
    api: APIRequest,
    email,
    username,
    enabled,
    first_name,
    last_name,
    password,
):
    """Create user"""

    json_body = RhubApiAuthUserCreateUserJsonBody(
        email=email,
        username=username,
        enabled=enabled,
        first_name=first_name,
        last_name=last_name,
        password=password,
    )

    response = user_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@user.command()
@click.argument("user_id", type=str)
@pass_api
def get(
    api: APIRequest,
    user_id,
):
    """Get user"""

    response = user_get(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@user.command()
@click.argument("user_id", type=str)
@pass_api
def remove(
    api: APIRequest,
    user_id,
):
    """Delete user"""

    response = user_remove(
        user_id=user_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@user.command()
@click.argument("user_id", type=str)
@click.option("--email", type=str)
@click.option("--enabled", is_flag=True)
@click.option("--first-name", type=str)
@click.option("--last-name", type=str)
@click.option("--password", type=str)
@click.option("--username", type=str)
@pass_api
def update(
    api: APIRequest,
    user_id,
    email,
    enabled,
    first_name,
    last_name,
    password,
    username,
):
    """Update user"""

    json_body = RhubApiAuthUserUpdateUserJsonBody(
        email=email,
        enabled=enabled,
        first_name=first_name,
        last_name=last_name,
        password=password,
        username=username,
    )

    response = user_update(
        user_id=user_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


user.add_command(groups)
user.add_command(roles)

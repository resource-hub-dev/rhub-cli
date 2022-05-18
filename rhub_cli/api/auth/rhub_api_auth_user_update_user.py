from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_user_update_user_json_body import RhubApiAuthUserUpdateUserJsonBody
from ...models.rhub_api_auth_user_update_user_response_200 import RhubApiAuthUserUpdateUserResponse200
from ...models.rhub_api_auth_user_update_user_response_default import RhubApiAuthUserUpdateUserResponseDefault
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserUpdateUserJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthUserUpdateUserResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthUserUpdateUserResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserUpdateUserJsonBody,
) -> Response[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]:
    """Update user

     Update user in the database. Returns updated user data including extra
    fields added by auth database.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        user_id (str):
        json_body (RhubApiAuthUserUpdateUserJsonBody): See [Keycloak API: UserRepresentation](
              https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
             Example: {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True,
            'mapRoles': True, 'view': True}, 'createdTimestamp': 1614717256570,
            'disableableCredentialTypes': [], 'email': 'testuser1@example.com', 'emailVerified':
            False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
            'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username':
            'testuser1'}.

    Returns:
        Response[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserUpdateUserJsonBody,
) -> Optional[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]:
    """Update user

     Update user in the database. Returns updated user data including extra
    fields added by auth database.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        user_id (str):
        json_body (RhubApiAuthUserUpdateUserJsonBody): See [Keycloak API: UserRepresentation](
              https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
             Example: {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True,
            'mapRoles': True, 'view': True}, 'createdTimestamp': 1614717256570,
            'disableableCredentialTypes': [], 'email': 'testuser1@example.com', 'emailVerified':
            False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
            'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username':
            'testuser1'}.

    Returns:
        Response[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserUpdateUserJsonBody,
) -> Response[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]:
    """Update user

     Update user in the database. Returns updated user data including extra
    fields added by auth database.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        user_id (str):
        json_body (RhubApiAuthUserUpdateUserJsonBody): See [Keycloak API: UserRepresentation](
              https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
             Example: {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True,
            'mapRoles': True, 'view': True}, 'createdTimestamp': 1614717256570,
            'disableableCredentialTypes': [], 'email': 'testuser1@example.com', 'emailVerified':
            False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
            'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username':
            'testuser1'}.

    Returns:
        Response[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserUpdateUserJsonBody,
) -> Optional[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]:
    """Update user

     Update user in the database. Returns updated user data including extra
    fields added by auth database.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        user_id (str):
        json_body (RhubApiAuthUserUpdateUserJsonBody): See [Keycloak API: UserRepresentation](
              https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
             Example: {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True,
            'mapRoles': True, 'view': True}, 'createdTimestamp': 1614717256570,
            'disableableCredentialTypes': [], 'email': 'testuser1@example.com', 'emailVerified':
            False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
            'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username':
            'testuser1'}.

    Returns:
        Response[Union[RhubApiAuthUserUpdateUserResponse200, RhubApiAuthUserUpdateUserResponseDefault]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

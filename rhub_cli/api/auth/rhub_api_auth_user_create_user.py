from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_user_create_user_json_body import RhubApiAuthUserCreateUserJsonBody
from ...models.rhub_api_auth_user_create_user_response_200 import RhubApiAuthUserCreateUserResponse200
from ...models.rhub_api_auth_user_create_user_response_default import RhubApiAuthUserCreateUserResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserCreateUserJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/user".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthUserCreateUserResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthUserCreateUserResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserCreateUserJsonBody,
) -> Response[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]:
    """Create user

     Create a user in the database. Returns created user data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        json_body (RhubApiAuthUserCreateUserJsonBody): See [Keycloak API: UserRepresentation](
              https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
             Example: {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True,
            'mapRoles': True, 'view': True}, 'createdTimestamp': 1614717256570,
            'disableableCredentialTypes': [], 'email': 'testuser1@example.com', 'emailVerified':
            False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
            'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username':
            'testuser1'}.

    Returns:
        Response[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserCreateUserJsonBody,
) -> Optional[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]:
    """Create user

     Create a user in the database. Returns created user data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        json_body (RhubApiAuthUserCreateUserJsonBody): See [Keycloak API: UserRepresentation](
              https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
             Example: {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True,
            'mapRoles': True, 'view': True}, 'createdTimestamp': 1614717256570,
            'disableableCredentialTypes': [], 'email': 'testuser1@example.com', 'emailVerified':
            False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
            'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username':
            'testuser1'}.

    Returns:
        Response[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserCreateUserJsonBody,
) -> Response[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]:
    """Create user

     Create a user in the database. Returns created user data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        json_body (RhubApiAuthUserCreateUserJsonBody): See [Keycloak API: UserRepresentation](
              https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
             Example: {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True,
            'mapRoles': True, 'view': True}, 'createdTimestamp': 1614717256570,
            'disableableCredentialTypes': [], 'email': 'testuser1@example.com', 'emailVerified':
            False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
            'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username':
            'testuser1'}.

    Returns:
        Response[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserCreateUserJsonBody,
) -> Optional[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]:
    """Create user

     Create a user in the database. Returns created user data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        json_body (RhubApiAuthUserCreateUserJsonBody): See [Keycloak API: UserRepresentation](
              https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)
             Example: {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True,
            'mapRoles': True, 'view': True}, 'createdTimestamp': 1614717256570,
            'disableableCredentialTypes': [], 'email': 'testuser1@example.com', 'emailVerified':
            False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
            'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username':
            'testuser1'}.

    Returns:
        Response[Union[RhubApiAuthUserCreateUserResponse200, RhubApiAuthUserCreateUserResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

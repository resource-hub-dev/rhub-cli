from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_role_create_role_json_body import RhubApiAuthRoleCreateRoleJsonBody
from ...models.rhub_api_auth_role_create_role_response_200 import RhubApiAuthRoleCreateRoleResponse200
from ...models.rhub_api_auth_role_create_role_response_default import RhubApiAuthRoleCreateRoleResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthRoleCreateRoleJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/role".format(client.base_url)

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
) -> Optional[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthRoleCreateRoleResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthRoleCreateRoleResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthRoleCreateRoleJsonBody,
) -> Response[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]:
    """Create role

     Create a role in the database. Returns created role data with extra
    fields added by auth database (UUID and other fields).

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        json_body (RhubApiAuthRoleCreateRoleJsonBody):

    Returns:
        Response[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]
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
    json_body: RhubApiAuthRoleCreateRoleJsonBody,
) -> Optional[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]:
    """Create role

     Create a role in the database. Returns created role data with extra
    fields added by auth database (UUID and other fields).

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        json_body (RhubApiAuthRoleCreateRoleJsonBody):

    Returns:
        Response[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthRoleCreateRoleJsonBody,
) -> Response[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]:
    """Create role

     Create a role in the database. Returns created role data with extra
    fields added by auth database (UUID and other fields).

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        json_body (RhubApiAuthRoleCreateRoleJsonBody):

    Returns:
        Response[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]
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
    json_body: RhubApiAuthRoleCreateRoleJsonBody,
) -> Optional[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]:
    """Create role

     Create a role in the database. Returns created role data with extra
    fields added by auth database (UUID and other fields).

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        json_body (RhubApiAuthRoleCreateRoleJsonBody):

    Returns:
        Response[Union[RhubApiAuthRoleCreateRoleResponse200, RhubApiAuthRoleCreateRoleResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_role_get_role_response_200 import RhubApiAuthRoleGetRoleResponse200
from ...models.rhub_api_auth_role_get_role_response_default import RhubApiAuthRoleGetRoleResponseDefault
from ...types import Response


def _get_kwargs(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/role/{role_id}".format(client.base_url, role_id=role_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthRoleGetRoleResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthRoleGetRoleResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]:
    """Get role

     Returns role data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `description` and others.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        role_id (str):

    Returns:
        Response[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]:
    """Get role

     Returns role data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `description` and others.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        role_id (str):

    Returns:
        Response[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]:
    """Get role

     Returns role data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `description` and others.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        role_id (str):

    Returns:
        Response[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]:
    """Get role

     Returns role data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `description` and others.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        role_id (str):

    Returns:
        Response[Union[RhubApiAuthRoleGetRoleResponse200, RhubApiAuthRoleGetRoleResponseDefault]]
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
        )
    ).parsed

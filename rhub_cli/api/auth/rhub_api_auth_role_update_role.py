from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_role_update_role_json_body import RhubApiAuthRoleUpdateRoleJsonBody
from ...models.rhub_api_auth_role_update_role_response_200 import RhubApiAuthRoleUpdateRoleResponse200
from ...models.rhub_api_auth_role_update_role_response_default import RhubApiAuthRoleUpdateRoleResponseDefault
from ...types import Response


def _get_kwargs(
    role_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthRoleUpdateRoleJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/role/{role_id}".format(client.base_url, role_id=role_id)

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
) -> Optional[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthRoleUpdateRoleResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthRoleUpdateRoleResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]:
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
    json_body: RhubApiAuthRoleUpdateRoleJsonBody,
) -> Response[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]:
    """Update role

     Update role in the database. Returns updated role data including extra
    fields added by auth database.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        role_id (str):
        json_body (RhubApiAuthRoleUpdateRoleJsonBody): See [Keycloak API: RoleRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
             Example: {'attributes': {}, 'clientRole': False, 'composite': False, 'composites': {},
            'containerId': 'admin', 'description': 'adminRole', 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin'}.

    Returns:
        Response[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubApiAuthRoleUpdateRoleJsonBody,
) -> Optional[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]:
    """Update role

     Update role in the database. Returns updated role data including extra
    fields added by auth database.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        role_id (str):
        json_body (RhubApiAuthRoleUpdateRoleJsonBody): See [Keycloak API: RoleRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
             Example: {'attributes': {}, 'clientRole': False, 'composite': False, 'composites': {},
            'containerId': 'admin', 'description': 'adminRole', 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin'}.

    Returns:
        Response[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthRoleUpdateRoleJsonBody,
) -> Response[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]:
    """Update role

     Update role in the database. Returns updated role data including extra
    fields added by auth database.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        role_id (str):
        json_body (RhubApiAuthRoleUpdateRoleJsonBody): See [Keycloak API: RoleRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
             Example: {'attributes': {}, 'clientRole': False, 'composite': False, 'composites': {},
            'containerId': 'admin', 'description': 'adminRole', 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin'}.

    Returns:
        Response[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    role_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthRoleUpdateRoleJsonBody,
) -> Optional[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]:
    """Update role

     Update role in the database. Returns updated role data including extra
    fields added by auth database.

    See [Keycloak API: RoleRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

    Args:
        role_id (str):
        json_body (RhubApiAuthRoleUpdateRoleJsonBody): See [Keycloak API: RoleRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)
             Example: {'attributes': {}, 'clientRole': False, 'composite': False, 'composites': {},
            'containerId': 'admin', 'description': 'adminRole', 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin'}.

    Returns:
        Response[Union[RhubApiAuthRoleUpdateRoleResponse200, RhubApiAuthRoleUpdateRoleResponseDefault]]
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

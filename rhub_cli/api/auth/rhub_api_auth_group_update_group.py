from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_group_update_group_json_body import RhubApiAuthGroupUpdateGroupJsonBody
from ...models.rhub_api_auth_group_update_group_response_200 import RhubApiAuthGroupUpdateGroupResponse200
from ...models.rhub_api_auth_group_update_group_response_default import RhubApiAuthGroupUpdateGroupResponseDefault
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthGroupUpdateGroupJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/group/{group_id}".format(client.base_url, group_id=group_id)

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
) -> Optional[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthGroupUpdateGroupResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthGroupUpdateGroupResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthGroupUpdateGroupJsonBody,
) -> Response[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]:
    """Update group

     Update group in the database. Returns updated group data including extra
    fields added by auth database.

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        group_id (str):
        json_body (RhubApiAuthGroupUpdateGroupJsonBody): See [Keycloak API: GroupRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
             Example: {'access': {'manage': True, 'manageMembership': True, 'view': True},
            'attributes': {'mailing-list': ['admin-list@example.com']}, 'clientRoles': {}, 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path': '/admin', 'realmRoles':
            [], 'subGroups': []}.

    Returns:
        Response[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthGroupUpdateGroupJsonBody,
) -> Optional[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]:
    """Update group

     Update group in the database. Returns updated group data including extra
    fields added by auth database.

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        group_id (str):
        json_body (RhubApiAuthGroupUpdateGroupJsonBody): See [Keycloak API: GroupRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
             Example: {'access': {'manage': True, 'manageMembership': True, 'view': True},
            'attributes': {'mailing-list': ['admin-list@example.com']}, 'clientRoles': {}, 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path': '/admin', 'realmRoles':
            [], 'subGroups': []}.

    Returns:
        Response[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthGroupUpdateGroupJsonBody,
) -> Response[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]:
    """Update group

     Update group in the database. Returns updated group data including extra
    fields added by auth database.

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        group_id (str):
        json_body (RhubApiAuthGroupUpdateGroupJsonBody): See [Keycloak API: GroupRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
             Example: {'access': {'manage': True, 'manageMembership': True, 'view': True},
            'attributes': {'mailing-list': ['admin-list@example.com']}, 'clientRoles': {}, 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path': '/admin', 'realmRoles':
            [], 'subGroups': []}.

    Returns:
        Response[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthGroupUpdateGroupJsonBody,
) -> Optional[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]:
    """Update group

     Update group in the database. Returns updated group data including extra
    fields added by auth database.

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        group_id (str):
        json_body (RhubApiAuthGroupUpdateGroupJsonBody): See [Keycloak API: GroupRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
             Example: {'access': {'manage': True, 'manageMembership': True, 'view': True},
            'attributes': {'mailing-list': ['admin-list@example.com']}, 'clientRoles': {}, 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path': '/admin', 'realmRoles':
            [], 'subGroups': []}.

    Returns:
        Response[Union[RhubApiAuthGroupUpdateGroupResponse200, RhubApiAuthGroupUpdateGroupResponseDefault]]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

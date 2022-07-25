from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_group_create_group_json_body import RhubApiAuthGroupCreateGroupJsonBody
from ...models.rhub_api_auth_group_create_group_response_200 import RhubApiAuthGroupCreateGroupResponse200
from ...models.rhub_api_auth_group_create_group_response_default import RhubApiAuthGroupCreateGroupResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthGroupCreateGroupJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/group".format(client.base_url)

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
) -> Optional[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthGroupCreateGroupResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthGroupCreateGroupResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthGroupCreateGroupJsonBody,
) -> Response[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]:
    """Create group

     Create a group in the database. Returns created group data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        json_body (RhubApiAuthGroupCreateGroupJsonBody): See [Keycloak API: GroupRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
             Example: {'access': {'manage': True, 'manageMembership': True, 'view': True},
            'attributes': {'mailing-list': ['admin-list@example.com']}, 'clientRoles': {}, 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path': '/admin', 'realmRoles':
            [], 'subGroups': []}.

    Returns:
        Response[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]
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
    json_body: RhubApiAuthGroupCreateGroupJsonBody,
) -> Optional[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]:
    """Create group

     Create a group in the database. Returns created group data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        json_body (RhubApiAuthGroupCreateGroupJsonBody): See [Keycloak API: GroupRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
             Example: {'access': {'manage': True, 'manageMembership': True, 'view': True},
            'attributes': {'mailing-list': ['admin-list@example.com']}, 'clientRoles': {}, 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path': '/admin', 'realmRoles':
            [], 'subGroups': []}.

    Returns:
        Response[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthGroupCreateGroupJsonBody,
) -> Response[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]:
    """Create group

     Create a group in the database. Returns created group data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        json_body (RhubApiAuthGroupCreateGroupJsonBody): See [Keycloak API: GroupRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
             Example: {'access': {'manage': True, 'manageMembership': True, 'view': True},
            'attributes': {'mailing-list': ['admin-list@example.com']}, 'clientRoles': {}, 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path': '/admin', 'realmRoles':
            [], 'subGroups': []}.

    Returns:
        Response[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]
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
    json_body: RhubApiAuthGroupCreateGroupJsonBody,
) -> Optional[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]:
    """Create group

     Create a group in the database. Returns created group data with extra
    fields added by auth database (UUID and other fields).

    See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        json_body (RhubApiAuthGroupCreateGroupJsonBody): See [Keycloak API: GroupRepresentation](
            https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)
             Example: {'access': {'manage': True, 'manageMembership': True, 'view': True},
            'attributes': {'mailing-list': ['admin-list@example.com']}, 'clientRoles': {}, 'id':
            'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path': '/admin', 'realmRoles':
            [], 'subGroups': []}.

    Returns:
        Response[Union[RhubApiAuthGroupCreateGroupResponse200, RhubApiAuthGroupCreateGroupResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

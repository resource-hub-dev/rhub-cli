from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_user_list_user_groups_response_200_item import RhubApiAuthUserListUserGroupsResponse200Item
from ...models.rhub_api_auth_user_list_user_groups_response_default import RhubApiAuthUserListUserGroupsResponseDefault
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}/groups".format(client.base_url, user_id=user_id)

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
) -> Optional[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubApiAuthUserListUserGroupsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubApiAuthUserListUserGroupsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]:
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
) -> Response[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]:
    """Get user groups

     See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        user_id (str):

    Returns:
        Response[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
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
) -> Optional[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]:
    """Get user groups

     See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        user_id (str):

    Returns:
        Response[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]:
    """Get user groups

     See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        user_id (str):

    Returns:
        Response[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]:
    """Get user groups

     See also [Keycloak API: GroupRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

    Args:
        user_id (str):

    Returns:
        Response[Union[List[RhubApiAuthUserListUserGroupsResponse200Item], RhubApiAuthUserListUserGroupsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed

from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_user_list_user_roles_response_200_item import RhubApiAuthUserListUserRolesResponse200Item
from ...models.rhub_api_auth_user_list_user_roles_response_default import RhubApiAuthUserListUserRolesResponseDefault
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}/roles".format(client.base_url, user_id=user_id)

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
) -> Optional[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubApiAuthUserListUserRolesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubApiAuthUserListUserRolesResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]:
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
) -> Response[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]:
    """Get user roles

    Args:
        user_id (str):

    Returns:
        Response[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]
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
) -> Optional[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]:
    """Get user roles

    Args:
        user_id (str):

    Returns:
        Response[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]:
    """Get user roles

    Args:
        user_id (str):

    Returns:
        Response[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]
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
) -> Optional[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]:
    """Get user roles

    Args:
        user_id (str):

    Returns:
        Response[Union[List[RhubApiAuthUserListUserRolesResponse200Item], RhubApiAuthUserListUserRolesResponseDefault]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed

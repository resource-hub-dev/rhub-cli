from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_role_delete_role_response_default import RhubApiAuthRoleDeleteRoleResponseDefault
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
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiAuthRoleDeleteRoleResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]:
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
) -> Response[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]:
    """Delete role

    Args:
        role_id (str):

    Returns:
        Response[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]
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
) -> Optional[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]:
    """Delete role

    Args:
        role_id (str):

    Returns:
        Response[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]:
    """Delete role

    Args:
        role_id (str):

    Returns:
        Response[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]
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
) -> Optional[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]:
    """Delete role

    Args:
        role_id (str):

    Returns:
        Response[Union[Any, RhubApiAuthRoleDeleteRoleResponseDefault]]
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
        )
    ).parsed

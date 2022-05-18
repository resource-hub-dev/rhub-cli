from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_group_delete_group_response_default import RhubApiAuthGroupDeleteGroupResponseDefault
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/group/{group_id}".format(client.base_url, group_id=group_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiAuthGroupDeleteGroupResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]:
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
) -> Response[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]:
    """Delete group

    Args:
        group_id (str):

    Returns:
        Response[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
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
) -> Optional[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]:
    """Delete group

    Args:
        group_id (str):

    Returns:
        Response[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]:
    """Delete group

    Args:
        group_id (str):

    Returns:
        Response[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]:
    """Delete group

    Args:
        group_id (str):

    Returns:
        Response[Union[Any, RhubApiAuthGroupDeleteGroupResponseDefault]]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed

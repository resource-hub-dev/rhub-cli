from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_cluster_get_cluster_event_response_default import (
    RhubApiLabClusterGetClusterEventResponseDefault,
)
from ...types import Response


def _get_kwargs(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/cluster_event/{event_id}".format(client.base_url, event_id=event_id)

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
) -> Optional[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Any:
            return cast(Any, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    else:
        response_default = RhubApiLabClusterGetClusterEventResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]:
    """Get cluster event

    Args:
        event_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]:
    """Get cluster event

    Args:
        event_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]:
    """Get cluster event

    Args:
        event_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]:
    """Get cluster event

    Args:
        event_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterGetClusterEventResponseDefault]]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
        )
    ).parsed

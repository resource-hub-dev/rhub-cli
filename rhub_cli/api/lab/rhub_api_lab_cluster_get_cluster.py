from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_cluster_get_cluster_response_200 import RhubApiLabClusterGetClusterResponse200
from ...models.rhub_api_lab_cluster_get_cluster_response_default import RhubApiLabClusterGetClusterResponseDefault
from ...types import Response


def _get_kwargs(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/cluster/{cluster_id}".format(client.base_url, cluster_id=cluster_id)

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
) -> Optional[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiLabClusterGetClusterResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiLabClusterGetClusterResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]:
    """Get cluster

    Args:
        cluster_id (int):

    Returns:
        Response[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]:
    """Get cluster

    Args:
        cluster_id (int):

    Returns:
        Response[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]:
    """Get cluster

    Args:
        cluster_id (int):

    Returns:
        Response[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]:
    """Get cluster

    Args:
        cluster_id (int):

    Returns:
        Response[Union[RhubApiLabClusterGetClusterResponse200, RhubApiLabClusterGetClusterResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed

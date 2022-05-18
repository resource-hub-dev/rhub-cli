from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_cluster_delete_cluster_hosts_response_default import (
    RhubApiLabClusterDeleteClusterHostsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/cluster/{cluster_id}/hosts".format(client.base_url, cluster_id=cluster_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    else:
        response_default = RhubApiLabClusterDeleteClusterHostsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]:
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
) -> Response[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]:
    """Delete cluster hosts

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]
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
) -> Optional[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]:
    """Delete cluster hosts

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]:
    """Delete cluster hosts

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]
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
) -> Optional[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]:
    """Delete cluster hosts

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterDeleteClusterHostsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed

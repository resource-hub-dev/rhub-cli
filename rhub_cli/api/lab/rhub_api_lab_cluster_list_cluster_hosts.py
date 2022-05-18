from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_cluster_list_cluster_hosts_response_200_item import (
    RhubApiLabClusterListClusterHostsResponse200Item,
)
from ...models.rhub_api_lab_cluster_list_cluster_hosts_response_default import (
    RhubApiLabClusterListClusterHostsResponseDefault,
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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.text
        for response_200_item_data in _response_200:
            response_200_item = RhubApiLabClusterListClusterHostsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubApiLabClusterListClusterHostsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]
]:
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
) -> Response[
    Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]
]:
    """Get cluster hosts

    Args:
        cluster_id (int):

    Returns:
        Response[Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]]
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
) -> Optional[
    Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]
]:
    """Get cluster hosts

    Args:
        cluster_id (int):

    Returns:
        Response[Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]
]:
    """Get cluster hosts

    Args:
        cluster_id (int):

    Returns:
        Response[Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]]
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
) -> Optional[
    Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]
]:
    """Get cluster hosts

    Args:
        cluster_id (int):

    Returns:
        Response[Union[List[RhubApiLabClusterListClusterHostsResponse200Item], RhubApiLabClusterListClusterHostsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed

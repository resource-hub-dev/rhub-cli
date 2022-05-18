from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_cluster_update_cluster_json_body import RhubApiLabClusterUpdateClusterJsonBody
from ...models.rhub_api_lab_cluster_update_cluster_response_200 import RhubApiLabClusterUpdateClusterResponse200
from ...models.rhub_api_lab_cluster_update_cluster_response_default import RhubApiLabClusterUpdateClusterResponseDefault
from ...types import Response


def _get_kwargs(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabClusterUpdateClusterJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/cluster/{cluster_id}".format(client.base_url, cluster_id=cluster_id)

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
) -> Optional[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiLabClusterUpdateClusterResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiLabClusterUpdateClusterResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]:
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
    json_body: RhubApiLabClusterUpdateClusterJsonBody,
) -> Response[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]:
    """Update cluster

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster) for more info.

    Args:
        cluster_id (int):
        json_body (RhubApiLabClusterUpdateClusterJsonBody):

    Returns:
        Response[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubApiLabClusterUpdateClusterJsonBody,
) -> Optional[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]:
    """Update cluster

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster) for more info.

    Args:
        cluster_id (int):
        json_body (RhubApiLabClusterUpdateClusterJsonBody):

    Returns:
        Response[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabClusterUpdateClusterJsonBody,
) -> Response[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]:
    """Update cluster

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster) for more info.

    Args:
        cluster_id (int):
        json_body (RhubApiLabClusterUpdateClusterJsonBody):

    Returns:
        Response[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabClusterUpdateClusterJsonBody,
) -> Optional[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]:
    """Update cluster

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster) for more info.

    Args:
        cluster_id (int):
        json_body (RhubApiLabClusterUpdateClusterJsonBody):

    Returns:
        Response[Union[RhubApiLabClusterUpdateClusterResponse200, RhubApiLabClusterUpdateClusterResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

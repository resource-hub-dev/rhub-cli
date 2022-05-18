from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_cluster_delete_cluster_response_default import RhubApiLabClusterDeleteClusterResponseDefault
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
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    else:
        response_default = RhubApiLabClusterDeleteClusterResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]:
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
) -> Response[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]:
    """Delete cluster

     Clusters are not deleted immediately after calling this endpoint. Instead,
    Tower job will be launched (`Product.tower_template_name_delete`) and the
    cluster is marked as deleted from the job by changing status to \"Deleted\".
    If deletion fails status should be changed to \"Deletion Failed\" and
    cluster won't be deleted.

    Clusters that are in a creating state cannot be deleted. Before deleting,
    the cluster must be in the `Active` state or in any of failed states.

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]
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
) -> Optional[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]:
    """Delete cluster

     Clusters are not deleted immediately after calling this endpoint. Instead,
    Tower job will be launched (`Product.tower_template_name_delete`) and the
    cluster is marked as deleted from the job by changing status to \"Deleted\".
    If deletion fails status should be changed to \"Deletion Failed\" and
    cluster won't be deleted.

    Clusters that are in a creating state cannot be deleted. Before deleting,
    the cluster must be in the `Active` state or in any of failed states.

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cluster_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]:
    """Delete cluster

     Clusters are not deleted immediately after calling this endpoint. Instead,
    Tower job will be launched (`Product.tower_template_name_delete`) and the
    cluster is marked as deleted from the job by changing status to \"Deleted\".
    If deletion fails status should be changed to \"Deletion Failed\" and
    cluster won't be deleted.

    Clusters that are in a creating state cannot be deleted. Before deleting,
    the cluster must be in the `Active` state or in any of failed states.

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]
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
) -> Optional[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]:
    """Delete cluster

     Clusters are not deleted immediately after calling this endpoint. Instead,
    Tower job will be launched (`Product.tower_template_name_delete`) and the
    cluster is marked as deleted from the job by changing status to \"Deleted\".
    If deletion fails status should be changed to \"Deletion Failed\" and
    cluster won't be deleted.

    Clusters that are in a creating state cannot be deleted. Before deleting,
    the cluster must be in the `Active` state or in any of failed states.

    Args:
        cluster_id (int):

    Returns:
        Response[Union[Any, RhubApiLabClusterDeleteClusterResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed

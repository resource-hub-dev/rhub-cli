from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_cluster_create_cluster_json_body import RhubApiLabClusterCreateClusterJsonBody
from ...models.rhub_api_lab_cluster_create_cluster_response_200 import RhubApiLabClusterCreateClusterResponse200
from ...models.rhub_api_lab_cluster_create_cluster_response_default import RhubApiLabClusterCreateClusterResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabClusterCreateClusterJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/cluster".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiLabClusterCreateClusterResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiLabClusterCreateClusterResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabClusterCreateClusterJsonBody,
) -> Response[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]:
    """Create cluster

     Create a new cluster and install selected product. If cluster provisioning
    and product installation is successfully queued in region Tower, cluster
    creation is considered as successful by this endpoint. Provisioning or
    installation takes some time and can fail. Use _GET_ endpoint to get the
    current status of cluster.

    ## Reservation system

    When the Reservation System is enabled in a region, a new cluster in
    that region will be required to select the length of the reservation in
    `reservation_expiration` field. Reservation sets soft-limit on cluster,
    when reservation expires cluster will be scheduled for deletion. Maximal
    `reservation_expiration` date is determined from the date of creation (or
    current expiration date when extending expiration) and
    `reservation_expiration_max` attribute on the region.

    When the Lifespan System is enabled in a region, `lifespan_expiration`
    date will automatically be applied to the cluster by backend at time of
    creation. The date is configured on region. Unlike the reservation
    expiration, lifespan is hard-limit and this date can not be set nor
    modified once cluster is created. When lifespan expires cluster will be
    unconditionally scheduled for deletion.

    ## Shared cluster

    All users can use shared clusters even if they don't have permissions for
    the cluster region or reservations in the region are disabled.

    Shared clusters are created in a special group, if `shared` is set to
    `true` when creating cluster, provided `group_id` will be ignored.
    Reservation expiration and also lifespan expiration is disabled on shared
    clusters, and only user with `sharedcluster` role can create shared
    clusters.

    ## Product

    If product parameters are invalid, problem response may have extra field
    `invalid_product_params` with a short description why parameters are not
    valid (eg. `{\"example_param\": \"is required\"}`).

    Args:
        json_body (RhubApiLabClusterCreateClusterJsonBody):

    Returns:
        Response[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabClusterCreateClusterJsonBody,
) -> Optional[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]:
    """Create cluster

     Create a new cluster and install selected product. If cluster provisioning
    and product installation is successfully queued in region Tower, cluster
    creation is considered as successful by this endpoint. Provisioning or
    installation takes some time and can fail. Use _GET_ endpoint to get the
    current status of cluster.

    ## Reservation system

    When the Reservation System is enabled in a region, a new cluster in
    that region will be required to select the length of the reservation in
    `reservation_expiration` field. Reservation sets soft-limit on cluster,
    when reservation expires cluster will be scheduled for deletion. Maximal
    `reservation_expiration` date is determined from the date of creation (or
    current expiration date when extending expiration) and
    `reservation_expiration_max` attribute on the region.

    When the Lifespan System is enabled in a region, `lifespan_expiration`
    date will automatically be applied to the cluster by backend at time of
    creation. The date is configured on region. Unlike the reservation
    expiration, lifespan is hard-limit and this date can not be set nor
    modified once cluster is created. When lifespan expires cluster will be
    unconditionally scheduled for deletion.

    ## Shared cluster

    All users can use shared clusters even if they don't have permissions for
    the cluster region or reservations in the region are disabled.

    Shared clusters are created in a special group, if `shared` is set to
    `true` when creating cluster, provided `group_id` will be ignored.
    Reservation expiration and also lifespan expiration is disabled on shared
    clusters, and only user with `sharedcluster` role can create shared
    clusters.

    ## Product

    If product parameters are invalid, problem response may have extra field
    `invalid_product_params` with a short description why parameters are not
    valid (eg. `{\"example_param\": \"is required\"}`).

    Args:
        json_body (RhubApiLabClusterCreateClusterJsonBody):

    Returns:
        Response[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabClusterCreateClusterJsonBody,
) -> Response[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]:
    """Create cluster

     Create a new cluster and install selected product. If cluster provisioning
    and product installation is successfully queued in region Tower, cluster
    creation is considered as successful by this endpoint. Provisioning or
    installation takes some time and can fail. Use _GET_ endpoint to get the
    current status of cluster.

    ## Reservation system

    When the Reservation System is enabled in a region, a new cluster in
    that region will be required to select the length of the reservation in
    `reservation_expiration` field. Reservation sets soft-limit on cluster,
    when reservation expires cluster will be scheduled for deletion. Maximal
    `reservation_expiration` date is determined from the date of creation (or
    current expiration date when extending expiration) and
    `reservation_expiration_max` attribute on the region.

    When the Lifespan System is enabled in a region, `lifespan_expiration`
    date will automatically be applied to the cluster by backend at time of
    creation. The date is configured on region. Unlike the reservation
    expiration, lifespan is hard-limit and this date can not be set nor
    modified once cluster is created. When lifespan expires cluster will be
    unconditionally scheduled for deletion.

    ## Shared cluster

    All users can use shared clusters even if they don't have permissions for
    the cluster region or reservations in the region are disabled.

    Shared clusters are created in a special group, if `shared` is set to
    `true` when creating cluster, provided `group_id` will be ignored.
    Reservation expiration and also lifespan expiration is disabled on shared
    clusters, and only user with `sharedcluster` role can create shared
    clusters.

    ## Product

    If product parameters are invalid, problem response may have extra field
    `invalid_product_params` with a short description why parameters are not
    valid (eg. `{\"example_param\": \"is required\"}`).

    Args:
        json_body (RhubApiLabClusterCreateClusterJsonBody):

    Returns:
        Response[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabClusterCreateClusterJsonBody,
) -> Optional[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]:
    """Create cluster

     Create a new cluster and install selected product. If cluster provisioning
    and product installation is successfully queued in region Tower, cluster
    creation is considered as successful by this endpoint. Provisioning or
    installation takes some time and can fail. Use _GET_ endpoint to get the
    current status of cluster.

    ## Reservation system

    When the Reservation System is enabled in a region, a new cluster in
    that region will be required to select the length of the reservation in
    `reservation_expiration` field. Reservation sets soft-limit on cluster,
    when reservation expires cluster will be scheduled for deletion. Maximal
    `reservation_expiration` date is determined from the date of creation (or
    current expiration date when extending expiration) and
    `reservation_expiration_max` attribute on the region.

    When the Lifespan System is enabled in a region, `lifespan_expiration`
    date will automatically be applied to the cluster by backend at time of
    creation. The date is configured on region. Unlike the reservation
    expiration, lifespan is hard-limit and this date can not be set nor
    modified once cluster is created. When lifespan expires cluster will be
    unconditionally scheduled for deletion.

    ## Shared cluster

    All users can use shared clusters even if they don't have permissions for
    the cluster region or reservations in the region are disabled.

    Shared clusters are created in a special group, if `shared` is set to
    `true` when creating cluster, provided `group_id` will be ignored.
    Reservation expiration and also lifespan expiration is disabled on shared
    clusters, and only user with `sharedcluster` role can create shared
    clusters.

    ## Product

    If product parameters are invalid, problem response may have extra field
    `invalid_product_params` with a short description why parameters are not
    valid (eg. `{\"example_param\": \"is required\"}`).

    Args:
        json_body (RhubApiLabClusterCreateClusterJsonBody):

    Returns:
        Response[Union[RhubApiLabClusterCreateClusterResponse200, RhubApiLabClusterCreateClusterResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

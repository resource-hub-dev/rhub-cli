from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_region_get_usage_response_200 import RhubApiLabRegionGetUsageResponse200
from ...models.rhub_api_lab_region_get_usage_response_default import RhubApiLabRegionGetUsageResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
    with_openstack_limits: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}/usage".format(client.base_url, region_id=region_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["with_openstack_limits"] = with_openstack_limits

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiLabRegionGetUsageResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiLabRegionGetUsageResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    with_openstack_limits: Union[Unset, None, bool] = UNSET,
) -> Response[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]:
    """Get region usage

     `user_quota`,`user_quota_usage`, `total_quota` and `total_quota_usage` are
    values calculated from the data we store about clusters. In other words,
    it's how many resources Resource Hub can use (quota), and how many it
    currently uses (quota usage). It does not count resources that are not
    managed by Resource Hub.

    User quota and its usage is scoped to the currently logged in user. Total
    quota is overall quota and usage of the region.

    If query parameter `with_openstack_limits` is set to `true` response will
    also contain `openstack_limit`, which are real OpenStack limits that are
    applied to the project's account in the region. It is retrieved from the
    OpenStack API.

    Args:
        region_id (int):
        with_openstack_limits (Union[Unset, None, bool]):

    Returns:
        Response[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        with_openstack_limits=with_openstack_limits,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    region_id: int,
    *,
    client: AuthenticatedClient,
    with_openstack_limits: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]:
    """Get region usage

     `user_quota`,`user_quota_usage`, `total_quota` and `total_quota_usage` are
    values calculated from the data we store about clusters. In other words,
    it's how many resources Resource Hub can use (quota), and how many it
    currently uses (quota usage). It does not count resources that are not
    managed by Resource Hub.

    User quota and its usage is scoped to the currently logged in user. Total
    quota is overall quota and usage of the region.

    If query parameter `with_openstack_limits` is set to `true` response will
    also contain `openstack_limit`, which are real OpenStack limits that are
    applied to the project's account in the region. It is retrieved from the
    OpenStack API.

    Args:
        region_id (int):
        with_openstack_limits (Union[Unset, None, bool]):

    Returns:
        Response[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
        with_openstack_limits=with_openstack_limits,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    with_openstack_limits: Union[Unset, None, bool] = UNSET,
) -> Response[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]:
    """Get region usage

     `user_quota`,`user_quota_usage`, `total_quota` and `total_quota_usage` are
    values calculated from the data we store about clusters. In other words,
    it's how many resources Resource Hub can use (quota), and how many it
    currently uses (quota usage). It does not count resources that are not
    managed by Resource Hub.

    User quota and its usage is scoped to the currently logged in user. Total
    quota is overall quota and usage of the region.

    If query parameter `with_openstack_limits` is set to `true` response will
    also contain `openstack_limit`, which are real OpenStack limits that are
    applied to the project's account in the region. It is retrieved from the
    OpenStack API.

    Args:
        region_id (int):
        with_openstack_limits (Union[Unset, None, bool]):

    Returns:
        Response[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        with_openstack_limits=with_openstack_limits,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
    with_openstack_limits: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]:
    """Get region usage

     `user_quota`,`user_quota_usage`, `total_quota` and `total_quota_usage` are
    values calculated from the data we store about clusters. In other words,
    it's how many resources Resource Hub can use (quota), and how many it
    currently uses (quota usage). It does not count resources that are not
    managed by Resource Hub.

    User quota and its usage is scoped to the currently logged in user. Total
    quota is overall quota and usage of the region.

    If query parameter `with_openstack_limits` is set to `true` response will
    also contain `openstack_limit`, which are real OpenStack limits that are
    applied to the project's account in the region. It is retrieved from the
    OpenStack API.

    Args:
        region_id (int):
        with_openstack_limits (Union[Unset, None, bool]):

    Returns:
        Response[Union[RhubApiLabRegionGetUsageResponse200, RhubApiLabRegionGetUsageResponseDefault]]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
            with_openstack_limits=with_openstack_limits,
        )
    ).parsed

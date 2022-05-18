from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_region_list_region_products_filter import RhubApiLabRegionListRegionProductsFilter
from ...models.rhub_api_lab_region_list_region_products_response_200_item import (
    RhubApiLabRegionListRegionProductsResponse200Item,
)
from ...models.rhub_api_lab_region_list_region_products_response_default import (
    RhubApiLabRegionListRegionProductsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiLabRegionListRegionProductsFilter] = UNSET,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}/products".format(client.base_url, region_id=region_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_filter_: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict() if filter_ else None

    if not isinstance(json_filter_, Unset) and json_filter_ is not None:
        params.update(json_filter_)

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
) -> Optional[
    Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubApiLabRegionListRegionProductsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubApiLabRegionListRegionProductsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]
]:
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
    filter_: Union[Unset, None, RhubApiLabRegionListRegionProductsFilter] = UNSET,
) -> Response[
    Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]
]:
    """Get list of products that can be installed in the selected region.

    Args:
        region_id (int):
        filter_ (Union[Unset, None, RhubApiLabRegionListRegionProductsFilter]):

    Returns:
        Response[Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        filter_=filter_,
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
    filter_: Union[Unset, None, RhubApiLabRegionListRegionProductsFilter] = UNSET,
) -> Optional[
    Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]
]:
    """Get list of products that can be installed in the selected region.

    Args:
        region_id (int):
        filter_ (Union[Unset, None, RhubApiLabRegionListRegionProductsFilter]):

    Returns:
        Response[Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]]
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiLabRegionListRegionProductsFilter] = UNSET,
) -> Response[
    Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]
]:
    """Get list of products that can be installed in the selected region.

    Args:
        region_id (int):
        filter_ (Union[Unset, None, RhubApiLabRegionListRegionProductsFilter]):

    Returns:
        Response[Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        filter_=filter_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiLabRegionListRegionProductsFilter] = UNSET,
) -> Optional[
    Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]
]:
    """Get list of products that can be installed in the selected region.

    Args:
        region_id (int):
        filter_ (Union[Unset, None, RhubApiLabRegionListRegionProductsFilter]):

    Returns:
        Response[Union[List[RhubApiLabRegionListRegionProductsResponse200Item], RhubApiLabRegionListRegionProductsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
            filter_=filter_,
        )
    ).parsed

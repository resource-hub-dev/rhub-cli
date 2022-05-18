from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_product_list_product_regions_filter import RhubApiLabProductListProductRegionsFilter
from ...models.rhub_api_lab_product_list_product_regions_response_200_item import (
    RhubApiLabProductListProductRegionsResponse200Item,
)
from ...models.rhub_api_lab_product_list_product_regions_response_default import (
    RhubApiLabProductListProductRegionsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiLabProductListProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/lab/product/{product_id}/regions".format(client.base_url, product_id=product_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_filter_: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict() if filter_ else None

    if not isinstance(json_filter_, Unset) and json_filter_ is not None:
        params.update(json_filter_)

    params["page"] = page

    params["limit"] = limit

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
    Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RhubApiLabProductListProductRegionsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    else:
        response_default = RhubApiLabProductListProductRegionsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiLabProductListProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[
    Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]
]:
    """Get list of regions where product can be installed.

    Args:
        product_id (int):
        filter_ (Union[Unset, None, RhubApiLabProductListProductRegionsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiLabProductListProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[
    Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]
]:
    """Get list of regions where product can be installed.

    Args:
        product_id (int):
        filter_ (Union[Unset, None, RhubApiLabProductListProductRegionsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiLabProductListProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[
    Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]
]:
    """Get list of regions where product can be installed.

    Args:
        product_id (int):
        filter_ (Union[Unset, None, RhubApiLabProductListProductRegionsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
        filter_=filter_,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiLabProductListProductRegionsFilter] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[
    Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]
]:
    """Get list of regions where product can be installed.

    Args:
        product_id (int):
        filter_ (Union[Unset, None, RhubApiLabProductListProductRegionsFilter]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[List[RhubApiLabProductListProductRegionsResponse200Item], RhubApiLabProductListProductRegionsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            filter_=filter_,
            page=page,
            limit=limit,
        )
    ).parsed

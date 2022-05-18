from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_product_get_product_response_200 import RhubApiLabProductGetProductResponse200
from ...models.rhub_api_lab_product_get_product_response_default import RhubApiLabProductGetProductResponseDefault
from ...types import Response


def _get_kwargs(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/product/{product_id}".format(client.base_url, product_id=product_id)

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
) -> Optional[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiLabProductGetProductResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiLabProductGetProductResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]:
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
) -> Response[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]:
    """Get product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
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
) -> Optional[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]:
    """Get product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]:
    """Get product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]:
    """Get product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubApiLabProductGetProductResponse200, RhubApiLabProductGetProductResponseDefault]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
        )
    ).parsed

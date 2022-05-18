from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_product_delete_product_response_default import RhubApiLabProductDeleteProductResponseDefault
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
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    else:
        response_default = RhubApiLabProductDeleteProductResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]:
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
) -> Response[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]:
    """Delete product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]
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
) -> Optional[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]:
    """Delete product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]:
    """Delete product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]
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
) -> Optional[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]:
    """Delete product

    Args:
        product_id (int):

    Returns:
        Response[Union[Any, RhubApiLabProductDeleteProductResponseDefault]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
        )
    ).parsed

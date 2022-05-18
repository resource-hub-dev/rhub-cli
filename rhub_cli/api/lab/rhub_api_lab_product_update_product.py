from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_product_update_product_json_body import RhubApiLabProductUpdateProductJsonBody
from ...models.rhub_api_lab_product_update_product_response_default import RhubApiLabProductUpdateProductResponseDefault
from ...types import Response


def _get_kwargs(
    product_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabProductUpdateProductJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/product/{product_id}".format(client.base_url, product_id=product_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiLabProductUpdateProductResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]:
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
    json_body: RhubApiLabProductUpdateProductJsonBody,
) -> Response[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]:
    """Update product

    Args:
        product_id (int):
        json_body (RhubApiLabProductUpdateProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubApiLabProductUpdateProductJsonBody,
) -> Optional[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]:
    """Update product

    Args:
        product_id (int):
        json_body (RhubApiLabProductUpdateProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabProductUpdateProductJsonBody,
) -> Response[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]:
    """Update product

    Args:
        product_id (int):
        json_body (RhubApiLabProductUpdateProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabProductUpdateProductJsonBody,
) -> Optional[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]:
    """Update product

    Args:
        product_id (int):
        json_body (RhubApiLabProductUpdateProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabProductUpdateProductResponseDefault]]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_product_create_product_json_body import RhubApiLabProductCreateProductJsonBody
from ...models.rhub_api_lab_product_create_product_response_default import RhubApiLabProductCreateProductResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabProductCreateProductJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/product".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiLabProductCreateProductResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiLabProductCreateProductResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiLabProductCreateProductResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabProductCreateProductJsonBody,
) -> Response[Union[Any, RhubApiLabProductCreateProductResponseDefault]]:
    """Create product

     `tower_template_name_create` is the Tower template name to create the
    cluster, and `tower_template_name_delete` to delete.

    Args:
        json_body (RhubApiLabProductCreateProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabProductCreateProductResponseDefault]]
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
    json_body: RhubApiLabProductCreateProductJsonBody,
) -> Optional[Union[Any, RhubApiLabProductCreateProductResponseDefault]]:
    """Create product

     `tower_template_name_create` is the Tower template name to create the
    cluster, and `tower_template_name_delete` to delete.

    Args:
        json_body (RhubApiLabProductCreateProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabProductCreateProductResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabProductCreateProductJsonBody,
) -> Response[Union[Any, RhubApiLabProductCreateProductResponseDefault]]:
    """Create product

     `tower_template_name_create` is the Tower template name to create the
    cluster, and `tower_template_name_delete` to delete.

    Args:
        json_body (RhubApiLabProductCreateProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabProductCreateProductResponseDefault]]
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
    json_body: RhubApiLabProductCreateProductJsonBody,
) -> Optional[Union[Any, RhubApiLabProductCreateProductResponseDefault]]:
    """Create product

     `tower_template_name_create` is the Tower template name to create the
    cluster, and `tower_template_name_delete` to delete.

    Args:
        json_body (RhubApiLabProductCreateProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabProductCreateProductResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

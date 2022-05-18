from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_region_add_region_product_json_body import RhubApiLabRegionAddRegionProductJsonBody
from ...models.rhub_api_lab_region_add_region_product_response_default import (
    RhubApiLabRegionAddRegionProductResponseDefault,
)
from ...types import Response


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionAddRegionProductJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}/products".format(client.base_url, region_id=region_id)

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
) -> Optional[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    else:
        response_default = RhubApiLabRegionAddRegionProductResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]:
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
    json_body: RhubApiLabRegionAddRegionProductJsonBody,
) -> Response[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]:
    """Add product to region or disable/enable product in region

    Args:
        region_id (int):
        json_body (RhubApiLabRegionAddRegionProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubApiLabRegionAddRegionProductJsonBody,
) -> Optional[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]:
    """Add product to region or disable/enable product in region

    Args:
        region_id (int):
        json_body (RhubApiLabRegionAddRegionProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionAddRegionProductJsonBody,
) -> Response[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]:
    """Add product to region or disable/enable product in region

    Args:
        region_id (int):
        json_body (RhubApiLabRegionAddRegionProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionAddRegionProductJsonBody,
) -> Optional[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]:
    """Add product to region or disable/enable product in region

    Args:
        region_id (int):
        json_body (RhubApiLabRegionAddRegionProductJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionAddRegionProductResponseDefault]]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

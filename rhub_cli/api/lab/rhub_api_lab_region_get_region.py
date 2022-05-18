from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_region_get_region_response_200 import RhubApiLabRegionGetRegionResponse200
from ...models.rhub_api_lab_region_get_region_response_default import RhubApiLabRegionGetRegionResponseDefault
from ...types import Response


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}".format(client.base_url, region_id=region_id)

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
) -> Optional[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiLabRegionGetRegionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiLabRegionGetRegionResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]:
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
) -> Response[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]:
    """Get region

    Args:
        region_id (int):

    Returns:
        Response[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
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
) -> Optional[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]:
    """Get region

    Args:
        region_id (int):

    Returns:
        Response[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]:
    """Get region

    Args:
        region_id (int):

    Returns:
        Response[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]:
    """Get region

    Args:
        region_id (int):

    Returns:
        Response[Union[Any, RhubApiLabRegionGetRegionResponse200, RhubApiLabRegionGetRegionResponseDefault]]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
        )
    ).parsed

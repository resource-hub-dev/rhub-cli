from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.rhub_api_bare_metal_image_image_list_response_200 import RhubApiBareMetalImageImageListResponse200
from ...models.rhub_api_bare_metal_image_image_list_response_default import (
    RhubApiBareMetalImageImageListResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bare_metal/image".format(client.base_url)

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
) -> Optional[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiBareMetalImageImageListResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiBareMetalImageImageListResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]:
    """Get image list

    Returns:
        Response[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]:
    """Get image list

    Returns:
        Response[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]:
    """Get image list

    Returns:
        Response[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]:
    """Get image list

    Returns:
        Response[Union[RhubApiBareMetalImageImageListResponse200, RhubApiBareMetalImageImageListResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

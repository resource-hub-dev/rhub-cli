from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.rhub_api_bare_metal_host_host_get_response_200 import RhubApiBareMetalHostHostGetResponse200
from ...models.rhub_api_bare_metal_host_host_get_response_default import RhubApiBareMetalHostHostGetResponseDefault
from ...types import Response


def _get_kwargs(
    host_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bare_metal/host/{host_id}".format(client.base_url, host_id=host_id)

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
) -> Optional[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiBareMetalHostHostGetResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiBareMetalHostHostGetResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    host_id: int,
    *,
    client: Client,
) -> Response[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]:
    """Get host

    Args:
        host_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    host_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]:
    """Get host

    Args:
        host_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]
    """

    return sync_detailed(
        host_id=host_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    host_id: int,
    *,
    client: Client,
) -> Response[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]:
    """Get host

    Args:
        host_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    host_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]:
    """Get host

    Args:
        host_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalHostHostGetResponse200, RhubApiBareMetalHostHostGetResponseDefault]]
    """

    return (
        await asyncio_detailed(
            host_id=host_id,
            client=client,
        )
    ).parsed

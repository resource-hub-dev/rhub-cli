from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.rhub_api_bare_metal_handler_handler_get_response_200 import RhubApiBareMetalHandlerHandlerGetResponse200
from ...models.rhub_api_bare_metal_handler_handler_get_response_default import (
    RhubApiBareMetalHandlerHandlerGetResponseDefault,
)
from ...types import Response


def _get_kwargs(
    handler_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bare_metal/handler/{handler_id}".format(client.base_url, handler_id=handler_id)

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
) -> Optional[
    Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]
]:
    if response.status_code == 200:
        response_200 = RhubApiBareMetalHandlerHandlerGetResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiBareMetalHandlerHandlerGetResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    handler_id: int,
    *,
    client: Client,
) -> Response[
    Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]
]:
    """Get handler

    Args:
        handler_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        handler_id=handler_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    handler_id: int,
    *,
    client: Client,
) -> Optional[
    Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]
]:
    """Get handler

    Args:
        handler_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]]
    """

    return sync_detailed(
        handler_id=handler_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    handler_id: int,
    *,
    client: Client,
) -> Response[
    Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]
]:
    """Get handler

    Args:
        handler_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        handler_id=handler_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    handler_id: int,
    *,
    client: Client,
) -> Optional[
    Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]
]:
    """Get handler

    Args:
        handler_id (int):

    Returns:
        Response[Union[Any, RhubApiBareMetalHandlerHandlerGetResponse200, RhubApiBareMetalHandlerHandlerGetResponseDefault]]
    """

    return (
        await asyncio_detailed(
            handler_id=handler_id,
            client=client,
        )
    ).parsed

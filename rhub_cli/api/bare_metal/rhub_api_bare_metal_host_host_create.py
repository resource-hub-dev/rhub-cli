from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.rhub_api_bare_metal_host_host_create_json_body import RhubApiBareMetalHostHostCreateJsonBody
from ...models.rhub_api_bare_metal_host_host_create_response_default import (
    RhubApiBareMetalHostHostCreateResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: RhubApiBareMetalHostHostCreateJsonBody,
) -> Dict[str, Any]:
    url = "{}/bare_metal/host".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiBareMetalHostHostCreateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: RhubApiBareMetalHostHostCreateJsonBody,
) -> Response[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]:
    """Create bare metal host

    Args:
        json_body (RhubApiBareMetalHostHostCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]
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
    client: Client,
    json_body: RhubApiBareMetalHostHostCreateJsonBody,
) -> Optional[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]:
    """Create bare metal host

    Args:
        json_body (RhubApiBareMetalHostHostCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: RhubApiBareMetalHostHostCreateJsonBody,
) -> Response[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]:
    """Create bare metal host

    Args:
        json_body (RhubApiBareMetalHostHostCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]
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
    client: Client,
    json_body: RhubApiBareMetalHostHostCreateJsonBody,
) -> Optional[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]:
    """Create bare metal host

    Args:
        json_body (RhubApiBareMetalHostHostCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiBareMetalHostHostCreateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

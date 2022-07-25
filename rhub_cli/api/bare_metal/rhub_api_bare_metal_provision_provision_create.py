from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.rhub_api_bare_metal_provision_provision_create_json_body import (
    RhubApiBareMetalProvisionProvisionCreateJsonBody,
)
from ...models.rhub_api_bare_metal_provision_provision_create_response_default import (
    RhubApiBareMetalProvisionProvisionCreateResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: RhubApiBareMetalProvisionProvisionCreateJsonBody,
) -> Dict[str, Any]:
    url = "{}/bare_metal/provision".format(client.base_url)

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
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiBareMetalProvisionProvisionCreateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: RhubApiBareMetalProvisionProvisionCreateJsonBody,
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]:
    """Add bare metal provision

    Args:
        json_body (RhubApiBareMetalProvisionProvisionCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]
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
    json_body: RhubApiBareMetalProvisionProvisionCreateJsonBody,
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]:
    """Add bare metal provision

    Args:
        json_body (RhubApiBareMetalProvisionProvisionCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: RhubApiBareMetalProvisionProvisionCreateJsonBody,
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]:
    """Add bare metal provision

    Args:
        json_body (RhubApiBareMetalProvisionProvisionCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]
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
    json_body: RhubApiBareMetalProvisionProvisionCreateJsonBody,
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]:
    """Add bare metal provision

    Args:
        json_body (RhubApiBareMetalProvisionProvisionCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionCreateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_token_get_token_info_response_200 import RhubApiAuthTokenGetTokenInfoResponse200
from ...models.rhub_api_auth_token_get_token_info_response_default import RhubApiAuthTokenGetTokenInfoResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/token".format(client.base_url)

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
) -> Optional[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthTokenGetTokenInfoResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthTokenGetTokenInfoResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]:
    """Get auth token info

    Returns:
        Response[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]
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
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]:
    """Get auth token info

    Returns:
        Response[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]:
    """Get auth token info

    Returns:
        Response[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]:
    """Get auth token info

    Returns:
        Response[Union[RhubApiAuthTokenGetTokenInfoResponse200, RhubApiAuthTokenGetTokenInfoResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

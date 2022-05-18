from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.rhub_api_auth_token_refresh_token_response_200 import RhubApiAuthTokenRefreshTokenResponse200
from ...models.rhub_api_auth_token_refresh_token_response_default import RhubApiAuthTokenRefreshTokenResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    authorization: str,
) -> Dict[str, Any]:
    url = "{}/auth/token/refresh".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["Authorization"] = authorization

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthTokenRefreshTokenResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthTokenRefreshTokenResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    authorization: str,
) -> Response[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]:
    """Refresh token

     This endpoint requires HTTP bearer authentication. The bearer token in
    'Authorization' header is not access token but refresh token. If refresh
    was successful return new oauth2 token info. Response is the same as
    from token create endpoint.

    Args:
        authorization (str):  Example: Bearer eyJhbGciOiJIUzI1...VLzc.

    Returns:
        Response[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        authorization=authorization,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    authorization: str,
) -> Optional[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]:
    """Refresh token

     This endpoint requires HTTP bearer authentication. The bearer token in
    'Authorization' header is not access token but refresh token. If refresh
    was successful return new oauth2 token info. Response is the same as
    from token create endpoint.

    Args:
        authorization (str):  Example: Bearer eyJhbGciOiJIUzI1...VLzc.

    Returns:
        Response[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    authorization: str,
) -> Response[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]:
    """Refresh token

     This endpoint requires HTTP bearer authentication. The bearer token in
    'Authorization' header is not access token but refresh token. If refresh
    was successful return new oauth2 token info. Response is the same as
    from token create endpoint.

    Args:
        authorization (str):  Example: Bearer eyJhbGciOiJIUzI1...VLzc.

    Returns:
        Response[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        authorization=authorization,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    authorization: str,
) -> Optional[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]:
    """Refresh token

     This endpoint requires HTTP bearer authentication. The bearer token in
    'Authorization' header is not access token but refresh token. If refresh
    was successful return new oauth2 token info. Response is the same as
    from token create endpoint.

    Args:
        authorization (str):  Example: Bearer eyJhbGciOiJIUzI1...VLzc.

    Returns:
        Response[Union[RhubApiAuthTokenRefreshTokenResponse200, RhubApiAuthTokenRefreshTokenResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed

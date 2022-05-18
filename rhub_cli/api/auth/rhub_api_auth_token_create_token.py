from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.rhub_api_auth_token_create_token_response_200 import RhubApiAuthTokenCreateTokenResponse200
from ...models.rhub_api_auth_token_create_token_response_default import RhubApiAuthTokenCreateTokenResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    authorization: str,
) -> Dict[str, Any]:
    url = "{}/auth/token/create".format(client.base_url)

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
) -> Optional[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthTokenCreateTokenResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthTokenCreateTokenResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]:
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
) -> Response[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]:
    """Login and get access token

     This endpoint requires HTTP basic authentication. If credentials are
    correct then it returns oauth2 token info - access token, refresh token
    and some other informations about generated token.

    Args:
        authorization (str):  Example: Basic dXNlcm5hbWU6cGFzc3dvcmQ=.

    Returns:
        Response[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]
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
) -> Optional[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]:
    """Login and get access token

     This endpoint requires HTTP basic authentication. If credentials are
    correct then it returns oauth2 token info - access token, refresh token
    and some other informations about generated token.

    Args:
        authorization (str):  Example: Basic dXNlcm5hbWU6cGFzc3dvcmQ=.

    Returns:
        Response[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    authorization: str,
) -> Response[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]:
    """Login and get access token

     This endpoint requires HTTP basic authentication. If credentials are
    correct then it returns oauth2 token info - access token, refresh token
    and some other informations about generated token.

    Args:
        authorization (str):  Example: Basic dXNlcm5hbWU6cGFzc3dvcmQ=.

    Returns:
        Response[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]
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
) -> Optional[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]:
    """Login and get access token

     This endpoint requires HTTP basic authentication. If credentials are
    correct then it returns oauth2 token info - access token, refresh token
    and some other informations about generated token.

    Args:
        authorization (str):  Example: Basic dXNlcm5hbWU6cGFzc3dvcmQ=.

    Returns:
        Response[Union[RhubApiAuthTokenCreateTokenResponse200, RhubApiAuthTokenCreateTokenResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed

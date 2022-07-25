from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_satellite_server_get_response_200 import RhubApiSatelliteServerGetResponse200
from ...models.rhub_api_satellite_server_get_response_default import RhubApiSatelliteServerGetResponseDefault
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/satellite/server/{server_id}".format(client.base_url, server_id=server_id)

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
) -> Optional[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiSatelliteServerGetResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiSatelliteServerGetResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]:
    """Get Satellite server

    Args:
        server_id (int):

    Returns:
        Response[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]:
    """Get Satellite server

    Args:
        server_id (int):

    Returns:
        Response[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]:
    """Get Satellite server

    Args:
        server_id (int):

    Returns:
        Response[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]:
    """Get Satellite server

    Args:
        server_id (int):

    Returns:
        Response[Union[Any, RhubApiSatelliteServerGetResponse200, RhubApiSatelliteServerGetResponseDefault]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
        )
    ).parsed

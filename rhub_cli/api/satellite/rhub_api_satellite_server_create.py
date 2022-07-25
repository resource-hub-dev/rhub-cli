from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_satellite_server_create_json_body import RhubApiSatelliteServerCreateJsonBody
from ...models.rhub_api_satellite_server_create_response_200 import RhubApiSatelliteServerCreateResponse200
from ...models.rhub_api_satellite_server_create_response_default import RhubApiSatelliteServerCreateResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiSatelliteServerCreateJsonBody,
) -> Dict[str, Any]:
    url = "{}/satellite/server".format(client.base_url)

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
) -> Optional[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiSatelliteServerCreateResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiSatelliteServerCreateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiSatelliteServerCreateJsonBody,
) -> Response[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]:
    """Create Satellite server

    Args:
        json_body (RhubApiSatelliteServerCreateJsonBody):

    Returns:
        Response[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]
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
    client: AuthenticatedClient,
    json_body: RhubApiSatelliteServerCreateJsonBody,
) -> Optional[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]:
    """Create Satellite server

    Args:
        json_body (RhubApiSatelliteServerCreateJsonBody):

    Returns:
        Response[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiSatelliteServerCreateJsonBody,
) -> Response[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]:
    """Create Satellite server

    Args:
        json_body (RhubApiSatelliteServerCreateJsonBody):

    Returns:
        Response[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]
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
    client: AuthenticatedClient,
    json_body: RhubApiSatelliteServerCreateJsonBody,
) -> Optional[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]:
    """Create Satellite server

    Args:
        json_body (RhubApiSatelliteServerCreateJsonBody):

    Returns:
        Response[Union[RhubApiSatelliteServerCreateResponse200, RhubApiSatelliteServerCreateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

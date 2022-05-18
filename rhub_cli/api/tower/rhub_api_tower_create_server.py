from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_create_server_json_body import RhubApiTowerCreateServerJsonBody
from ...models.rhub_api_tower_create_server_response_200 import RhubApiTowerCreateServerResponse200
from ...models.rhub_api_tower_create_server_response_default import RhubApiTowerCreateServerResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerCreateServerJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/server".format(client.base_url)

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
) -> Optional[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiTowerCreateServerResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiTowerCreateServerResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerCreateServerJsonBody,
) -> Response[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]:
    """Create Tower server

    Args:
        json_body (RhubApiTowerCreateServerJsonBody):

    Returns:
        Response[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]
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
    json_body: RhubApiTowerCreateServerJsonBody,
) -> Optional[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]:
    """Create Tower server

    Args:
        json_body (RhubApiTowerCreateServerJsonBody):

    Returns:
        Response[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerCreateServerJsonBody,
) -> Response[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]:
    """Create Tower server

    Args:
        json_body (RhubApiTowerCreateServerJsonBody):

    Returns:
        Response[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]
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
    json_body: RhubApiTowerCreateServerJsonBody,
) -> Optional[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]:
    """Create Tower server

    Args:
        json_body (RhubApiTowerCreateServerJsonBody):

    Returns:
        Response[Union[RhubApiTowerCreateServerResponse200, RhubApiTowerCreateServerResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

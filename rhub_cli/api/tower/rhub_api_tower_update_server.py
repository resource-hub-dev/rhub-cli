from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_update_server_json_body import RhubApiTowerUpdateServerJsonBody
from ...models.rhub_api_tower_update_server_response_200 import RhubApiTowerUpdateServerResponse200
from ...models.rhub_api_tower_update_server_response_default import RhubApiTowerUpdateServerResponseDefault
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerUpdateServerJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/server/{server_id}".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiTowerUpdateServerResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiTowerUpdateServerResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]:
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
    json_body: RhubApiTowerUpdateServerJsonBody,
) -> Response[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]:
    """Change Tower server

    Args:
        server_id (int):
        json_body (RhubApiTowerUpdateServerJsonBody):

    Returns:
        Response[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubApiTowerUpdateServerJsonBody,
) -> Optional[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]:
    """Change Tower server

    Args:
        server_id (int):
        json_body (RhubApiTowerUpdateServerJsonBody):

    Returns:
        Response[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerUpdateServerJsonBody,
) -> Response[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]:
    """Change Tower server

    Args:
        server_id (int):
        json_body (RhubApiTowerUpdateServerJsonBody):

    Returns:
        Response[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerUpdateServerJsonBody,
) -> Optional[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]:
    """Change Tower server

    Args:
        server_id (int):
        json_body (RhubApiTowerUpdateServerJsonBody):

    Returns:
        Response[Union[RhubApiTowerUpdateServerResponse200, RhubApiTowerUpdateServerResponseDefault]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

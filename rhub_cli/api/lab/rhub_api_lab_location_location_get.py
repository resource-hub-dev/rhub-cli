from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_location_location_get_response_200 import RhubApiLabLocationLocationGetResponse200
from ...models.rhub_api_lab_location_location_get_response_default import RhubApiLabLocationLocationGetResponseDefault
from ...types import Response


def _get_kwargs(
    location_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/lab/location/{location_id}".format(client.base_url, location_id=location_id)

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
) -> Optional[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiLabLocationLocationGetResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiLabLocationLocationGetResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    location_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]:
    """Get location

    Args:
        location_id (int):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    location_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]:
    """Get location

    Args:
        location_id (int):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]
    """

    return sync_detailed(
        location_id=location_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    location_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]:
    """Get location

    Args:
        location_id (int):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    location_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]:
    """Get location

    Args:
        location_id (int):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationGetResponse200, RhubApiLabLocationLocationGetResponseDefault]]
    """

    return (
        await asyncio_detailed(
            location_id=location_id,
            client=client,
        )
    ).parsed

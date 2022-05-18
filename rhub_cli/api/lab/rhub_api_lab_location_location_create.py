from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_location_location_create_json_body import RhubApiLabLocationLocationCreateJsonBody
from ...models.rhub_api_lab_location_location_create_response_default import (
    RhubApiLabLocationLocationCreateResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabLocationLocationCreateJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/location".format(client.base_url)

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
) -> Optional[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiLabLocationLocationCreateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabLocationLocationCreateJsonBody,
) -> Response[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]:
    """Create location

    Args:
        json_body (RhubApiLabLocationLocationCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]
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
    json_body: RhubApiLabLocationLocationCreateJsonBody,
) -> Optional[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]:
    """Create location

    Args:
        json_body (RhubApiLabLocationLocationCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabLocationLocationCreateJsonBody,
) -> Response[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]:
    """Create location

    Args:
        json_body (RhubApiLabLocationLocationCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]
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
    json_body: RhubApiLabLocationLocationCreateJsonBody,
) -> Optional[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]:
    """Create location

    Args:
        json_body (RhubApiLabLocationLocationCreateJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabLocationLocationCreateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

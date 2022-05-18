from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_region_update_region_json_body import RhubApiLabRegionUpdateRegionJsonBody
from ...models.rhub_api_lab_region_update_region_response_default import RhubApiLabRegionUpdateRegionResponseDefault
from ...types import Response


def _get_kwargs(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionUpdateRegionJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/region/{region_id}".format(client.base_url, region_id=region_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiLabRegionUpdateRegionResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionUpdateRegionJsonBody,
) -> Response[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]:
    """Update region

    Args:
        region_id (int):
        json_body (RhubApiLabRegionUpdateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionUpdateRegionJsonBody,
) -> Optional[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]:
    """Update region

    Args:
        region_id (int):
        json_body (RhubApiLabRegionUpdateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]
    """

    return sync_detailed(
        region_id=region_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionUpdateRegionJsonBody,
) -> Response[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]:
    """Update region

    Args:
        region_id (int):
        json_body (RhubApiLabRegionUpdateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]
    """

    kwargs = _get_kwargs(
        region_id=region_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    region_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionUpdateRegionJsonBody,
) -> Optional[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]:
    """Update region

    Args:
        region_id (int):
        json_body (RhubApiLabRegionUpdateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionUpdateRegionResponseDefault]]
    """

    return (
        await asyncio_detailed(
            region_id=region_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_region_create_region_json_body import RhubApiLabRegionCreateRegionJsonBody
from ...models.rhub_api_lab_region_create_region_response_default import RhubApiLabRegionCreateRegionResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionCreateRegionJsonBody,
) -> Dict[str, Any]:
    url = "{}/lab/region".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiLabRegionCreateRegionResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionCreateRegionJsonBody,
) -> Response[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]:
    """Create region

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster)
    for more info how reservation, lifespan, and other properties affects clusters.

    `quota` and `lifespan` can be set to `null` to provide unlimited access
    to the region.

    `users_group` limits region to a selected group of users, if the value
    is `null` any user can use region.

    Args:
        json_body (RhubApiLabRegionCreateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]
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
    json_body: RhubApiLabRegionCreateRegionJsonBody,
) -> Optional[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]:
    """Create region

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster)
    for more info how reservation, lifespan, and other properties affects clusters.

    `quota` and `lifespan` can be set to `null` to provide unlimited access
    to the region.

    `users_group` limits region to a selected group of users, if the value
    is `null` any user can use region.

    Args:
        json_body (RhubApiLabRegionCreateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiLabRegionCreateRegionJsonBody,
) -> Response[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]:
    """Create region

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster)
    for more info how reservation, lifespan, and other properties affects clusters.

    `quota` and `lifespan` can be set to `null` to provide unlimited access
    to the region.

    `users_group` limits region to a selected group of users, if the value
    is `null` any user can use region.

    Args:
        json_body (RhubApiLabRegionCreateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]
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
    json_body: RhubApiLabRegionCreateRegionJsonBody,
) -> Optional[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]:
    """Create region

     See [create cluster endpoint](#/lab/rhub.api.lab.cluster.create_cluster)
    for more info how reservation, lifespan, and other properties affects clusters.

    `quota` and `lifespan` can be set to `null` to provide unlimited access
    to the region.

    `users_group` limits region to a selected group of users, if the value
    is `null` any user can use region.

    Args:
        json_body (RhubApiLabRegionCreateRegionJsonBody):

    Returns:
        Response[Union[Any, RhubApiLabRegionCreateRegionResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

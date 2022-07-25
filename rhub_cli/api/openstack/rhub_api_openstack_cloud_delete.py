from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_openstack_cloud_delete_response_default import RhubApiOpenstackCloudDeleteResponseDefault
from ...types import Response


def _get_kwargs(
    cloud_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/openstack/cloud/{cloud_id}".format(client.base_url, cloud_id=cloud_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    else:
        response_default = RhubApiOpenstackCloudDeleteResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cloud_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]:
    """Delete OpenStack cloud

    Args:
        cloud_id (int):

    Returns:
        Response[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]
    """

    kwargs = _get_kwargs(
        cloud_id=cloud_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cloud_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]:
    """Delete OpenStack cloud

    Args:
        cloud_id (int):

    Returns:
        Response[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]
    """

    return sync_detailed(
        cloud_id=cloud_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cloud_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]:
    """Delete OpenStack cloud

    Args:
        cloud_id (int):

    Returns:
        Response[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]
    """

    kwargs = _get_kwargs(
        cloud_id=cloud_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cloud_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]:
    """Delete OpenStack cloud

    Args:
        cloud_id (int):

    Returns:
        Response[Union[Any, RhubApiOpenstackCloudDeleteResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cloud_id=cloud_id,
            client=client,
        )
    ).parsed

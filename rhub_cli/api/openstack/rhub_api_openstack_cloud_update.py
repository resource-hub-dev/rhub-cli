from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_openstack_cloud_update_json_body import RhubApiOpenstackCloudUpdateJsonBody
from ...models.rhub_api_openstack_cloud_update_response_default import RhubApiOpenstackCloudUpdateResponseDefault
from ...types import Response


def _get_kwargs(
    cloud_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackCloudUpdateJsonBody,
) -> Dict[str, Any]:
    url = "{}/openstack/cloud/{cloud_id}".format(client.base_url, cloud_id=cloud_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiOpenstackCloudUpdateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]:
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
    json_body: RhubApiOpenstackCloudUpdateJsonBody,
) -> Response[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]:
    """Update OpenStack cloud

    Args:
        cloud_id (int):
        json_body (RhubApiOpenstackCloudUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]
    """

    kwargs = _get_kwargs(
        cloud_id=cloud_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubApiOpenstackCloudUpdateJsonBody,
) -> Optional[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]:
    """Update OpenStack cloud

    Args:
        cloud_id (int):
        json_body (RhubApiOpenstackCloudUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]
    """

    return sync_detailed(
        cloud_id=cloud_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cloud_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackCloudUpdateJsonBody,
) -> Response[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]:
    """Update OpenStack cloud

    Args:
        cloud_id (int):
        json_body (RhubApiOpenstackCloudUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]
    """

    kwargs = _get_kwargs(
        cloud_id=cloud_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cloud_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackCloudUpdateJsonBody,
) -> Optional[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]:
    """Update OpenStack cloud

    Args:
        cloud_id (int):
        json_body (RhubApiOpenstackCloudUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiOpenstackCloudUpdateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cloud_id=cloud_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

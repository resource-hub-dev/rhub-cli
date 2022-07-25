from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_openstack_project_limits_get_response_200 import RhubApiOpenstackProjectLimitsGetResponse200
from ...models.rhub_api_openstack_project_limits_get_response_default import (
    RhubApiOpenstackProjectLimitsGetResponseDefault,
)
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/openstack/project/{project_id}/limits".format(client.base_url, project_id=project_id)

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
) -> Optional[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiOpenstackProjectLimitsGetResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiOpenstackProjectLimitsGetResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]:
    """Get OpenStack project limits

    Args:
        project_id (int):

    Returns:
        Response[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]:
    """Get OpenStack project limits

    Args:
        project_id (int):

    Returns:
        Response[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]:
    """Get OpenStack project limits

    Args:
        project_id (int):

    Returns:
        Response[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]:
    """Get OpenStack project limits

    Args:
        project_id (int):

    Returns:
        Response[Union[RhubApiOpenstackProjectLimitsGetResponse200, RhubApiOpenstackProjectLimitsGetResponseDefault]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed

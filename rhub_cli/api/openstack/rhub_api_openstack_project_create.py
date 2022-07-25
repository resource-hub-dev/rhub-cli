from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_openstack_project_create_json_body import RhubApiOpenstackProjectCreateJsonBody
from ...models.rhub_api_openstack_project_create_response_200 import RhubApiOpenstackProjectCreateResponse200
from ...models.rhub_api_openstack_project_create_response_default import RhubApiOpenstackProjectCreateResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackProjectCreateJsonBody,
) -> Dict[str, Any]:
    url = "{}/openstack/project".format(client.base_url)

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
) -> Optional[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiOpenstackProjectCreateResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiOpenstackProjectCreateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackProjectCreateJsonBody,
) -> Response[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]:
    """Create OpenStack project

    Args:
        json_body (RhubApiOpenstackProjectCreateJsonBody):

    Returns:
        Response[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]
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
    json_body: RhubApiOpenstackProjectCreateJsonBody,
) -> Optional[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]:
    """Create OpenStack project

    Args:
        json_body (RhubApiOpenstackProjectCreateJsonBody):

    Returns:
        Response[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackProjectCreateJsonBody,
) -> Response[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]:
    """Create OpenStack project

    Args:
        json_body (RhubApiOpenstackProjectCreateJsonBody):

    Returns:
        Response[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]
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
    json_body: RhubApiOpenstackProjectCreateJsonBody,
) -> Optional[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]:
    """Create OpenStack project

    Args:
        json_body (RhubApiOpenstackProjectCreateJsonBody):

    Returns:
        Response[Union[RhubApiOpenstackProjectCreateResponse200, RhubApiOpenstackProjectCreateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

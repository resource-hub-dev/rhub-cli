from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_openstack_project_update_json_body import RhubApiOpenstackProjectUpdateJsonBody
from ...models.rhub_api_openstack_project_update_response_default import RhubApiOpenstackProjectUpdateResponseDefault
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackProjectUpdateJsonBody,
) -> Dict[str, Any]:
    url = "{}/openstack/project/{project_id}".format(client.base_url, project_id=project_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiOpenstackProjectUpdateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]:
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
    json_body: RhubApiOpenstackProjectUpdateJsonBody,
) -> Response[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]:
    """Update OpenStack project

    Args:
        project_id (int):
        json_body (RhubApiOpenstackProjectUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubApiOpenstackProjectUpdateJsonBody,
) -> Optional[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]:
    """Update OpenStack project

    Args:
        project_id (int):
        json_body (RhubApiOpenstackProjectUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackProjectUpdateJsonBody,
) -> Response[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]:
    """Update OpenStack project

    Args:
        project_id (int):
        json_body (RhubApiOpenstackProjectUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiOpenstackProjectUpdateJsonBody,
) -> Optional[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]:
    """Update OpenStack project

    Args:
        project_id (int):
        json_body (RhubApiOpenstackProjectUpdateJsonBody):

    Returns:
        Response[Union[Any, RhubApiOpenstackProjectUpdateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

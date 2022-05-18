from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_launch_template_json_body import RhubApiTowerLaunchTemplateJsonBody
from ...models.rhub_api_tower_launch_template_response_200 import RhubApiTowerLaunchTemplateResponse200
from ...models.rhub_api_tower_launch_template_response_default import RhubApiTowerLaunchTemplateResponseDefault
from ...types import Response


def _get_kwargs(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerLaunchTemplateJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/template/{template_id}/launch".format(client.base_url, template_id=template_id)

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
) -> Optional[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiTowerLaunchTemplateResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiTowerLaunchTemplateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerLaunchTemplateJsonBody,
) -> Response[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]:
    """Launch Tower template

    Args:
        template_id (int):
        json_body (RhubApiTowerLaunchTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerLaunchTemplateJsonBody,
) -> Optional[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]:
    """Launch Tower template

    Args:
        template_id (int):
        json_body (RhubApiTowerLaunchTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerLaunchTemplateJsonBody,
) -> Response[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]:
    """Launch Tower template

    Args:
        template_id (int):
        json_body (RhubApiTowerLaunchTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerLaunchTemplateJsonBody,
) -> Optional[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]:
    """Launch Tower template

    Args:
        template_id (int):
        json_body (RhubApiTowerLaunchTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerLaunchTemplateResponse200, RhubApiTowerLaunchTemplateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_update_template_json_body import RhubApiTowerUpdateTemplateJsonBody
from ...models.rhub_api_tower_update_template_response_200 import RhubApiTowerUpdateTemplateResponse200
from ...models.rhub_api_tower_update_template_response_default import RhubApiTowerUpdateTemplateResponseDefault
from ...types import Response


def _get_kwargs(
    template_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerUpdateTemplateJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/template/{template_id}".format(client.base_url, template_id=template_id)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiTowerUpdateTemplateResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiTowerUpdateTemplateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]:
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
    json_body: RhubApiTowerUpdateTemplateJsonBody,
) -> Response[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]:
    """Change Tower template

    Args:
        template_id (int):
        json_body (RhubApiTowerUpdateTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]
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
    json_body: RhubApiTowerUpdateTemplateJsonBody,
) -> Optional[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]:
    """Change Tower template

    Args:
        template_id (int):
        json_body (RhubApiTowerUpdateTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]
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
    json_body: RhubApiTowerUpdateTemplateJsonBody,
) -> Response[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]:
    """Change Tower template

    Args:
        template_id (int):
        json_body (RhubApiTowerUpdateTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]
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
    json_body: RhubApiTowerUpdateTemplateJsonBody,
) -> Optional[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]:
    """Change Tower template

    Args:
        template_id (int):
        json_body (RhubApiTowerUpdateTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerUpdateTemplateResponse200, RhubApiTowerUpdateTemplateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_create_template_json_body import RhubApiTowerCreateTemplateJsonBody
from ...models.rhub_api_tower_create_template_response_200 import RhubApiTowerCreateTemplateResponse200
from ...models.rhub_api_tower_create_template_response_default import RhubApiTowerCreateTemplateResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerCreateTemplateJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/template".format(client.base_url)

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
) -> Optional[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiTowerCreateTemplateResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiTowerCreateTemplateResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerCreateTemplateJsonBody,
) -> Response[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]:
    """Create Tower template

    Args:
        json_body (RhubApiTowerCreateTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]
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
    json_body: RhubApiTowerCreateTemplateJsonBody,
) -> Optional[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]:
    """Create Tower template

    Args:
        json_body (RhubApiTowerCreateTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerCreateTemplateJsonBody,
) -> Response[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]:
    """Create Tower template

    Args:
        json_body (RhubApiTowerCreateTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]
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
    json_body: RhubApiTowerCreateTemplateJsonBody,
) -> Optional[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]:
    """Create Tower template

    Args:
        json_body (RhubApiTowerCreateTemplateJsonBody):

    Returns:
        Response[Union[RhubApiTowerCreateTemplateResponse200, RhubApiTowerCreateTemplateResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

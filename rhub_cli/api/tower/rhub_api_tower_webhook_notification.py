from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_webhook_notification_json_body import RhubApiTowerWebhookNotificationJsonBody
from ...models.rhub_api_tower_webhook_notification_response_default import (
    RhubApiTowerWebhookNotificationResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerWebhookNotificationJsonBody,
) -> Dict[str, Any]:
    url = "{}/tower/webhook_notification".format(client.base_url)

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
) -> Optional[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    else:
        response_default = RhubApiTowerWebhookNotificationResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerWebhookNotificationJsonBody,
) -> Response[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubApiTowerWebhookNotificationJsonBody):

    Returns:
        Response[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]
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
    json_body: RhubApiTowerWebhookNotificationJsonBody,
) -> Optional[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubApiTowerWebhookNotificationJsonBody):

    Returns:
        Response[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerWebhookNotificationJsonBody,
) -> Response[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubApiTowerWebhookNotificationJsonBody):

    Returns:
        Response[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]
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
    json_body: RhubApiTowerWebhookNotificationJsonBody,
) -> Optional[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubApiTowerWebhookNotificationJsonBody):

    Returns:
        Response[Union[Any, RhubApiTowerWebhookNotificationResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

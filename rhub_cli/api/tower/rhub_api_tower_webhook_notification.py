from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_webhook_notification_json_body import RhubApiTowerWebhookNotificationJsonBody
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerWebhookNotificationJsonBody,
) -> Response[Any]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubApiTowerWebhookNotificationJsonBody):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: RhubApiTowerWebhookNotificationJsonBody,
) -> Response[Any]:
    """Incoming webhook notification from Tower

    Args:
        json_body (RhubApiTowerWebhookNotificationJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)

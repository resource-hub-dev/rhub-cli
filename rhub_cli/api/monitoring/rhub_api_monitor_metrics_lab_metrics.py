from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_monitor_metrics_lab_metrics_response_200 import RhubApiMonitorMetricsLabMetricsResponse200
from ...models.rhub_api_monitor_metrics_lab_metrics_response_default import (
    RhubApiMonitorMetricsLabMetricsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/monitor/lab/metrics".format(client.base_url)

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
) -> Optional[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiMonitorMetricsLabMetricsResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiMonitorMetricsLabMetricsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]:
    """Lab (QuickLab) usage metrics

    Returns:
        Response[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]:
    """Lab (QuickLab) usage metrics

    Returns:
        Response[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]:
    """Lab (QuickLab) usage metrics

    Returns:
        Response[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]:
    """Lab (QuickLab) usage metrics

    Returns:
        Response[Union[RhubApiMonitorMetricsLabMetricsResponse200, RhubApiMonitorMetricsLabMetricsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

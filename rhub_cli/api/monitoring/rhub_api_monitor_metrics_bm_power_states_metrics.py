from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_monitor_metrics_bm_power_states_metrics_response_200 import (
    RhubApiMonitorMetricsBmPowerStatesMetricsResponse200,
)
from ...models.rhub_api_monitor_metrics_bm_power_states_metrics_response_default import (
    RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/monitor/bm/power_states_metrics".format(client.base_url)

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
) -> Optional[
    Union[
        RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault
    ]
]:
    if response.status_code == 200:
        response_200 = RhubApiMonitorMetricsBmPowerStatesMetricsResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault
    ]
]:
    """Get summarized power states from Bare Metal hosts

    Returns:
        Response[Union[RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault]]
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
) -> Optional[
    Union[
        RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault
    ]
]:
    """Get summarized power states from Bare Metal hosts

    Returns:
        Response[Union[RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault
    ]
]:
    """Get summarized power states from Bare Metal hosts

    Returns:
        Response[Union[RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault]]
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
) -> Optional[
    Union[
        RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault
    ]
]:
    """Get summarized power states from Bare Metal hosts

    Returns:
        Response[Union[RhubApiMonitorMetricsBmPowerStatesMetricsResponse200, RhubApiMonitorMetricsBmPowerStatesMetricsResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

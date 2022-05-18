from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_scheduler_cron_update_job_json_body import RhubApiSchedulerCronUpdateJobJsonBody
from ...models.rhub_api_scheduler_cron_update_job_response_200 import RhubApiSchedulerCronUpdateJobResponse200
from ...models.rhub_api_scheduler_cron_update_job_response_default import RhubApiSchedulerCronUpdateJobResponseDefault
from ...types import Response


def _get_kwargs(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiSchedulerCronUpdateJobJsonBody,
) -> Dict[str, Any]:
    url = "{}/scheduler/cron/{cron_job_id}".format(client.base_url, cron_job_id=cron_job_id)

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
) -> Optional[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiSchedulerCronUpdateJobResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiSchedulerCronUpdateJobResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiSchedulerCronUpdateJobJsonBody,
) -> Response[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]:
    """Update CronJob

    Args:
        cron_job_id (int):
        json_body (RhubApiSchedulerCronUpdateJobJsonBody):

    Returns:
        Response[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]
    """

    kwargs = _get_kwargs(
        cron_job_id=cron_job_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiSchedulerCronUpdateJobJsonBody,
) -> Optional[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]:
    """Update CronJob

    Args:
        cron_job_id (int):
        json_body (RhubApiSchedulerCronUpdateJobJsonBody):

    Returns:
        Response[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]
    """

    return sync_detailed(
        cron_job_id=cron_job_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiSchedulerCronUpdateJobJsonBody,
) -> Response[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]:
    """Update CronJob

    Args:
        cron_job_id (int):
        json_body (RhubApiSchedulerCronUpdateJobJsonBody):

    Returns:
        Response[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]
    """

    kwargs = _get_kwargs(
        cron_job_id=cron_job_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiSchedulerCronUpdateJobJsonBody,
) -> Optional[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]:
    """Update CronJob

    Args:
        cron_job_id (int):
        json_body (RhubApiSchedulerCronUpdateJobJsonBody):

    Returns:
        Response[Union[RhubApiSchedulerCronUpdateJobResponse200, RhubApiSchedulerCronUpdateJobResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cron_job_id=cron_job_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

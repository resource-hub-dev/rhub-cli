from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_scheduler_cron_delete_job_response_default import RhubApiSchedulerCronDeleteJobResponseDefault
from ...types import Response


def _get_kwargs(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/scheduler/cron/{cron_job_id}".format(client.base_url, cron_job_id=cron_job_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    else:
        response_default = RhubApiSchedulerCronDeleteJobResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]:
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
) -> Response[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]:
    """Delete CronJob

    Args:
        cron_job_id (int):

    Returns:
        Response[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]
    """

    kwargs = _get_kwargs(
        cron_job_id=cron_job_id,
        client=client,
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
) -> Optional[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]:
    """Delete CronJob

    Args:
        cron_job_id (int):

    Returns:
        Response[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]
    """

    return sync_detailed(
        cron_job_id=cron_job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]:
    """Delete CronJob

    Args:
        cron_job_id (int):

    Returns:
        Response[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]
    """

    kwargs = _get_kwargs(
        cron_job_id=cron_job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    cron_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]:
    """Delete CronJob

    Args:
        cron_job_id (int):

    Returns:
        Response[Union[Any, RhubApiSchedulerCronDeleteJobResponseDefault]]
    """

    return (
        await asyncio_detailed(
            cron_job_id=cron_job_id,
            client=client,
        )
    ).parsed

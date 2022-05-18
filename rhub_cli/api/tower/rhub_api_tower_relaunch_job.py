from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_relaunch_job_response_200 import RhubApiTowerRelaunchJobResponse200
from ...models.rhub_api_tower_relaunch_job_response_default import RhubApiTowerRelaunchJobResponseDefault
from ...types import Response


def _get_kwargs(
    job_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/tower/job/{job_id}/relaunch".format(client.base_url, job_id=job_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiTowerRelaunchJobResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiTowerRelaunchJobResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    job_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]:
    """Re-launch Tower job

    Args:
        job_id (int):

    Returns:
        Response[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    job_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]:
    """Re-launch Tower job

    Args:
        job_id (int):

    Returns:
        Response[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]:
    """Re-launch Tower job

    Args:
        job_id (int):

    Returns:
        Response[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    job_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]:
    """Re-launch Tower job

    Args:
        job_id (int):

    Returns:
        Response[Union[RhubApiTowerRelaunchJobResponse200, RhubApiTowerRelaunchJobResponseDefault]]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed

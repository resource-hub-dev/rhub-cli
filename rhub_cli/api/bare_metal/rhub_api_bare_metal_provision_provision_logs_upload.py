from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.rhub_api_bare_metal_provision_provision_logs_upload_response_default import (
    RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault,
)
from ...types import Response


def _get_kwargs(
    provision_id: int,
    *,
    client: Client,
    multipart_data: Any,
) -> Dict[str, Any]:
    url = "{}/bare_metal/provision/{provision_id}/logs".format(client.base_url, provision_id=provision_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    provision_id: int,
    *,
    client: Client,
    multipart_data: Any,
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]:
    """Endpoint to upload provision logs

    Args:
        provision_id (int):
        multipart_data (Any):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]
    """

    kwargs = _get_kwargs(
        provision_id=provision_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    provision_id: int,
    *,
    client: Client,
    multipart_data: Any,
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]:
    """Endpoint to upload provision logs

    Args:
        provision_id (int):
        multipart_data (Any):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]
    """

    return sync_detailed(
        provision_id=provision_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    provision_id: int,
    *,
    client: Client,
    multipart_data: Any,
) -> Response[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]:
    """Endpoint to upload provision logs

    Args:
        provision_id (int):
        multipart_data (Any):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]
    """

    kwargs = _get_kwargs(
        provision_id=provision_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    provision_id: int,
    *,
    client: Client,
    multipart_data: Any,
) -> Optional[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]:
    """Endpoint to upload provision logs

    Args:
        provision_id (int):
        multipart_data (Any):

    Returns:
        Response[Union[Any, RhubApiBareMetalProvisionProvisionLogsUploadResponseDefault]]
    """

    return (
        await asyncio_detailed(
            provision_id=provision_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed

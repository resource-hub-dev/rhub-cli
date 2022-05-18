from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_lab_location_location_list_response_200 import RhubApiLabLocationLocationListResponse200
from ...models.rhub_api_lab_location_location_list_response_default import RhubApiLabLocationLocationListResponseDefault
from ...models.rhub_api_lab_location_location_list_sort import RhubApiLabLocationLocationListSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, None, RhubApiLabLocationLocationListSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/lab/location".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiLabLocationLocationListResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiLabLocationLocationListResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, None, RhubApiLabLocationLocationListSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]:
    """Get location list

    Args:
        sort (Union[Unset, None, RhubApiLabLocationLocationListSort]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        sort=sort,
        page=page,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, None, RhubApiLabLocationLocationListSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]:
    """Get location list

    Args:
        sort (Union[Unset, None, RhubApiLabLocationLocationListSort]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]
    """

    return sync_detailed(
        client=client,
        sort=sort,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, None, RhubApiLabLocationLocationListSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]:
    """Get location list

    Args:
        sort (Union[Unset, None, RhubApiLabLocationLocationListSort]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        sort=sort,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sort: Union[Unset, None, RhubApiLabLocationLocationListSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]:
    """Get location list

    Args:
        sort (Union[Unset, None, RhubApiLabLocationLocationListSort]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubApiLabLocationLocationListResponse200, RhubApiLabLocationLocationListResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            sort=sort,
            page=page,
            limit=limit,
        )
    ).parsed

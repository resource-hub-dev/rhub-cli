from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_tower_list_templates_filter import RhubApiTowerListTemplatesFilter
from ...models.rhub_api_tower_list_templates_response_200 import RhubApiTowerListTemplatesResponse200
from ...models.rhub_api_tower_list_templates_response_default import RhubApiTowerListTemplatesResponseDefault
from ...models.rhub_api_tower_list_templates_sort import RhubApiTowerListTemplatesSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiTowerListTemplatesFilter] = UNSET,
    sort: Union[Unset, None, RhubApiTowerListTemplatesSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tower/template".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_filter_: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict() if filter_ else None

    if not isinstance(json_filter_, Unset) and json_filter_ is not None:
        params.update(json_filter_)

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
) -> Optional[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiTowerListTemplatesResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiTowerListTemplatesResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiTowerListTemplatesFilter] = UNSET,
    sort: Union[Unset, None, RhubApiTowerListTemplatesSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]:
    """Get list of Tower templates

    Args:
        filter_ (Union[Unset, None, RhubApiTowerListTemplatesFilter]):
        sort (Union[Unset, None, RhubApiTowerListTemplatesSort]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
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
    filter_: Union[Unset, None, RhubApiTowerListTemplatesFilter] = UNSET,
    sort: Union[Unset, None, RhubApiTowerListTemplatesSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]:
    """Get list of Tower templates

    Args:
        filter_ (Union[Unset, None, RhubApiTowerListTemplatesFilter]):
        sort (Union[Unset, None, RhubApiTowerListTemplatesSort]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_: Union[Unset, None, RhubApiTowerListTemplatesFilter] = UNSET,
    sort: Union[Unset, None, RhubApiTowerListTemplatesSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]:
    """Get list of Tower templates

    Args:
        filter_ (Union[Unset, None, RhubApiTowerListTemplatesFilter]):
        sort (Union[Unset, None, RhubApiTowerListTemplatesSort]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
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
    filter_: Union[Unset, None, RhubApiTowerListTemplatesFilter] = UNSET,
    sort: Union[Unset, None, RhubApiTowerListTemplatesSort] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]:
    """Get list of Tower templates

    Args:
        filter_ (Union[Unset, None, RhubApiTowerListTemplatesFilter]):
        sort (Union[Unset, None, RhubApiTowerListTemplatesSort]):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Returns:
        Response[Union[RhubApiTowerListTemplatesResponse200, RhubApiTowerListTemplatesResponseDefault]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            sort=sort,
            page=page,
            limit=limit,
        )
    ).parsed

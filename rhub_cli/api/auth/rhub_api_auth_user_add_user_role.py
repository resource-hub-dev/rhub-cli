from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_user_add_user_role_json_body import RhubApiAuthUserAddUserRoleJsonBody
from ...models.rhub_api_auth_user_add_user_role_response_default import RhubApiAuthUserAddUserRoleResponseDefault
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserAddUserRoleJsonBody,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}/roles".format(client.base_url, user_id=user_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    else:
        response_default = RhubApiAuthUserAddUserRoleResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserAddUserRoleJsonBody,
) -> Response[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]:
    """Add user to role

    Args:
        user_id (str):
        json_body (RhubApiAuthUserAddUserRoleJsonBody):

    Returns:
        Response[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserAddUserRoleJsonBody,
) -> Optional[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]:
    """Add user to role

    Args:
        user_id (str):
        json_body (RhubApiAuthUserAddUserRoleJsonBody):

    Returns:
        Response[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserAddUserRoleJsonBody,
) -> Response[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]:
    """Add user to role

    Args:
        user_id (str):
        json_body (RhubApiAuthUserAddUserRoleJsonBody):

    Returns:
        Response[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiAuthUserAddUserRoleJsonBody,
) -> Optional[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]:
    """Add user to role

    Args:
        user_id (str):
        json_body (RhubApiAuthUserAddUserRoleJsonBody):

    Returns:
        Response[Union[Any, RhubApiAuthUserAddUserRoleResponseDefault]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

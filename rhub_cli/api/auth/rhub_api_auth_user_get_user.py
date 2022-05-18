from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_auth_user_get_user_response_200 import RhubApiAuthUserGetUserResponse200
from ...models.rhub_api_auth_user_get_user_response_default import RhubApiAuthUserGetUserResponseDefault
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/auth/user/{user_id}".format(client.base_url, user_id=user_id)

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
) -> Optional[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiAuthUserGetUserResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiAuthUserGetUserResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]:
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
) -> Response[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]:
    """Get user

     Returns user data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `createdTimestamp` and others.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        user_id (str):

    Returns:
        Response[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
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
) -> Optional[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]:
    """Get user

     Returns user data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `createdTimestamp` and others.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        user_id (str):

    Returns:
        Response[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]:
    """Get user

     Returns user data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `createdTimestamp` and others.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        user_id (str):

    Returns:
        Response[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]:
    """Get user

     Returns user data including extra fields added by auth database. Data
    object contains at least properties that are in the schema but also
    database internal data like `createdTimestamp` and others.

    See also [Keycloak API: UserRepresentation](
      https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

    Args:
        user_id (str):

    Returns:
        Response[Union[RhubApiAuthUserGetUserResponse200, RhubApiAuthUserGetUserResponseDefault]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed

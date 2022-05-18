from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_policies_get_policy_response_200 import RhubApiPoliciesGetPolicyResponse200
from ...models.rhub_api_policies_get_policy_response_default import RhubApiPoliciesGetPolicyResponseDefault
from ...types import Response


def _get_kwargs(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/policies/{policy_id}".format(client.base_url, policy_id=policy_id)

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
) -> Optional[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiPoliciesGetPolicyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    else:
        response_default = RhubApiPoliciesGetPolicyResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]:
    """Get policy

    Args:
        policy_id (int):

    Returns:
        Response[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]:
    """Get policy

    Args:
        policy_id (int):

    Returns:
        Response[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]:
    """Get policy

    Args:
        policy_id (int):

    Returns:
        Response[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    policy_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]:
    """Get policy

    Args:
        policy_id (int):

    Returns:
        Response[Union[Any, RhubApiPoliciesGetPolicyResponse200, RhubApiPoliciesGetPolicyResponseDefault]]
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
        )
    ).parsed

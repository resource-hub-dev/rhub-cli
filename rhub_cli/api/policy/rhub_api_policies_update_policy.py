from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.rhub_api_policies_update_policy_json_body import RhubApiPoliciesUpdatePolicyJsonBody
from ...models.rhub_api_policies_update_policy_response_200 import RhubApiPoliciesUpdatePolicyResponse200
from ...models.rhub_api_policies_update_policy_response_default import RhubApiPoliciesUpdatePolicyResponseDefault
from ...types import Response


def _get_kwargs(
    policy_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiPoliciesUpdatePolicyJsonBody,
) -> Dict[str, Any]:
    url = "{}/policies/{policy_id}".format(client.base_url, policy_id=policy_id)

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
) -> Optional[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]:
    if response.status_code == 200:
        response_200 = RhubApiPoliciesUpdatePolicyResponse200.from_dict(response.json())

        return response_200

    else:
        response_default = RhubApiPoliciesUpdatePolicyResponseDefault.from_dict(response.json())

        return response_default

    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]:
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
    json_body: RhubApiPoliciesUpdatePolicyJsonBody,
) -> Response[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]:
    """Update policy

    Args:
        policy_id (int):
        json_body (RhubApiPoliciesUpdatePolicyJsonBody):

    Returns:
        Response[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
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
    json_body: RhubApiPoliciesUpdatePolicyJsonBody,
) -> Optional[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]:
    """Update policy

    Args:
        policy_id (int):
        json_body (RhubApiPoliciesUpdatePolicyJsonBody):

    Returns:
        Response[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    policy_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiPoliciesUpdatePolicyJsonBody,
) -> Response[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]:
    """Update policy

    Args:
        policy_id (int):
        json_body (RhubApiPoliciesUpdatePolicyJsonBody):

    Returns:
        Response[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    policy_id: int,
    *,
    client: AuthenticatedClient,
    json_body: RhubApiPoliciesUpdatePolicyJsonBody,
) -> Optional[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]:
    """Update policy

    Args:
        policy_id (int):
        json_body (RhubApiPoliciesUpdatePolicyJsonBody):

    Returns:
        Response[Union[RhubApiPoliciesUpdatePolicyResponse200, RhubApiPoliciesUpdatePolicyResponseDefault]]
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

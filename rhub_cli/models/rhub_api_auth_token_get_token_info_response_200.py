from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RhubApiAuthTokenGetTokenInfoResponse200")


@attr.s(auto_attribs=True)
class RhubApiAuthTokenGetTokenInfoResponse200:
    """See [RFC 7662, Section 2.2](https://tools.ietf.org/html/rfc7662#section-2.2)
    and [Keycloak API: AccessToken](https://www.keycloak.org/docs-api/11.0/rest-api/#_accesstoken)

        Example:
            {'acr': '1', 'active': True, 'allowed-origins': ['http://localhost:8080'], 'aud': 'account', 'azp': 'rhub-app',
                'client_id': 'rhub-app', 'email': 'testuser1@example.com', 'email_verified': False, 'exp': 1617791654,
                'family_name': 'user1', 'given_name': 'test', 'iat': 1617791354, 'iss':
                'http://localhost:8082/auth/realms/rhub', 'jti': '640eb3a2-a193-4998-aa5b-5f0ba5beb154', 'name': 'test user1',
                'preferred_username': 'testuser1', 'realm_access': {'roles': ['offline_access', 'uma_authorization']},
                'resource_access': {'account': {'roles': ['manage-account', 'manage-account-links', 'view-profile']}}, 'scope':
                'profile email', 'session_state': '82b7637e-69a2-41e1-ab0b-e3d6b6e1fb0a', 'sub':
                '743a5375-3513-4749-acb9-1cde1e159e3b', 'typ': 'Bearer', 'username': 'testuser1'}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        rhub_api_auth_token_get_token_info_response_200 = cls()

        rhub_api_auth_token_get_token_info_response_200.additional_properties = d
        return rhub_api_auth_token_get_token_info_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

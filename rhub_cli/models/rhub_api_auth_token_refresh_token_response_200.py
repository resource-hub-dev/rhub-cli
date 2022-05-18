from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RhubApiAuthTokenRefreshTokenResponse200")


@attr.s(auto_attribs=True)
class RhubApiAuthTokenRefreshTokenResponse200:
    """
    Example:
        {'access_token': 'eyJhbGciOiJSUzI1...oJhA', 'expires_in': 300, 'not-before-policy': 0, 'refresh_expires_in':
            1800, 'refresh_token': 'eyJhbGciOiJIUzI1...fc8A', 'scope': 'profile email', 'session_state':
            '82b7637e-69a2-41e1-ab0b-e3d6b6e1fb0a', 'token_type': 'Bearer'}

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
        rhub_api_auth_token_refresh_token_response_200 = cls()

        rhub_api_auth_token_refresh_token_response_200.additional_properties = d
        return rhub_api_auth_token_refresh_token_response_200

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

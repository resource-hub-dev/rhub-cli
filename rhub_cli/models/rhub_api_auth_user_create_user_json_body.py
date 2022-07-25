from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiAuthUserCreateUserJsonBody")


@attr.s(auto_attribs=True)
class RhubApiAuthUserCreateUserJsonBody:
    """See [Keycloak API: UserRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_userrepresentation)

      Example:
          {'access': {'impersonate': True, 'manage': True, 'manageGroupMembership': True, 'mapRoles': True, 'view': True},
              'createdTimestamp': 1614717256570, 'disableableCredentialTypes': [], 'email': 'testuser1@example.com',
              'emailVerified': False, 'enabled': True, 'firstName': 'test', 'id': '743a5375-3513-4749-acb9-1cde1e159e3b',
              'lastName': 'user1', 'notBefore': 0, 'requiredActions': [], 'totp': False, 'username': 'testuser1'}

      Attributes:
          email (str):
          username (str):
          enabled (Union[Unset, bool]):
          first_name (Union[Unset, str]):
          id (Union[Unset, str]):
          last_name (Union[Unset, str]):
          password (Union[Unset, str]):
    """

    email: str
    username: str
    enabled: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        username = self.username
        enabled = self.enabled
        first_name = self.first_name
        id = self.id
        last_name = self.last_name
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "username": username,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        email = d.pop("email")

        username = d.pop("username")

        enabled = d.pop("enabled", UNSET)

        first_name = d.pop("firstName", UNSET)

        id = d.pop("id", UNSET)

        last_name = d.pop("lastName", UNSET)

        password = d.pop("password", UNSET)

        rhub_api_auth_user_create_user_json_body = cls(
            email=email,
            username=username,
            enabled=enabled,
            first_name=first_name,
            id=id,
            last_name=last_name,
            password=password,
        )

        rhub_api_auth_user_create_user_json_body.additional_properties = d
        return rhub_api_auth_user_create_user_json_body

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

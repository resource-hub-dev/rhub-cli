from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_auth_role_create_role_json_body_attributes import RhubApiAuthRoleCreateRoleJsonBodyAttributes
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiAuthRoleCreateRoleJsonBody")


@attr.s(auto_attribs=True)
class RhubApiAuthRoleCreateRoleJsonBody:
    """See [Keycloak API: RoleRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_rolerepresentation)

        Example:
            {'attributes': {}, 'clientRole': False, 'composite': False, 'composites': {}, 'containerId': 'admin',
                'description': 'adminRole', 'id': 'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin'}

        Attributes:
            name (str):
            attributes (Union[Unset, RhubApiAuthRoleCreateRoleJsonBodyAttributes]): Role attributes
            id (Union[Unset, str]):
    """

    name: str
    attributes: Union[Unset, RhubApiAuthRoleCreateRoleJsonBodyAttributes] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        name = d.pop("name")

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, RhubApiAuthRoleCreateRoleJsonBodyAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RhubApiAuthRoleCreateRoleJsonBodyAttributes.from_dict(_attributes)

        id = d.pop("id", UNSET)

        rhub_api_auth_role_create_role_json_body = cls(
            name=name,
            attributes=attributes,
            id=id,
        )

        rhub_api_auth_role_create_role_json_body.additional_properties = d
        return rhub_api_auth_role_create_role_json_body

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

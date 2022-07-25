from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_auth_group_list_groups_response_200_item_attributes import (
    RhubApiAuthGroupListGroupsResponse200ItemAttributes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiAuthGroupListGroupsResponse200Item")


@attr.s(auto_attribs=True)
class RhubApiAuthGroupListGroupsResponse200Item:
    """See [Keycloak API: GroupRepresentation](
    https://www.keycloak.org/docs-api/11.0/rest-api/#_grouprepresentation)

        Example:
            {'access': {'manage': True, 'manageMembership': True, 'view': True}, 'attributes': {'mailing-list': ['admin-
                list@example.com']}, 'clientRoles': {}, 'id': 'fa831aa3-7a5a-4667-9c3f-bf20465058f6', 'name': 'admin', 'path':
                '/admin', 'realmRoles': [], 'subGroups': []}

        Attributes:
            attributes (Union[Unset, RhubApiAuthGroupListGroupsResponse200ItemAttributes]): Group attributes
            id (Union[Unset, str]):
            name (Union[Unset, str]):
    """

    attributes: Union[Unset, RhubApiAuthGroupListGroupsResponse200ItemAttributes] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, RhubApiAuthGroupListGroupsResponse200ItemAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = RhubApiAuthGroupListGroupsResponse200ItemAttributes.from_dict(_attributes)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rhub_api_auth_group_list_groups_response_200_item = cls(
            attributes=attributes,
            id=id,
            name=name,
        )

        rhub_api_auth_group_list_groups_response_200_item.additional_properties = d
        return rhub_api_auth_group_list_groups_response_200_item

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

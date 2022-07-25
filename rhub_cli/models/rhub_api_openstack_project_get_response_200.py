from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackProjectGetResponse200")


@attr.s(auto_attribs=True)
class RhubApiOpenstackProjectGetResponse200:
    """
    Attributes:
        cloud_id (Union[Unset, int]):
        cloud_name (Union[Unset, str]):
        description (Union[Unset, None, str]):
        group_id (Union[Unset, None, str]):
        group_name (Union[Unset, None, str]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):  Example: myproject.
        owner_id (Union[Unset, str]): Defaults to user who created a project.
        owner_name (Union[Unset, str]):
    """

    cloud_id: Union[Unset, int] = UNSET
    cloud_name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    group_id: Union[Unset, None, str] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    owner_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_id = self.cloud_id
        cloud_name = self.cloud_name
        description = self.description
        group_id = self.group_id
        group_name = self.group_name
        id = self.id
        name = self.name
        owner_id = self.owner_id
        owner_name = self.owner_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_id is not UNSET:
            field_dict["cloud_id"] = cloud_id
        if cloud_name is not UNSET:
            field_dict["cloud_name"] = cloud_name
        if description is not UNSET:
            field_dict["description"] = description
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        cloud_id = d.pop("cloud_id", UNSET)

        cloud_name = d.pop("cloud_name", UNSET)

        description = d.pop("description", UNSET)

        group_id = d.pop("group_id", UNSET)

        group_name = d.pop("group_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_name = d.pop("owner_name", UNSET)

        rhub_api_openstack_project_get_response_200 = cls(
            cloud_id=cloud_id,
            cloud_name=cloud_name,
            description=description,
            group_id=group_id,
            group_name=group_name,
            id=id,
            name=name,
            owner_id=owner_id,
            owner_name=owner_name,
        )

        rhub_api_openstack_project_get_response_200.additional_properties = d
        return rhub_api_openstack_project_get_response_200

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

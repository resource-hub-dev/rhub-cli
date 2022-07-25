from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackProjectListFilter")


@attr.s(auto_attribs=True)
class RhubApiOpenstackProjectListFilter:
    """
    Attributes:
        cloud_id (Union[Unset, int]): ID of the cloud.
        name (Union[Unset, str]): Name of a project. Wildcard ``%`` can be used to match zero, one, or multiple
            characters
        owner_id (Union[Unset, None, str]):
    """

    cloud_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_id = self.cloud_id
        name = self.name
        owner_id = self.owner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_id is not UNSET:
            field_dict["cloud_id"] = cloud_id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        cloud_id = d.pop("cloud_id", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        rhub_api_openstack_project_list_filter = cls(
            cloud_id=cloud_id,
            name=name,
            owner_id=owner_id,
        )

        rhub_api_openstack_project_list_filter.additional_properties = d
        return rhub_api_openstack_project_list_filter

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

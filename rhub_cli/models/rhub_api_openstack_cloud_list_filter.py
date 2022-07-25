from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackCloudListFilter")


@attr.s(auto_attribs=True)
class RhubApiOpenstackCloudListFilter:
    """
    Attributes:
        name (Union[Unset, str]): Name of a cloud. Wildcard ``%`` can be used to match zero, one, or multiple characters
        owner_group_id (Union[Unset, None, str]):
    """

    name: Union[Unset, str] = UNSET
    owner_group_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        owner_group_id = self.owner_group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_group_id is not UNSET:
            field_dict["owner_group_id"] = owner_group_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        name = d.pop("name", UNSET)

        owner_group_id = d.pop("owner_group_id", UNSET)

        rhub_api_openstack_cloud_list_filter = cls(
            name=name,
            owner_group_id=owner_group_id,
        )

        rhub_api_openstack_cloud_list_filter.additional_properties = d
        return rhub_api_openstack_cloud_list_filter

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

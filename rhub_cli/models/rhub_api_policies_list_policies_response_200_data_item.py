from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiPoliciesListPoliciesResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiPoliciesListPoliciesResponse200DataItem:
    """
    Attributes:
        department (Union[Unset, str]): Department Name
        id (Union[Unset, int]): Internal ID
        name (Union[Unset, str]): Name
    """

    department: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        department = self.department
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if department is not UNSET:
            field_dict["department"] = department
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        department = d.pop("department", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rhub_api_policies_list_policies_response_200_data_item = cls(
            department=department,
            id=id,
            name=name,
        )

        rhub_api_policies_list_policies_response_200_data_item.additional_properties = d
        return rhub_api_policies_list_policies_response_200_data_item

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

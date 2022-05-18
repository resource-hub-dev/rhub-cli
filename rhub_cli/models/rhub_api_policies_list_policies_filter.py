from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiPoliciesListPoliciesFilter")


@attr.s(auto_attribs=True)
class RhubApiPoliciesListPoliciesFilter:
    """
    Attributes:
        department (Union[Unset, str]): Department of a policy. Wildcard ``%`` can be used to match zero, one, or
            multiple characters
        name (Union[Unset, str]): Name of a policy. Wildcard ``%`` can be used to match zero, one, or multiple
            characters
    """

    department: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        department = self.department
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if department is not UNSET:
            field_dict["department"] = department
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        department = d.pop("department", UNSET)

        name = d.pop("name", UNSET)

        rhub_api_policies_list_policies_filter = cls(
            department=department,
            name=name,
        )

        rhub_api_policies_list_policies_filter.additional_properties = d
        return rhub_api_policies_list_policies_filter

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

from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_policies_create_policy_response_200_constraint import (
    RhubApiPoliciesCreatePolicyResponse200Constraint,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiPoliciesCreatePolicyResponse200")


@attr.s(auto_attribs=True)
class RhubApiPoliciesCreatePolicyResponse200:
    """
    Attributes:
        constraint (Union[Unset, RhubApiPoliciesCreatePolicyResponse200Constraint]):
        department (Union[Unset, str]): Department Name
        id (Union[Unset, int]): Internal ID
        name (Union[Unset, str]): Name
    """

    constraint: Union[Unset, RhubApiPoliciesCreatePolicyResponse200Constraint] = UNSET
    department: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        constraint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.constraint, Unset):
            constraint = self.constraint.to_dict()

        department = self.department
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constraint is not UNSET:
            field_dict["constraint"] = constraint
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
        _constraint = d.pop("constraint", UNSET)
        constraint: Union[Unset, RhubApiPoliciesCreatePolicyResponse200Constraint]
        if isinstance(_constraint, Unset):
            constraint = UNSET
        else:
            constraint = RhubApiPoliciesCreatePolicyResponse200Constraint.from_dict(_constraint)

        department = d.pop("department", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rhub_api_policies_create_policy_response_200 = cls(
            constraint=constraint,
            department=department,
            id=id,
            name=name,
        )

        rhub_api_policies_create_policy_response_200.additional_properties = d
        return rhub_api_policies_create_policy_response_200

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

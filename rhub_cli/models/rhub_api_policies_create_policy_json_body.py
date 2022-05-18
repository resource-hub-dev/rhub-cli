from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_policies_create_policy_json_body_constraint import RhubApiPoliciesCreatePolicyJsonBodyConstraint
from ..models.rhub_api_policies_create_policy_json_body_id import RhubApiPoliciesCreatePolicyJsonBodyId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiPoliciesCreatePolicyJsonBody")


@attr.s(auto_attribs=True)
class RhubApiPoliciesCreatePolicyJsonBody:
    """
    Attributes:
        department (str): Department Name
        name (str): Name
        constraint (Union[Unset, RhubApiPoliciesCreatePolicyJsonBodyConstraint]):
        id (Union[Unset, RhubApiPoliciesCreatePolicyJsonBodyId]): Internal ID
    """

    department: str
    name: str
    constraint: Union[Unset, RhubApiPoliciesCreatePolicyJsonBodyConstraint] = UNSET
    id: Union[Unset, RhubApiPoliciesCreatePolicyJsonBodyId] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        department = self.department
        name = self.name
        constraint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.constraint, Unset):
            constraint = self.constraint.to_dict()

        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "department": department,
                "name": name,
            }
        )
        if constraint is not UNSET:
            field_dict["constraint"] = constraint
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        department = d.pop("department")

        name = d.pop("name")

        _constraint = d.pop("constraint", UNSET)
        constraint: Union[Unset, RhubApiPoliciesCreatePolicyJsonBodyConstraint]
        if isinstance(_constraint, Unset):
            constraint = UNSET
        else:
            constraint = RhubApiPoliciesCreatePolicyJsonBodyConstraint.from_dict(_constraint)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiPoliciesCreatePolicyJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiPoliciesCreatePolicyJsonBodyId.from_dict(_id)

        rhub_api_policies_create_policy_json_body = cls(
            department=department,
            name=name,
            constraint=constraint,
            id=id,
        )

        rhub_api_policies_create_policy_json_body.additional_properties = d
        return rhub_api_policies_create_policy_json_body

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

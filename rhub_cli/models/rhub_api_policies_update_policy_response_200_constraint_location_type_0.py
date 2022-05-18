from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_policies_update_policy_response_200_constraint_location_type_0_id import (
    RhubApiPoliciesUpdatePolicyResponse200ConstraintLocationType0Id,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiPoliciesUpdatePolicyResponse200ConstraintLocationType0")


@attr.s(auto_attribs=True)
class RhubApiPoliciesUpdatePolicyResponse200ConstraintLocationType0:
    """
    Attributes:
        description (Union[Unset, None, str]): Long description of location, address, ... Example: Raleigh.
        id (Union[Unset, RhubApiPoliciesUpdatePolicyResponse200ConstraintLocationType0Id]):
        name (Union[Unset, str]): Short name of location / IATA identifier / ... Example: RDU.
    """

    description: Union[Unset, None, str] = UNSET
    id: Union[Unset, RhubApiPoliciesUpdatePolicyResponse200ConstraintLocationType0Id] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiPoliciesUpdatePolicyResponse200ConstraintLocationType0Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiPoliciesUpdatePolicyResponse200ConstraintLocationType0Id.from_dict(_id)

        name = d.pop("name", UNSET)

        rhub_api_policies_update_policy_response_200_constraint_location_type_0 = cls(
            description=description,
            id=id,
            name=name,
        )

        rhub_api_policies_update_policy_response_200_constraint_location_type_0.additional_properties = d
        return rhub_api_policies_update_policy_response_200_constraint_location_type_0

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

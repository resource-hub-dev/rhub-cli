import datetime
from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.rhub_api_policies_get_policy_response_200_constraint_limit import (
    RhubApiPoliciesGetPolicyResponse200ConstraintLimit,
)
from ..models.rhub_api_policies_get_policy_response_200_constraint_location_type_0 import (
    RhubApiPoliciesGetPolicyResponse200ConstraintLocationType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiPoliciesGetPolicyResponse200Constraint")


@attr.s(auto_attribs=True)
class RhubApiPoliciesGetPolicyResponse200Constraint:
    """
    Attributes:
        cost (Union[Unset, None, float]):
        density (Union[Unset, None, str]):
        limit (Union[Unset, None, RhubApiPoliciesGetPolicyResponse200ConstraintLimit]):
        location (Union[Any, RhubApiPoliciesGetPolicyResponse200ConstraintLocationType0, Unset]):
        location_id (Union[Any, Unset, int]):
        sched_avail (Union[Unset, None, List[datetime.datetime]]):
        serv_avail (Union[Unset, None, float]):
        tag (Union[Unset, None, List[str]]):
    """

    cost: Union[Unset, None, float] = UNSET
    density: Union[Unset, None, str] = UNSET
    limit: Union[Unset, None, RhubApiPoliciesGetPolicyResponse200ConstraintLimit] = UNSET
    location: Union[Any, RhubApiPoliciesGetPolicyResponse200ConstraintLocationType0, Unset] = UNSET
    location_id: Union[Any, Unset, int] = UNSET
    sched_avail: Union[Unset, None, List[datetime.datetime]] = UNSET
    serv_avail: Union[Unset, None, float] = UNSET
    tag: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost = self.cost
        density = self.density
        limit: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.limit, Unset):
            limit = self.limit.to_dict() if self.limit else None

        location: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.location, Unset):
            location = UNSET

        elif isinstance(self.location, RhubApiPoliciesGetPolicyResponse200ConstraintLocationType0):
            location = UNSET
            if not isinstance(self.location, Unset):
                location = self.location.to_dict()

        else:
            location = self.location

        location_id: Union[Any, Unset, int]
        if isinstance(self.location_id, Unset):
            location_id = UNSET

        else:
            location_id = self.location_id

        sched_avail: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.sched_avail, Unset):
            if self.sched_avail is None:
                sched_avail = None
            else:
                sched_avail = []
                for sched_avail_item_data in self.sched_avail:
                    sched_avail_item = sched_avail_item_data.isoformat()

                    sched_avail.append(sched_avail_item)

        serv_avail = self.serv_avail
        tag: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tag, Unset):
            if self.tag is None:
                tag = None
            else:
                tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost is not UNSET:
            field_dict["cost"] = cost
        if density is not UNSET:
            field_dict["density"] = density
        if limit is not UNSET:
            field_dict["limit"] = limit
        if location is not UNSET:
            field_dict["location"] = location
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if sched_avail is not UNSET:
            field_dict["sched_avail"] = sched_avail
        if serv_avail is not UNSET:
            field_dict["serv_avail"] = serv_avail
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        cost = d.pop("cost", UNSET)

        density = d.pop("density", UNSET)

        _limit = d.pop("limit", UNSET)
        limit: Union[Unset, None, RhubApiPoliciesGetPolicyResponse200ConstraintLimit]
        if _limit is None:
            limit = None
        elif isinstance(_limit, Unset):
            limit = UNSET
        else:
            limit = RhubApiPoliciesGetPolicyResponse200ConstraintLimit.from_dict(_limit)

        def _parse_location(
            data: object,
        ) -> Union[Any, RhubApiPoliciesGetPolicyResponse200ConstraintLocationType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _location_type_0 = data
                location_type_0: Union[Unset, RhubApiPoliciesGetPolicyResponse200ConstraintLocationType0]
                if isinstance(_location_type_0, Unset):
                    location_type_0 = UNSET
                else:
                    location_type_0 = RhubApiPoliciesGetPolicyResponse200ConstraintLocationType0.from_dict(
                        _location_type_0
                    )

                return location_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiPoliciesGetPolicyResponse200ConstraintLocationType0, Unset], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_location_id(data: object) -> Union[Any, Unset, int]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, Unset, int], data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        sched_avail = []
        _sched_avail = d.pop("sched_avail", UNSET)
        for sched_avail_item_data in _sched_avail or []:
            sched_avail_item = isoparse(sched_avail_item_data)

            sched_avail.append(sched_avail_item)

        serv_avail = d.pop("serv_avail", UNSET)

        tag = cast(List[str], d.pop("tag", UNSET))

        rhub_api_policies_get_policy_response_200_constraint = cls(
            cost=cost,
            density=density,
            limit=limit,
            location=location,
            location_id=location_id,
            sched_avail=sched_avail,
            serv_avail=serv_avail,
            tag=tag,
        )

        rhub_api_policies_get_policy_response_200_constraint.additional_properties = d
        return rhub_api_policies_get_policy_response_200_constraint

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

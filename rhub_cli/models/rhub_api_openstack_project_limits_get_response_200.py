from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_openstack_project_limits_get_response_200_absolute import (
    RhubApiOpenstackProjectLimitsGetResponse200Absolute,
)
from ..models.rhub_api_openstack_project_limits_get_response_200_rate_item import (
    RhubApiOpenstackProjectLimitsGetResponse200RateItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackProjectLimitsGetResponse200")


@attr.s(auto_attribs=True)
class RhubApiOpenstackProjectLimitsGetResponse200:
    """
    Attributes:
        absolute (Union[Unset, RhubApiOpenstackProjectLimitsGetResponse200Absolute]):
        rate (Union[Unset, List[RhubApiOpenstackProjectLimitsGetResponse200RateItem]]):
    """

    absolute: Union[Unset, RhubApiOpenstackProjectLimitsGetResponse200Absolute] = UNSET
    rate: Union[Unset, List[RhubApiOpenstackProjectLimitsGetResponse200RateItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        absolute: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.absolute, Unset):
            absolute = self.absolute.to_dict()

        rate: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rate, Unset):
            rate = []
            for rate_item_data in self.rate:
                rate_item = rate_item_data.to_dict()

                rate.append(rate_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if absolute is not UNSET:
            field_dict["absolute"] = absolute
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _absolute = d.pop("absolute", UNSET)
        absolute: Union[Unset, RhubApiOpenstackProjectLimitsGetResponse200Absolute]
        if isinstance(_absolute, Unset):
            absolute = UNSET
        else:
            absolute = RhubApiOpenstackProjectLimitsGetResponse200Absolute.from_dict(_absolute)

        rate = []
        _rate = d.pop("rate", UNSET)
        for rate_item_data in _rate or []:
            rate_item = RhubApiOpenstackProjectLimitsGetResponse200RateItem.from_dict(rate_item_data)

            rate.append(rate_item)

        rhub_api_openstack_project_limits_get_response_200 = cls(
            absolute=absolute,
            rate=rate,
        )

        rhub_api_openstack_project_limits_get_response_200.additional_properties = d
        return rhub_api_openstack_project_limits_get_response_200

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

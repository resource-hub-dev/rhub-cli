from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabLocationLocationRegionListFilter")


@attr.s(auto_attribs=True)
class RhubApiLabLocationLocationRegionListFilter:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        location (Union[Unset, str]): Location of a region. Wildcard ``%`` can be used to match zero, one, or multiple
            characters
        name (Union[Unset, str]): Name of a region. Wildcard ``%`` can be used to match zero, one, or multiple
            characters
        reservations_enabled (Union[Unset, bool]):
    """

    enabled: Union[Unset, bool] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    reservations_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        location = self.location
        name = self.name
        reservations_enabled = self.reservations_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if reservations_enabled is not UNSET:
            field_dict["reservations_enabled"] = reservations_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        enabled = d.pop("enabled", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        reservations_enabled = d.pop("reservations_enabled", UNSET)

        rhub_api_lab_location_location_region_list_filter = cls(
            enabled=enabled,
            location=location,
            name=name,
            reservations_enabled=reservations_enabled,
        )

        rhub_api_lab_location_location_region_list_filter.additional_properties = d
        return rhub_api_lab_location_location_region_list_filter

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

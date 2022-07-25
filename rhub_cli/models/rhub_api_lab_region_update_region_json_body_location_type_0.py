from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabRegionUpdateRegionJsonBodyLocationType0")


@attr.s(auto_attribs=True)
class RhubApiLabRegionUpdateRegionJsonBodyLocationType0:
    """
    Attributes:
        description (Union[Unset, None, str]): Long description of location, address, ... Example: Raleigh.
        id (Union[Unset, int]):
        name (Union[Unset, str]): Short name of location / IATA identifier / ... Example: RDU.
    """

    description: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        id = self.id
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

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rhub_api_lab_region_update_region_json_body_location_type_0 = cls(
            description=description,
            id=id,
            name=name,
        )

        rhub_api_lab_region_update_region_json_body_location_type_0.additional_properties = d
        return rhub_api_lab_region_update_region_json_body_location_type_0

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

from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabRegionAddRegionProductJsonBody")


@attr.s(auto_attribs=True)
class RhubApiLabRegionAddRegionProductJsonBody:
    """
    Attributes:
        id (int):
        enabled (Union[Unset, bool]):
    """

    id: int
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        id = d.pop("id")

        enabled = d.pop("enabled", UNSET)

        rhub_api_lab_region_add_region_product_json_body = cls(
            id=id,
            enabled=enabled,
        )

        rhub_api_lab_region_add_region_product_json_body.additional_properties = d
        return rhub_api_lab_region_add_region_product_json_body

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

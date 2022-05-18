from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region import (
    RhubApiLabProductListProductRegionsResponse200ItemRegion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabProductListProductRegionsResponse200Item")


@attr.s(auto_attribs=True)
class RhubApiLabProductListProductRegionsResponse200Item:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        product_id (Union[Unset, int]):
        region (Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegion]):
        region_id (Union[Unset, int]):
    """

    enabled: Union[Unset, bool] = UNSET
    product_id: Union[Unset, int] = UNSET
    region: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegion] = UNSET
    region_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        product_id = self.product_id
        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        region_id = self.region_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if region is not UNSET:
            field_dict["region"] = region
        if region_id is not UNSET:
            field_dict["region_id"] = region_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        enabled = d.pop("enabled", UNSET)

        product_id = d.pop("product_id", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = RhubApiLabProductListProductRegionsResponse200ItemRegion.from_dict(_region)

        region_id = d.pop("region_id", UNSET)

        rhub_api_lab_product_list_product_regions_response_200_item = cls(
            enabled=enabled,
            product_id=product_id,
            region=region,
            region_id=region_id,
        )

        rhub_api_lab_product_list_product_regions_response_200_item.additional_properties = d
        return rhub_api_lab_product_list_product_regions_response_200_item

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

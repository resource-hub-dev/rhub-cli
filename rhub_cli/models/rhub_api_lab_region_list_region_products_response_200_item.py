from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_lab_region_list_region_products_response_200_item_product import (
    RhubApiLabRegionListRegionProductsResponse200ItemProduct,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabRegionListRegionProductsResponse200Item")


@attr.s(auto_attribs=True)
class RhubApiLabRegionListRegionProductsResponse200Item:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        product (Union[Unset, RhubApiLabRegionListRegionProductsResponse200ItemProduct]):
        product_id (Union[Unset, int]):
        region_id (Union[Unset, int]):
    """

    enabled: Union[Unset, bool] = UNSET
    product: Union[Unset, RhubApiLabRegionListRegionProductsResponse200ItemProduct] = UNSET
    product_id: Union[Unset, int] = UNSET
    region_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        product_id = self.product_id
        region_id = self.region_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if product is not UNSET:
            field_dict["product"] = product
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if region_id is not UNSET:
            field_dict["region_id"] = region_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        enabled = d.pop("enabled", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, RhubApiLabRegionListRegionProductsResponse200ItemProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = RhubApiLabRegionListRegionProductsResponse200ItemProduct.from_dict(_product)

        product_id = d.pop("product_id", UNSET)

        region_id = d.pop("region_id", UNSET)

        rhub_api_lab_region_list_region_products_response_200_item = cls(
            enabled=enabled,
            product=product,
            product_id=product_id,
            region_id=region_id,
        )

        rhub_api_lab_region_list_region_products_response_200_item.additional_properties = d
        return rhub_api_lab_region_list_region_products_response_200_item

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

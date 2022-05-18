from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.rhub_api_lab_product_list_products_response_200_data_item_flavors_additional_property import (
    RhubApiLabProductListProductsResponse200DataItemFlavorsAdditionalProperty,
)

T = TypeVar("T", bound="RhubApiLabProductListProductsResponse200DataItemFlavors")


@attr.s(auto_attribs=True)
class RhubApiLabProductListProductsResponse200DataItemFlavors:
    """ """

    additional_properties: Dict[
        str, RhubApiLabProductListProductsResponse200DataItemFlavorsAdditionalProperty
    ] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        rhub_api_lab_product_list_products_response_200_data_item_flavors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RhubApiLabProductListProductsResponse200DataItemFlavorsAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        rhub_api_lab_product_list_products_response_200_data_item_flavors.additional_properties = additional_properties
        return rhub_api_lab_product_list_products_response_200_data_item_flavors

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RhubApiLabProductListProductsResponse200DataItemFlavorsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: RhubApiLabProductListProductsResponse200DataItemFlavorsAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

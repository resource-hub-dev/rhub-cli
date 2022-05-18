from copy import copy
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.rhub_api_lab_product_get_product_response_200_flavors_additional_property import (
    RhubApiLabProductGetProductResponse200FlavorsAdditionalProperty,
)

T = TypeVar("T", bound="RhubApiLabProductGetProductResponse200Flavors")


@attr.s(auto_attribs=True)
class RhubApiLabProductGetProductResponse200Flavors:
    """ """

    additional_properties: Dict[str, RhubApiLabProductGetProductResponse200FlavorsAdditionalProperty] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        rhub_api_lab_product_get_product_response_200_flavors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RhubApiLabProductGetProductResponse200FlavorsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        rhub_api_lab_product_get_product_response_200_flavors.additional_properties = additional_properties
        return rhub_api_lab_product_get_product_response_200_flavors

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RhubApiLabProductGetProductResponse200FlavorsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RhubApiLabProductGetProductResponse200FlavorsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

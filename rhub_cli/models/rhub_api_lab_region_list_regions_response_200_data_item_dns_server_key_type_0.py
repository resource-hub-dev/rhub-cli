from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabRegionListRegionsResponse200DataItemDnsServerKeyType0")


@attr.s(auto_attribs=True)
class RhubApiLabRegionListRegionsResponse200DataItemDnsServerKeyType0:
    """Credentials to store in Vault

    Attributes:
        name (Union[Unset, str]):
        secret (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        secret = self.secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        name = d.pop("name", UNSET)

        secret = d.pop("secret", UNSET)

        rhub_api_lab_region_list_regions_response_200_data_item_dns_server_key_type_0 = cls(
            name=name,
            secret=secret,
        )

        rhub_api_lab_region_list_regions_response_200_data_item_dns_server_key_type_0.additional_properties = d
        return rhub_api_lab_region_list_regions_response_200_data_item_dns_server_key_type_0

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

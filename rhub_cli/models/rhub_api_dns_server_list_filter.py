from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiDnsServerListFilter")


@attr.s(auto_attribs=True)
class RhubApiDnsServerListFilter:
    """
    Attributes:
        hostname (Union[Unset, str]): Hostname of a server. Wildcard ``%`` can be used to match zero, one, or multiple
            characters
    """

    hostname: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        hostname = d.pop("hostname", UNSET)

        rhub_api_dns_server_list_filter = cls(
            hostname=hostname,
        )

        rhub_api_dns_server_list_filter.additional_properties = d
        return rhub_api_dns_server_list_filter

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

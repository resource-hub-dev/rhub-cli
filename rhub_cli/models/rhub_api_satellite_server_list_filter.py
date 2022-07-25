from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiSatelliteServerListFilter")


@attr.s(auto_attribs=True)
class RhubApiSatelliteServerListFilter:
    """
    Attributes:
        hostname (Union[Unset, str]): Hostname of a server. Wildcard ``%`` can be used to match zero, one, or multiple
            characters
        owner_group_id (Union[Unset, None, str]):
    """

    hostname: Union[Unset, str] = UNSET
    owner_group_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname
        owner_group_id = self.owner_group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if owner_group_id is not UNSET:
            field_dict["owner_group_id"] = owner_group_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        hostname = d.pop("hostname", UNSET)

        owner_group_id = d.pop("owner_group_id", UNSET)

        rhub_api_satellite_server_list_filter = cls(
            hostname=hostname,
            owner_group_id=owner_group_id,
        )

        rhub_api_satellite_server_list_filter.additional_properties = d
        return rhub_api_satellite_server_list_filter

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

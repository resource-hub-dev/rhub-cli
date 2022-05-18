from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabClusterRebootHostsJsonBodyHostsType1Item")


@attr.s(auto_attribs=True)
class RhubApiLabClusterRebootHostsJsonBodyHostsType1Item:
    """
    Attributes:
        fqdn (Union[Unset, str]):
        id (Union[Unset, int]):
    """

    fqdn: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fqdn = self.fqdn
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        fqdn = d.pop("fqdn", UNSET)

        id = d.pop("id", UNSET)

        rhub_api_lab_cluster_reboot_hosts_json_body_hosts_type_1_item = cls(
            fqdn=fqdn,
            id=id,
        )

        rhub_api_lab_cluster_reboot_hosts_json_body_hosts_type_1_item.additional_properties = d
        return rhub_api_lab_cluster_reboot_hosts_json_body_hosts_type_1_item

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

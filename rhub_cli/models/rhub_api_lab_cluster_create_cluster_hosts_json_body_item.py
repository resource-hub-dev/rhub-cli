from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabClusterCreateClusterHostsJsonBodyItem")


@attr.s(auto_attribs=True)
class RhubApiLabClusterCreateClusterHostsJsonBodyItem:
    """
    Attributes:
        fqdn (str):
        ipaddr (List[str]):
        cluster_id (Union[Unset, int]):
        id (Union[Unset, int]):
        num_vcpus (Union[Unset, None, int]):
        num_volumes (Union[Unset, None, int]):
        ram_mb (Union[Unset, None, int]):
        volumes_gb (Union[Unset, None, int]):
    """

    fqdn: str
    ipaddr: List[str]
    cluster_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    num_vcpus: Union[Unset, None, int] = UNSET
    num_volumes: Union[Unset, None, int] = UNSET
    ram_mb: Union[Unset, None, int] = UNSET
    volumes_gb: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fqdn = self.fqdn
        ipaddr = []
        for ipaddr_item_data in self.ipaddr:

            ipaddr_item = ipaddr_item_data

            ipaddr.append(ipaddr_item)

        cluster_id = self.cluster_id
        id = self.id
        num_vcpus = self.num_vcpus
        num_volumes = self.num_volumes
        ram_mb = self.ram_mb
        volumes_gb = self.volumes_gb

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fqdn": fqdn,
                "ipaddr": ipaddr,
            }
        )
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if id is not UNSET:
            field_dict["id"] = id
        if num_vcpus is not UNSET:
            field_dict["num_vcpus"] = num_vcpus
        if num_volumes is not UNSET:
            field_dict["num_volumes"] = num_volumes
        if ram_mb is not UNSET:
            field_dict["ram_mb"] = ram_mb
        if volumes_gb is not UNSET:
            field_dict["volumes_gb"] = volumes_gb

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        fqdn = d.pop("fqdn")

        ipaddr = []
        _ipaddr = d.pop("ipaddr")
        for ipaddr_item_data in _ipaddr:

            def _parse_ipaddr_item(data: object) -> str:
                return cast(str, data)

            ipaddr_item = _parse_ipaddr_item(ipaddr_item_data)

            ipaddr.append(ipaddr_item)

        cluster_id = d.pop("cluster_id", UNSET)

        id = d.pop("id", UNSET)

        num_vcpus = d.pop("num_vcpus", UNSET)

        num_volumes = d.pop("num_volumes", UNSET)

        ram_mb = d.pop("ram_mb", UNSET)

        volumes_gb = d.pop("volumes_gb", UNSET)

        rhub_api_lab_cluster_create_cluster_hosts_json_body_item = cls(
            fqdn=fqdn,
            ipaddr=ipaddr,
            cluster_id=cluster_id,
            id=id,
            num_vcpus=num_vcpus,
            num_volumes=num_volumes,
            ram_mb=ram_mb,
            volumes_gb=volumes_gb,
        )

        rhub_api_lab_cluster_create_cluster_hosts_json_body_item.additional_properties = d
        return rhub_api_lab_cluster_create_cluster_hosts_json_body_item

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

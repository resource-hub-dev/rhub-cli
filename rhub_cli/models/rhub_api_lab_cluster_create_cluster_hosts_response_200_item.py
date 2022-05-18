from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_lab_cluster_create_cluster_hosts_response_200_item_cluster_id import (
    RhubApiLabClusterCreateClusterHostsResponse200ItemClusterId,
)
from ..models.rhub_api_lab_cluster_create_cluster_hosts_response_200_item_id import (
    RhubApiLabClusterCreateClusterHostsResponse200ItemId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabClusterCreateClusterHostsResponse200Item")


@attr.s(auto_attribs=True)
class RhubApiLabClusterCreateClusterHostsResponse200Item:
    """
    Attributes:
        cluster_id (Union[Unset, RhubApiLabClusterCreateClusterHostsResponse200ItemClusterId]):
        fqdn (Union[Unset, str]):
        id (Union[Unset, RhubApiLabClusterCreateClusterHostsResponse200ItemId]):
        ipaddr (Union[Unset, List[str]]):
        num_vcpus (Union[Unset, None, int]):
        num_volumes (Union[Unset, None, int]):
        ram_mb (Union[Unset, None, int]):
        volumes_gb (Union[Unset, None, int]):
    """

    cluster_id: Union[Unset, RhubApiLabClusterCreateClusterHostsResponse200ItemClusterId] = UNSET
    fqdn: Union[Unset, str] = UNSET
    id: Union[Unset, RhubApiLabClusterCreateClusterHostsResponse200ItemId] = UNSET
    ipaddr: Union[Unset, List[str]] = UNSET
    num_vcpus: Union[Unset, None, int] = UNSET
    num_volumes: Union[Unset, None, int] = UNSET
    ram_mb: Union[Unset, None, int] = UNSET
    volumes_gb: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_id, Unset):
            cluster_id = self.cluster_id.to_dict()

        fqdn = self.fqdn
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        ipaddr: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ipaddr, Unset):
            ipaddr = []
            for ipaddr_item_data in self.ipaddr:

                ipaddr_item = ipaddr_item_data

                ipaddr.append(ipaddr_item)

        num_vcpus = self.num_vcpus
        num_volumes = self.num_volumes
        ram_mb = self.ram_mb
        volumes_gb = self.volumes_gb

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if id is not UNSET:
            field_dict["id"] = id
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
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
        _cluster_id = d.pop("cluster_id", UNSET)
        cluster_id: Union[Unset, RhubApiLabClusterCreateClusterHostsResponse200ItemClusterId]
        if isinstance(_cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = RhubApiLabClusterCreateClusterHostsResponse200ItemClusterId.from_dict(_cluster_id)

        fqdn = d.pop("fqdn", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiLabClusterCreateClusterHostsResponse200ItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiLabClusterCreateClusterHostsResponse200ItemId.from_dict(_id)

        ipaddr = []
        _ipaddr = d.pop("ipaddr", UNSET)
        for ipaddr_item_data in _ipaddr or []:

            def _parse_ipaddr_item(data: object) -> str:
                return cast(str, data)

            ipaddr_item = _parse_ipaddr_item(ipaddr_item_data)

            ipaddr.append(ipaddr_item)

        num_vcpus = d.pop("num_vcpus", UNSET)

        num_volumes = d.pop("num_volumes", UNSET)

        ram_mb = d.pop("ram_mb", UNSET)

        volumes_gb = d.pop("volumes_gb", UNSET)

        rhub_api_lab_cluster_create_cluster_hosts_response_200_item = cls(
            cluster_id=cluster_id,
            fqdn=fqdn,
            id=id,
            ipaddr=ipaddr,
            num_vcpus=num_vcpus,
            num_volumes=num_volumes,
            ram_mb=ram_mb,
            volumes_gb=volumes_gb,
        )

        rhub_api_lab_cluster_create_cluster_hosts_response_200_item.additional_properties = d
        return rhub_api_lab_cluster_create_cluster_hosts_response_200_item

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

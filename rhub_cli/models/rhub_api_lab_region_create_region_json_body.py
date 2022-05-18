from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_lab_region_create_region_json_body_id import RhubApiLabRegionCreateRegionJsonBodyId
from ..models.rhub_api_lab_region_create_region_json_body_location_type_0 import (
    RhubApiLabRegionCreateRegionJsonBodyLocationType0,
)
from ..models.rhub_api_lab_region_create_region_json_body_total_quota_type_0 import (
    RhubApiLabRegionCreateRegionJsonBodyTotalQuotaType0,
)
from ..models.rhub_api_lab_region_create_region_json_body_user_quota_type_0 import (
    RhubApiLabRegionCreateRegionJsonBodyUserQuotaType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabRegionCreateRegionJsonBody")


@attr.s(auto_attribs=True)
class RhubApiLabRegionCreateRegionJsonBody:
    """
    Attributes:
        dns_server (Any):
        download_server (str):  Example: https://download.example.com.
        name (str):  Example: rdu2-a.
        openstack (Any):
        satellite (Any):
        tower_id (int):
        vault_server (str):  Example: https://vault.example.com.
        banner (Union[Unset, str]):
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        id (Union[Unset, RhubApiLabRegionCreateRegionJsonBodyId]):
        lifespan_length (Union[Unset, None, int]):
        location (Union[Any, RhubApiLabRegionCreateRegionJsonBodyLocationType0, Unset]):
        location_id (Union[Any, Unset, int]):
        owner_group (Union[Unset, str]):  Example: 7670ac07-cb21-448d-af8a-6e3882216be3.
        owner_group_name (Union[Unset, None, str]):
        reservation_expiration_max (Union[Unset, None, int]):
        reservations_enabled (Union[Unset, bool]):
        total_quota (Union[Any, RhubApiLabRegionCreateRegionJsonBodyTotalQuotaType0, Unset]):  Example: {'num_vcpus':
            40000, 'num_volumes': 40000, 'ram_mb': 200000000, 'volumes_gb': 540000}.
        user_quota (Union[Any, RhubApiLabRegionCreateRegionJsonBodyUserQuotaType0, Unset]):  Example: {'num_vcpus': 40,
            'num_volumes': 40, 'ram_mb': 200000, 'volumes_gb': 540}.
        users_group (Union[Unset, None, str]):
        users_group_name (Union[Unset, None, str]):
    """

    dns_server: Any
    download_server: str
    name: str
    openstack: Any
    satellite: Any
    tower_id: int
    vault_server: str
    banner: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, RhubApiLabRegionCreateRegionJsonBodyId] = UNSET
    lifespan_length: Union[Unset, None, int] = UNSET
    location: Union[Any, RhubApiLabRegionCreateRegionJsonBodyLocationType0, Unset] = UNSET
    location_id: Union[Any, Unset, int] = UNSET
    owner_group: Union[Unset, str] = UNSET
    owner_group_name: Union[Unset, None, str] = UNSET
    reservation_expiration_max: Union[Unset, None, int] = UNSET
    reservations_enabled: Union[Unset, bool] = UNSET
    total_quota: Union[Any, RhubApiLabRegionCreateRegionJsonBodyTotalQuotaType0, Unset] = UNSET
    user_quota: Union[Any, RhubApiLabRegionCreateRegionJsonBodyUserQuotaType0, Unset] = UNSET
    users_group: Union[Unset, None, str] = UNSET
    users_group_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dns_server = self.dns_server
        download_server = self.download_server
        name = self.name
        openstack = self.openstack
        satellite = self.satellite
        tower_id = self.tower_id
        vault_server = self.vault_server
        banner = self.banner
        description = self.description
        enabled = self.enabled
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        lifespan_length = self.lifespan_length
        location: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.location, Unset):
            location = UNSET

        elif isinstance(self.location, RhubApiLabRegionCreateRegionJsonBodyLocationType0):
            location = UNSET
            if not isinstance(self.location, Unset):
                location = self.location.to_dict()

        else:
            location = self.location

        location_id: Union[Any, Unset, int]
        if isinstance(self.location_id, Unset):
            location_id = UNSET

        else:
            location_id = self.location_id

        owner_group = self.owner_group
        owner_group_name = self.owner_group_name
        reservation_expiration_max = self.reservation_expiration_max
        reservations_enabled = self.reservations_enabled
        total_quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.total_quota, Unset):
            total_quota = UNSET

        elif isinstance(self.total_quota, RhubApiLabRegionCreateRegionJsonBodyTotalQuotaType0):
            total_quota = UNSET
            if not isinstance(self.total_quota, Unset):
                total_quota = self.total_quota.to_dict()

        else:
            total_quota = self.total_quota

        user_quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.user_quota, Unset):
            user_quota = UNSET

        elif isinstance(self.user_quota, RhubApiLabRegionCreateRegionJsonBodyUserQuotaType0):
            user_quota = UNSET
            if not isinstance(self.user_quota, Unset):
                user_quota = self.user_quota.to_dict()

        else:
            user_quota = self.user_quota

        users_group = self.users_group
        users_group_name = self.users_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dns_server": dns_server,
                "download_server": download_server,
                "name": name,
                "openstack": openstack,
                "satellite": satellite,
                "tower_id": tower_id,
                "vault_server": vault_server,
            }
        )
        if banner is not UNSET:
            field_dict["banner"] = banner
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if lifespan_length is not UNSET:
            field_dict["lifespan_length"] = lifespan_length
        if location is not UNSET:
            field_dict["location"] = location
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if owner_group is not UNSET:
            field_dict["owner_group"] = owner_group
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name
        if reservation_expiration_max is not UNSET:
            field_dict["reservation_expiration_max"] = reservation_expiration_max
        if reservations_enabled is not UNSET:
            field_dict["reservations_enabled"] = reservations_enabled
        if total_quota is not UNSET:
            field_dict["total_quota"] = total_quota
        if user_quota is not UNSET:
            field_dict["user_quota"] = user_quota
        if users_group is not UNSET:
            field_dict["users_group"] = users_group
        if users_group_name is not UNSET:
            field_dict["users_group_name"] = users_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        dns_server = d.pop("dns_server")

        download_server = d.pop("download_server")

        name = d.pop("name")

        openstack = d.pop("openstack")

        satellite = d.pop("satellite")

        tower_id = d.pop("tower_id")

        vault_server = d.pop("vault_server")

        banner = d.pop("banner", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiLabRegionCreateRegionJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiLabRegionCreateRegionJsonBodyId.from_dict(_id)

        lifespan_length = d.pop("lifespan_length", UNSET)

        def _parse_location(data: object) -> Union[Any, RhubApiLabRegionCreateRegionJsonBodyLocationType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _location_type_0 = data
                location_type_0: Union[Unset, RhubApiLabRegionCreateRegionJsonBodyLocationType0]
                if isinstance(_location_type_0, Unset):
                    location_type_0 = UNSET
                else:
                    location_type_0 = RhubApiLabRegionCreateRegionJsonBodyLocationType0.from_dict(_location_type_0)

                return location_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiLabRegionCreateRegionJsonBodyLocationType0, Unset], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_location_id(data: object) -> Union[Any, Unset, int]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, Unset, int], data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        owner_group = d.pop("owner_group", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        reservation_expiration_max = d.pop("reservation_expiration_max", UNSET)

        reservations_enabled = d.pop("reservations_enabled", UNSET)

        def _parse_total_quota(data: object) -> Union[Any, RhubApiLabRegionCreateRegionJsonBodyTotalQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _total_quota_type_0 = data
                total_quota_type_0: Union[Unset, RhubApiLabRegionCreateRegionJsonBodyTotalQuotaType0]
                if isinstance(_total_quota_type_0, Unset):
                    total_quota_type_0 = UNSET
                else:
                    total_quota_type_0 = RhubApiLabRegionCreateRegionJsonBodyTotalQuotaType0.from_dict(
                        _total_quota_type_0
                    )

                return total_quota_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiLabRegionCreateRegionJsonBodyTotalQuotaType0, Unset], data)

        total_quota = _parse_total_quota(d.pop("total_quota", UNSET))

        def _parse_user_quota(data: object) -> Union[Any, RhubApiLabRegionCreateRegionJsonBodyUserQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _user_quota_type_0 = data
                user_quota_type_0: Union[Unset, RhubApiLabRegionCreateRegionJsonBodyUserQuotaType0]
                if isinstance(_user_quota_type_0, Unset):
                    user_quota_type_0 = UNSET
                else:
                    user_quota_type_0 = RhubApiLabRegionCreateRegionJsonBodyUserQuotaType0.from_dict(_user_quota_type_0)

                return user_quota_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiLabRegionCreateRegionJsonBodyUserQuotaType0, Unset], data)

        user_quota = _parse_user_quota(d.pop("user_quota", UNSET))

        users_group = d.pop("users_group", UNSET)

        users_group_name = d.pop("users_group_name", UNSET)

        rhub_api_lab_region_create_region_json_body = cls(
            dns_server=dns_server,
            download_server=download_server,
            name=name,
            openstack=openstack,
            satellite=satellite,
            tower_id=tower_id,
            vault_server=vault_server,
            banner=banner,
            description=description,
            enabled=enabled,
            id=id,
            lifespan_length=lifespan_length,
            location=location,
            location_id=location_id,
            owner_group=owner_group,
            owner_group_name=owner_group_name,
            reservation_expiration_max=reservation_expiration_max,
            reservations_enabled=reservations_enabled,
            total_quota=total_quota,
            user_quota=user_quota,
            users_group=users_group,
            users_group_name=users_group_name,
        )

        rhub_api_lab_region_create_region_json_body.additional_properties = d
        return rhub_api_lab_region_create_region_json_body

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

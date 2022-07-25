from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_location_type_0 import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionLocationType0,
)
from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_openstack import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack,
)
from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_satellite_type_0 import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteType0,
)
from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_total_quota_type_0 import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuotaType0,
)
from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_user_quota_type_0 import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuotaType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabProductListProductRegionsResponse200ItemRegion")


@attr.s(auto_attribs=True)
class RhubApiLabProductListProductRegionsResponse200ItemRegion:
    """
    Attributes:
        banner (Union[Unset, str]):
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        id (Union[Unset, int]):
        lifespan_length (Union[Unset, None, int]):
        location (Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionLocationType0, Unset]):
        location_id (Union[Any, Unset, int]):
        name (Union[Unset, str]):  Example: rdu2-a.
        openstack (Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack]):
        openstack_id (Union[Unset, int]):
        openstack_keyname (Union[Unset, str]): SSH key name
        owner_group_id (Union[Unset, str]):  Example: 7670ac07-cb21-448d-af8a-6e3882216be3.
        owner_group_name (Union[Unset, None, str]):
        reservation_expiration_max (Union[Unset, None, int]):
        reservations_enabled (Union[Unset, bool]):
        satellite (Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteType0, Unset]):
        satellite_id (Union[Any, Unset, int]):
        total_quota (Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuotaType0, Unset]):
            Example: {'num_vcpus': 40000, 'num_volumes': 40000, 'ram_mb': 200000000, 'volumes_gb': 540000}.
        tower_id (Union[Unset, int]):
        user_quota (Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuotaType0, Unset]):
            Example: {'num_vcpus': 40, 'num_volumes': 40, 'ram_mb': 200000, 'volumes_gb': 540}.
        users_group_id (Union[Unset, None, str]):
        users_group_name (Union[Unset, None, str]):
    """

    banner: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    lifespan_length: Union[Unset, None, int] = UNSET
    location: Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionLocationType0, Unset] = UNSET
    location_id: Union[Any, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    openstack: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack] = UNSET
    openstack_id: Union[Unset, int] = UNSET
    openstack_keyname: Union[Unset, str] = UNSET
    owner_group_id: Union[Unset, str] = UNSET
    owner_group_name: Union[Unset, None, str] = UNSET
    reservation_expiration_max: Union[Unset, None, int] = UNSET
    reservations_enabled: Union[Unset, bool] = UNSET
    satellite: Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteType0, Unset] = UNSET
    satellite_id: Union[Any, Unset, int] = UNSET
    total_quota: Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuotaType0, Unset] = UNSET
    tower_id: Union[Unset, int] = UNSET
    user_quota: Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuotaType0, Unset] = UNSET
    users_group_id: Union[Unset, None, str] = UNSET
    users_group_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        banner = self.banner
        description = self.description
        enabled = self.enabled
        id = self.id
        lifespan_length = self.lifespan_length
        location: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.location, Unset):
            location = UNSET

        elif isinstance(self.location, RhubApiLabProductListProductRegionsResponse200ItemRegionLocationType0):
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

        name = self.name
        openstack: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.openstack, Unset):
            openstack = self.openstack.to_dict()

        openstack_id = self.openstack_id
        openstack_keyname = self.openstack_keyname
        owner_group_id = self.owner_group_id
        owner_group_name = self.owner_group_name
        reservation_expiration_max = self.reservation_expiration_max
        reservations_enabled = self.reservations_enabled
        satellite: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.satellite, Unset):
            satellite = UNSET

        elif isinstance(self.satellite, RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteType0):
            satellite = UNSET
            if not isinstance(self.satellite, Unset):
                satellite = self.satellite.to_dict()

        else:
            satellite = self.satellite

        satellite_id: Union[Any, Unset, int]
        if isinstance(self.satellite_id, Unset):
            satellite_id = UNSET

        else:
            satellite_id = self.satellite_id

        total_quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.total_quota, Unset):
            total_quota = UNSET

        elif isinstance(self.total_quota, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuotaType0):
            total_quota = UNSET
            if not isinstance(self.total_quota, Unset):
                total_quota = self.total_quota.to_dict()

        else:
            total_quota = self.total_quota

        tower_id = self.tower_id
        user_quota: Union[Any, Dict[str, Any], Unset]
        if isinstance(self.user_quota, Unset):
            user_quota = UNSET

        elif isinstance(self.user_quota, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuotaType0):
            user_quota = UNSET
            if not isinstance(self.user_quota, Unset):
                user_quota = self.user_quota.to_dict()

        else:
            user_quota = self.user_quota

        users_group_id = self.users_group_id
        users_group_name = self.users_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if name is not UNSET:
            field_dict["name"] = name
        if openstack is not UNSET:
            field_dict["openstack"] = openstack
        if openstack_id is not UNSET:
            field_dict["openstack_id"] = openstack_id
        if openstack_keyname is not UNSET:
            field_dict["openstack_keyname"] = openstack_keyname
        if owner_group_id is not UNSET:
            field_dict["owner_group_id"] = owner_group_id
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name
        if reservation_expiration_max is not UNSET:
            field_dict["reservation_expiration_max"] = reservation_expiration_max
        if reservations_enabled is not UNSET:
            field_dict["reservations_enabled"] = reservations_enabled
        if satellite is not UNSET:
            field_dict["satellite"] = satellite
        if satellite_id is not UNSET:
            field_dict["satellite_id"] = satellite_id
        if total_quota is not UNSET:
            field_dict["total_quota"] = total_quota
        if tower_id is not UNSET:
            field_dict["tower_id"] = tower_id
        if user_quota is not UNSET:
            field_dict["user_quota"] = user_quota
        if users_group_id is not UNSET:
            field_dict["users_group_id"] = users_group_id
        if users_group_name is not UNSET:
            field_dict["users_group_name"] = users_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        banner = d.pop("banner", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        lifespan_length = d.pop("lifespan_length", UNSET)

        def _parse_location(
            data: object,
        ) -> Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionLocationType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _location_type_0 = data
                location_type_0: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionLocationType0]
                if isinstance(_location_type_0, Unset):
                    location_type_0 = UNSET
                else:
                    location_type_0 = RhubApiLabProductListProductRegionsResponse200ItemRegionLocationType0.from_dict(
                        _location_type_0
                    )

                return location_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionLocationType0, Unset], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_location_id(data: object) -> Union[Any, Unset, int]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, Unset, int], data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        name = d.pop("name", UNSET)

        _openstack = d.pop("openstack", UNSET)
        openstack: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack]
        if isinstance(_openstack, Unset):
            openstack = UNSET
        else:
            openstack = RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack.from_dict(_openstack)

        openstack_id = d.pop("openstack_id", UNSET)

        openstack_keyname = d.pop("openstack_keyname", UNSET)

        owner_group_id = d.pop("owner_group_id", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        reservation_expiration_max = d.pop("reservation_expiration_max", UNSET)

        reservations_enabled = d.pop("reservations_enabled", UNSET)

        def _parse_satellite(
            data: object,
        ) -> Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _satellite_type_0 = data
                satellite_type_0: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteType0]
                if isinstance(_satellite_type_0, Unset):
                    satellite_type_0 = UNSET
                else:
                    satellite_type_0 = RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteType0.from_dict(
                        _satellite_type_0
                    )

                return satellite_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteType0, Unset], data)

        satellite = _parse_satellite(d.pop("satellite", UNSET))

        def _parse_satellite_id(data: object) -> Union[Any, Unset, int]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, Unset, int], data)

        satellite_id = _parse_satellite_id(d.pop("satellite_id", UNSET))

        def _parse_total_quota(
            data: object,
        ) -> Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _total_quota_type_0 = data
                total_quota_type_0: Union[
                    Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuotaType0
                ]
                if isinstance(_total_quota_type_0, Unset):
                    total_quota_type_0 = UNSET
                else:
                    total_quota_type_0 = (
                        RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuotaType0.from_dict(
                            _total_quota_type_0
                        )
                    )

                return total_quota_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionTotalQuotaType0, Unset], data
            )

        total_quota = _parse_total_quota(d.pop("total_quota", UNSET))

        tower_id = d.pop("tower_id", UNSET)

        def _parse_user_quota(
            data: object,
        ) -> Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuotaType0, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _user_quota_type_0 = data
                user_quota_type_0: Union[Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuotaType0]
                if isinstance(_user_quota_type_0, Unset):
                    user_quota_type_0 = UNSET
                else:
                    user_quota_type_0 = (
                        RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuotaType0.from_dict(
                            _user_quota_type_0
                        )
                    )

                return user_quota_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Any, RhubApiLabProductListProductRegionsResponse200ItemRegionUserQuotaType0, Unset], data)

        user_quota = _parse_user_quota(d.pop("user_quota", UNSET))

        users_group_id = d.pop("users_group_id", UNSET)

        users_group_name = d.pop("users_group_name", UNSET)

        rhub_api_lab_product_list_product_regions_response_200_item_region = cls(
            banner=banner,
            description=description,
            enabled=enabled,
            id=id,
            lifespan_length=lifespan_length,
            location=location,
            location_id=location_id,
            name=name,
            openstack=openstack,
            openstack_id=openstack_id,
            openstack_keyname=openstack_keyname,
            owner_group_id=owner_group_id,
            owner_group_name=owner_group_name,
            reservation_expiration_max=reservation_expiration_max,
            reservations_enabled=reservations_enabled,
            satellite=satellite,
            satellite_id=satellite_id,
            total_quota=total_quota,
            tower_id=tower_id,
            user_quota=user_quota,
            users_group_id=users_group_id,
            users_group_name=users_group_name,
        )

        rhub_api_lab_product_list_product_regions_response_200_item_region.additional_properties = d
        return rhub_api_lab_product_list_product_regions_response_200_item_region

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

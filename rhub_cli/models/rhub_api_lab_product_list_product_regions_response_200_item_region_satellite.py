from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_satellite_credentials_type_0 import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteCredentialsType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabProductListProductRegionsResponse200ItemRegionSatellite")


@attr.s(auto_attribs=True)
class RhubApiLabProductListProductRegionsResponse200ItemRegionSatellite:
    """
    Example:
        {'credentials': 'kv/region/rdu2-a/satellite', 'hostname': 'satellite.example.com', 'insecure': False}

    Attributes:
        credentials (Union[RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteCredentialsType0, Unset,
            str]):
        hostname (Union[Unset, str]):
        insecure (Union[Unset, bool]):
    """

    credentials: Union[
        RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteCredentialsType0, Unset, str
    ] = UNSET
    hostname: Union[Unset, str] = UNSET
    insecure: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Dict[str, Any], Unset, str]
        if isinstance(self.credentials, Unset):
            credentials = UNSET

        elif isinstance(
            self.credentials, RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteCredentialsType0
        ):
            credentials = UNSET
            if not isinstance(self.credentials, Unset):
                credentials = self.credentials.to_dict()

        else:
            credentials = self.credentials

        hostname = self.hostname
        insecure = self.insecure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if insecure is not UNSET:
            field_dict["insecure"] = insecure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)

        def _parse_credentials(
            data: object,
        ) -> Union[RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteCredentialsType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _credentials_type_0 = data
                credentials_type_0: Union[
                    Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteCredentialsType0
                ]
                if isinstance(_credentials_type_0, Unset):
                    credentials_type_0 = UNSET
                else:
                    credentials_type_0 = (
                        RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteCredentialsType0.from_dict(
                            _credentials_type_0
                        )
                    )

                return credentials_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[RhubApiLabProductListProductRegionsResponse200ItemRegionSatelliteCredentialsType0, Unset, str],
                data,
            )

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        hostname = d.pop("hostname", UNSET)

        insecure = d.pop("insecure", UNSET)

        rhub_api_lab_product_list_product_regions_response_200_item_region_satellite = cls(
            credentials=credentials,
            hostname=hostname,
            insecure=insecure,
        )

        rhub_api_lab_product_list_product_regions_response_200_item_region_satellite.additional_properties = d
        return rhub_api_lab_product_list_product_regions_response_200_item_region_satellite

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

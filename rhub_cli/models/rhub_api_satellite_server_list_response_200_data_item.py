from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_satellite_server_list_response_200_data_item_credentials_type_0 import (
    RhubApiSatelliteServerListResponse200DataItemCredentialsType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiSatelliteServerListResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiSatelliteServerListResponse200DataItem:
    """
    Attributes:
        credentials (Union[RhubApiSatelliteServerListResponse200DataItemCredentialsType0, Unset, str]):
        description (Union[Unset, None, str]):  Example: Satellite server for RDU site..
        hostname (Union[Unset, str]):
        id (Union[Unset, int]):
        insecure (Union[Unset, bool]):
        name (Union[Unset, str]):  Example: satellite-rdu.
        owner_group_id (Union[Unset, str]):
        owner_group_name (Union[Unset, str]):
    """

    credentials: Union[RhubApiSatelliteServerListResponse200DataItemCredentialsType0, Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    insecure: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    owner_group_id: Union[Unset, str] = UNSET
    owner_group_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Dict[str, Any], Unset, str]
        if isinstance(self.credentials, Unset):
            credentials = UNSET

        elif isinstance(self.credentials, RhubApiSatelliteServerListResponse200DataItemCredentialsType0):
            credentials = UNSET
            if not isinstance(self.credentials, Unset):
                credentials = self.credentials.to_dict()

        else:
            credentials = self.credentials

        description = self.description
        hostname = self.hostname
        id = self.id
        insecure = self.insecure
        name = self.name
        owner_group_id = self.owner_group_id
        owner_group_name = self.owner_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if description is not UNSET:
            field_dict["description"] = description
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if insecure is not UNSET:
            field_dict["insecure"] = insecure
        if name is not UNSET:
            field_dict["name"] = name
        if owner_group_id is not UNSET:
            field_dict["owner_group_id"] = owner_group_id
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)

        def _parse_credentials(
            data: object,
        ) -> Union[RhubApiSatelliteServerListResponse200DataItemCredentialsType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _credentials_type_0 = data
                credentials_type_0: Union[Unset, RhubApiSatelliteServerListResponse200DataItemCredentialsType0]
                if isinstance(_credentials_type_0, Unset):
                    credentials_type_0 = UNSET
                else:
                    credentials_type_0 = RhubApiSatelliteServerListResponse200DataItemCredentialsType0.from_dict(
                        _credentials_type_0
                    )

                return credentials_type_0
            except:  # noqa: E722
                pass
            return cast(Union[RhubApiSatelliteServerListResponse200DataItemCredentialsType0, Unset, str], data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        description = d.pop("description", UNSET)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        insecure = d.pop("insecure", UNSET)

        name = d.pop("name", UNSET)

        owner_group_id = d.pop("owner_group_id", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        rhub_api_satellite_server_list_response_200_data_item = cls(
            credentials=credentials,
            description=description,
            hostname=hostname,
            id=id,
            insecure=insecure,
            name=name,
            owner_group_id=owner_group_id,
            owner_group_name=owner_group_name,
        )

        rhub_api_satellite_server_list_response_200_data_item.additional_properties = d
        return rhub_api_satellite_server_list_response_200_data_item

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

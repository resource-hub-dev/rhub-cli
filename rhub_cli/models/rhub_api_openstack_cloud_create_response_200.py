from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_openstack_cloud_create_response_200_credentials_type_0 import (
    RhubApiOpenstackCloudCreateResponse200CredentialsType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackCloudCreateResponse200")


@attr.s(auto_attribs=True)
class RhubApiOpenstackCloudCreateResponse200:
    """
    Attributes:
        credentials (Union[RhubApiOpenstackCloudCreateResponse200CredentialsType0, Unset, str]):  Example:
            kv/openstack/rhub-rdu.
        description (Union[Unset, None, str]):  Example: Private cloud for RHub located in RDU..
        domain_id (Union[Unset, str]):  Example: default.
        domain_name (Union[Unset, str]):  Example: Default.
        id (Union[Unset, int]):
        name (Union[Unset, str]):  Example: rhub-rdu.
        networks (Union[Unset, List[str]]): Network providers that can be used in the cloud Example:
            ['provider_net_rhub'].
        owner_group_id (Union[Unset, str]):
        owner_group_name (Union[Unset, str]):
        url (Union[Unset, str]):  Example: https://rhub-cloud.rdu.example.com:13000.
    """

    credentials: Union[RhubApiOpenstackCloudCreateResponse200CredentialsType0, Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    domain_id: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    networks: Union[Unset, List[str]] = UNSET
    owner_group_id: Union[Unset, str] = UNSET
    owner_group_name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Dict[str, Any], Unset, str]
        if isinstance(self.credentials, Unset):
            credentials = UNSET

        elif isinstance(self.credentials, RhubApiOpenstackCloudCreateResponse200CredentialsType0):
            credentials = UNSET
            if not isinstance(self.credentials, Unset):
                credentials = self.credentials.to_dict()

        else:
            credentials = self.credentials

        description = self.description
        domain_id = self.domain_id
        domain_name = self.domain_name
        id = self.id
        name = self.name
        networks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = self.networks

        owner_group_id = self.owner_group_id
        owner_group_name = self.owner_group_name
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if description is not UNSET:
            field_dict["description"] = description
        if domain_id is not UNSET:
            field_dict["domain_id"] = domain_id
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if networks is not UNSET:
            field_dict["networks"] = networks
        if owner_group_id is not UNSET:
            field_dict["owner_group_id"] = owner_group_id
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)

        def _parse_credentials(
            data: object,
        ) -> Union[RhubApiOpenstackCloudCreateResponse200CredentialsType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _credentials_type_0 = data
                credentials_type_0: Union[Unset, RhubApiOpenstackCloudCreateResponse200CredentialsType0]
                if isinstance(_credentials_type_0, Unset):
                    credentials_type_0 = UNSET
                else:
                    credentials_type_0 = RhubApiOpenstackCloudCreateResponse200CredentialsType0.from_dict(
                        _credentials_type_0
                    )

                return credentials_type_0
            except:  # noqa: E722
                pass
            return cast(Union[RhubApiOpenstackCloudCreateResponse200CredentialsType0, Unset, str], data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        description = d.pop("description", UNSET)

        domain_id = d.pop("domain_id", UNSET)

        domain_name = d.pop("domain_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        networks = cast(List[str], d.pop("networks", UNSET))

        owner_group_id = d.pop("owner_group_id", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        url = d.pop("url", UNSET)

        rhub_api_openstack_cloud_create_response_200 = cls(
            credentials=credentials,
            description=description,
            domain_id=domain_id,
            domain_name=domain_name,
            id=id,
            name=name,
            networks=networks,
            owner_group_id=owner_group_id,
            owner_group_name=owner_group_name,
            url=url,
        )

        rhub_api_openstack_cloud_create_response_200.additional_properties = d
        return rhub_api_openstack_cloud_create_response_200

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

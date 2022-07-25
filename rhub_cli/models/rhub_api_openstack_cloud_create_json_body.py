from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_openstack_cloud_create_json_body_credentials_type_0 import (
    RhubApiOpenstackCloudCreateJsonBodyCredentialsType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackCloudCreateJsonBody")


@attr.s(auto_attribs=True)
class RhubApiOpenstackCloudCreateJsonBody:
    """
    Attributes:
        credentials (Union[RhubApiOpenstackCloudCreateJsonBodyCredentialsType0, str]):  Example: kv/openstack/rhub-rdu.
        domain_id (str):  Example: default.
        domain_name (str):  Example: Default.
        name (str):  Example: rhub-rdu.
        networks (List[str]): Network providers that can be used in the cloud Example: ['provider_net_rhub'].
        owner_group_id (str):
        url (str):  Example: https://rhub-cloud.rdu.example.com:13000.
        description (Union[Unset, None, str]):  Example: Private cloud for RHub located in RDU..
        id (Union[Unset, int]):
        owner_group_name (Union[Unset, str]):
    """

    credentials: Union[RhubApiOpenstackCloudCreateJsonBodyCredentialsType0, str]
    domain_id: str
    domain_name: str
    name: str
    networks: List[str]
    owner_group_id: str
    url: str
    description: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    owner_group_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        if isinstance(self.credentials, RhubApiOpenstackCloudCreateJsonBodyCredentialsType0):
            credentials = self.credentials.to_dict()

        else:
            credentials = self.credentials

        domain_id = self.domain_id
        domain_name = self.domain_name
        name = self.name
        networks = self.networks

        owner_group_id = self.owner_group_id
        url = self.url
        description = self.description
        id = self.id
        owner_group_name = self.owner_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "domain_id": domain_id,
                "domain_name": domain_name,
                "name": name,
                "networks": networks,
                "owner_group_id": owner_group_id,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if owner_group_name is not UNSET:
            field_dict["owner_group_name"] = owner_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)

        def _parse_credentials(data: object) -> Union[RhubApiOpenstackCloudCreateJsonBodyCredentialsType0, str]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = RhubApiOpenstackCloudCreateJsonBodyCredentialsType0.from_dict(data)

                return credentials_type_0
            except:  # noqa: E722
                pass
            return cast(Union[RhubApiOpenstackCloudCreateJsonBodyCredentialsType0, str], data)

        credentials = _parse_credentials(d.pop("credentials"))

        domain_id = d.pop("domain_id")

        domain_name = d.pop("domain_name")

        name = d.pop("name")

        networks = cast(List[str], d.pop("networks"))

        owner_group_id = d.pop("owner_group_id")

        url = d.pop("url")

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        owner_group_name = d.pop("owner_group_name", UNSET)

        rhub_api_openstack_cloud_create_json_body = cls(
            credentials=credentials,
            domain_id=domain_id,
            domain_name=domain_name,
            name=name,
            networks=networks,
            owner_group_id=owner_group_id,
            url=url,
            description=description,
            id=id,
            owner_group_name=owner_group_name,
        )

        rhub_api_openstack_cloud_create_json_body.additional_properties = d
        return rhub_api_openstack_cloud_create_json_body

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

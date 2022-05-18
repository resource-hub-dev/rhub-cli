from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_lab_product_list_product_regions_response_200_item_region_openstack_credentials_type_0 import (
    RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstackCredentialsType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack")


@attr.s(auto_attribs=True)
class RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstack:
    """
    Example:
        {'credentials': 'kv/region/rdu2-a/openstack', 'domain_id': 'default', 'domain_name': 'Default', 'keyname':
            'rhub', 'networks': ['provider_net_rhub'], 'project': 'rhub', 'url': 'https://openstack.example.com:13000'}

    Attributes:
        credentials (Union[RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstackCredentialsType0, Unset,
            str]):
        domain_id (Union[Unset, str]):
        domain_name (Union[Unset, str]):
        keyname (Union[Unset, str]): SSH key name
        networks (Union[Unset, List[str]]): Network providers that can be used in the region
        project (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    credentials: Union[
        RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstackCredentialsType0, Unset, str
    ] = UNSET
    domain_id: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    keyname: Union[Unset, str] = UNSET
    networks: Union[Unset, List[str]] = UNSET
    project: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Dict[str, Any], Unset, str]
        if isinstance(self.credentials, Unset):
            credentials = UNSET

        elif isinstance(
            self.credentials, RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstackCredentialsType0
        ):
            credentials = UNSET
            if not isinstance(self.credentials, Unset):
                credentials = self.credentials.to_dict()

        else:
            credentials = self.credentials

        domain_id = self.domain_id
        domain_name = self.domain_name
        keyname = self.keyname
        networks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = self.networks

        project = self.project
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if domain_id is not UNSET:
            field_dict["domain_id"] = domain_id
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if keyname is not UNSET:
            field_dict["keyname"] = keyname
        if networks is not UNSET:
            field_dict["networks"] = networks
        if project is not UNSET:
            field_dict["project"] = project
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)

        def _parse_credentials(
            data: object,
        ) -> Union[RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstackCredentialsType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _credentials_type_0 = data
                credentials_type_0: Union[
                    Unset, RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstackCredentialsType0
                ]
                if isinstance(_credentials_type_0, Unset):
                    credentials_type_0 = UNSET
                else:
                    credentials_type_0 = (
                        RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstackCredentialsType0.from_dict(
                            _credentials_type_0
                        )
                    )

                return credentials_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[RhubApiLabProductListProductRegionsResponse200ItemRegionOpenstackCredentialsType0, Unset, str],
                data,
            )

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        domain_id = d.pop("domain_id", UNSET)

        domain_name = d.pop("domain_name", UNSET)

        keyname = d.pop("keyname", UNSET)

        networks = cast(List[str], d.pop("networks", UNSET))

        project = d.pop("project", UNSET)

        url = d.pop("url", UNSET)

        rhub_api_lab_product_list_product_regions_response_200_item_region_openstack = cls(
            credentials=credentials,
            domain_id=domain_id,
            domain_name=domain_name,
            keyname=keyname,
            networks=networks,
            project=project,
            url=url,
        )

        rhub_api_lab_product_list_product_regions_response_200_item_region_openstack.additional_properties = d
        return rhub_api_lab_product_list_product_regions_response_200_item_region_openstack

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

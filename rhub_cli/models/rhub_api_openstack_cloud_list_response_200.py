from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_openstack_cloud_list_response_200_data_item import RhubApiOpenstackCloudListResponse200DataItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiOpenstackCloudListResponse200")


@attr.s(auto_attribs=True)
class RhubApiOpenstackCloudListResponse200:
    """
    Attributes:
        data (Union[Unset, List[RhubApiOpenstackCloudListResponse200DataItem]]):
        total (Union[Unset, int]): The total number of items
    """

    data: Union[Unset, List[RhubApiOpenstackCloudListResponse200DataItem]] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = RhubApiOpenstackCloudListResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        total = d.pop("total", UNSET)

        rhub_api_openstack_cloud_list_response_200 = cls(
            data=data,
            total=total,
        )

        rhub_api_openstack_cloud_list_response_200.additional_properties = d
        return rhub_api_openstack_cloud_list_response_200

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

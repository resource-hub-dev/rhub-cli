from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiMonitorMetricsBmHostsToMonitorListResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiMonitorMetricsBmHostsToMonitorListResponse200DataItem:
    """
    Attributes:
        name (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        name = d.pop("name", UNSET)

        rhub_api_monitor_metrics_bm_hosts_to_monitor_list_response_200_data_item = cls(
            name=name,
        )

        rhub_api_monitor_metrics_bm_hosts_to_monitor_list_response_200_data_item.additional_properties = d
        return rhub_api_monitor_metrics_bm_hosts_to_monitor_list_response_200_data_item

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

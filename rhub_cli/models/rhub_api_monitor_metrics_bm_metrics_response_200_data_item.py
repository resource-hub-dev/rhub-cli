from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiMonitorMetricsBmMetricsResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiMonitorMetricsBmMetricsResponse200DataItem:
    """
    Attributes:
        all_ (Union[Unset, int]):
        available (Union[Unset, int]):
        cpus_available (Union[Unset, int]):
        cpus_used (Union[Unset, int]):
        memory_available (Union[Unset, int]):
        memory_used (Union[Unset, int]):
        platform (Union[Unset, str]):
        provisioned (Union[Unset, int]):
        requested (Union[Unset, int]):
    """

    all_: Union[Unset, int] = UNSET
    available: Union[Unset, int] = UNSET
    cpus_available: Union[Unset, int] = UNSET
    cpus_used: Union[Unset, int] = UNSET
    memory_available: Union[Unset, int] = UNSET
    memory_used: Union[Unset, int] = UNSET
    platform: Union[Unset, str] = UNSET
    provisioned: Union[Unset, int] = UNSET
    requested: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_ = self.all_
        available = self.available
        cpus_available = self.cpus_available
        cpus_used = self.cpus_used
        memory_available = self.memory_available
        memory_used = self.memory_used
        platform = self.platform
        provisioned = self.provisioned
        requested = self.requested

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if available is not UNSET:
            field_dict["available"] = available
        if cpus_available is not UNSET:
            field_dict["cpus_available"] = cpus_available
        if cpus_used is not UNSET:
            field_dict["cpus_used"] = cpus_used
        if memory_available is not UNSET:
            field_dict["memory_available"] = memory_available
        if memory_used is not UNSET:
            field_dict["memory_used"] = memory_used
        if platform is not UNSET:
            field_dict["platform"] = platform
        if provisioned is not UNSET:
            field_dict["provisioned"] = provisioned
        if requested is not UNSET:
            field_dict["requested"] = requested

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        all_ = d.pop("all", UNSET)

        available = d.pop("available", UNSET)

        cpus_available = d.pop("cpus_available", UNSET)

        cpus_used = d.pop("cpus_used", UNSET)

        memory_available = d.pop("memory_available", UNSET)

        memory_used = d.pop("memory_used", UNSET)

        platform = d.pop("platform", UNSET)

        provisioned = d.pop("provisioned", UNSET)

        requested = d.pop("requested", UNSET)

        rhub_api_monitor_metrics_bm_metrics_response_200_data_item = cls(
            all_=all_,
            available=available,
            cpus_available=cpus_available,
            cpus_used=cpus_used,
            memory_available=memory_available,
            memory_used=memory_used,
            platform=platform,
            provisioned=provisioned,
            requested=requested,
        )

        rhub_api_monitor_metrics_bm_metrics_response_200_data_item.additional_properties = d
        return rhub_api_monitor_metrics_bm_metrics_response_200_data_item

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

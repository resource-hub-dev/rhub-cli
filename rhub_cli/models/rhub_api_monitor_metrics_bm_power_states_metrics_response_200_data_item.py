from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiMonitorMetricsBmPowerStatesMetricsResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiMonitorMetricsBmPowerStatesMetricsResponse200DataItem:
    """
    Attributes:
        all_ (Union[Unset, int]):
        off (Union[Unset, int]):
        on (Union[Unset, int]):
        platform (Union[Unset, str]):
        wattage_off (Union[Unset, int]):
        wattage_on (Union[Unset, int]):
    """

    all_: Union[Unset, int] = UNSET
    off: Union[Unset, int] = UNSET
    on: Union[Unset, int] = UNSET
    platform: Union[Unset, str] = UNSET
    wattage_off: Union[Unset, int] = UNSET
    wattage_on: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_ = self.all_
        off = self.off
        on = self.on
        platform = self.platform
        wattage_off = self.wattage_off
        wattage_on = self.wattage_on

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if off is not UNSET:
            field_dict["off"] = off
        if on is not UNSET:
            field_dict["on"] = on
        if platform is not UNSET:
            field_dict["platform"] = platform
        if wattage_off is not UNSET:
            field_dict["wattage_off"] = wattage_off
        if wattage_on is not UNSET:
            field_dict["wattage_on"] = wattage_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        all_ = d.pop("all", UNSET)

        off = d.pop("off", UNSET)

        on = d.pop("on", UNSET)

        platform = d.pop("platform", UNSET)

        wattage_off = d.pop("wattage_off", UNSET)

        wattage_on = d.pop("wattage_on", UNSET)

        rhub_api_monitor_metrics_bm_power_states_metrics_response_200_data_item = cls(
            all_=all_,
            off=off,
            on=on,
            platform=platform,
            wattage_off=wattage_off,
            wattage_on=wattage_on,
        )

        rhub_api_monitor_metrics_bm_power_states_metrics_response_200_data_item.additional_properties = d
        return rhub_api_monitor_metrics_bm_power_states_metrics_response_200_data_item

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

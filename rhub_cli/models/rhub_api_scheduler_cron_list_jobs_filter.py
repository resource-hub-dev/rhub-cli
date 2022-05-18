from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiSchedulerCronListJobsFilter")


@attr.s(auto_attribs=True)
class RhubApiSchedulerCronListJobsFilter:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        name (Union[Unset, str]): Name of a job. Wildcard ``%`` can be used to match zero, one, or multiple characters
    """

    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        rhub_api_scheduler_cron_list_jobs_filter = cls(
            enabled=enabled,
            name=name,
        )

        rhub_api_scheduler_cron_list_jobs_filter.additional_properties = d
        return rhub_api_scheduler_cron_list_jobs_filter

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

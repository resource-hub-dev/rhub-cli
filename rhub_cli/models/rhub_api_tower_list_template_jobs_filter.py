from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerListTemplateJobsFilter")


@attr.s(auto_attribs=True)
class RhubApiTowerListTemplateJobsFilter:
    """
    Attributes:
        launched_by (Union[Unset, str]): ID of the user who launched template
    """

    launched_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        launched_by = self.launched_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if launched_by is not UNSET:
            field_dict["launched_by"] = launched_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        launched_by = d.pop("launched_by", UNSET)

        rhub_api_tower_list_template_jobs_filter = cls(
            launched_by=launched_by,
        )

        rhub_api_tower_list_template_jobs_filter.additional_properties = d
        return rhub_api_tower_list_template_jobs_filter

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

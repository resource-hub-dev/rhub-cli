from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerListTemplatesFilter")


@attr.s(auto_attribs=True)
class RhubApiTowerListTemplatesFilter:
    """
    Attributes:
        name (Union[Unset, str]): Name of a template. Wildcard ``%`` can be used to match zero, one, or multiple
            characters
        server_id (Union[Unset, int]): ID of the server
    """

    name: Union[Unset, str] = UNSET
    server_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        server_id = self.server_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if server_id is not UNSET:
            field_dict["server_id"] = server_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        name = d.pop("name", UNSET)

        server_id = d.pop("server_id", UNSET)

        rhub_api_tower_list_templates_filter = cls(
            name=name,
            server_id=server_id,
        )

        rhub_api_tower_list_templates_filter.additional_properties = d
        return rhub_api_tower_list_templates_filter

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

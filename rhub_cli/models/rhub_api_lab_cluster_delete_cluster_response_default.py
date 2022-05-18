from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabClusterDeleteClusterResponseDefault")


@attr.s(auto_attribs=True)
class RhubApiLabClusterDeleteClusterResponseDefault:
    """
    Attributes:
        detail (Union[Unset, str]):
        status (Union[Unset, int]):
        title (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    detail: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        detail = self.detail
        status = self.status
        title = self.title
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        detail = d.pop("detail", UNSET)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        rhub_api_lab_cluster_delete_cluster_response_default = cls(
            detail=detail,
            status=status,
            title=title,
            type=type,
        )

        rhub_api_lab_cluster_delete_cluster_response_default.additional_properties = d
        return rhub_api_lab_cluster_delete_cluster_response_default

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

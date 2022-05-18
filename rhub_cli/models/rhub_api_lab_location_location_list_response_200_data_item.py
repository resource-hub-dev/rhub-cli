from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_lab_location_location_list_response_200_data_item_id import (
    RhubApiLabLocationLocationListResponse200DataItemId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabLocationLocationListResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiLabLocationLocationListResponse200DataItem:
    """
    Attributes:
        description (Union[Unset, None, str]): Long description of location, address, ... Example: Raleigh.
        id (Union[Unset, RhubApiLabLocationLocationListResponse200DataItemId]):
        name (Union[Unset, str]): Short name of location / IATA identifier / ... Example: RDU.
    """

    description: Union[Unset, None, str] = UNSET
    id: Union[Unset, RhubApiLabLocationLocationListResponse200DataItemId] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiLabLocationLocationListResponse200DataItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiLabLocationLocationListResponse200DataItemId.from_dict(_id)

        name = d.pop("name", UNSET)

        rhub_api_lab_location_location_list_response_200_data_item = cls(
            description=description,
            id=id,
            name=name,
        )

        rhub_api_lab_location_location_list_response_200_data_item.additional_properties = d
        return rhub_api_lab_location_location_list_response_200_data_item

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

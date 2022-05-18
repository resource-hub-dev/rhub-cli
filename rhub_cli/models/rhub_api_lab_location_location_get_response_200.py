from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_lab_location_location_get_response_200_id import RhubApiLabLocationLocationGetResponse200Id
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabLocationLocationGetResponse200")


@attr.s(auto_attribs=True)
class RhubApiLabLocationLocationGetResponse200:
    """
    Attributes:
        description (Union[Unset, None, str]): Long description of location, address, ... Example: Raleigh.
        id (Union[Unset, RhubApiLabLocationLocationGetResponse200Id]):
        name (Union[Unset, str]): Short name of location / IATA identifier / ... Example: RDU.
    """

    description: Union[Unset, None, str] = UNSET
    id: Union[Unset, RhubApiLabLocationLocationGetResponse200Id] = UNSET
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
        id: Union[Unset, RhubApiLabLocationLocationGetResponse200Id]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiLabLocationLocationGetResponse200Id.from_dict(_id)

        name = d.pop("name", UNSET)

        rhub_api_lab_location_location_get_response_200 = cls(
            description=description,
            id=id,
            name=name,
        )

        rhub_api_lab_location_location_get_response_200.additional_properties = d
        return rhub_api_lab_location_location_get_response_200

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

from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_tower_list_templates_response_200_data_item_id import (
    RhubApiTowerListTemplatesResponse200DataItemId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerListTemplatesResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiTowerListTemplatesResponse200DataItem:
    """
    Attributes:
        description (Union[Unset, str]):
        id (Union[Unset, RhubApiTowerListTemplatesResponse200DataItemId]): Internal ID
        name (Union[Unset, str]):
        server_id (Union[Unset, int]):
        tower_template_id (Union[Unset, int]):
        tower_template_is_workflow (Union[Unset, bool]): Is template workflow?
    """

    description: Union[Unset, str] = UNSET
    id: Union[Unset, RhubApiTowerListTemplatesResponse200DataItemId] = UNSET
    name: Union[Unset, str] = UNSET
    server_id: Union[Unset, int] = UNSET
    tower_template_id: Union[Unset, int] = UNSET
    tower_template_is_workflow: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name
        server_id = self.server_id
        tower_template_id = self.tower_template_id
        tower_template_is_workflow = self.tower_template_is_workflow

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if tower_template_id is not UNSET:
            field_dict["tower_template_id"] = tower_template_id
        if tower_template_is_workflow is not UNSET:
            field_dict["tower_template_is_workflow"] = tower_template_is_workflow

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiTowerListTemplatesResponse200DataItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiTowerListTemplatesResponse200DataItemId.from_dict(_id)

        name = d.pop("name", UNSET)

        server_id = d.pop("server_id", UNSET)

        tower_template_id = d.pop("tower_template_id", UNSET)

        tower_template_is_workflow = d.pop("tower_template_is_workflow", UNSET)

        rhub_api_tower_list_templates_response_200_data_item = cls(
            description=description,
            id=id,
            name=name,
            server_id=server_id,
            tower_template_id=tower_template_id,
            tower_template_is_workflow=tower_template_is_workflow,
        )

        rhub_api_tower_list_templates_response_200_data_item.additional_properties = d
        return rhub_api_tower_list_templates_response_200_data_item

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

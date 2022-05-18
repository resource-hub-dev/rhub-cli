from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_tower_create_template_json_body_id import RhubApiTowerCreateTemplateJsonBodyId
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerCreateTemplateJsonBody")


@attr.s(auto_attribs=True)
class RhubApiTowerCreateTemplateJsonBody:
    """
    Attributes:
        name (str):
        server_id (int):
        tower_template_id (int):
        tower_template_is_workflow (bool): Is template workflow?
        description (Union[Unset, str]):
        id (Union[Unset, RhubApiTowerCreateTemplateJsonBodyId]): Internal ID
    """

    name: str
    server_id: int
    tower_template_id: int
    tower_template_is_workflow: bool
    description: Union[Unset, str] = UNSET
    id: Union[Unset, RhubApiTowerCreateTemplateJsonBodyId] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        server_id = self.server_id
        tower_template_id = self.tower_template_id
        tower_template_is_workflow = self.tower_template_is_workflow
        description = self.description
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "server_id": server_id,
                "tower_template_id": tower_template_id,
                "tower_template_is_workflow": tower_template_is_workflow,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        name = d.pop("name")

        server_id = d.pop("server_id")

        tower_template_id = d.pop("tower_template_id")

        tower_template_is_workflow = d.pop("tower_template_is_workflow")

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiTowerCreateTemplateJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiTowerCreateTemplateJsonBodyId.from_dict(_id)

        rhub_api_tower_create_template_json_body = cls(
            name=name,
            server_id=server_id,
            tower_template_id=tower_template_id,
            tower_template_is_workflow=tower_template_is_workflow,
            description=description,
            id=id,
        )

        rhub_api_tower_create_template_json_body.additional_properties = d
        return rhub_api_tower_create_template_json_body

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

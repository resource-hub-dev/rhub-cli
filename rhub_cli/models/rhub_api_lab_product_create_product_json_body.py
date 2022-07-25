from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_lab_product_create_product_json_body_flavors import RhubApiLabProductCreateProductJsonBodyFlavors
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabProductCreateProductJsonBody")


@attr.s(auto_attribs=True)
class RhubApiLabProductCreateProductJsonBody:
    """
    Attributes:
        name (str):  Example: OpenShift.
        parameters (List[Any]):
        tower_template_name_create (str):  Example: rhub-openshift-create.
        tower_template_name_delete (str):  Example: rhub-openshift-delete.
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        flavors (Union[Unset, None, RhubApiLabProductCreateProductJsonBodyFlavors]):
        id (Union[Unset, int]):
    """

    name: str
    parameters: List[Any]
    tower_template_name_create: str
    tower_template_name_delete: str
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    flavors: Union[Unset, None, RhubApiLabProductCreateProductJsonBodyFlavors] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        parameters = []
        for parameters_item_data in self.parameters:

            parameters_item = parameters_item_data

            parameters.append(parameters_item)

        tower_template_name_create = self.tower_template_name_create
        tower_template_name_delete = self.tower_template_name_delete
        description = self.description
        enabled = self.enabled
        flavors: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.flavors, Unset):
            flavors = self.flavors.to_dict() if self.flavors else None

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parameters": parameters,
                "tower_template_name_create": tower_template_name_create,
                "tower_template_name_delete": tower_template_name_delete,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if flavors is not UNSET:
            field_dict["flavors"] = flavors
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        name = d.pop("name")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:

            def _parse_parameters_item(data: object) -> Any:
                return cast(Any, data)

            parameters_item = _parse_parameters_item(parameters_item_data)

            parameters.append(parameters_item)

        tower_template_name_create = d.pop("tower_template_name_create")

        tower_template_name_delete = d.pop("tower_template_name_delete")

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _flavors = d.pop("flavors", UNSET)
        flavors: Union[Unset, None, RhubApiLabProductCreateProductJsonBodyFlavors]
        if _flavors is None:
            flavors = None
        elif isinstance(_flavors, Unset):
            flavors = UNSET
        else:
            flavors = RhubApiLabProductCreateProductJsonBodyFlavors.from_dict(_flavors)

        id = d.pop("id", UNSET)

        rhub_api_lab_product_create_product_json_body = cls(
            name=name,
            parameters=parameters,
            tower_template_name_create=tower_template_name_create,
            tower_template_name_delete=tower_template_name_delete,
            description=description,
            enabled=enabled,
            flavors=flavors,
            id=id,
        )

        rhub_api_lab_product_create_product_json_body.additional_properties = d
        return rhub_api_lab_product_create_product_json_body

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

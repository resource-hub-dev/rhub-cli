from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.rhub_api_lab_product_list_products_response_200_data_item_flavors import (
    RhubApiLabProductListProductsResponse200DataItemFlavors,
)
from ..models.rhub_api_lab_product_list_products_response_200_data_item_id import (
    RhubApiLabProductListProductsResponse200DataItemId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabProductListProductsResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiLabProductListProductsResponse200DataItem:
    """
    Attributes:
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        flavors (Union[Unset, None, RhubApiLabProductListProductsResponse200DataItemFlavors]):
        id (Union[Unset, RhubApiLabProductListProductsResponse200DataItemId]):
        name (Union[Unset, str]):  Example: OpenShift.
        parameters (Union[Unset, List[Any]]):
        tower_template_name_create (Union[Unset, str]):  Example: rhub-openshift-create.
        tower_template_name_delete (Union[Unset, str]):  Example: rhub-openshift-delete.
    """

    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    flavors: Union[Unset, None, RhubApiLabProductListProductsResponse200DataItemFlavors] = UNSET
    id: Union[Unset, RhubApiLabProductListProductsResponse200DataItemId] = UNSET
    name: Union[Unset, str] = UNSET
    parameters: Union[Unset, List[Any]] = UNSET
    tower_template_name_create: Union[Unset, str] = UNSET
    tower_template_name_delete: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        enabled = self.enabled
        flavors: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.flavors, Unset):
            flavors = self.flavors.to_dict() if self.flavors else None

        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        name = self.name
        parameters: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:

                parameters_item = parameters_item_data

                parameters.append(parameters_item)

        tower_template_name_create = self.tower_template_name_create
        tower_template_name_delete = self.tower_template_name_delete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if flavors is not UNSET:
            field_dict["flavors"] = flavors
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if tower_template_name_create is not UNSET:
            field_dict["tower_template_name_create"] = tower_template_name_create
        if tower_template_name_delete is not UNSET:
            field_dict["tower_template_name_delete"] = tower_template_name_delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _flavors = d.pop("flavors", UNSET)
        flavors: Union[Unset, None, RhubApiLabProductListProductsResponse200DataItemFlavors]
        if _flavors is None:
            flavors = None
        elif isinstance(_flavors, Unset):
            flavors = UNSET
        else:
            flavors = RhubApiLabProductListProductsResponse200DataItemFlavors.from_dict(_flavors)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiLabProductListProductsResponse200DataItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiLabProductListProductsResponse200DataItemId.from_dict(_id)

        name = d.pop("name", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:

            def _parse_parameters_item(data: object) -> Any:
                return cast(Any, data)

            parameters_item = _parse_parameters_item(parameters_item_data)

            parameters.append(parameters_item)

        tower_template_name_create = d.pop("tower_template_name_create", UNSET)

        tower_template_name_delete = d.pop("tower_template_name_delete", UNSET)

        rhub_api_lab_product_list_products_response_200_data_item = cls(
            description=description,
            enabled=enabled,
            flavors=flavors,
            id=id,
            name=name,
            parameters=parameters,
            tower_template_name_create=tower_template_name_create,
            tower_template_name_delete=tower_template_name_delete,
        )

        rhub_api_lab_product_list_products_response_200_data_item.additional_properties = d
        return rhub_api_lab_product_list_products_response_200_data_item

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

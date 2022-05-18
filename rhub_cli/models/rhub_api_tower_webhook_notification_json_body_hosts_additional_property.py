from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_tower_webhook_notification_json_body_hosts_additional_property_localhost import (
    RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalProperty")


@attr.s(auto_attribs=True)
class RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalProperty:
    """
    Attributes:
        localhost (Union[Unset, RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost]):
    """

    localhost: Union[Unset, RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        localhost: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.localhost, Unset):
            localhost = self.localhost.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if localhost is not UNSET:
            field_dict["localhost"] = localhost

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _localhost = d.pop("localhost", UNSET)
        localhost: Union[Unset, RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost]
        if isinstance(_localhost, Unset):
            localhost = UNSET
        else:
            localhost = RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost.from_dict(_localhost)

        rhub_api_tower_webhook_notification_json_body_hosts_additional_property = cls(
            localhost=localhost,
        )

        rhub_api_tower_webhook_notification_json_body_hosts_additional_property.additional_properties = d
        return rhub_api_tower_webhook_notification_json_body_hosts_additional_property

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

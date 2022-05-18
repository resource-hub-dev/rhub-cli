from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost")


@attr.s(auto_attribs=True)
class RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost:
    """
    Attributes:
        changed (Union[Unset, int]):
        dark (Union[Unset, int]):
        failed (Union[Unset, bool]):
        failures (Union[Unset, int]):
        ignored (Union[Unset, int]):
        ok (Union[Unset, int]):
        processed (Union[Unset, int]):
        rescued (Union[Unset, int]):
        skipped (Union[Unset, int]):
    """

    changed: Union[Unset, int] = UNSET
    dark: Union[Unset, int] = UNSET
    failed: Union[Unset, bool] = UNSET
    failures: Union[Unset, int] = UNSET
    ignored: Union[Unset, int] = UNSET
    ok: Union[Unset, int] = UNSET
    processed: Union[Unset, int] = UNSET
    rescued: Union[Unset, int] = UNSET
    skipped: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        changed = self.changed
        dark = self.dark
        failed = self.failed
        failures = self.failures
        ignored = self.ignored
        ok = self.ok
        processed = self.processed
        rescued = self.rescued
        skipped = self.skipped

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed is not UNSET:
            field_dict["changed"] = changed
        if dark is not UNSET:
            field_dict["dark"] = dark
        if failed is not UNSET:
            field_dict["failed"] = failed
        if failures is not UNSET:
            field_dict["failures"] = failures
        if ignored is not UNSET:
            field_dict["ignored"] = ignored
        if ok is not UNSET:
            field_dict["ok"] = ok
        if processed is not UNSET:
            field_dict["processed"] = processed
        if rescued is not UNSET:
            field_dict["rescued"] = rescued
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        changed = d.pop("changed", UNSET)

        dark = d.pop("dark", UNSET)

        failed = d.pop("failed", UNSET)

        failures = d.pop("failures", UNSET)

        ignored = d.pop("ignored", UNSET)

        ok = d.pop("ok", UNSET)

        processed = d.pop("processed", UNSET)

        rescued = d.pop("rescued", UNSET)

        skipped = d.pop("skipped", UNSET)

        rhub_api_tower_webhook_notification_json_body_hosts_additional_property_localhost = cls(
            changed=changed,
            dark=dark,
            failed=failed,
            failures=failures,
            ignored=ignored,
            ok=ok,
            processed=processed,
            rescued=rescued,
            skipped=skipped,
        )

        rhub_api_tower_webhook_notification_json_body_hosts_additional_property_localhost.additional_properties = d
        return rhub_api_tower_webhook_notification_json_body_hosts_additional_property_localhost

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

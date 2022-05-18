import datetime
from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.rhub_api_tower_webhook_notification_json_body_hosts import RhubApiTowerWebhookNotificationJsonBodyHosts
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerWebhookNotificationJsonBody")


@attr.s(auto_attribs=True)
class RhubApiTowerWebhookNotificationJsonBody:
    """
    Attributes:
        body (Union[Unset, None, str]): Enumerates all the nodes in the workflow job with a description of the job
            associated with each
        created_by (Union[Unset, str]):
        credential (Union[Unset, None, str]): Credential used by Job
        extra_vars (Union[Unset, None, str]): Extra variables for playbook encoded as a dictionary within a string
        finished (Union[Unset, None, datetime.datetime]): Date/Time job finished
        hosts (Union[Unset, None, RhubApiTowerWebhookNotificationJsonBodyHosts]):
        id (Union[Unset, int]): jobId
        inventory (Union[Unset, None, str]): Inventory used by Job
        limit (Union[Unset, None, str]): Job limit
        name (Union[Unset, str]): jobName
        playbook (Union[Unset, None, str]): Playbook executed in Job
        project (Union[Unset, None, str]): Project job belongs to
        started (Union[Unset, None, datetime.datetime]): Date/Time job started
        status (Union[Unset, str]): Job status
        traceback (Union[Unset, None, str]): Traceback if failed
        url (Union[Unset, str]): URL to Job on Tower
    """

    body: Union[Unset, None, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    credential: Union[Unset, None, str] = UNSET
    extra_vars: Union[Unset, None, str] = UNSET
    finished: Union[Unset, None, datetime.datetime] = UNSET
    hosts: Union[Unset, None, RhubApiTowerWebhookNotificationJsonBodyHosts] = UNSET
    id: Union[Unset, int] = UNSET
    inventory: Union[Unset, None, str] = UNSET
    limit: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    playbook: Union[Unset, None, str] = UNSET
    project: Union[Unset, None, str] = UNSET
    started: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    traceback: Union[Unset, None, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        created_by = self.created_by
        credential = self.credential
        extra_vars = self.extra_vars
        finished: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished, Unset):
            finished = self.finished.isoformat() if self.finished else None

        hosts: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts.to_dict() if self.hosts else None

        id = self.id
        inventory = self.inventory
        limit = self.limit
        name = self.name
        playbook = self.playbook
        project = self.project
        started: Union[Unset, None, str] = UNSET
        if not isinstance(self.started, Unset):
            started = self.started.isoformat() if self.started else None

        status = self.status
        traceback = self.traceback
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if credential is not UNSET:
            field_dict["credential"] = credential
        if extra_vars is not UNSET:
            field_dict["extra_vars"] = extra_vars
        if finished is not UNSET:
            field_dict["finished"] = finished
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if id is not UNSET:
            field_dict["id"] = id
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if limit is not UNSET:
            field_dict["limit"] = limit
        if name is not UNSET:
            field_dict["name"] = name
        if playbook is not UNSET:
            field_dict["playbook"] = playbook
        if project is not UNSET:
            field_dict["project"] = project
        if started is not UNSET:
            field_dict["started"] = started
        if status is not UNSET:
            field_dict["status"] = status
        if traceback is not UNSET:
            field_dict["traceback"] = traceback
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        body = d.pop("body", UNSET)

        created_by = d.pop("created_by", UNSET)

        credential = d.pop("credential", UNSET)

        extra_vars = d.pop("extra_vars", UNSET)

        _finished = d.pop("finished", UNSET)
        finished: Union[Unset, None, datetime.datetime]
        if _finished is None:
            finished = None
        elif isinstance(_finished, Unset):
            finished = UNSET
        else:
            finished = isoparse(_finished)

        _hosts = d.pop("hosts", UNSET)
        hosts: Union[Unset, None, RhubApiTowerWebhookNotificationJsonBodyHosts]
        if _hosts is None:
            hosts = None
        elif isinstance(_hosts, Unset):
            hosts = UNSET
        else:
            hosts = RhubApiTowerWebhookNotificationJsonBodyHosts.from_dict(_hosts)

        id = d.pop("id", UNSET)

        inventory = d.pop("inventory", UNSET)

        limit = d.pop("limit", UNSET)

        name = d.pop("name", UNSET)

        playbook = d.pop("playbook", UNSET)

        project = d.pop("project", UNSET)

        _started = d.pop("started", UNSET)
        started: Union[Unset, None, datetime.datetime]
        if _started is None:
            started = None
        elif isinstance(_started, Unset):
            started = UNSET
        else:
            started = isoparse(_started)

        status = d.pop("status", UNSET)

        traceback = d.pop("traceback", UNSET)

        url = d.pop("url", UNSET)

        rhub_api_tower_webhook_notification_json_body = cls(
            body=body,
            created_by=created_by,
            credential=credential,
            extra_vars=extra_vars,
            finished=finished,
            hosts=hosts,
            id=id,
            inventory=inventory,
            limit=limit,
            name=name,
            playbook=playbook,
            project=project,
            started=started,
            status=status,
            traceback=traceback,
            url=url,
        )

        rhub_api_tower_webhook_notification_json_body.additional_properties = d
        return rhub_api_tower_webhook_notification_json_body

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

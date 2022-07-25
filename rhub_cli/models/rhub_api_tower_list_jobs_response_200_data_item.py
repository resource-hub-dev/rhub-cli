import datetime
from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiTowerListJobsResponse200DataItem")


@attr.s(auto_attribs=True)
class RhubApiTowerListJobsResponse200DataItem:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        failed (Union[Unset, bool]):
        finished (Union[Unset, bool]):
        finished_at (Union[Unset, None, datetime.datetime]):
        id (Union[Unset, int]): Internal ID
        launched_by (Union[Unset, str]):
        started (Union[Unset, bool]):
        started_at (Union[Unset, None, datetime.datetime]):
        status (Union[Unset, str]): Job status
        template_id (Union[Unset, int]):
        tower_job_id (Union[Unset, int]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    failed: Union[Unset, bool] = UNSET
    finished: Union[Unset, bool] = UNSET
    finished_at: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    launched_by: Union[Unset, str] = UNSET
    started: Union[Unset, bool] = UNSET
    started_at: Union[Unset, None, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    template_id: Union[Unset, int] = UNSET
    tower_job_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        failed = self.failed
        finished = self.finished
        finished_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat() if self.finished_at else None

        id = self.id
        launched_by = self.launched_by
        started = self.started
        started_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat() if self.started_at else None

        status = self.status
        template_id = self.template_id
        tower_job_id = self.tower_job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if failed is not UNSET:
            field_dict["failed"] = failed
        if finished is not UNSET:
            field_dict["finished"] = finished
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if id is not UNSET:
            field_dict["id"] = id
        if launched_by is not UNSET:
            field_dict["launched_by"] = launched_by
        if started is not UNSET:
            field_dict["started"] = started
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if tower_job_id is not UNSET:
            field_dict["tower_job_id"] = tower_job_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        failed = d.pop("failed", UNSET)

        finished = d.pop("finished", UNSET)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: Union[Unset, None, datetime.datetime]
        if _finished_at is None:
            finished_at = None
        elif isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)

        id = d.pop("id", UNSET)

        launched_by = d.pop("launched_by", UNSET)

        started = d.pop("started", UNSET)

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, None, datetime.datetime]
        if _started_at is None:
            started_at = None
        elif isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        status = d.pop("status", UNSET)

        template_id = d.pop("template_id", UNSET)

        tower_job_id = d.pop("tower_job_id", UNSET)

        rhub_api_tower_list_jobs_response_200_data_item = cls(
            created_at=created_at,
            failed=failed,
            finished=finished,
            finished_at=finished_at,
            id=id,
            launched_by=launched_by,
            started=started,
            started_at=started_at,
            status=status,
            template_id=template_id,
            tower_job_id=tower_job_id,
        )

        rhub_api_tower_list_jobs_response_200_data_item.additional_properties = d
        return rhub_api_tower_list_jobs_response_200_data_item

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

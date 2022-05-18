import datetime
from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.rhub_api_scheduler_cron_create_job_json_body_id import RhubApiSchedulerCronCreateJobJsonBodyId
from ..models.rhub_api_scheduler_cron_create_job_json_body_job_name import RhubApiSchedulerCronCreateJobJsonBodyJobName
from ..models.rhub_api_scheduler_cron_create_job_json_body_job_params import (
    RhubApiSchedulerCronCreateJobJsonBodyJobParams,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiSchedulerCronCreateJobJsonBody")


@attr.s(auto_attribs=True)
class RhubApiSchedulerCronCreateJobJsonBody:
    """
    Attributes:
        job_name (RhubApiSchedulerCronCreateJobJsonBodyJobName):
        name (str):
        time_expr (str): cron time expression
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        id (Union[Unset, RhubApiSchedulerCronCreateJobJsonBodyId]):
        job_params (Union[Unset, None, RhubApiSchedulerCronCreateJobJsonBodyJobParams]):
        last_run (Union[Unset, None, datetime.datetime]):
    """

    job_name: RhubApiSchedulerCronCreateJobJsonBodyJobName
    name: str
    time_expr: str
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    id: Union[Unset, RhubApiSchedulerCronCreateJobJsonBodyId] = UNSET
    job_params: Union[Unset, None, RhubApiSchedulerCronCreateJobJsonBodyJobParams] = UNSET
    last_run: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name.value

        name = self.name
        time_expr = self.time_expr
        description = self.description
        enabled = self.enabled
        id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        job_params: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.job_params, Unset):
            job_params = self.job_params.to_dict() if self.job_params else None

        last_run: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat() if self.last_run else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_name": job_name,
                "name": name,
                "time_expr": time_expr,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if job_params is not UNSET:
            field_dict["job_params"] = job_params
        if last_run is not UNSET:
            field_dict["last_run"] = last_run

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        job_name = RhubApiSchedulerCronCreateJobJsonBodyJobName(d.pop("job_name"))

        name = d.pop("name")

        time_expr = d.pop("time_expr")

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, RhubApiSchedulerCronCreateJobJsonBodyId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = RhubApiSchedulerCronCreateJobJsonBodyId.from_dict(_id)

        _job_params = d.pop("job_params", UNSET)
        job_params: Union[Unset, None, RhubApiSchedulerCronCreateJobJsonBodyJobParams]
        if _job_params is None:
            job_params = None
        elif isinstance(_job_params, Unset):
            job_params = UNSET
        else:
            job_params = RhubApiSchedulerCronCreateJobJsonBodyJobParams.from_dict(_job_params)

        _last_run = d.pop("last_run", UNSET)
        last_run: Union[Unset, None, datetime.datetime]
        if _last_run is None:
            last_run = None
        elif isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = isoparse(_last_run)

        rhub_api_scheduler_cron_create_job_json_body = cls(
            job_name=job_name,
            name=name,
            time_expr=time_expr,
            description=description,
            enabled=enabled,
            id=id,
            job_params=job_params,
            last_run=last_run,
        )

        rhub_api_scheduler_cron_create_job_json_body.additional_properties = d
        return rhub_api_scheduler_cron_create_job_json_body

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

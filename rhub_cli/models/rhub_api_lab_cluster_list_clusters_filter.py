from copy import copy
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rhub_api_lab_cluster_list_clusters_filter_status import RhubApiLabClusterListClustersFilterStatus
from ..models.rhub_api_lab_cluster_list_clusters_filter_status_flag import RhubApiLabClusterListClustersFilterStatusFlag
from ..types import UNSET, Unset

T = TypeVar("T", bound="RhubApiLabClusterListClustersFilter")


@attr.s(auto_attribs=True)
class RhubApiLabClusterListClustersFilter:
    """
    Attributes:
        deleted (Union[Unset, bool]): List deleted clusters. By default deleted clusters are not
            included in the listing. When this filter is set to `true` only
            deleted clusters will be listed.
        group_id (Union[Unset, None, str]): ID of the group or ``null``.
        name (Union[Unset, str]): Name of a cluster. Wildcard ``%`` can be used to match zero, one, or multiple
            characters
        region_id (Union[Unset, int]): ID of the region.
        shared (Union[Unset, bool]): Filter shared clusters
        status (Union[Unset, None, RhubApiLabClusterListClustersFilterStatus]):
        status_flag (Union[Unset, None, RhubApiLabClusterListClustersFilterStatusFlag]):
        user_id (Union[Unset, str]): ID of the user.
    """

    deleted: Union[Unset, bool] = UNSET
    group_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    region_id: Union[Unset, int] = UNSET
    shared: Union[Unset, bool] = UNSET
    status: Union[Unset, None, RhubApiLabClusterListClustersFilterStatus] = UNSET
    status_flag: Union[Unset, None, RhubApiLabClusterListClustersFilterStatusFlag] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deleted = self.deleted
        group_id = self.group_id
        name = self.name
        region_id = self.region_id
        shared = self.shared
        status: Union[Unset, None, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        status_flag: Union[Unset, None, str] = UNSET
        if not isinstance(self.status_flag, Unset):
            status_flag = self.status_flag.value if self.status_flag else None

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if region_id is not UNSET:
            field_dict["region_id"] = region_id
        if shared is not UNSET:
            field_dict["shared"] = shared
        if status is not UNSET:
            field_dict["status"] = status
        if status_flag is not UNSET:
            field_dict["status_flag"] = status_flag
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = copy(src_dict)
        deleted = d.pop("deleted", UNSET)

        group_id = d.pop("group_id", UNSET)

        name = d.pop("name", UNSET)

        region_id = d.pop("region_id", UNSET)

        shared = d.pop("shared", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, RhubApiLabClusterListClustersFilterStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = RhubApiLabClusterListClustersFilterStatus(_status)

        _status_flag = d.pop("status_flag", UNSET)
        status_flag: Union[Unset, None, RhubApiLabClusterListClustersFilterStatusFlag]
        if _status_flag is None:
            status_flag = None
        elif isinstance(_status_flag, Unset):
            status_flag = UNSET
        else:
            status_flag = RhubApiLabClusterListClustersFilterStatusFlag(_status_flag)

        user_id = d.pop("user_id", UNSET)

        rhub_api_lab_cluster_list_clusters_filter = cls(
            deleted=deleted,
            group_id=group_id,
            name=name,
            region_id=region_id,
            shared=shared,
            status=status,
            status_flag=status_flag,
            user_id=user_id,
        )

        rhub_api_lab_cluster_list_clusters_filter.additional_properties = d
        return rhub_api_lab_cluster_list_clusters_filter

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

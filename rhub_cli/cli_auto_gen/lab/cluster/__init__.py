import json

import click

from rhub_cli.api.lab.rhub_api_lab_cluster_create_cluster import sync_detailed as cluster_create
from rhub_cli.api.lab.rhub_api_lab_cluster_delete_cluster import sync_detailed as cluster_remove
from rhub_cli.api.lab.rhub_api_lab_cluster_get_cluster import sync_detailed as cluster_get
from rhub_cli.api.lab.rhub_api_lab_cluster_list_clusters import sync_detailed as cluster_get_list
from rhub_cli.api.lab.rhub_api_lab_cluster_update_cluster import sync_detailed as cluster_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_json_body import RhubApiLabClusterCreateClusterJsonBody
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_json_body_product_params import (
    RhubApiLabClusterCreateClusterJsonBodyProductParams,
)
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_json_body_status import (
    RhubApiLabClusterCreateClusterJsonBodyStatus,
)
from rhub_cli.models.rhub_api_lab_cluster_list_clusters_filter import RhubApiLabClusterListClustersFilter
from rhub_cli.models.rhub_api_lab_cluster_list_clusters_filter_status import RhubApiLabClusterListClustersFilterStatus
from rhub_cli.models.rhub_api_lab_cluster_list_clusters_filter_status_flag import (
    RhubApiLabClusterListClustersFilterStatusFlag,
)
from rhub_cli.models.rhub_api_lab_cluster_list_clusters_sort import RhubApiLabClusterListClustersSort
from rhub_cli.models.rhub_api_lab_cluster_update_cluster_json_body import RhubApiLabClusterUpdateClusterJsonBody
from rhub_cli.models.rhub_api_lab_cluster_update_cluster_json_body_product_params import (
    RhubApiLabClusterUpdateClusterJsonBodyProductParams,
)
from rhub_cli.models.rhub_api_lab_cluster_update_cluster_json_body_status import (
    RhubApiLabClusterUpdateClusterJsonBodyStatus,
)
from rhub_cli.types import UNSET

from .events import events
from .hosts import hosts
from .reboot import reboot


@click.group()
def cluster():
    pass


@cluster.command()
@click.option(
    "--sort",
    type=click.Choice(
        [
            "name",
            "-name",
            "reservation_expiration",
            "-reservation_expiration",
            "lifespan_expiration",
            "-lifespan_expiration",
        ]
    ),
)
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option(
    "--filter-deleted",
    is_flag=True,
    help="List deleted clusters. By default deleted clusters are not included in the listing. When this filter is set to `true` only deleted clusters will be listed.",
)
@click.option("--filter-group-id", type=str, help="ID of the group or ``null``.")
@click.option(
    "--filter-name",
    type=str,
    help="Name of a cluster. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option("--filter-region-id", type=int, help="ID of the region.")
@click.option("--filter-shared", is_flag=True, help="Filter shared clusters")
@click.option(
    "--filter-status",
    type=click.Choice(
        [
            "Active",
            "Create Failed",
            "Deleted",
            "Delete Failed",
            "Deleting",
            "Deletion Failed",
            "Deletion Queued",
            "Installation Failed",
            "Installation Queued",
            "Installing",
            "Post-Deleting",
            "Post-Deletion Failed",
            "Post-Deletion Queued",
            "Post-Installation Failed",
            "Post-Installation Queued",
            "Post-Installing",
            "Post-Provisioning",
            "Post-Provisioning Failed",
            "Post-Provisioning Queued",
            "Pre-Deleting",
            "Pre-Deletion Failed",
            "Pre-Deletion Queued",
            "Pre-Installation Failed",
            "Pre-Installation Queued",
            "Pre-Installing",
            "Pre-Provisioning",
            "Pre-Provisioning Failed",
            "Pre-Provisioning Queued",
            "Provisioning",
            "Provisioning Failed",
            "Provisioning Queued",
            "Queued",
        ]
    ),
)
@click.option("--filter-status-flag", type=click.Choice(["active", "creating", "deleted", "deleting", "failed"]))
@click.option("--filter-user-id", type=str, help="ID of the user.")
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_deleted,
    filter_group_id,
    filter_name,
    filter_region_id,
    filter_shared,
    filter_status,
    filter_status_flag,
    filter_user_id,
):
    """Get cluster list"""

    if filter_status_flag is not None:
        filter_status_flag = RhubApiLabClusterListClustersFilterStatusFlag(filter_status_flag)

    if filter_status is not None:
        filter_status = RhubApiLabClusterListClustersFilterStatus(filter_status)

    if sort is not None:
        sort = RhubApiLabClusterListClustersSort(sort)

    filter_ = RhubApiLabClusterListClustersFilter(
        deleted=filter_deleted,
        group_id=filter_group_id,
        name=filter_name,
        region_id=filter_region_id,
        shared=filter_shared,
        status=filter_status,
        status_flag=filter_status_flag,
        user_id=filter_user_id,
    )

    response = cluster_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@click.option("--name", required=True, type=str)
@click.option("--product-id", required=True, type=int)
@click.option("--product-params", required=True)
@click.option("--region-id", required=True, type=int)
@click.option("--description", type=str)
@click.option("--lifespan-expiration", type=click.DateTime(), help="Hard-limit expiration.")
@click.option("--project-id", type=int)
@click.option("--quota")
@click.option("--quota-usage")
@click.option("--reservation-expiration", type=click.DateTime(), help="Soft-limit expiration.")
@click.option("--shared", is_flag=True)
@click.option(
    "--status",
    type=click.Choice(
        [
            "Active",
            "Create Failed",
            "Deleted",
            "Delete Failed",
            "Deleting",
            "Deletion Failed",
            "Deletion Queued",
            "Installation Failed",
            "Installation Queued",
            "Installing",
            "Post-Deleting",
            "Post-Deletion Failed",
            "Post-Deletion Queued",
            "Post-Installation Failed",
            "Post-Installation Queued",
            "Post-Installing",
            "Post-Provisioning",
            "Post-Provisioning Failed",
            "Post-Provisioning Queued",
            "Pre-Deleting",
            "Pre-Deletion Failed",
            "Pre-Deletion Queued",
            "Pre-Installation Failed",
            "Pre-Installation Queued",
            "Pre-Installing",
            "Pre-Provisioning",
            "Pre-Provisioning Failed",
            "Pre-Provisioning Queued",
            "Provisioning",
            "Provisioning Failed",
            "Provisioning Queued",
            "Queued",
        ]
    ),
)
@pass_api
def create(
    api: APIRequest,
    name,
    product_id,
    product_params,
    region_id,
    description,
    lifespan_expiration,
    project_id,
    quota,
    quota_usage,
    reservation_expiration,
    shared,
    status,
):
    """Create cluster"""

    if status is not None:
        status = RhubApiLabClusterCreateClusterJsonBodyStatus(status)

    if product_params is None:
        product_params = UNSET
    else:
        _tmp = RhubApiLabClusterCreateClusterJsonBodyProductParams()
        _tmp.additional_properties = json.loads(product_params)  # TODO: check if dict
        product_params = _tmp

    json_body = RhubApiLabClusterCreateClusterJsonBody(
        name=name,
        product_id=product_id,
        product_params=product_params,
        region_id=region_id,
        description=description,
        lifespan_expiration=lifespan_expiration,
        project_id=project_id,
        quota=quota,
        quota_usage=quota_usage,
        reservation_expiration=reservation_expiration,
        shared=shared,
        status=status,
    )

    response = cluster_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@click.argument("cluster_id", type=int)
@pass_api
def get(
    api: APIRequest,
    cluster_id,
):
    """Get cluster"""

    response = cluster_get(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@click.argument("cluster_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    cluster_id,
):
    """Delete cluster"""

    response = cluster_remove(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@cluster.command()
@click.argument("cluster_id", type=int)
@click.option("--description", type=str)
@click.option("--lifespan-expiration", type=click.DateTime(), help="Hard-limit expiration.")
@click.option("--name", type=str)
@click.option("--product-id", type=int)
@click.option("--product-params")
@click.option("--project-id", type=int)
@click.option("--quota")
@click.option("--quota-usage")
@click.option("--region-id", type=int)
@click.option("--reservation-expiration", type=click.DateTime(), help="Soft-limit expiration.")
@click.option("--shared", is_flag=True)
@click.option(
    "--status",
    type=click.Choice(
        [
            "Active",
            "Create Failed",
            "Deleted",
            "Delete Failed",
            "Deleting",
            "Deletion Failed",
            "Deletion Queued",
            "Installation Failed",
            "Installation Queued",
            "Installing",
            "Post-Deleting",
            "Post-Deletion Failed",
            "Post-Deletion Queued",
            "Post-Installation Failed",
            "Post-Installation Queued",
            "Post-Installing",
            "Post-Provisioning",
            "Post-Provisioning Failed",
            "Post-Provisioning Queued",
            "Pre-Deleting",
            "Pre-Deletion Failed",
            "Pre-Deletion Queued",
            "Pre-Installation Failed",
            "Pre-Installation Queued",
            "Pre-Installing",
            "Pre-Provisioning",
            "Pre-Provisioning Failed",
            "Pre-Provisioning Queued",
            "Provisioning",
            "Provisioning Failed",
            "Provisioning Queued",
            "Queued",
        ]
    ),
)
@pass_api
def update(
    api: APIRequest,
    cluster_id,
    description,
    lifespan_expiration,
    name,
    product_id,
    product_params,
    project_id,
    quota,
    quota_usage,
    region_id,
    reservation_expiration,
    shared,
    status,
):
    """Update cluster"""

    if status is not None:
        status = RhubApiLabClusterUpdateClusterJsonBodyStatus(status)

    if product_params is None:
        product_params = UNSET
    else:
        _tmp = RhubApiLabClusterUpdateClusterJsonBodyProductParams()
        _tmp.additional_properties = json.loads(product_params)  # TODO: check if dict
        product_params = _tmp

    json_body = RhubApiLabClusterUpdateClusterJsonBody(
        description=description,
        lifespan_expiration=lifespan_expiration,
        name=name,
        product_id=product_id,
        product_params=product_params,
        project_id=project_id,
        quota=quota,
        quota_usage=quota_usage,
        region_id=region_id,
        reservation_expiration=reservation_expiration,
        shared=shared,
        status=status,
    )

    response = cluster_update(
        cluster_id=cluster_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


cluster.add_command(events)
cluster.add_command(hosts)
cluster.add_command(reboot)

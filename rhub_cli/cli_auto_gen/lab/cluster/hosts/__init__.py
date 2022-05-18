import json

import click

from rhub_cli.api.lab.rhub_api_lab_cluster_create_cluster_hosts import sync_detailed as hosts_create
from rhub_cli.api.lab.rhub_api_lab_cluster_delete_cluster_hosts import sync_detailed as hosts_remove
from rhub_cli.api.lab.rhub_api_lab_cluster_list_cluster_hosts import sync_detailed as hosts_get_list
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_hosts_json_body_item import (
    RhubApiLabClusterCreateClusterHostsJsonBodyItem,
)
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_hosts_json_body_item_cluster_id import (
    RhubApiLabClusterCreateClusterHostsJsonBodyItemClusterId,
)
from rhub_cli.models.rhub_api_lab_cluster_create_cluster_hosts_json_body_item_id import (
    RhubApiLabClusterCreateClusterHostsJsonBodyItemId,
)
from rhub_cli.types import UNSET


@click.group()
def hosts():
    pass


@hosts.command()
@click.argument("cluster_id", type=int)
@pass_api
def get_list(
    api: APIRequest,
    cluster_id,
):
    """Get cluster hosts"""

    response = hosts_get_list(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@hosts.command()
@click.argument("cluster_id", type=int)
@click.option("--json-body-item-fqdn", required=True, type=str)
@click.option("--json-body-item-ipaddr-item", required=True, type=str)
@click.option("--json-body-item-cluster-id")
@click.option("--json-body-item-id")
@click.option("--json-body-item-num-vcpus", type=int)
@click.option("--json-body-item-num-volumes", type=int)
@click.option("--json-body-item-ram-mb", type=int)
@click.option("--json-body-item-volumes-gb", type=int)
@pass_api
def create(
    api: APIRequest,
    cluster_id,
    json_body_item_fqdn,
    json_body_item_ipaddr_item,
    json_body_item_cluster_id,
    json_body_item_id,
    json_body_item_num_vcpus,
    json_body_item_num_volumes,
    json_body_item_ram_mb,
    json_body_item_volumes_gb,
):
    """Create or update cluster hosts"""

    if json_body_item_id is None:
        json_body_item_id = UNSET
    else:
        _tmp = RhubApiLabClusterCreateClusterHostsJsonBodyItemId()
        _tmp.additional_properties = json.loads(json_body_item_id)  # TODO: check if dict
        json_body_item_id = _tmp

    if json_body_item_cluster_id is None:
        json_body_item_cluster_id = UNSET
    else:
        _tmp = RhubApiLabClusterCreateClusterHostsJsonBodyItemClusterId()
        _tmp.additional_properties = json.loads(json_body_item_cluster_id)  # TODO: check if dict
        json_body_item_cluster_id = _tmp

    json_body_item_ipaddr = []
    if json_body_item_ipaddr_item is not None:
        json_body_item_ipaddr.append(json_body_item_ipaddr_item)

    json_body_item = RhubApiLabClusterCreateClusterHostsJsonBodyItem(
        fqdn=json_body_item_fqdn,
        ipaddr=json_body_item_ipaddr,
        cluster_id=json_body_item_cluster_id,
        id=json_body_item_id,
        num_vcpus=json_body_item_num_vcpus,
        num_volumes=json_body_item_num_volumes,
        ram_mb=json_body_item_ram_mb,
        volumes_gb=json_body_item_volumes_gb,
    )

    json_body = []
    if json_body_item is not None:
        json_body.append(json_body_item)

    response = hosts_create(
        cluster_id=cluster_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@hosts.command()
@click.argument("cluster_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    cluster_id,
):
    """Delete cluster hosts"""

    response = hosts_remove(
        cluster_id=cluster_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)

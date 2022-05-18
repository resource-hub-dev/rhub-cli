import click

from rhub_cli.api.lab.rhub_api_lab_cluster_reboot_hosts import sync_detailed as reboot_create
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_lab_cluster_reboot_hosts_json_body import RhubApiLabClusterRebootHostsJsonBody
from rhub_cli.models.rhub_api_lab_cluster_reboot_hosts_json_body_type import RhubApiLabClusterRebootHostsJsonBodyType


@click.group()
def reboot():
    pass


@reboot.command()
@click.argument("cluster_id", type=int)
@click.option("--hosts")
@click.option("--type", default=RhubApiLabClusterRebootHostsJsonBodyType.SOFT, type=click.Choice(["soft", "hard"]))
@pass_api
def create(
    api: APIRequest,
    cluster_id,
    hosts,
    type,
):
    """Reboot cluster hosts"""

    if type is not None:
        type = RhubApiLabClusterRebootHostsJsonBodyType(type)

    json_body = RhubApiLabClusterRebootHostsJsonBody(
        hosts=hosts,
        type=type,
    )

    response = reboot_create(
        cluster_id=cluster_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

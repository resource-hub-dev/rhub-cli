import click

from rhub_cli.api.tower.rhub_api_tower_webhook_notification import sync_detailed as webhook_notification_create
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_tower_webhook_notification_json_body import RhubApiTowerWebhookNotificationJsonBody
from rhub_cli.models.rhub_api_tower_webhook_notification_json_body_hosts import (
    RhubApiTowerWebhookNotificationJsonBodyHosts,
)
from rhub_cli.models.rhub_api_tower_webhook_notification_json_body_hosts_additional_property import (
    RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalProperty,
)
from rhub_cli.models.rhub_api_tower_webhook_notification_json_body_hosts_additional_property_localhost import (
    RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost,
)


@click.group()
def webhook_notification():
    pass


@webhook_notification.command()
@click.option(
    "--body",
    type=str,
    help="Enumerates all the nodes in the workflow job with a description of the job associated with each",
)
@click.option("--created-by", type=str)
@click.option("--credential", type=str, help="Credential used by Job")
@click.option("--extra-vars", type=str, help="Extra variables for playbook encoded as a dictionary within a string")
@click.option("--finished", type=click.DateTime(), help="Date/Time job finished")
@click.option("--id", type=int, help="jobId")
@click.option("--inventory", type=str, help="Inventory used by Job")
@click.option("--limit", type=str, help="Job limit")
@click.option("--name", type=str, help="jobName")
@click.option("--playbook", type=str, help="Playbook executed in Job")
@click.option("--project", type=str, help="Project job belongs to")
@click.option("--started", type=click.DateTime(), help="Date/Time job started")
@click.option("--status", type=str, help="Job status")
@click.option("--traceback", type=str, help="Traceback if failed")
@click.option("--url", type=str, help="URL to Job on Tower")
@click.option("--hosts-additional-property-localhost-changed", type=int)
@click.option("--hosts-additional-property-localhost-dark", type=int)
@click.option("--hosts-additional-property-localhost-failed", is_flag=True)
@click.option("--hosts-additional-property-localhost-failures", type=int)
@click.option("--hosts-additional-property-localhost-ignored", type=int)
@click.option("--hosts-additional-property-localhost-ok", type=int)
@click.option("--hosts-additional-property-localhost-processed", type=int)
@click.option("--hosts-additional-property-localhost-rescued", type=int)
@click.option("--hosts-additional-property-localhost-skipped", type=int)
@pass_api
def create(
    api: APIRequest,
    body,
    created_by,
    credential,
    extra_vars,
    finished,
    id,
    inventory,
    limit,
    name,
    playbook,
    project,
    started,
    status,
    traceback,
    url,
    hosts_additional_property_localhost_changed,
    hosts_additional_property_localhost_dark,
    hosts_additional_property_localhost_failed,
    hosts_additional_property_localhost_failures,
    hosts_additional_property_localhost_ignored,
    hosts_additional_property_localhost_ok,
    hosts_additional_property_localhost_processed,
    hosts_additional_property_localhost_rescued,
    hosts_additional_property_localhost_skipped,
):
    """Incoming webhook notification from Tower"""

    hosts_additional_property_localhost = RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalPropertyLocalhost(
        changed=hosts_additional_property_localhost_changed,
        dark=hosts_additional_property_localhost_dark,
        failed=hosts_additional_property_localhost_failed,
        failures=hosts_additional_property_localhost_failures,
        ignored=hosts_additional_property_localhost_ignored,
        ok=hosts_additional_property_localhost_ok,
        processed=hosts_additional_property_localhost_processed,
        rescued=hosts_additional_property_localhost_rescued,
        skipped=hosts_additional_property_localhost_skipped,
    )

    hosts_additional_property = RhubApiTowerWebhookNotificationJsonBodyHostsAdditionalProperty(
        localhost=hosts_additional_property_localhost,
    )

    hosts = RhubApiTowerWebhookNotificationJsonBodyHosts()
    hosts.additional_properties = {"hosts": hosts_additional_property}

    json_body = RhubApiTowerWebhookNotificationJsonBody(
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

    response = webhook_notification_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

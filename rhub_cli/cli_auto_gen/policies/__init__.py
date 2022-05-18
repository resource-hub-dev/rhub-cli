import json

import click

from rhub_cli.api.policy.rhub_api_policies_create_policy import sync_detailed as policies_create
from rhub_cli.api.policy.rhub_api_policies_delete_policy import sync_detailed as policies_remove
from rhub_cli.api.policy.rhub_api_policies_get_policy import sync_detailed as policies_get
from rhub_cli.api.policy.rhub_api_policies_list_policies import sync_detailed as policies_get_list
from rhub_cli.api.policy.rhub_api_policies_update_policy import sync_detailed as policies_update
from rhub_cli.api_request import APIRequest, pass_api
from rhub_cli.models.rhub_api_policies_create_policy_json_body import RhubApiPoliciesCreatePolicyJsonBody
from rhub_cli.models.rhub_api_policies_create_policy_json_body_constraint import (
    RhubApiPoliciesCreatePolicyJsonBodyConstraint,
)
from rhub_cli.models.rhub_api_policies_create_policy_json_body_constraint_limit import (
    RhubApiPoliciesCreatePolicyJsonBodyConstraintLimit,
)
from rhub_cli.models.rhub_api_policies_create_policy_json_body_id import RhubApiPoliciesCreatePolicyJsonBodyId
from rhub_cli.models.rhub_api_policies_list_policies_filter import RhubApiPoliciesListPoliciesFilter
from rhub_cli.models.rhub_api_policies_list_policies_sort import RhubApiPoliciesListPoliciesSort
from rhub_cli.models.rhub_api_policies_update_policy_json_body import RhubApiPoliciesUpdatePolicyJsonBody
from rhub_cli.models.rhub_api_policies_update_policy_json_body_constraint import (
    RhubApiPoliciesUpdatePolicyJsonBodyConstraint,
)
from rhub_cli.models.rhub_api_policies_update_policy_json_body_constraint_limit import (
    RhubApiPoliciesUpdatePolicyJsonBodyConstraintLimit,
)
from rhub_cli.models.rhub_api_policies_update_policy_json_body_id import RhubApiPoliciesUpdatePolicyJsonBodyId
from rhub_cli.types import UNSET


@click.group()
def policies():
    pass


@policies.command()
@click.option("--sort", type=click.Choice(["name", "-name", "department", "-department"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option(
    "--filter-department",
    type=str,
    help="Department of a policy. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@click.option(
    "--filter-name",
    type=str,
    help="Name of a policy. Wildcard ``%`` can be used to match zero, one, or multiple characters",
)
@pass_api
def get_list(
    api: APIRequest,
    sort,
    page,
    limit,
    filter_department,
    filter_name,
):
    """Get policy list"""

    if sort is not None:
        sort = RhubApiPoliciesListPoliciesSort(sort)

    filter_ = RhubApiPoliciesListPoliciesFilter(
        department=filter_department,
        name=filter_name,
    )

    response = policies_get_list(
        filter_=filter_,
        sort=sort,
        page=page,
        limit=limit,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@policies.command()
@click.option("--department", required=True, type=str, help="Department Name")
@click.option("--name", required=True, type=str, help="Name")
@click.option("--id", help="Internal ID")
@click.option("--constraint-cost", type=float)
@click.option("--constraint-density", type=str)
@click.option("--constraint-limit")
@click.option("--constraint-location")
@click.option("--constraint-location-id")
@click.option("--constraint-sched-avail-item", type=click.DateTime())
@click.option("--constraint-serv-avail", type=float)
@click.option("--constraint-tag-item", type=str)
@pass_api
def create(
    api: APIRequest,
    department,
    name,
    id,
    constraint_cost,
    constraint_density,
    constraint_limit,
    constraint_location,
    constraint_location_id,
    constraint_sched_avail_item,
    constraint_serv_avail,
    constraint_tag_item,
):
    """Create policy"""

    constraint_tag = []
    if constraint_tag_item is not None:
        constraint_tag.append(constraint_tag_item)

    constraint_sched_avail = []
    if constraint_sched_avail_item is not None:
        constraint_sched_avail.append(constraint_sched_avail_item)

    if constraint_limit is None:
        constraint_limit = UNSET
    else:
        _tmp = RhubApiPoliciesCreatePolicyJsonBodyConstraintLimit()
        _tmp.additional_properties = json.loads(constraint_limit)  # TODO: check if dict
        constraint_limit = _tmp

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiPoliciesCreatePolicyJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    constraint = RhubApiPoliciesCreatePolicyJsonBodyConstraint(
        cost=constraint_cost,
        density=constraint_density,
        limit=constraint_limit,
        location=constraint_location,
        location_id=constraint_location_id,
        sched_avail=constraint_sched_avail,
        serv_avail=constraint_serv_avail,
        tag=constraint_tag,
    )

    json_body = RhubApiPoliciesCreatePolicyJsonBody(
        department=department,
        name=name,
        constraint=constraint,
        id=id,
    )

    response = policies_create(
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@policies.command()
@click.argument("policy_id", type=int)
@pass_api
def get(
    api: APIRequest,
    policy_id,
):
    """Get policy"""

    response = policies_get(
        policy_id=policy_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@policies.command()
@click.argument("policy_id", type=int)
@pass_api
def remove(
    api: APIRequest,
    policy_id,
):
    """Delete policy"""

    response = policies_remove(
        policy_id=policy_id,
        client=api.authenticated_client,
    )
    api.handle_response(response)


@policies.command()
@click.argument("policy_id", type=int)
@click.option("--department", type=str, help="Department Name")
@click.option("--id", help="Internal ID")
@click.option("--name", type=str, help="Name")
@click.option("--constraint-cost", type=float)
@click.option("--constraint-density", type=str)
@click.option("--constraint-limit")
@click.option("--constraint-location")
@click.option("--constraint-location-id")
@click.option("--constraint-sched-avail-item", type=click.DateTime())
@click.option("--constraint-serv-avail", type=float)
@click.option("--constraint-tag-item", type=str)
@pass_api
def update(
    api: APIRequest,
    policy_id,
    department,
    id,
    name,
    constraint_cost,
    constraint_density,
    constraint_limit,
    constraint_location,
    constraint_location_id,
    constraint_sched_avail_item,
    constraint_serv_avail,
    constraint_tag_item,
):
    """Update policy"""

    constraint_tag = []
    if constraint_tag_item is not None:
        constraint_tag.append(constraint_tag_item)

    constraint_sched_avail = []
    if constraint_sched_avail_item is not None:
        constraint_sched_avail.append(constraint_sched_avail_item)

    if constraint_limit is None:
        constraint_limit = UNSET
    else:
        _tmp = RhubApiPoliciesUpdatePolicyJsonBodyConstraintLimit()
        _tmp.additional_properties = json.loads(constraint_limit)  # TODO: check if dict
        constraint_limit = _tmp

    if id is None:
        id = UNSET
    else:
        _tmp = RhubApiPoliciesUpdatePolicyJsonBodyId()
        _tmp.additional_properties = json.loads(id)  # TODO: check if dict
        id = _tmp

    constraint = RhubApiPoliciesUpdatePolicyJsonBodyConstraint(
        cost=constraint_cost,
        density=constraint_density,
        limit=constraint_limit,
        location=constraint_location,
        location_id=constraint_location_id,
        sched_avail=constraint_sched_avail,
        serv_avail=constraint_serv_avail,
        tag=constraint_tag,
    )

    json_body = RhubApiPoliciesUpdatePolicyJsonBody(
        constraint=constraint,
        department=department,
        id=id,
        name=name,
    )

    response = policies_update(
        policy_id=policy_id,
        json_body=json_body,
        client=api.authenticated_client,
    )
    api.handle_response(response)

import click

from .hosts import hosts
from .metrics import metrics
from .power_states_metrics import power_states_metrics


@click.group()
def bm():
    pass


bm.add_command(hosts)
bm.add_command(metrics)
bm.add_command(power_states_metrics)

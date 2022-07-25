from rhub_cli.cli_main import cli

from .auth import auth
from .bare_metal import bare_metal
from .cowsay import cowsay
from .dns import dns
from .lab import lab
from .me import me
from .monitor import monitor
from .openstack import openstack
from .ping import ping
from .policies import policies
from .satellite import satellite
from .scheduler import scheduler
from .tower import tower

cli.add_command(auth)
cli.add_command(bare_metal)
cli.add_command(cowsay)
cli.add_command(dns)
cli.add_command(lab)
cli.add_command(me)
cli.add_command(monitor)
cli.add_command(openstack)
cli.add_command(ping)
cli.add_command(policies)
cli.add_command(satellite)
cli.add_command(scheduler)
cli.add_command(tower)

from rhub_cli.cli_main import cli

from .auth import auth
from .cowsay import cowsay
from .lab import lab
from .me import me
from .ping import ping
from .policies import policies
from .scheduler import scheduler
from .tower import tower

cli.add_command(auth)
cli.add_command(cowsay)
cli.add_command(lab)
cli.add_command(me)
cli.add_command(ping)
cli.add_command(policies)
cli.add_command(scheduler)
cli.add_command(tower)

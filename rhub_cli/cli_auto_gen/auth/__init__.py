import click

from .group import group
from .role import role
from .token import token
from .user import user


@click.group()
def auth():
    pass


auth.add_command(group)
auth.add_command(role)
auth.add_command(token)
auth.add_command(user)

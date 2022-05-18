import pathlib
from typing import Optional

import click

from .api_request import APIRequest

CONTEXT_SETTINGS = dict(
    help_option_names=["-h", "--help"],
    show_default=True,
    max_content_width=100000,
)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--base-url",  # TODO: add type
    envvar="BASE_URL",
    metavar="URL",
    help="Base URL used for API calls.",
)
@click.option(
    "--user",
    help="User used for authentication.",
)
@click.option(
    "--password",
    hide_input=True,
    help="Password used for authentication.",
)
@click.option(
    "--data-format",
    default=APIRequest.DEFAULT_FORMAT,
    type=click.Choice([APIRequest.DEFAULT_FORMAT, APIRequest.JSON_FORMAT, APIRequest.YAML_FORMAT]),
    help="Defines the output format.",
)
@click.option(
    "--output-file",
    type=click.Path(file_okay=True, writable=True, resolve_path=True, path_type=pathlib.Path),
    help="Output file.",
)
@click.option(
    "--pretty",
    is_flag=True,
    help="Uses pretty output.",
)
@click.version_option("0.1")
@click.pass_context
def cli(
    context,
    base_url: str,
    user: str,
    password: str,
    data_format: str,
    output_file: Optional[pathlib.Path],
    pretty: bool,
):
    """A client library for accessing Resource Hub"""
    context.obj = APIRequest(
        base_url=base_url, user=user, password=password, data_format=data_format, output_file=output_file, pretty=pretty
    )

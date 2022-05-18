import json
import pathlib
from pprint import pformat
from typing import Optional

import click
import httpx
import yaml

from .client import AuthenticatedClient, Client
from .types import Response


class APIRequest:
    # this class should be re-written for each CLI
    TIMEOUT = 5.0
    VERIFY_SSL = False
    INDENT_COUNT = 2
    DEFAULT_FORMAT = "python-str"
    JSON_FORMAT = "json"
    YAML_FORMAT = "yaml"

    def __init__(
        self,
        base_url: str,
        user: str,
        password: str,
        data_format: str,
        output_file: Optional[pathlib.Path],
        pretty: bool,
    ):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.data_format = data_format
        self.output_file = output_file
        self.pretty = pretty

        self.client = self._get_client()
        self.authenticated_client = self._get_authenticated_client()

    def _get_client(self) -> Client:
        return Client(base_url=self.base_url, timeout=self.TIMEOUT, verify_ssl=self.VERIFY_SSL)

    def _get_authenticated_client(self) -> AuthenticatedClient:
        # Needs further implementation
        response = httpx.post(
            url=f"{self.base_url}/auth/token/create",
            verify=self.VERIFY_SSL,
            auth=(self.user, self.password),
        )

        return AuthenticatedClient(
            base_url=self.base_url,
            token=response.json()["access_token"],
            timeout=self.TIMEOUT,
            verify_ssl=self.VERIFY_SSL,
        )

    def handle_response(self, response: Response):
        data = response
        if response.status_code == 200 and response.parsed:
            if isinstance(response.parsed, str):
                data = response.parsed
            else:
                data = response.parsed.to_dict()
                if self.data_format == self.DEFAULT_FORMAT and self.pretty:
                    data = pformat(data, indent=self.INDENT_COUNT)
                elif self.data_format == self.JSON_FORMAT:
                    data = json.dumps(
                        data,
                        indent=self.INDENT_COUNT if self.pretty else None,
                    )
                elif self.data_format == self.YAML_FORMAT:
                    data = yaml.dump(data, indent=self.INDENT_COUNT)
        if response.status_code == 204:
            data = f"Success - HTTP204"

        if self.output_file:
            self.output_file.write_text(data)
        else:
            click.echo(data)


pass_api = click.make_pass_decorator(APIRequest, ensure=True)

from enum import Enum


class RhubApiDnsServerListSort(str, Enum):
    HOSTNAME = "hostname"
    VALUE_1 = "-hostname"

    def __str__(self) -> str:
        return str(self.value)

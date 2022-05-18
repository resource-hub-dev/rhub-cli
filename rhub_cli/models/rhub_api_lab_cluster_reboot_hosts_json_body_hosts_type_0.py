from enum import Enum


class RhubApiLabClusterRebootHostsJsonBodyHostsType0(str, Enum):
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)

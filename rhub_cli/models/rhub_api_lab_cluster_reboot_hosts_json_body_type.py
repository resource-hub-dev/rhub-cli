from enum import Enum


class RhubApiLabClusterRebootHostsJsonBodyType(str, Enum):
    SOFT = "soft"
    HARD = "hard"

    def __str__(self) -> str:
        return str(self.value)

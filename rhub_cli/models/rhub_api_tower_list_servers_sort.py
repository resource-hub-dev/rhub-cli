from enum import Enum


class RhubApiTowerListServersSort(str, Enum):
    NAME = "name"
    VALUE_1 = "-name"

    def __str__(self) -> str:
        return str(self.value)

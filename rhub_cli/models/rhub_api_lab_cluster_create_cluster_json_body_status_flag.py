from enum import Enum


class RhubApiLabClusterCreateClusterJsonBodyStatusFlag(str, Enum):
    ACTIVE = "active"
    CREATING = "creating"
    DELETED = "deleted"
    DELETING = "deleting"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)

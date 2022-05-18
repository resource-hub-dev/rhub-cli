from enum import Enum


class RhubApiLabClusterListClustersSort(str, Enum):
    NAME = "name"
    VALUE_1 = "-name"
    RESERVATION_EXPIRATION = "reservation_expiration"
    VALUE_3 = "-reservation_expiration"
    LIFESPAN_EXPIRATION = "lifespan_expiration"
    VALUE_5 = "-lifespan_expiration"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class RhubApiLabRegionListRegionsSort(str, Enum):
    NAME = "name"
    VALUE_1 = "-name"
    LOCATION = "location"
    VALUE_3 = "-location"
    RESERVATION_EXPIRATION_MAX = "reservation_expiration_max"
    VALUE_5 = "-reservation_expiration_max"

    def __str__(self) -> str:
        return str(self.value)

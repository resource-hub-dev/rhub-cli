from enum import Enum


class RhubApiPoliciesListPoliciesSort(str, Enum):
    NAME = "name"
    VALUE_1 = "-name"
    DEPARTMENT = "department"
    VALUE_3 = "-department"

    def __str__(self) -> str:
        return str(self.value)

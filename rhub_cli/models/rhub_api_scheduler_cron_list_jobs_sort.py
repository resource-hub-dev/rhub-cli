from enum import Enum


class RhubApiSchedulerCronListJobsSort(str, Enum):
    NAME = "name"
    VALUE_1 = "-name"

    def __str__(self) -> str:
        return str(self.value)

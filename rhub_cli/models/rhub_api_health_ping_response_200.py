from enum import Enum


class RhubApiHealthPingResponse200(str, Enum):
    PONG = "pong"

    def __str__(self) -> str:
        return str(self.value)

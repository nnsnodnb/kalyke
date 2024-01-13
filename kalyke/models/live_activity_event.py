from enum import Enum


class LiveActivityEvent(Enum):
    START: str = "start"
    UPDATE: str = "update"
    END: str = "end"

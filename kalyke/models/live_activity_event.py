from enum import Enum


class LiveActivityEvent(Enum):
    start: str = "start"
    update: str = "update"
    end: str = "end"

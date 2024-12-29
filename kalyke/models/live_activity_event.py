from enum import Enum


class LiveActivityEvent(Enum):
    START = "start"
    UPDATE = "update"
    END = "end"

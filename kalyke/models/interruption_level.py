from enum import Enum


class InterruptionLevel(Enum):
    PASSIVE = "passive"
    ACTIVE = "active"
    TIME_SENSITIVE = "time-sensitive"
    CRITICAL = "critical"

from enum import Enum


class InterruptionLevel(Enum):
    PASSIVE: str = "passive"
    ACTIVE: str = "active"
    TIME_SENSITIVE: str = "time-sensitive"
    CRITICAL: str = "critical"

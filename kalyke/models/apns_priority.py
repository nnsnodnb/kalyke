from enum import Enum


class ApnsPriority(Enum):
    IMMEDIATELY: int = 10
    BASED_ON_POWER: int = 5
    POWER_CONSIDERATIONS_OVER_ALL_OTHER_FACTORS: int = 1

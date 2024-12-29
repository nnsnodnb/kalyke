from enum import Enum


class ApnsPriority(Enum):
    IMMEDIATELY = 10
    BASED_ON_POWER = 5
    POWER_CONSIDERATIONS_OVER_ALL_OTHER_FACTORS = 1

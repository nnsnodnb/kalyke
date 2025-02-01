from dataclasses import dataclass, field
from typing import Optional, Union

from ..exceptions import VolumeOutOfRangeException


@dataclass(frozen=True)
class CriticalSound:
    critical: bool
    volume: float
    name: Optional[str] = field(default=None)

    def __post_init__(self):
        if 0.0 <= self.volume <= 1.0:
            pass
        else:
            raise VolumeOutOfRangeException(volume=self.volume)

    def dict(self) -> dict[str, Union[int, str, float]]:
        sound: dict[str, Union[int, str, float]] = {
            "critical": int(self.critical),
            "volume": self.volume,
        }
        if self.name:
            sound["name"] = self.name

        return sound

from typing import Dict, Optional, Union

from ..exceptions import VolumeOutOfRangeException


class CriticalSound:
    _critical: int
    name: Optional[str]
    volume: Optional[float]

    def __init__(
        self,
        critical: bool = False,
        name: Optional[str] = None,
        volume: Optional[float] = 1.0,
    ) -> None:
        self._critical = int(critical)
        self.name = name
        if 0.0 <= volume <= 1.0:
            self.volume = volume
        else:
            raise VolumeOutOfRangeException(volume=volume)

    @property
    def critical(self) -> bool:
        return bool(self._critical)

    def dict(self) -> Dict[str, Union[str, float]]:
        sound: Dict[str, Union[str, float]] = {
            "critical": self._critical
        }
        if self.name:
            sound["name"] = self.name
        if self.volume:
            sound["volume"] = self.volume

        return sound

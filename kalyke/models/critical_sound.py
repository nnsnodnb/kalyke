from typing import Dict, Optional, Union

from ..exceptions import VolumeOutOfRangeException


class CriticalSound:
    _critical: int
    name: Optional[str]
    volume: float

    def __init__(
        self,
        critical: bool,
        volume: float,
        name: Optional[str] = None,
    ) -> None:
        self._critical = int(critical)
        if 0.0 <= volume <= 1.0:
            self.volume = volume
        else:
            raise VolumeOutOfRangeException(volume=volume)
        self.name = name

    @property
    def critical(self) -> bool:
        return bool(self._critical)

    def dict(self) -> Dict[str, Union[int, str, float]]:
        sound: Dict[str, Union[int, str, float]] = {
            "critical": self._critical,
            "volume": self.volume,
        }
        if self.name:
            sound["name"] = self.name

        return sound

class VolumeOutOfRangeException(Exception):
    _volume: float

    def __init__(self, volume: float) -> None:
        self._volume = volume

    def __str__(self) -> str:
        return (
            f"The volume must be a value between 0.0 and 1.0. Did set {self._volume}."
        )

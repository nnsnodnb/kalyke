import time
import uuid
from dataclasses import dataclass, field

import httpx

from .apns_priority import ApnsPriority
from .apns_push_type import ApnsPushType


@dataclass(frozen=True)
class ApnsConfig:
    topic: str
    push_type: ApnsPushType = field(default=ApnsPushType.ALERT)
    identifier: str | None = field(default=None)
    priority: ApnsPriority = field(default=ApnsPriority.IMMEDIATELY)
    expiration: int = field(default_factory=lambda: int(time.time()) + 2592000)
    collapse_id: str | None = field(default=None)

    def __post_init__(self):
        if self.identifier:
            try:
                _ = uuid.UUID(hex=self.identifier, version=4)
            except ValueError as e:
                raise ValueError(f"{self.identifier} is invalid format.") from e

    def make_headers(self) -> dict[str, str]:
        headers: dict[str, str | None] = {
            "apns-push-type": self.push_type.value,
            "apns-id": self.identifier,
            "apns-expiration": str(self.expiration),
            "apns-priority": str(self.priority.value),
            "apns-topic": self.topic,
            "apns-collapse-id": self.collapse_id,
            "user-agent": f"python-httpx/{httpx.__version__} {self.topic}",
        }
        attached_headers: dict[str, str] = {k: v for k, v in headers.items() if v is not None}
        return attached_headers


@dataclass(frozen=True)
class LiveActivityApnsConfig(ApnsConfig):  # type: ignore[override]
    push_type: ApnsPushType = field(default=ApnsPushType.LIVEACTIVITY, init=False)

    def __post_init__(self):
        if not self.topic.endswith(".push-type.liveactivity"):
            raise ValueError(f"topic must end with .push-type.liveactivity, but {self.topic}.")
        if self.priority == ApnsPriority.POWER_CONSIDERATIONS_OVER_ALL_OTHER_FACTORS:
            raise ValueError("priority must be BASED_ON_POWER or IMMEDIATELY.")
        super().__post_init__()


@dataclass(frozen=True)
class VoIPApnsConfig(ApnsConfig):  # type: ignore[override]
    push_type: ApnsPushType = field(default=ApnsPushType.VOIP, init=False)

    def __post_init__(self):
        if not self.topic.endswith(".voip"):
            raise ValueError(f"topic must end with .voip, but {self.topic}.")
        super().__post_init__()

from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Union

from ..exceptions import RelevanceScoreOutOfRangeException
from .critical_sound import CriticalSound
from .interruption_level import InterruptionLevel
from .payload_alert import PayloadAlert


@dataclass(frozen=True)
class Payload:
    alert: Optional[Union[str, PayloadAlert]] = field(default=None)
    badge: Optional[int] = field(default=None)
    sound: Optional[Union[str, CriticalSound]] = field(default=None)
    thread_id: Optional[str] = field(default=None)
    category: Optional[str] = field(default=None)
    content_available: bool = field(default=False)
    mutable_content: bool = field(default=False)
    target_content_identifier: Optional[str] = field(default=None)
    interruption_level: Optional[InterruptionLevel] = field(default=None)
    relevance_score: Optional[float] = field(default=None)
    filter_criteria: Optional[str] = field(default=None)
    custom: Optional[Dict[str, Any]] = field(default=None)

    def __post_init__(self):
        if self.relevance_score:
            if 0.0 <= self.relevance_score <= 1.0:
                pass
            else:
                raise RelevanceScoreOutOfRangeException(relevance_score=self.relevance_score)

    def dict(self) -> Dict[str, Any]:
        aps: Dict[str, Any] = {
            "alert": self.alert.dict() if isinstance(self.alert, PayloadAlert) else self.alert,
            "badge": self.badge,
            "sound": self.sound,
            "thread-id": self.thread_id,
            "category": self.category,
            "target-content-identifier": self.target_content_identifier,
            "relevance-score": self.relevance_score,
            "filter-criteria": self.filter_criteria,
        }
        if self.content_available:
            aps["content-available"] = 1
        if self.mutable_content:
            aps["mutable-content"] = 1
        if self.interruption_level is not None:
            aps["interruption-level"] = self.interruption_level.value
        aps = {k: v for k, v in aps.items() if v is not None}
        payload = {
            "aps": aps,
        }
        if self.custom:
            payload.update(self.custom)

        return payload

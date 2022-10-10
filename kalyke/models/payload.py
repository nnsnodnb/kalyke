from typing import Any, Dict, Optional, Union

from .critical_sound import CriticalSound
from .interruption_level import InterruptionLevel
from .payload_alert import PayloadAlert
from ..exceptions import RelevanceScoreOutOfRangeException


class Payload:
    alert: Optional[Union[str, PayloadAlert]]
    badge: Optional[int]
    sound: Optional[Union[str, CriticalSound]]
    thread_id: Optional[str]
    category: Optional[str]
    _content_available: int
    _mutable_content: int
    target_content_identifier: Optional[str]
    interruption_level: InterruptionLevel
    relevance_score: Optional[float]
    filter_criteria: Optional[str]
    custom: Optional[Dict[str, Any]]

    def __init__(
        self,
        alert: Optional[Union[str, PayloadAlert]] = None,
        badge: Optional[int] = None,
        sound: Optional[Union[str, CriticalSound]] = None,
        thread_id: Optional[str] = None,
        category: Optional[str] = None,
        content_available: bool = False,
        mutable_content: bool = False,
        target_content_identifier: Optional[str] = None,
        interruption_level: InterruptionLevel = InterruptionLevel.ACTIVE,
        relevance_score: Optional[float] = None,
        filter_criteria: Optional[str] = None,
        custom: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.alert = alert
        self.badge = badge
        self.sound = sound
        self.thread_id = thread_id
        self.category = category
        self._content_available = int(content_available)
        self._mutable_content = int(mutable_content)
        self.target_content_identifier = target_content_identifier
        self.interruption_level = interruption_level
        if relevance_score:
            if 0.0 <= relevance_score <= 1.0:
                self.relevance_score = relevance_score
            else:
                raise RelevanceScoreOutOfRangeException(relevance_score=relevance_score)
        else:
            self.relevance_score = relevance_score
        self.filter_criteria = filter_criteria
        self.custom = custom

    @property
    def content_available(self) -> bool:
        return bool(self._content_available)

    @property
    def mutable_content(self) -> bool:
        return bool(self._mutable_content)

    def dict(self) -> Dict[str, Any]:
        aps = {
            "alert": self.alert.dict()
            if isinstance(self.alert, PayloadAlert)
            else self.alert,
            "badge": self.badge,
            "sound": self.sound,
            "thread-id": self.thread_id,
            "category": self.category,
            "content-available": self._content_available,
            "mutable-content": self._mutable_content,
            "target-content-identifier": self.target_content_identifier,
            "interruption-level": self.interruption_level.value,
            "relevance-score": self.relevance_score,
            "filter-criteria": self.filter_criteria,
        }
        aps = {k: v for k, v in aps.items() if v is not None}
        payload = {
            "aps": aps,
        }
        if self.custom:
            payload.update(self.custom)

        return payload

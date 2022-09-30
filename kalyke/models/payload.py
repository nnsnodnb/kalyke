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
        if 0.0 <= relevance_score <= 1.0:
            self.relevance_score = relevance_score
        else:
            raise RelevanceScoreOutOfRangeException(relevance_score=relevance_score)
        self.filter_criteria = filter_criteria

    @property
    def content_available(self) -> bool:
        return bool(self._content_available)

    @property
    def mutable_content(self) -> bool:
        return bool(self._mutable_content)

    def dict(self) -> Dict[str, Any]:
        payload: Dict[str, Any] = {}
        if self.alert:
            payload["alert"] = self.alert.dict() if isinstance(self.alert, PayloadAlert) else self.alert
        if self.badge:
            payload["badge"] = self.badge
        if self.sound:
            payload["sound"] = self.sound.dict() if isinstance(self.sound, CriticalSound) else self.sound
        if self.thread_id:
            payload["thread-id"] = self.thread_id
        if self.category:
            payload["category"] = self.category
        payload["content-available"] = self._content_available
        payload["mutable-content"] = self._mutable_content
        if self.target_content_identifier:
            payload["target-content-identifier"] = self.target_content_identifier
        payload["interruption-level"] = self.interruption_level.value
        if self.relevance_score:
            payload["relevance-score"] = self.relevance_score
        if self.filter_criteria:
            payload["filter-criteria"] = self.filter_criteria

        return payload

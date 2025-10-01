import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from ..exceptions import (
    LiveActivityAttributesIsNotJSONSerializable,
    LiveActivityContentStateIsNotJSONSerializable,
    RelevanceScoreOutOfRangeException,
)
from .critical_sound import CriticalSound
from .interruption_level import InterruptionLevel
from .live_activity_event import LiveActivityEvent
from .payload_alert import PayloadAlert


@dataclass(frozen=True)
class Payload:
    alert: str | PayloadAlert | None = field(default=None)
    badge: int | None = field(default=None)
    sound: str | CriticalSound | None = field(default=None)
    thread_id: str | None = field(default=None)
    category: str | None = field(default=None)
    content_available: bool = field(default=False)
    mutable_content: bool = field(default=False)
    target_content_identifier: str | None = field(default=None)
    interruption_level: InterruptionLevel | None = field(default=None)
    relevance_score: float | None = field(default=None)
    filter_criteria: str | None = field(default=None)
    custom: dict[str, Any] | None = field(default=None)

    def __post_init__(self):
        if self.relevance_score:
            self._validate_relevance_score()

    def _validate_relevance_score(self):
        if 0.0 <= self.relevance_score <= 1.0:
            pass
        else:
            raise RelevanceScoreOutOfRangeException(relevance_score=self.relevance_score)

    def dict(self) -> dict[str, Any]:
        aps: dict[str, Any] = {
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


@dataclass(frozen=True)
class LiveActivityPayload(Payload):
    timestamp: datetime = field(default_factory=datetime.now)
    event: LiveActivityEvent = field(default=LiveActivityEvent.UPDATE)
    content_state: dict[str, Any] = field(default_factory=dict)
    stale_date: datetime | None = field(default=None)
    dismissal_date: datetime | None = field(default=None)
    attributes_type: str | None = field(default=None)
    attributes: dict[str, Any] | None = field(default=None)

    def __post_init__(self):
        if self.event == LiveActivityEvent.START:
            self._validate_event_is_start()
        try:
            _ = json.dumps(self.content_state)
        except TypeError as e:
            raise LiveActivityContentStateIsNotJSONSerializable() from e
        super().__post_init__()

    def _validate_relevance_score(self):
        # You can set any Double value; for example, 25, 50, 75, or 100.
        pass

    def _validate_event_is_start(self):
        if self.attributes_type is None or self.attributes is None:
            raise ValueError(
                "attributes_type and attributes must be specified when event is start.\nPlease see documentation: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification"  # noqa: E501
            )
        try:
            _ = json.dumps(self.attributes)
        except TypeError as e:
            raise LiveActivityAttributesIsNotJSONSerializable() from e

    def dict(self) -> dict[str, Any]:
        payload = super().dict()
        additional: dict[str, Any | None] = {
            "timestamp": int(self.timestamp.timestamp()),
            "event": self.event.value,
            "content-state": self.content_state,
            "state-date": int(self.stale_date.timestamp()) if self.stale_date else None,
            "dismissal-date": int(self.dismissal_date.timestamp()) if self.dismissal_date else None,
        }
        additional = {k: v for k, v in additional.items() if v is not None}
        payload["aps"].update(additional)

        return payload

import time
import uuid
from typing import Dict, Optional

import httpx

from .apns_priority import ApnsPriority
from .apns_push_type import ApnsPushType


class ApnsConfig:
    topic: str
    push_type: ApnsPushType
    identifier: Optional[str]
    expiration: int
    priority: int
    collapse_id: Optional[str]

    def __init__(
        self,
        topic: str,
        push_type: ApnsPushType = ApnsPushType.ALERT,
        identifier: Optional[str] = None,
        expiration: Optional[int] = None,
        priority: int = 10,
        collapse_id: Optional[str] = None,
    ) -> None:
        self.topic = topic
        self.push_type = push_type
        if identifier:
            self._valid_identifier(identifier=identifier)
            self.identifier = identifier
        else:
            self.identifier = None
        self.expiration = expiration if expiration is not None else int(time.time()) + 2592000
        self.priority = ApnsPriority(priority).value
        self.collapse_id = collapse_id

    @staticmethod
    def _valid_identifier(identifier) -> None:
        try:
            uuid_obj = uuid.UUID(hex=identifier, version=4)
        except ValueError:
            raise ValueError(f"{identifier} is invalid format.")
        if identifier != str(uuid_obj):
            raise ValueError("Please check your identifier.")

    def make_headers(self) -> Dict[str, str]:
        headers = {
            "apns-push-type": self.push_type.value,
            "apns-id": self.identifier,
            "apns-expiration": str(self.expiration),
            "apns-priority": str(self.priority),
            "apns-topic": self.topic,
            "apns-collapse-id": self.collapse_id,
            "user-agent": f"python-httpx/{httpx.__version__} {self.topic}",
        }
        headers = {k: v for k, v in headers.items() if v is not None}
        return headers

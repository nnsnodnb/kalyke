from dataclasses import dataclass
from typing import Any

from httpx import AsyncClient

from ..models import VoIPApnsConfig
from .apns import ApnsClient as BaseClient


@dataclass(frozen=True)
class VoIPClient(BaseClient):
    async def send_message(
        self,
        device_token: str,
        payload: dict[str, Any],  # type: ignore[override]
        apns_config: VoIPApnsConfig,  # type: ignore[override]
    ) -> str:
        return await super().send_message(
            device_token=device_token,
            payload=payload,
            apns_config=apns_config,
        )

    def _init_client(
        self,
        apns_config: VoIPApnsConfig,  # type: ignore[override]
    ) -> AsyncClient:
        return super()._init_client(apns_config=apns_config)

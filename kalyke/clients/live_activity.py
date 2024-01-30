from dataclasses import dataclass
from typing import Any, Dict, Union

from httpx import AsyncClient

from ..models import LiveActivityApnsConfig, LiveActivityPayload
from .apns import ApnsClient


@dataclass(frozen=True)
class LiveActivityClient(ApnsClient):
    async def send_message(
        self,
        device_token: str,
        payload: Union[LiveActivityPayload, Dict[str, Any]],  # type: ignore[override]
        apns_config: LiveActivityApnsConfig,  # type: ignore[override]
    ) -> str:
        return await super().send_message(
            device_token=device_token,
            payload=payload,
            apns_config=apns_config,
        )

    def _init_client(
        self,
        apns_config: LiveActivityApnsConfig,  # type: ignore[override]
    ) -> AsyncClient:
        return super()._init_client(apns_config=apns_config)

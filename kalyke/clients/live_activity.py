from dataclasses import dataclass

from httpx import AsyncClient

from ..models import LiveActivityApnsConfig, LiveActivityPayload
from .apns import ApnsClient


@dataclass
class LiveActivityClient(ApnsClient):
    async def send_message(
        self,
        device_token: str,
        payload: LiveActivityPayload,
        apns_config: LiveActivityApnsConfig,
    ) -> str:
        return await super().send_message(
            device_token=device_token,
            payload=payload,
            apns_config=apns_config,
        )

    def _init_client(self, apns_config: LiveActivityApnsConfig) -> AsyncClient:
        return super()._init_client(apns_config=apns_config)

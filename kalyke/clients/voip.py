from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Union

import httpx
from httpx import AsyncClient

from ..models import VoIPApnsConfig
from . import __Client as BaseClient


@dataclass
class VoIPClient(BaseClient):
    use_sandbox: bool
    auth_key_filepath: Union[str, Path]
    _auth_key_filepath: Path = field(init=False)

    def __post_init__(self):
        if isinstance(self.auth_key_filepath, Path):
            self._auth_key_filepath = self.auth_key_filepath
        else:
            self._auth_key_filepath = Path(self.auth_key_filepath)

    async def send_message(
        self,
        device_token: str,
        payload: Dict[str, Any],
        apns_config: VoIPApnsConfig,
    ) -> str:
        return await super().send_message(
            device_token=device_token,
            payload=payload,
            apns_config=apns_config,
        )

    def _init_client(self, apns_config: VoIPApnsConfig) -> AsyncClient:
        headers = apns_config.make_headers()
        context = httpx.create_ssl_context()
        context.load_cert_chain(self._auth_key_filepath)
        client = AsyncClient(headers=headers, verify=context, http2=True)
        return client

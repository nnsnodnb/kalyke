import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional, Union

import httpx
from httpx import AsyncClient

from ..models import VoIPApnsConfig
from . import __Client as BaseClient


@dataclass(frozen=True)
class VoIPClient(BaseClient):
    use_sandbox: bool
    auth_key_filepath: Union[str, Path]
    key_filepath: Optional[Union[str, Path]] = field(default=None)
    password: Optional[str] = field(default=None)

    def __post_init__(self) -> None:
        if self.key_filepath is None and self.password is not None:
            warnings.warn(UserWarning("password is ignored because key_filepath is None."))

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
        context.load_cert_chain(
            certfile=self._get_auth_key_filepath(),
            keyfile=self.key_filepath,
            password=self.password,
        )
        client = AsyncClient(headers=headers, verify=context, http2=True)
        return client

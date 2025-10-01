from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import jwt
from httpx import AsyncClient

from ..models import ApnsConfig
from . import __Client as BaseClient


@dataclass(frozen=True)
class ApnsClient(BaseClient):
    use_sandbox: bool
    team_id: str
    auth_key_id: str
    auth_key_filepath: str | Path

    def _init_client(self, apns_config: ApnsConfig) -> AsyncClient:
        headers = apns_config.make_headers()
        headers["authorization"] = f"bearer {self._make_authorization()}"
        client = AsyncClient(headers=headers, http2=True)
        return client

    def _make_authorization(self) -> str:
        auth_key = self._get_auth_key_filepath().read_text()
        token = jwt.encode(
            payload={
                "iss": self.team_id,
                "iat": str(int(datetime.now().timestamp())),
            },
            key=auth_key,
            algorithm="ES256",
            headers={
                "alg": "ES256",
                "kid": self.auth_key_id,
            },
        )
        return token

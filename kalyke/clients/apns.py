from datetime import datetime
from pathlib import Path
from typing import Union

import jwt
from httpx import AsyncClient

from ..models import ApnsConfig
from . import __Client as BaseClient


class ApnsClient(BaseClient):
    _team_id: str
    _auth_key_id: str
    _auth_key_filepath: Path

    def __init__(
        self,
        use_sandbox: bool,
        team_id: str,
        auth_key_id: str,
        auth_key_filepath: Union[str, Path],
    ) -> None:
        self.use_sandbox = use_sandbox
        self._team_id = team_id
        self._auth_key_id = auth_key_id
        if isinstance(auth_key_filepath, Path):
            self._auth_key_filepath = auth_key_filepath
        else:
            self._auth_key_filepath = Path(auth_key_filepath)

    def _init_client(self, apns_config: ApnsConfig) -> AsyncClient:
        headers = apns_config.make_headers()
        headers["authorization"] = f"bearer {self._make_authorization()}"
        client = AsyncClient(headers=headers, http2=True)
        return client

    def _make_authorization(self) -> str:
        auth_key = self._auth_key_filepath.read_text()
        token = jwt.encode(
            payload={
                "iss": self._team_id,
                "iat": str(int(datetime.now().timestamp())),
            },
            key=auth_key,
            algorithm="ES256",
            headers={
                "alg": "ES256",
                "kid": self._auth_key_id,
            },
        )
        return token

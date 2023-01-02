import time
from pathlib import Path
from typing import Any, Dict, Union

import jwt
from httpx import AsyncClient

from ..internal.status_code import StatusCode
from ..models import ApnsConfig, Payload
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

    async def send_message(
        self,
        device_token: str,
        payload: Union[Payload, Dict[str, Any]],
        apns_config: ApnsConfig,
    ) -> str:
        if isinstance(payload, Payload):
            data = payload.dict()
        elif isinstance(payload, Dict):
            data = payload
        else:
            data = {}

        async with self._init_client(apns_config=apns_config) as client:
            request_url = self._make_url(device_token=device_token)
            res = await self._send(client=client, url=request_url, data=data)

        status_code = StatusCode(res.status_code)
        if status_code.is_success:
            return res.headers["apns-id"]

        raise self._handle_error(error_json=res.json())

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
                "iat": str(int(time.time())),
            },
            key=auth_key,
            algorithm="ES256",
            headers={
                "alg": "ES256",
                "kid": self._auth_key_id,
            },
        )
        return token

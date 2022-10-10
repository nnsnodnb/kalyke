import importlib
import json
import time
from pathlib import Path
from typing import Any, Dict, Union

import jwt

from httpx import AsyncClient, Response

from . import __Client as BaseClient
from .. import exceptions
from ..internal.status_code import StatusCode
from ..models import ApnsConfig, Payload


class ApnsClient(BaseClient):
    _team_id: str
    _auth_key_id: str
    _auth_key_filepath: Path

    __max_body_size: int = 4 * 1024

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

    def _check_payload_size(self, data: Dict[str, Any]) -> None:
        obj = json.dumps(data, separators=(",", ":"), sort_keys=True).encode()
        if len(obj) > self.__max_body_size:
            raise exceptions.PayloadTooLarge()

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
            res = await self.__send(client=client, url=request_url, data=data)

        status_code = StatusCode(res.status_code)
        if status_code.is_success:
            return res.headers["apns-id"]

        self._handle_error(error_json=res.json(), status_code=status_code)

    async def __send(
        self, client: AsyncClient, url: str, data: Dict[str, Any]
    ) -> Response:
        return await client.post(url=url, json=data)

    def _handle_error(self, error_json: Dict[str, Any], status_code: StatusCode):
        reason = error_json["reason"]
        if (
            status_code.is_bad_request
            or status_code.is_token_error
            or status_code.is_not_found
            or status_code.is_method_not_allowed
            or status_code.is_payload_too_large
            or status_code.is_too_many_requests
            or status_code.is_internal_server_error
            or status_code.is_service_unavailable
        ):
            exceptions_module = importlib.import_module("kalyke.exceptions")
            exception_class = getattr(exceptions_module, reason)
            raise exception_class()
        elif status_code.is_token_inactive:
            timestamp = error_json["timestamp"]

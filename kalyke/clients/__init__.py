import importlib
import urllib.parse
from pathlib import Path
from typing import Any

from httpx import AsyncClient, Response

from ..exceptions import ApnsProviderException
from ..models import ApnsConfig, Payload


class __Client:
    use_sandbox: bool
    auth_key_filepath: str | Path

    async def send_message(
        self,
        device_token: str,
        payload: Payload | dict[str, Any],
        apns_config: ApnsConfig,
    ) -> str:
        if isinstance(payload, Payload):
            data = payload.dict()
        elif isinstance(payload, dict):
            data = payload
        else:
            raise ValueError("Type of 'payload' must be specified by Payload or Dict[str, Any].")

        async with self._init_client(apns_config=apns_config) as client:
            request_url = self._make_url(device_token=device_token)
            res = await self._send(client=client, url=request_url, data=data)

        if res.is_success:
            return res.headers["apns-id"]

        raise self._handle_error(error_json=res.json())

    @property
    def _base_url(self) -> str:
        if self.use_sandbox:
            return "https://api.sandbox.push.apple.com"
        else:
            return "https://api.push.apple.com"

    def _init_client(self, apns_config: ApnsConfig) -> AsyncClient:
        raise NotImplementedError

    def _make_url(self, device_token: str) -> str:
        return f"{self._base_url}/3/device/{urllib.parse.quote(device_token)}"

    async def _send(self, client: AsyncClient, url: str, data: dict[str, Any]) -> Response:
        return await client.post(url=url, json=data)

    def _handle_error(self, error_json: dict[str, Any]) -> ApnsProviderException:
        reason = error_json.pop("reason")
        exceptions_module = importlib.import_module("kalyke.exceptions")
        exception_class = getattr(exceptions_module, reason)

        return exception_class(error=error_json)

    def _get_auth_key_filepath(self) -> Path:
        if isinstance(self.auth_key_filepath, Path):
            return self.auth_key_filepath
        else:
            return Path(self.auth_key_filepath)

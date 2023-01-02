import importlib
import urllib.parse
from typing import Any, Dict, Union

from httpx import AsyncClient, Response

from ..exceptions import ApnsProviderException
from ..models import ApnsConfig, Payload


class __Client(object):
    use_sandbox: bool

    async def send_message(
        self,
        device_token: str,
        payload: Union[Payload, Dict[str, Any]],
        apns_config: ApnsConfig,
    ) -> str:
        raise NotImplementedError

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

    async def _send(self, client: AsyncClient, url: str, data: Dict[str, Any]) -> Response:
        return await client.post(url=url, json=data)

    def _handle_error(self, error_json: Dict[str, Any]) -> ApnsProviderException:
        reason = error_json.pop("reason")
        exceptions_module = importlib.import_module("kalyke.exceptions")
        exception_class = getattr(exceptions_module, reason)

        return exception_class(error=error_json)

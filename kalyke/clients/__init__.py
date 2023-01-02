import importlib
import urllib.parse
from typing import Any, Callable, Dict, Union

from httpx import AsyncClient, Response

from ..internal.status_code import StatusCode
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

    def _handle_error(self, error_json: Dict[str, Any], status_code: StatusCode) -> Callable:
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

            return exception_class
        elif status_code.is_token_inactive:
            timestamp = error_json["timestamp"]

        return NotImplementedError

from pathlib import Path
from typing import Any, Dict, Union

import httpx
from httpx import AsyncClient

from ..internal.status_code import StatusCode
from ..models import ApnsConfig
from . import __Client as BaseClient


class VoIPClient(BaseClient):
    _auth_key_filepath: Path

    def __init__(self, use_sandbox: bool, auth_key_file_path: Union[str, Path]) -> None:
        self.use_sandbox = use_sandbox
        if isinstance(auth_key_file_path, Path):
            self._auth_key_filepath = auth_key_file_path
        else:
            self._auth_key_filepath = Path(auth_key_file_path)

    async def send_message(self, device_token: str, payload: Dict[str, Any], apns_config: ApnsConfig) -> str:
        async with self._init_client(apns_config=apns_config) as client:
            request_url = self._make_url(device_token=device_token)
            res = await self._send(client=client, url=request_url, data=payload)

        status_code = StatusCode(res.status_code)
        if status_code.is_success:
            return res.headers["apns-id"]

        self._handle_error(error_json=res.json(), status_code=status_code)

    def _init_client(self, apns_config: ApnsConfig) -> AsyncClient:
        headers = apns_config.make_headers()
        context = httpx.create_ssl_context()
        context.load_cert_chain(self._auth_key_filepath)
        client = AsyncClient(headers=headers, verify=context, http2=True)
        return client

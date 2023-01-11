from pathlib import Path
from typing import Union

import httpx
from httpx import AsyncClient

from ..models import ApnsConfig
from . import __Client as BaseClient


class VoIPClient(BaseClient):
    _auth_key_filepath: Path

    def __init__(self, use_sandbox: bool, auth_key_filepath: Union[str, Path]) -> None:
        self.use_sandbox = use_sandbox
        if isinstance(auth_key_filepath, Path):
            self._auth_key_filepath = auth_key_filepath
        else:
            self._auth_key_filepath = Path(auth_key_filepath)

    def _init_client(self, apns_config: ApnsConfig) -> AsyncClient:
        headers = apns_config.make_headers()
        context = httpx.create_ssl_context()
        context.load_cert_chain(self._auth_key_filepath)
        client = AsyncClient(headers=headers, verify=context, http2=True)
        return client

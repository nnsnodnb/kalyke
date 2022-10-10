import urllib.parse

from httpx import AsyncClient


class __Client:
    use_sandbox: bool

    @property
    def __max_body_size(self) -> int:
        raise NotImplementedError

    @property
    def _base_url(self) -> str:
        if self.use_sandbox:
            return "https://api.sandbox.push.apple.com"
        else:
            return "https://api.push.apple.com"

    def _init_client(self, **kwargs) -> AsyncClient:
        raise NotImplementedError

    def _make_url(self, device_token: str) -> str:
        return f"{self._base_url}/3/device/{urllib.parse.quote(device_token)}"

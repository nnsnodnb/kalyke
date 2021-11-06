import time
from collections import namedtuple
from pathlib import Path
from typing import Dict, Union

import jwt


SANDBOX_HOST = "api.development.push.apple.com:443"
PRODUCTION_HOST = "api.push.apple.com:443"

RESPONSE_CODES: Dict[str, int] = {
    "Success": 200,
    "BadRequest": 400,
    "TokenError": 403,
    "MethodNotAllowed": 405,
    "TokenInactive": 410,
    "PayloadTooLarge": 413,
    "TooManyRequests": 429,
    "InternalServerError": 500,
    "ServerUnavailable": 503,
}

ResponseStruct = namedtuple("ResponseStruct", " ".join(RESPONSE_CODES.keys()))  # type: ignore
Response = ResponseStruct(**RESPONSE_CODES)  # type: ignore


class _BaseClient(object):

    auth_key_path: Union[str, Path]
    base_url: str
    bundle_id: str
    apns_push_type: str

    def __init__(self, auth_key_path: Union[str, Path], use_sandbox: bool, bundle_id: str, apns_push_type: str) -> None:
        self.auth_key_path = auth_key_path if isinstance(auth_key_path, Path) else Path(auth_key_path)
        self.base_url = SANDBOX_HOST if use_sandbox else PRODUCTION_HOST
        self.bundle_id = bundle_id
        if apns_push_type not in ["alert", "background", "voip"]:
            # https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns/
            raise ValueError("Please choice alert, background or voip")


class APNsClient(_BaseClient):

    team_id: str

    def __init__(
        self, auth_key_path: Union[str, Path], use_sandbox: bool, bundle_id: str, team_id: str, apns_push_type: str
    ) -> None:
        super(APNsClient, self).__init__(auth_key_path, use_sandbox, bundle_id, apns_push_type)
        self.team_id = team_id

    def _create_token(self) -> str:
        auth_key = self.auth_key_path.read_text()
        token = jwt.encode(
            {"iss": self.team_id, "iat": time.time()},
            auth_key,
            algorithm="ES256",
            headers={
                "alg": "ES256",
                "kid": auth_key,
            },
        )
        return token


class VoIPClient(_BaseClient):
    def __init__(self, auth_key_path: Union[str, Path], use_sandbox: bool, bundle_id: str) -> None:
        if not bundle_id.endswith(".voip"):
            bundle_id = bundle_id + ".voip"
        super(VoIPClient, self).__init__(auth_key_path, use_sandbox, bundle_id, "voip")

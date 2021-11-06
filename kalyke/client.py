from collections import namedtuple
from typing import Dict


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

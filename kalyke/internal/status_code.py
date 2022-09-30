from enum import Enum


class StatusCode(Enum):
    SUCCESS: int = 200
    BAD_REQUEST: int = 400
    TOKEN_ERROR: int = 403
    METHOD_NOT_ALLOWED: int = 405
    TOKEN_INACTIVE: int = 410
    PAYLOAD_TOO_LARGE: int = 413
    TOO_MARY_REQUESTS: int = 429
    INTERNAL_SERVER_ERROR: int = 500
    SERVER_UNAVAILABLE: int = 503

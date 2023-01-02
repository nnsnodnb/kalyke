from enum import Enum
from typing import TypeVar

Self = TypeVar("Self", bound="StatusCode")


class StatusCode(Enum):
    SUCCESS: int = 200
    BAD_REQUEST: int = 400
    TOKEN_ERROR: int = 403
    NOT_FOUND: int = 404
    METHOD_NOT_ALLOWED: int = 405
    TOKEN_INACTIVE: int = 410
    PAYLOAD_TOO_LARGE: int = 413
    TOO_MARY_REQUESTS: int = 429
    INTERNAL_SERVER_ERROR: int = 500
    SERVER_UNAVAILABLE: int = 503

    @property
    def is_success(self) -> bool:
        return self == self.SUCCESS

    @property
    def is_bad_request(self) -> bool:
        return self == self.BAD_REQUEST

    @property
    def is_token_error(self) -> bool:
        return self == self.TOKEN_ERROR

    @property
    def is_not_found(self) -> bool:
        return self == self.NOT_FOUND

    @property
    def is_method_not_allowed(self) -> bool:
        return self == self.METHOD_NOT_ALLOWED

    @property
    def is_token_inactive(self) -> bool:
        return self == self.TOKEN_INACTIVE

    @property
    def is_payload_too_large(self) -> bool:
        return self == self.PAYLOAD_TOO_LARGE

    @property
    def is_too_many_requests(self) -> bool:
        return self == self.TOO_MARY_REQUESTS

    @property
    def is_internal_server_error(self) -> bool:
        return self == self.INTERNAL_SERVER_ERROR

    @property
    def is_service_unavailable(self) -> bool:
        return self == self.SERVER_UNAVAILABLE

import pytest

from kalyke.clients import __Client
from kalyke.exceptions import (
    BadCertificate,
    BadCertificateEnvironment,
    BadCollapseId,
    BadDeviceToken,
    BadExpirationDate,
    BadMessageId,
    BadPath,
    BadPriority,
    BadTopic,
    DeviceTokenNotForTopic,
    DuplicateHeaders,
    ExpiredProviderToken,
    ExpiredToken,
    Forbidden,
    IdleTimeout,
    InternalServerError,
    InvalidProviderToken,
    InvalidPushType,
    MethodNotAllowed,
    MissingDeviceToken,
    MissingProviderToken,
    MissingTopic,
    PayloadEmpty,
    PayloadTooLarge,
    ServiceUnavailable,
    Shutdown,
    TooManyProviderTokenUpdates,
    TooManyRequests,
    TopicDisallowed,
    Unregistered,
)


@pytest.mark.parametrize(
    "reason, expect",
    [
        (
            "BadCollapseId",
            BadCollapseId,
        ),
        (
            "BadDeviceToken",
            BadDeviceToken,
        ),
        (
            "BadExpirationDate",
            BadExpirationDate,
        ),
        (
            "BadMessageId",
            BadMessageId,
        ),
        (
            "BadPriority",
            BadPriority,
        ),
        (
            "BadTopic",
            BadTopic,
        ),
        (
            "DeviceTokenNotForTopic",
            DeviceTokenNotForTopic,
        ),
        (
            "DuplicateHeaders",
            DuplicateHeaders,
        ),
        (
            "IdleTimeout",
            IdleTimeout,
        ),
        (
            "InvalidPushType",
            InvalidPushType,
        ),
        (
            "MissingDeviceToken",
            MissingDeviceToken,
        ),
        (
            "MissingTopic",
            MissingTopic,
        ),
        (
            "PayloadEmpty",
            PayloadEmpty,
        ),
        (
            "TopicDisallowed",
            TopicDisallowed,
        ),
        (
            "BadCertificate",
            BadCertificate,
        ),
        (
            "BadCertificateEnvironment",
            BadCertificateEnvironment,
        ),
        (
            "ExpiredProviderToken",
            ExpiredProviderToken,
        ),
        (
            "Forbidden",
            Forbidden,
        ),
        (
            "InvalidProviderToken",
            InvalidProviderToken,
        ),
        (
            "MissingProviderToken",
            MissingProviderToken,
        ),
        (
            "BadPath",
            BadPath,
        ),
        (
            "MethodNotAllowed",
            MethodNotAllowed,
        ),
        (
            "ExpiredToken",
            ExpiredToken,
        ),
        (
            "Unregistered",
            Unregistered,
        ),
        (
            "PayloadTooLarge",
            PayloadTooLarge,
        ),
        (
            "TooManyProviderTokenUpdates",
            TooManyProviderTokenUpdates,
        ),
        (
            "TooManyRequests",
            TooManyRequests,
        ),
        (
            "InternalServerError",
            InternalServerError,
        ),
        (
            "ServiceUnavailable",
            ServiceUnavailable,
        ),
        (
            "Shutdown",
            Shutdown,
        ),
    ],
)
def test_handle_error(reason, expect):
    client = __Client()
    exception = client._handle_error(error_json={"reason": reason})

    assert isinstance(exception, expect)


def test_attributed_error():
    client = __Client()

    with pytest.raises(AttributeError) as e:
        _ = client._handle_error(error_json={"reason": "Unknown"})

    assert str(e.value) == "module 'kalyke.exceptions' has no attribute 'Unknown'"

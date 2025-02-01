from typing import Any


class VolumeOutOfRangeException(Exception):
    _volume: float

    def __init__(self, volume: float) -> None:
        self._volume = volume

    def __str__(self) -> str:
        return f"The volume must be a value between 0.0 and 1.0. Did set {self._volume}."


class RelevanceScoreOutOfRangeException(Exception):
    _relevance_score: float

    def __init__(self, relevance_score: float) -> None:
        self._relevance_score = relevance_score

    def __str__(self) -> str:
        return f"The system uses the relevance_score, a value between 0 and 1. Did set {self._relevance_score}."


class LiveActivityAttributesIsNotJSONSerializable(Exception):
    def __str__(self) -> str:
        return "attributes is not JSON serializable."


class LiveActivityContentStateIsNotJSONSerializable(Exception):
    def __str__(self) -> str:
        return "content-state is not JSON serializable."


# https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/handling_notification_responses_from_apns#3394535
class ApnsProviderException(Exception):
    def __init__(self, error: dict[str, Any]) -> None:
        self.error = error

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.__doc__}"


class BadCollapseId(ApnsProviderException):
    """
    The collapse identifier exceeds the maximum allowed size.
    """

    pass


class BadDeviceToken(ApnsProviderException):
    """
    The specified device token is invalid. Verify that the request contains a valid token and that the token matches
     the environment.
    """

    pass


class BadExpirationDate(ApnsProviderException):
    """
    The apns-expiration value is invalid.
    """

    pass


class BadMessageId(ApnsProviderException):
    """
    The apns-id value is invalid.
    """

    pass


class BadPriority(ApnsProviderException):
    """
    The apns-priority value is invalid.
    """

    pass


class BadTopic(ApnsProviderException):
    """
    The apns-topic value is invalid.
    """

    pass


class DeviceTokenNotForTopic(ApnsProviderException):
    """
    The device token doesn’t match the specified topic.
    """

    pass


class DuplicateHeaders(ApnsProviderException):
    """
    One or more headers are repeated.
    """

    pass


class IdleTimeout(ApnsProviderException):
    """
    Idle timeout.
    """

    pass


class InvalidPushType(ApnsProviderException):
    """
    The apns-push-type value is invalid.
    """

    pass


class MissingDeviceToken(ApnsProviderException):
    """
    The device token isn’t specified in the request :path. Verify that the :path header contains the device token.
    """

    pass


class MissingTopic(ApnsProviderException):
    """
    The apns-topic header of the request isn’t specified and is required. The apns-topic header is mandatory when
     the client is connected using a certificate that supports multiple topics.
    """

    pass


class PayloadEmpty(ApnsProviderException):
    """
    The message payload is empty.
    """

    pass


class TopicDisallowed(ApnsProviderException):
    """
    Pushing to this topic is not allowed.
    """

    pass


class BadCertificate(ApnsProviderException):
    """
    The certificate is invalid.
    """

    pass


class BadCertificateEnvironment(ApnsProviderException):
    """
    The client certificate is for the wrong environment.
    """

    pass


class ExpiredProviderToken(ApnsProviderException):
    """
    The provider token is stale and a new token should be generated.
    """

    pass


class Forbidden(ApnsProviderException):
    """
    The specified action is not allowed.
    """

    pass


class InvalidProviderToken(ApnsProviderException):
    """
    The provider token is not valid, or the token signature can't be verified.
    """

    pass


class MissingProviderToken(ApnsProviderException):
    """
    No provider certificate was used to connect to APNs, and the authorization header is missing or
     no provider token is specified.
    """

    pass


class BadPath(ApnsProviderException):
    """
    The request contained an invalid :path value.
    """

    pass


class MethodNotAllowed(ApnsProviderException):
    """
    The specified :method value isn’t POST.
    """

    pass


class ExpiredToken(ApnsProviderException):
    """
    The device token has expired.
    """

    pass


class Unregistered(ApnsProviderException):
    """
    The device token is inactive for the specified topic.
     There is no need to send further pushes to the same device token,
     unless your application retrieves the same device token, see Registering Your App with APNs.
     (https://developer.apple.com/documentation/usernotifications/registering_your_app_with_apns)
    """

    pass


class PayloadTooLarge(ApnsProviderException):
    """
    The message payload is too large. For information about the allowed payload size, see Create and Send a POST Request
     to APNs.
     (https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)
    """

    pass


class TooManyProviderTokenUpdates(ApnsProviderException):
    """
    The provider’s authentication token is being updated too often. Update the authentication token
     no more than once every 20 minutes.
    """

    pass


class TooManyRequests(ApnsProviderException):
    """
    Too many requests were made consecutively to the same device token.
    """

    pass


class InternalServerError(ApnsProviderException):
    """
    An internal server error occurred.
    """

    pass


class ServiceUnavailable(ApnsProviderException):
    """
    The service is unavailable.
    """

    pass


class Shutdown(ApnsProviderException):
    """
    The APNs server is shutting down.
    """

    pass

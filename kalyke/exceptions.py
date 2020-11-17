class KalykeException(Exception):
    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.__doc__)


class ImproperlyConfigured(KalykeException):
    pass


class PayloadTooLarge(KalykeException):
    """
    The message payload was too large. See Creation the Remote Notification Payload for details on maximum payload size.
    """

    pass


class BadCollapseId(KalykeException):
    """
    The collapse identifier exceeds the maximum allowed size.
    """

    pass


class BadDeviceToken(KalykeException):
    """
    The specified device token was bad.
     Verify that the request contains a valid token and that the token matches the environment.
    """

    pass


class BadExpirationDate(KalykeException):
    """
    The apns-expiration value is bad.
    """

    pass


class BadMessageId(KalykeException):
    """
    The apns-id value is bad.
    """

    pass


class BadPriority(KalykeException):
    """
    The apns-priority value is bad.
    """

    pass


class BadTopic(KalykeException):
    """
    The apns-topic was invalid.
    """

    pass


class DeviceTokenNotForTopic(KalykeException):
    """
    The device token does not match the specified topic.
    """

    pass


class DuplicateHeaders(KalykeException):
    """
    One or more headers were repeated.
    """

    pass


class IdleTimeout(KalykeException):
    """
    Idle time out.
    """

    pass


class MissingDeviceToken(KalykeException):
    """
    The device token is not specified in the request :path.
     Verify that the :path header contains the device token.
    """

    pass


class MissingTopic(KalykeException):
    """
    The apns-topic header of the request was not specified and was required.
     The apns-topic header is mandatory when the client is connected using a certificate that supports multiple topics.
    """

    pass


class PayloadEmpty(KalykeException):
    """
    The message payload was empty.
    """

    pass


class TopicDisallowed(KalykeException):
    """
    Pushing to this topic is not allowed.
    """

    pass


class BadCertificate(KalykeException):
    """
    The certificate was bad.
    """

    pass


class BadCertificateEnvironment(KalykeException):
    """
    The client certificate was for the wrong environment.
    """

    pass


class ExpiredProviderToken(KalykeException):
    """
    The provider token is stale and a new token should be generated.
    """

    pass


class Forbidden(KalykeException):
    """
    The specified action is not allowed.
    """

    pass


class InvalidProviderToken(KalykeException):
    """
    The provider token is not valid or the token signature could not be verified.
    """

    pass


class MissingProviderToken(KalykeException):
    """
    No provider certificate was used to connect to APNs
     and Authorization header was missing or no provider token was specified.
    """

    pass


class BadPath(KalykeException):
    """
    The request contained a bad :path value.
    """

    pass


class MethodNotAllowed(KalykeException):
    """
    The specified :method was not POST.
    """

    pass


class Unregistered(KalykeException):
    """
    The device token is inactive for the specified topic. Expected HTTP/2 status code is 410; see Table 8-4.
    """

    pass


class TooManyProviderTokenUpdates(KalykeException):
    """
    The provider token is being updated too often.
    """

    pass


class TooManyRequests(KalykeException):
    """
    Too many requests were made consecutively to the same device token.
    """

    pass


class InternalServerError(KalykeException):
    """
    An internal server error occurred.
    """

    pass


class ServiceUnavailable(KalykeException):
    """
    The service is unavailable.
    """

    pass


class Shutdown(KalykeException):
    """
    The server is shutting down.
    """

    pass


class InternalException(KalykeException):
    pass


class PartialBulkMessage(KalykeException):
    def __init__(self, message, failure_exceptions):
        super().__init__(message)
        self.failure_exceptions = failure_exceptions

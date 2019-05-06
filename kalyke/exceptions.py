class KalykeException(Exception):

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__doc__}'


class ImproperlyConfigured(KalykeException):
    pass


class PayloadTooLarge(KalykeException):
    """
    The message payload was too large. See Creation the Remote Notification Payload for details on maximum payload size.
    """
    pass

class KalykeException(Exception):

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__doc__}'


class ImproperlyConfigured(KalykeException):
    pass

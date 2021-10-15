class InvalidValueError(Exception):
    """Class for exception raised on invalid value"""

    def __init__(self, message="Input value is invalid"):
        """
        Custom exception
        :param message: message to output in console
        """

        self.message = message
        super(InvalidValueError, self).__init__(self.message)


class SizeLimitException(Exception):
    """Class for limit size exception"""

    def __init__(self, message="Invalid grid size"):
        """
        Custom exception
        :param message: message to output in console
        """

        self.message = message
        super(SizeLimitException, self).__init__(self.message)

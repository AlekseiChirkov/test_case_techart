class InvalidGroundValueError(Exception):
    """Class for exception raised on invalid value"""

    @classmethod
    def __init__(cls, message="Input value is invalid"):
        """
        Custom exception
        :param message: message to output in console
        """

        cls.message = message
        super(InvalidGroundValueError, cls).__init__(message)


class GroundSizeLimitError(Exception):
    """Class for limit size exception"""

    @classmethod
    def __init__(cls, message="Invalid grid size"):
        """
        Custom exception
        :param message: message to output in console
        """

        cls.message = message
        super(GroundSizeLimitError, cls).__init__(message)

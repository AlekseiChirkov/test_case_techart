class InvalidGroundValueError(Exception):
    """Class for exception raised on invalid value"""

    def __init__(self, message="Input value is invalid"):
        """
        Custom exception
        :param message: message to output in console
        """

        self.message = message
        super(InvalidGroundValueError, self).__init__(self.message)


class GroundSizeLimitError(Exception):
    """Class for limit size exception"""

    def __init__(self, message="Invalid grid size"):
        """
        Custom exception
        :param message: message to output in console
        """

        self.message = message
        super(GroundSizeLimitError, self).__init__(self.message)

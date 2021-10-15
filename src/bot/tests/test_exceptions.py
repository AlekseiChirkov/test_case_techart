from unittest import TestCase

from bot.ground import Ground
from bot.exceptions import InvalidGroundValueError, GroundSizeLimitError


class ExceptionsTests(TestCase):
    """Test exceptions"""

    def test_exception_raising(self) -> None:
        """
        Test that exception raising correctly
        :return: None
        """

        with self.assertRaises(InvalidGroundValueError):
            Ground("5a5 (1, 1)")

        with self.assertRaises(InvalidGroundValueError):
            Ground("5x5 1,1")

        with self.assertRaises(GroundSizeLimitError):
            Ground("5x5 (6, 6)")

    def test_exception_messages(self) -> None:
        """
        Test that exception messages valid
        :return: None
        """

        try:
            Ground("5x5 1,1")
        except InvalidGroundValueError as e:
            self.assertEqual(
                e.message, "Enter points in format like (1, 2) (4, 4)"
            )

        try:
            Ground("5a5 (1, 1)")
        except InvalidGroundValueError as e:
            self.assertEqual(
                e.message, "Input value must starts in format like 5x5"
            )

        try:
            Ground("5x5 (6, 6)")
        except GroundSizeLimitError as e:
            self.assertEqual(
                e.message, "Invalid grid size"
            )


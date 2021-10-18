from unittest import TestCase

from bot.exceptions import InvalidGroundValueError, GroundSizeLimitError
from bot.validators import InputValidator


SUCCESS_DATA = "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2)"


class InputValidatorTests(TestCase):
    """Test input validation"""

    def test_ground_data_input_validation_success(self) -> None:
        """
        Test that validation ground data input is successful
        :return: None
        """

        ground, points = InputValidator.validate_ground_data_input(
            SUCCESS_DATA
        )

        self.assertEqual(ground, (5, 5))
        self.assertEqual(points, (
            (0, 0), (1, 3), (4, 4), (4, 2), (4, 2), (0, 1), (3, 2)
        ))

    def test_ground_data_input_validation_failed(self) -> None:
        """
        Test that validation ground data input failed
        :return: None
        """

        ground_fail_data = "5a5 (0, 0) (1, 3)"
        points_fail_data = "5x5 0,0 1,3"

        with self.assertRaises(InvalidGroundValueError):
            InputValidator.validate_ground_data_input(ground_fail_data)

        with self.assertRaises(InvalidGroundValueError):
            InputValidator.validate_ground_data_input(points_fail_data)

    def test_ground_size_not_valid(self) -> None:
        """
        Test that ground size not valid
        :return: None
        """

        ground = (5, 5)
        points = ((6, 0), (1, 3), (4, 4), (4, 2), (4, 2), (0, 1), (3, 2))

        with self.assertRaises(GroundSizeLimitError):
            InputValidator.validate_ground_size(ground, points)

    def test_ground_input_validation_fails(self) -> None:
        """
        Test that ground input validation fails
        :return: None
        """

        ground = '5x5'
        with self.assertRaises(InvalidGroundValueError):
            InputValidator.validate_ground_input(ground)

    def test_coordinates_input_validation_fails(self) -> None:
        """
        Test that points input validation fails
        :return: None
        """

        points = '(0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2)'
        with self.assertRaises(InvalidGroundValueError):
            InputValidator.validate_coordinates_input(points)



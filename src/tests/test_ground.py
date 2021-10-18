from unittest import TestCase

from bot.exceptions import InvalidGroundValueError, GroundSizeLimitError
from bot.ground import Ground

DATA = "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"
SAMPLE_COORDINATES = Ground(DATA)


class CoordinatesModelTests(TestCase):
    """Test coordinates model is working"""

    def test_coordinates_create_successful(self) -> None:
        """
        Test creating a coordinates is successful
        :return: None
        """

        grid = (5, 5)
        points = (
            (0, 0), (1, 3), (4, 4), (4, 2), (4, 2),
            (0, 1), (3, 2), (2, 3), (4, 1)
        )
        coordinates = SAMPLE_COORDINATES

        self.assertEqual(coordinates.grid, grid)
        self.assertEqual(coordinates.coordinates, points)

    def test_invalid_data_exceptions(self) -> None:
        """
        Test that invalid data exceptions works correctly
        :return: None
        """

        with self.assertRaises(GroundSizeLimitError):
            Ground("1x1 (2, 2)")

        with self.assertRaises(InvalidGroundValueError):
            Ground("5a5 (1, 1) (2, 2)")

        with self.assertRaises(InvalidGroundValueError):
            Ground("5x5 1,1")


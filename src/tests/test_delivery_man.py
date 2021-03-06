from unittest import TestCase
from unittest.mock import patch

from bot.ground import Ground
from bot.delivery_man import DeliveryMan

DATA = "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"
SAMPLE_COORDINATES = Ground(DATA)


class DeliverPizzaTests(TestCase):
    """Test pizza delivery"""

    def test_delivery_pizza_route_calculation_successful(self) -> None:
        """
        Test pizza delivery route is calculating successfully
        :return: None
        """

        solution = DeliveryMan.get_route(
            SAMPLE_COORDINATES.coordinates
        )

        self.assertEqual(solution, 'DENNNDEEENDSSDDWWWWSDEEENDWNDEESSD')

    @patch('builtins.print')
    def test_route_solution_display(self, mock_print) -> None:
        """
        Test that route solution displays correctly
        :return: None
        """

        DeliveryMan.show_route(SAMPLE_COORDINATES.coordinates)
        mock_print.assert_called_with('DENNNDEEENDSSDDWWWWSDEEENDWNDEESSD')

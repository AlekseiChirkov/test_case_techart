from unittest import TestCase

from bot.ground import Ground
from bot.delivery_route import DeliveryRoute


DATA = "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"
SAMPLE_COORDINATES = Ground(DATA)


class DeliveryRouteTests(TestCase):
    """Test delivery routes"""

    def test_actions_list_creation(self) -> None:
        """
        Test that action list creates correctly
        :return: None
        """

        route = DeliveryRoute()
        action_1 = route._get_actions_list(0, 5, 'E')
        action_2 = route._get_actions_list(4, 1, 'W')
        action_3 = route._get_actions_list(4, 11, 'W')

        self.assertEqual(action_1, ['E' for _ in range(abs(0-5))])
        self.assertEqual(action_2, ['W' for _ in range(abs(4-1))])
        self.assertEqual(action_3, ['W' for _ in range(abs(4-11))])

    def test_delivery_route_solution(self) -> None:
        """
        Test that solution returns correctly
        :return: None
        """

        route = DeliveryRoute()
        solution1 = route.calculate_delivery_route([0, 0], [1, 1])
        solution2 = route.calculate_delivery_route([0, 0], [3, 1])
        solution3 = route.calculate_delivery_route([1, 5], [3, 1])

        self.assertEqual(solution1, "END")
        self.assertEqual(solution2, "EEEND")
        self.assertEqual(solution3, "EESSSSD")

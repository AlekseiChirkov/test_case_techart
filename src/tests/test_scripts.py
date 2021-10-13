from unittest import TestCase

from src.bot.scripts import Coords, ProcessDelivery

DATA = ['src/bot/scripts.py', '5,5|(1,1) (2,5) (5,5)']


class TestPizzaScripts(TestCase):
    """Class to test scripts of pizza delivery bot"""

    def setUp(self) -> None:
        self.data = Coords(DATA[1].split('|'))

    def test_validated_data(self):
        """
        Test that coordinates data is valid
        :return: None
        """

        grid, coords = [[5, 5], [(1, 1), (2, 5), (5, 5)]]
        self.assertEqual(grid, self.data.grid)
        self.assertEqual(coords, self.data.coords)

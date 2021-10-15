import re
from dataclasses import dataclass

from bot.exceptions import InvalidValueError, SizeLimitException


@dataclass
class Coordinates:
    """Class to process arguments from console/terminal"""

    def __init__(self, console_args: str):
        """
        Initialize grid size and delivery coordinates
        :param console_args: string argument from console
        """

        grid, points = self._validate_grid_size(console_args)
        self.grid = grid
        self.coordinates = points

    @staticmethod
    def _process_arguments_to_tuple(grid: str, points: list) -> (tuple, tuple):
        """
        Method creates tuples from strings
        :param grid: grid size in string
        :param points: delivery points in list with string items
        :return: processed strings in tuples
        """

        grid = tuple(map(int, grid.split('x')))
        points = tuple(tuple(map(int, point.split(','))) for point in points)
        return grid, points

    @staticmethod
    def _validate_input(argument: str) -> (tuple, tuple):
        """
        Input validation for grid and coordinates
        :param argument: string argument from console
        :return: processed strings into tuples
        """

        try:
            grid = re.findall(r'(\d+x\d+)', argument)[0]
        except IndexError:
            raise InvalidValueError(
                "Input value must starts in format like 5x5"
            )

        points = re.findall(r'\((\d+,\d+)\)', argument)
        if not points:
            raise InvalidValueError("Enter points in format like (1,2) (3,3)")

        return grid, points

    @classmethod
    def _validate_grid_size(cls, argument: str) -> (tuple, tuple):
        grid, points = cls._validate_input(argument)
        grid, points = cls._process_arguments_to_tuple(grid, points)

        for coordinates in points:
            limit = any(size < point for size, point in zip(grid, coordinates))
            if limit:
                raise SizeLimitException

        return grid, points

import re
import sys

from dataclasses import dataclass


@dataclass
class Coords:
    """Class to process arguments from console/terminal"""

    def __init__(self, console_args: str):
        """
        Initialize grid size and delivery coordinates
        :param console_args: string argument from console
        """

        grid, points = self._validate_grid_size(console_args)
        self.grid = grid
        self.coords = points

    @staticmethod
    def _validate_input(argument: str) -> (tuple, tuple):
        """
        Input validation for grid and coordinates
        :param argument: string argument from console
        :return: processed strings into tuples
        """

        grid = re.findall(r'(\d+x\d+)', argument)[0]
        points = re.findall(r'\((\d+,\d+)\)', argument)

        if not grid:
            raise ValueError("Enter a grid in format like 5x5")
        if not points:
            raise ValueError("Enter points in format like (1,2) (3,3)")

        grid = tuple(map(int, grid.split('x')))
        points = tuple(tuple(map(int, point.split(','))) for point in points)

        return grid, points

    @classmethod
    def _validate_grid_size(cls, argument: str) -> (tuple, tuple):
        grid, points = cls._validate_input(argument)

        for coordinates in points:
            limit = any(size < point for size, point in zip(grid, coordinates))
            if limit:
                raise ValueError("Coordinates out of grid size")

        return grid, points


class DeliveryRoute:
    """Class to get delivery route"""

    @staticmethod
    def _get_actions_list(coordinate1: int, coordinate2: int, action) -> list:
        """
        Method creates actions list
        :param coordinate1: current point
        :param coordinate2: next point
        :param action: action to add in list
        :return: list of actions
        """
        steps_count = abs(coordinate1-coordinate2)
        return [action for _ in range(steps_count)]

    @classmethod
    def get_delivery_route_solution(
            cls, current_coordinates: list, next_coordinates: list
    ) -> str:
        """
        Method calculates route to the next delivery point
        :param current_coordinates: list of the current coordinates [1, 3]
        :param next_coordinates: list of the next coordinates [5, 5]
        :return: string with steps to the next delivery point
        """

        x1, y1 = current_coordinates
        x2, y2 = next_coordinates

        action_x = 'E' if x1 < x2 else 'W'
        action_y = 'N' if y1 < y2 else 'S'

        route_solution_x = cls._get_actions_list(x1, x2, action_x)
        route_solution_y = cls._get_actions_list(y1, y2, action_y)

        route_solution = route_solution_x + route_solution_y
        route_solution.append('D')

        return "".join(route_solution)


class DeliverPizza:
    """Class to deliver pizza"""

    route = DeliveryRoute

    @classmethod
    def get_delivery_route(cls, coords: list) -> str:
        """
        Method to calculate route for bot to deliver pizza
        :param coords: list of coordinates [x, y]
        :return: string with route solution
        """

        route = ''
        current_coords = (0, 0)
        for next_coords in coords:
            current_path = cls.route.get_delivery_route_solution(
                current_coords, next_coords
            )
            current_coords = next_coords
            route += current_path

        return route


if __name__ == '__main__':
    data = Coords(sys.argv[1])
    route = DeliverPizza.get_delivery_route(data.coords)
    print(route)

import re
import sys

from dataclasses import dataclass


@dataclass
class Coords:
    """Class to process arguments from console/terminal"""

    def __init__(self, console_args):
        pizzas = re.findall(r'\d+,\d+', console_args[1])
        self.grid = [int(i) for i in console_args[0].split(',')]
        self.coords = [tuple(map(int, pizza.split(','))) for pizza in pizzas]


class ProcessDelivery:
    """Class to deliver pizza"""

    @staticmethod
    def _add_action(route_solution: list, action: str, steps: int):
        """
        Method adds action E or W or N or S to list of route solutions
        :param route_solution: list of route solutions
        :param action: route action E, W, N or S
        :param steps: actions count
        :return: list with new actions added
        """

        for i in range(steps):
            route_solution.append(action)

        return route_solution

    @classmethod
    def _get_route(cls, current_coords: list, next_coords: list) -> str:
        """
        Methods calculates route to the next point
        :param current_coords: list of current coordinates
        :param next_coords: list of next coordinates
        :return: str with steps of route solution
        """

        x1, y1 = current_coords
        x2, y2 = next_coords

        route_solution = list()

        route_solution = cls._add_action(
            route_solution, 'E' if x1 < x2 else 'W', abs(x1 - x2)
        )
        route_solution = cls._add_action(
            route_solution, 'N' if y1 < y2 else 's', abs(y1 - y2)
        )
        route_solution.append('D')

        return "".join(route_solution)

    @classmethod
    def calculate_route(cls, coords: list) -> str:
        """
        Method to calculate route with coords
        :param coords: list with x,y coords
        :return: string with route solution
        """

        route = ''
        current_coords = [0, 0]
        for next_coords in coords:
            current_path = cls._get_route(current_coords, next_coords)
            current_coords = next_coords
            route += current_path

        return route


if __name__ == '__main__':
    data = Coords(sys.argv[1].split('|'))
    route = ProcessDelivery.calculate_route(data.coords)

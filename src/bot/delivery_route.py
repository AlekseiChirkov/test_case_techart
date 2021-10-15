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
    def calculate_route_solution(
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





from bot.services import DeliveryRoute


class DeliverPizza:
    """Class to deliver pizza"""

    route = DeliveryRoute

    @classmethod
    def get_delivery_route(cls, coords: tuple) -> str:
        """
        Method to calculate route for bot to deliver pizza
        :param coords: tuple of coordinates [x, y]
        :return: string with route solution
        """

        solution = ''
        current_coords = (0, 0)
        for next_coords in coords:
            current_path = cls.route.get_delivery_route_solution(
                current_coords, next_coords
            )
            current_coords = next_coords
            solution += current_path

        return solution

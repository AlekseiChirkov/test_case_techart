from bot.delivery_route import DeliveryRoute


class DeliveryMan:
    """Class to deliver pizza"""

    route = DeliveryRoute

    @classmethod
    def get_route(cls, coords: tuple) -> str:
        """
        Method to calculate route for bot to deliver pizza
        :param coords: tuple of coordinates (x, y)
        :return: string with route solution
        """

        solution = ''
        current_coords = (0, 0)
        for next_coords in coords:
            current_path = cls.route.calculate_delivery_route(
                current_coords, next_coords
            )
            current_coords = next_coords
            solution += current_path

        return solution

    @classmethod
    def show_route(cls, coordinates: tuple) -> None:
        """
        Method print result of route solution in console
        :param coordinates: tuple with delivery data
        :return: None
        """

        print(cls.get_route(coordinates))

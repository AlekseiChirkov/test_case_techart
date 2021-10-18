import re

from bot.processors import ProcessObjectDatatype
from bot.exceptions import InvalidGroundValueError, GroundSizeLimitError


class InputValidator:
    """Class to validate input data"""

    @staticmethod
    def _get_ground_data(obj: str) -> str:
        """
        Method getting string and returning ground size data
        :param obj: string with ground and coordinates data
        :return: string with ground size list "5x5"
        """

        ground = obj.split(" ", 1)[0]
        if ground[1] != 'x':
            raise InvalidGroundValueError(
                "Enter ground in format like 5x5"
            )

        return ground

    @staticmethod
    def _get_coordinates_data(obj: str) -> list:
        """
        Method getting string and returning coordinates data
        :param obj: string with ground and coordinates data
        :return: list with coordinates like [(1, 2), (3, 3)]
        """

        points = re.findall(r'\((\d+, \d+)\)', obj)
        if not points:
            raise InvalidGroundValueError(
                "Enter points in format like (1, 2) (4, 4)"
            )

        return points

    @staticmethod
    def validate_coordinates_input(points: tuple) -> None:
        """
        Method validate coordinates datatype
        :param points: tuple with coordinates like ((1, 2), (3, 3))
        :return: None
        """

        for coordinate in points:
            if not isinstance(coordinate, tuple):
                raise InvalidGroundValueError(
                    f"Object must be a tuple"
                    f" with format like (1, 2), not {coordinate}"
                )

    @staticmethod
    def validate_ground_input(ground: tuple) -> None:
        """
        Method validate ground datatype
        :param ground: tuple with ground size like (5, 5)
        :return: None
        """

        if not isinstance(ground, tuple):
            raise InvalidGroundValueError(
                f"Object must be a tuple"
                f"with format (1, 2), not {ground}"
            )

    @staticmethod
    def validate_ground_size(ground: tuple, points: tuple) -> None:
        """
        Method validate ground size
        (coordinates should not go beyond the ground)
        :param ground: tuple with ground size like (5, 5)
        :param points: tuple with coordinates like ((1, 2), (3, 3))
        :return: None
        """

        for coordinates in points:
            limit = any(
                size < point for size, point in zip(ground, coordinates)
            )
            if limit:
                raise GroundSizeLimitError

    @classmethod
    def validate_ground_data_input(cls, obj: str) -> (tuple, tuple):
        """
        Method validates string with ground data
        :param obj: string with data
        :return: tuples ground and points
        """

        ground = cls._get_ground_data(obj)
        points = cls._get_coordinates_data(obj)

        ground, points = ProcessObjectDatatype.process_ground_data_to_tuples(
            ground, points
        )

        cls.validate_coordinates_input(points)
        cls.validate_ground_input(ground)
        cls.validate_ground_size(ground, points)

        return ground, points

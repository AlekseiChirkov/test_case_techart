import re

from bot.processors import ProcessObjectDatatype
from bot.exceptions import InvalidGroundValueError, GroundSizeLimitError


class InputValidator:
    """Class to validate input data"""

    @staticmethod
    def validate_coordinates_input(points: tuple):
        for coordinate in points:
            if not isinstance(coordinate, tuple):
                raise InvalidGroundValueError(
                    f"Object must be a tuple"
                    f" with format like (1, 2), not {coordinate}"
                )

    @staticmethod
    def validate_ground_input(ground: tuple):
        if not isinstance(ground, tuple):
            raise InvalidGroundValueError(
                f"Object must be a tuple"
                f"with format (1, 2), not {ground}"
            )

    @staticmethod
    def validate_ground_size(ground: tuple, points: tuple):
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

        try:
            ground = re.findall(r'(\d+x\d+)', obj)[0]
        except IndexError:
            raise InvalidGroundValueError(
                "Enter ground in format like 5x5"
            )

        points = re.findall(r'\((\d+, \d+)\)', obj)
        if not points:
            raise InvalidGroundValueError(
                "Enter points in format like (1, 2) (4, 4)"
            )

        ground, points = ProcessObjectDatatype.process_ground_data_to_tuples(
            ground, points
        )

        cls.validate_coordinates_input(points)
        cls.validate_ground_input(ground)
        cls.validate_ground_size(ground, points)

        return ground, points


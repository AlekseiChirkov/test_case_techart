from dataclasses import dataclass

from bot.validators import InputValidator


@dataclass
class Ground:
    """Class to process arguments from console/terminal"""

    def __init__(self, console_args: str):
        """
        Initialize grid size and delivery coordinates
        :param console_args: string argument from console
        """

        grid, points = InputValidator.validate_ground_data_input(
            console_args
        )
        self.grid = grid
        self.coordinates = points



from unittest import TestCase

from bot.processors import ProcessObjectDatatype


class ProcessObjectDatatypeTests(TestCase):
    """Test datatype processing"""

    def test_processing_ground_data_to_tuple(self) -> None:
        """
        Test that datatype processing successfully
        :return: None
        """

        ground, points = ProcessObjectDatatype.process_ground_data_to_tuples(
            '5x5', ['1, 2', '2, 2', '5, 4']
        )

        self.assertEqual(ground, (5, 5))
        self.assertEqual(points, ((1, 2), (2, 2), (5, 4)))

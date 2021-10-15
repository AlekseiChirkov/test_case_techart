class ProcessObjectDatatype:
    """Class to process objects to the desired type"""

    @staticmethod
    def process_ground_data_to_tuples(ground: str, points: list) -> (tuple, tuple):
        """
        Method convert string with ground and coordinates data to tuples
        :param ground: string with ground data
        :param points: list with coordinates data
        :return: two tuples ground and coordinates
        """

        ground = tuple(map(int, ground.split('x')))
        points = tuple(tuple(map(int, point.split(','))) for point in points)

        return ground, points

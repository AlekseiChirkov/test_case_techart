import sys

from bot.deliveries import DeliverPizza
from bot.models import Coordinates


if __name__ == '__main__':
    data = Coordinates(sys.argv[1])
    solution = DeliverPizza.get_delivery_route(data.coordinates)
    print(solution)

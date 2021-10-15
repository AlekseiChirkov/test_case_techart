import sys

from bot.delivery_man import DeliveryMan
from bot.ground import Ground


if __name__ == '__main__':
    data = Ground(sys.argv[1])
    solution = DeliveryMan.show_route(data.coordinates)
    DeliveryMan.print_solution(solution)

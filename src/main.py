import sys

from bot.delivery_man import DeliveryMan
from bot.ground import Ground


def main() -> None:
    """
    Main function to run process
    :return: None
    """

    data = Ground(sys.argv[1])
    DeliveryMan.show_route(data.coordinates)


if __name__ == '__main__':
    main()

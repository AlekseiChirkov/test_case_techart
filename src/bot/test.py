import re
from itertools import permutations


def add_action(arr, action, steps):
    for i in range(steps):
        arr.append(action)

    return arr


def get_solution(coords1, coords2):
    n1, m1 = coords1
    n2, m2 = coords2

    solution = list()

    solution = add_action(solution, 'E' if n1 < n2 else 'W', abs(n1 - n2))
    solution = add_action(solution, 'N' if m1 < m2 else 'S', abs(n1 - n2))

    solution.append('D')

    return "".join(solution)


def get_path(coords):
    l = 0
    path = ''
    prev_coords = [0, 0]
    for coord in coords:
        local_path = get_solution(prev_coords, coord)
        prev_coords = coord
        path += local_path

    return path


input_str = input()

pizzas = re.findall(r'\((\d+, \d+)\)', input_str)
pizzas_coords = list()

for pizza in pizzas:
    pizzas_coords.append(list(map(int, pizza.split(', '))))

path_len = 1000000000
cur_path = ''
for coords in permutations(pizzas_coords):
    path = get_path(coords)
    if len(path) < path_len:
        path_len = len(path)
        cur_path = path

print(cur_path)

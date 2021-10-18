# Description

Pizzabot - a robot that delivers pizza. The task is to instruct Pizzabot on how
to deliver pizzas to all the houses in a neighborhood. There is a grid
(where every point on it is a house) and a list of coordinates (points), each
point - house in need of pizza delivery. Script should return a list of
instructions for getting Pizzabot to those locations and deliver pizza.

# How Pizzabot works

Pizzabot has the following actions:

```
- N: Move north
- S: Move south
- E: Move east
- W: Move west
- D: Drop pizza
```

Pizzabot always starts at (0, 0) position. As with a Cartesian plane,
this point lies at the most south-westerly point of the grid.

Pizzabot receives an input string as the following: 5x5 (1, 2) (3, 3) (4, 4).
Where 5x5 - grid size and (1, 2) (3, 3) (4, 4) are points to deliver pizza.
Pizza bot tries to parse the input string and return a list of instructions.
The result string is ENNDEENDEND

# Version

1.0.0

# Requirements

- Python 3.x
- Ubuntu OS 16.04 or later

# How to use
## Launch in terminal

- Open Ubuntu terminal
- Enter pizzabot-horvku directory
- Enter command:
```sh
$ python3 ./src/main.py "5x5 (1, 1) (2, 5) (5, 5)"
```
- You will get following result: ENDENNNNDEEED

import random

# Constants for tetrominoes
EMPTY = 0
I = 1
J = 2
L = 3
O = 4
S = 5
T = 6
Z = 7

# Dimensions of the grid
WIDTH = 10
HEIGHT = 20

# Define tetromino shapes
tetrominoes = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, I, I, I, I, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, J, J, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, L, L, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, O, O, O, O, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, S, S, S, S, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, T, T, T, T, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, Z, Z, Z, Z, EMPTY, EMPTY]
]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == EMPTY:
                print(".", end="")
            else:
                print(chr(ord("A") - 1 + cell)), end
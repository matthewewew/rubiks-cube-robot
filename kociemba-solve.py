#testing kociemba library
from kociemba import solve

cube = "UUUUUUUUURRRRRRRRRFFFFFFBFFDDDDDDDDDLLLLLLLLLFBBBBBBBB"
solution = solve(cube)

print("solution: ", repr(solution))
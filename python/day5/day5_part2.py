from collections import defaultdict
from re import findall
from math import copysign

lines = [ line.rstrip() for line in open("day5_test.txt", "r")]

grid = defaultdict(int)

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

for line in lines:
    x1, y1, x2, y2 = map(int, findall(r'(\d+)', line))

    print("(" + str(x1) + "," + str(y1) + ") - (" + str(x2) + "," + str(y2) + ")")

    dx = sign(x2 - x1)
    dy = sign(y2 - y1)

    while (x1, y1) != (x2 + dx, y2 + dy):
        print("drawing (" + str(x1) + "," + str(y1) + ") - (" + str(x2) + "," + str(y2) + ")")
        grid[(x1,y1)] += 1
        x1, y1 = x1 + dx, y1 + dy

sum = sum(x > 1 for x in grid.values())
print(sum)
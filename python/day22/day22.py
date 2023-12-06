from collections import defaultdict
from heapq import heappop, heappush
import math
from re import M, findall
import copy
from math import floor, ceil, sqrt
from collections import Counter


def clamp(f):
    if f > 50:
        return 50
    elif f < -50:
        return -50
    else:
        return f

def read_file():
    f = open("data.txt", "r")
    res = []
    for line in f:
        g = list(map(lambda x: clamp(int(x)), findall(r'(-?\d+)', line.strip())))

        if g[0] == g[1]:
            continue

        if g[2] == g[3]:
            continue

        if g[4] == g[5]:
            continue

        g.append(line.startswith("on"))
        res.append(g)

    return res


input = read_file()
print(input)



cubes = defaultdict(int)
for line in input:
    print(line)
    for x in range(line[0], line[1] + 1):
        for y in range(line[2], line[3] + 1):
            for z in range(line[4], line[5] + 1):
                key = (x,y,z)
                if line[6]:
                    cubes[key] += 1
                else:
                    if key in cubes.keys():
                        del cubes[key]

#print(cubes)
print(len(cubes))
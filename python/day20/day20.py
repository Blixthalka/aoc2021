from collections import defaultdict
from heapq import heappop, heappush
from re import M, findall
import copy
from math import floor, ceil, sqrt
from collections import Counter

def read_file():
    f = open("data.txt", "r")

    curr = True
    algo = []
    data = {}
    y = 0
    for l in f:
        line = l.strip()
        print(line, not (line.startswith('#') or line.startswith('.')), curr)

        if not (line.startswith('#') or line.startswith('.')):
            curr = False
        elif curr:
            for c in line:
                if c == '#':
                    algo.append(1)
                else:
                    algo.append(0)
        else:
            for x, c in enumerate(line):
                if c == '#':
                   data[(x,y)] = 1
            y += 1

    return algo, data

algo, data = read_file()
#print(data)
#print(algo)

def bounding_box(data, index):
    max_r = max(map(lambda c: c[index], data.keys()))
    min_r = min(map(lambda c: c[index], data.keys()))
    return min_r, max_r

def print_data(data):
    min_y, max_y = bounding_box(data, 1)
    min_x, max_x = bounding_box(data, 0)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x,y) in data.keys() and data[(x,y)] == 1:
                v = '#'
            else:
                v = '.'
            print(v, end="")
        print("")
    print("")

def full_range(min_r, max_r, more):
    return range(min_r - more, max_r + more + 1)

print_data(data)
for i in range(100):
    print(i)
    data_c = {}
    min_y, max_y = bounding_box(data, 1)
    min_x, max_x = bounding_box(data, 0)

    y_range_1 = full_range(min_y, max_y, 1)
    x_range_1 = full_range(min_x, max_x, 1)
    y_range_0 = full_range(min_y, max_y, 0)
    x_range_0 = full_range(min_x, max_x, 0)

    x_range = x_range_1
    y_range = y_range_1

    for y in y_range:
        for x in x_range:
            binary = ''
            for dy in range(y - 1, y + 2):
                for dx in range(x - 1, x + 2):
                    if (dx,dy) in data.keys():
                        val = 1
                    else:
                        if algo[0] == 0:
                            val = 0
                        else:
                            if i % 2 == 0:
                               val = 0
                            else:
                                if (not dy in y_range_0) or (not dx in x_range_0):
                                    #print("outside", x_range, y_range, (dx,dy))
                                    val = 1
                                else:
                                    val = 0


                    binary = binary + str(val)
            # if (y == min(y_range)):
            #     print((x,y), binary, int(binary, 2), algo[int(binary, 2)])
            if algo[int(binary, 2)] == 1:
                data_c[(x,y)] = 1

    if i % 2 == 0 and algo[0] == 1:
        #print("running boundy", i)
        #print("bf")
        #print_data(data_c)
        # min_y, max_y = bounding_box(data, 1)
        # min_x, max_x = bounding_box(data, 0)

        x_range = full_range(min_x, max_x, 2)
        y_range = full_range(min_y, max_y, 2)

        for y in [min(y_range), max(y_range)]:
            for x in x_range:
                data_c[(x,y)] = 1

        for x in [min(x_range), max(x_range)]:
            for y in y_range:
                data_c[(x,y)] = 1

        #print("af")
       #print_data(data_c)

    data = data_c

print_data(data)
print(len(data))
from collections import defaultdict
from heapq import heappop, heappush
from re import findall



def read_file():
    f = open("day17.txt", "r")
    return list(map(int, findall(r'(-?\d+)', f.readline().strip())))

input = read_file()
print(input)

area = defaultdict(int)

min_x = min(input[0], input[1])
max_x = max(input[0], input[1])

min_y = min(input[2], input[3])
max_y = max(input[2], input[3])

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        area[(x,y)] += 1

dx, dy = 6, 3
max_y = -200000
hits = 0

z = 300
for dy_c in range(-z, z):
    for dx_c in range(-z, z):
        dy = dy_c
        dx = dx_c
        local_max_y = -2000000
        x, y = 0, 0
        #print("start", dy, dx)
        for _ in range(z):
            x += dx
            y += dy

            local_max_y = max(y, local_max_y)

            #print((x,y))

            if (x,y) in area.keys():
                print("hit", local_max_y, dy_c, dx_c)
                max_y = max(local_max_y, max_y)
                hits += 1
                break

            dx -= 1 if dx > 0 else 0
            dy -= 1


print(hits)
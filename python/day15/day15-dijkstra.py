from collections import defaultdict
from heapq import heappop, heappush

def read_file():
    f = open("day15.txt", "r")
    map = defaultdict(int)
    for y, line in enumerate(f):
        for x, val in enumerate(line.strip()):
            map[(x,y)] = int(val)
    return map


risk_map_original = read_file()
risk_map = defaultdict(int)


length_original_x = max(map(lambda c: c[0], risk_map_original)) + 1
length_original_y = max(map(lambda c: c[1], risk_map_original)) + 1

for add_y in range(0, 5):
    for add_x in range(0, 5):
        for (x,y), value in risk_map_original.items():
            risk = (value + add_x + add_y)
            if risk > 9:
                risk = risk % 9
            risk_map[(x + (add_x * length_original_x), y + (add_y * length_original_y))] = risk

max_x = max(map(lambda c: c[0], risk_map))
max_y = max(map(lambda c: c[1], risk_map))

def print_map(mapz):
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in mapz.keys():
                val = mapz[(x,y)]
            else:
                val = "."
            print("%3d " % (val), end="")
        print("")

path_map = defaultdict(int)

distances = {}
for k in risk_map:
    distances[k] = 222222222

distances[(0, 0)] = 0
heap = [(0, (0,0))]

#for _ in range(5):
while heap:
    (dist, (x, y)) = heappop(heap)

    for target in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        t_x, t_y = target
        if t_x > max_x or t_x < 0 or t_y > max_y or t_y < 0:
            continue

        new_dist = dist + risk_map[target]
        if new_dist >= distances[target]:
            continue

        distances[target] = new_dist
        heappush(heap, (new_dist, target))





print_map(distances)
print(distances[(max_x, max_y)])
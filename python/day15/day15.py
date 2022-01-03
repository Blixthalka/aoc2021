from collections import defaultdict


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
            if x == 0 and y == 0:
                print(str((x,y)) + ' ' + str(x + (add_x * length_original_x)))
            risk_map[(x + (add_x * length_original_x), y + (add_y * length_original_y))] = risk


max_x = max(map(lambda c: c[0], risk_map))
max_y = max(map(lambda c: c[1], risk_map))

def print_map(mapz):
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            val = mapz[(x,y)]
            print("%3d " % val, end="")
        print("")

#print_map(risk_map)

path_map = defaultdict(int)

for key, value in risk_map.items():
    (x,y) = key
    if x == max_x and y == max_y:
        path_map[key] = risk_map[key]
    else:
        path_map[key] = 222222



def update_risk(p_map, r_map):
    for y in range(max_y, -1, -1):
        for x in range(max_x, -1, -1):
            if x == max_x and y == max_y:
                continue
            min = 222222
            for target in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:

                if (target[0] > max_x or target[0] < 0):
                    continue
                if (target[1] > max_y or target[1] < 0):
                    continue

                val = p_map[target]
                if val < min:
                    min = val

            p_map[(x,y)] = r_map[(x,y)] + min

path_map_c = 1
s = 0
while path_map != path_map_c:
    path_map_c = path_map.copy()
    update_risk(path_map, risk_map)
    #print_map(path_map)
    #print("")
    s += 1
    print(s)

#print(s)

def walk(coord, risk):
    #print(coord)
    x = coord[0]
    y = coord[1]

    if x == max_x and y == max_y:
        return risk + risk_map[coord]

    lowest_target = 0
    lowest_target_score = 2222222222

    for target in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:

        if (target[0] > max_x or target[0] < 0):
            continue
        if (target[1] > max_y or target[1] < 0):
            continue

        if path_map[target] < lowest_target_score:
            lowest_target_score = path_map[target]
            lowest_target = target

    return walk(lowest_target, risk + risk_map[coord])


risk = 0
coord = (0,0)
while True:
   # print(coord)
    x = coord[0]
    y = coord[1]

    if x == max_x and y == max_y:
        risk += risk_map[coord]
        break

    lowest_target = 0
    lowest_target_score = 2222222222

    for target in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:

        if (target[0] > max_x or target[0] < 0):
            continue
        if (target[1] > max_y or target[1] < 0):
            continue

        if path_map[target] < lowest_target_score:
            lowest_target_score = path_map[target]
            lowest_target = target

    risk += risk_map[coord]
    coord = lowest_target


print_map(path_map)

print(risk - risk_map[(0,0)])

# print(best)


# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         if (x,y) in score_path:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print("")
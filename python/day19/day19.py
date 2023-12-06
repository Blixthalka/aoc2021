from collections import defaultdict
from heapq import heappop, heappush
from re import M, findall
import copy
from math import floor, ceil, sqrt
from collections import Counter

def read_file():
    f = open("data.txt", "r")

    scanners = []
    scanner = []
    for line in f:
        v = line.strip()

        if v.startswith("---"):
            pass
        elif v == "":
            scanners.append(scanner)
            scanner = []
        else:
            scanner.append(tuple([ int(c) for c in line.strip().split(",")]))

    scanners.append(scanner)
    return scanners

input = read_file()

def calc_pythagoras(scanner):
    res = {}
    for x1, y1, z1 in scanner:
        for x2, y2, z2 in scanner:
            if x1 == x2 and y1 == y2 and z1 == z2:
                continue
            distance = sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2) + pow(abs(z1 - z2), 2) )
            #print(distance, (x1,y1,z1), (x2,y2,z2))
            if distance in res.keys():
                #print("dist", distance, res[distance], "new", ((x1,y1,z1), (x2,y2,z2)))
                continue
            res[distance] = ((x1,y1,z1), (x2,y2,z2))
    return res

beacon_map = defaultdict(int)
beacon_pythagoras_map = calc_pythagoras(input[0])


for x, y, z in input[0]:
    beacon_map[(x,y,z)] += 1

del input[0]
overlapping_nodes = 12
overlapping = (overlapping_nodes * (overlapping_nodes - 1)) // 2

def contains_same_numbers(c1, c2):
    to_take = list(map(abs, c2))

    for v in map(abs, c1):
        if v in to_take:
            to_take.remove(v)
        else:
            return False
    return True

def contains_unique_numbers(c):
    x, y, z = c
    return x != y and x != z and y != z


def flip_pythagoras(pythagoras, move_map, do_flip, transform_to_beacon):
    unique_coords_map = defaultdict(int)
    flipped_pythagoras = {}

    for dist, (c1, c2) in pythagoras.items():
        c1_flipped = transform(flip(flip_move(c1, move_map), do_flip), transform_to_beacon)
        c2_flipped = transform(flip(flip_move(c2, move_map), do_flip), transform_to_beacon)

        flipped_pythagoras[dist] = (c1_flipped, c2_flipped)
        unique_coords_map[c1_flipped] += 1
        unique_coords_map[c2_flipped] += 1

    return flipped_pythagoras, list(unique_coords_map.keys())

def transform(coord, transform_to_beacon):
    #print("trans b4", coord, transform_to_beacon)
    res = tuple([transform_to_beacon[i] + v for i, v in enumerate(coord)])
    #print("trans af", res)
    return res

def flip_complete(coord, move_map, do_flip):
    return flip(flip_move(coord, move_map), do_flip)

def flip(coord, do_flip):
    ll = []
    for i, do in enumerate(do_flip):
        if do:
            ll.append(-coord[i])
        else:
            ll.append(coord[i])
    return tuple(ll)

def flip_move(coord, move_map):
    ll = [0,0,0]

    for i, j in move_map.items():
        ll[j] = coord[i]

    return tuple(ll)

def calc_flip_settings(curr_value, beacon_value):
    counter = 0
    print("flip", curr_value, beacon_value)
    for flip_x in [True, False]:
        for flip_y in [True, False]:
            for flip_z in [True, False]:
                for move_x in range(3):
                    for move_y in range(3):
                        for move_z in range(3):
                            move_map = {}
                            if move_x == move_y or move_x == move_z or move_y == move_z:
                                continue
                            move_map[0] = move_x
                            move_map[1] = move_y
                            move_map[2] = move_z

                            do_flip = [flip_x, flip_y, flip_z]

                            new_c1 = flip_complete(copy.deepcopy(curr_value[0]), move_map, do_flip)
                            new_c2 = flip_complete(copy.deepcopy(curr_value[1]), move_map, do_flip)
                            new_c3 = flip_complete(copy.deepcopy(curr_value[2]), move_map, do_flip)
                            print(do_flip, move_map)
                            #print("c", curr_value)
                            #print("n", (new_c1, new_c2, new_c3))
                            #print("b", beacon_value)

                            counter += 1

                            transform_to_beacon1 = []
                            for coord_index in range(3):
                                per_coord_count_list = []
                                for bb in [beacon_value[0][coord_index], beacon_value[1][coord_index], beacon_value[2][coord_index]]:
                                    for cc in [new_c1[coord_index], new_c2[coord_index], new_c3[coord_index]]:
                                        per_coord_count_list.append(bb - cc)

                                match_counter = Counter(per_coord_count_list)
                                symbol, count = match_counter.most_common(1)[0]
                                print("ss", symbol, count)
                                if count >= 3:
                                    transform_to_beacon1.append(symbol)

                            if len(transform_to_beacon1) == 3:
                                return do_flip, move_map, tuple(transform_to_beacon1)
                            #print("false", move_map, do_flip)
    print("counter", counter)
    raise OSError

scanner_positions = [(0,0,0)]
index = 0
while len(input) > 0:
    #print("len", len(input), index, beacon_pythagoras_map)
    scanner = copy.deepcopy(input[index])
    pythagoras = calc_pythagoras(scanner)

    matches = 0
    for dist in pythagoras.keys():
        if dist in beacon_pythagoras_map.keys():
            matches += 1

    print("matches", matches, overlapping)
    if matches >= overlapping:
        print("match", index, len(input))
        move_map = {}
        do_flip = []

        x_all = []
        iter = 1
        for key, c_val in pythagoras.items():
            curr_value = copy.deepcopy(c_val)
            if not key in beacon_pythagoras_map.keys():
                continue
            if not (contains_unique_numbers(curr_value[0]) and contains_unique_numbers(curr_value[1])):
                continue
            beacon_value = beacon_pythagoras_map[key]

            other_key = None
            other_val = None
            for other_key, other_val in pythagoras.items():
                if other_key == key:
                    continue
                other_val = copy.deepcopy(other_val)
                if not other_key in beacon_pythagoras_map.keys():
                    continue
                if not (contains_unique_numbers(other_val[0]) and contains_unique_numbers(other_val[1])):
                    continue
                if other_val[0] == curr_value[0] and other_val[1] != curr_value[1]:
                    break

            other_beacon_value = beacon_pythagoras_map[other_key]
            print("--", other_beacon_value, other_val)
            if other_beacon_value[0] != beacon_value[0] and other_beacon_value[0] != beacon_value[1]:
                beacon_other = other_beacon_value[0]
            elif other_beacon_value[1] != beacon_value[0] and other_beacon_value[1] != beacon_value[1]:
                beacon_other = other_beacon_value[1]

            b = (beacon_value[0], beacon_value[1], beacon_other)
            c = (curr_value[0], curr_value[1], other_val[1])

            do_flip, move_map, transform_to_beacon = calc_flip_settings(c, b)
            scanner_positions.append(transform_to_beacon)
            print("settings", do_flip, move_map, transform_to_beacon)
            break

        flipped_pythagoras, unique_coords_map = flip_pythagoras(pythagoras, move_map, do_flip, transform_to_beacon)

        for k, v in flipped_pythagoras.items():
            beacon_pythagoras_map[k] = v
        for m in unique_coords_map:
            beacon_map[m] += 1

        del input[index]
        index = 0
    else:
        index += 1


    print("-----", len(input))

hamming = []
for p1 in scanner_positions:
    for p2 in scanner_positions:
        if p1 == p2:
            continue
        ham = (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]))
        print(p1, p2, ham)
        hamming.append(ham)


print(len(scanner_positions))
[print(x) for x in scanner_positions]
print("num", len(beacon_map.keys()))
print("hamm", max(hamming))

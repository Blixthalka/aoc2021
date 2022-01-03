from collections import defaultdict
from heapq import heappop, heappush
from re import M, findall
import copy
from math import floor, ceil, sqrt

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
                print("dist", distance, res[distance], "new", ((x1,y1,z1), (x2,y2,z2)))
                continue
            res[distance] = ((x1,y1,z1), (x2,y2,z2))
    return res

beacon_map = defaultdict(int)
beacon_pythagoras_map = calc_pythagoras(input[0])


for x, y, z in input[0]:
    beacon_map[(x,y,z)] += 1

del input[0]
overlapping = 13 # 6 nodes
overlapping = 1 # 2


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


def flip_pythagoras(pythagoras, move_map, do_flip):
    unique_coords_map = defaultdict(int)
    flipped_pythagoras = {}

    for dist, (c1, c2) in pythagoras.items():
        c1_flipped = flip(flip_move(c1, move_map), do_flip)
        c2_flipped = flip(flip_move(c2, move_map), do_flip)

        flipped_pythagoras[dist] = (c1_flipped, c2_flipped)
        unique_coords_map[c1_flipped] += 1
        unique_coords_map[c2_flipped] += 1

    return flipped_pythagoras, list(unique_coords_map.keys())


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
    print(curr_value, beacon_value)
    for flip_x in [True, False]:
                for flip_y in [True, False]:
                    for flip_z in [True, False]:
                        for non_flip_index in range(3):
                            do_flip = [flip_x, flip_y, flip_z]
                            move_map = {}
                            for qq in range(3):
                                if qq == non_flip_index:
                                    move_map[qq] = non_flip_index
                                else:
                                    move_map[qq] = list(filter(lambda hh: hh != non_flip_index and hh != qq, range(3)))[0]
                            new_c1 = flip_complete(copy.deepcopy(curr_value[0]), move_map, do_flip)
                            new_c2 = flip_complete(copy.deepcopy(curr_value[1]), move_map, do_flip)
                            print(new_c1, new_c2, do_flip, move_map)
                            counter += 1

                            s = 0
                            for coord_index in range(3):
                                first1 = new_c1[coord_index] - beacon_value[0][coord_index]
                                second1 = new_c2[coord_index] - beacon_value[1][coord_index]
                                if coord_index == 2:
                                    print("y", first1, second1)

                                # first2 = new_c1[coord_index] - beacon_value[1][coord_index]
                                # second2 = new_c2[coord_index] - beacon_value[0][coord_index]

                                if first1 == second1:
                                    s += 1
                            #print(s, do_flip, move_map)
                            if s == 3:
                                print("settings", do_flip, move_map)
                                #return do_flip, move_map
    print(counter)
    raise OSError


print(beacon_pythagoras_map)
index = 0
while len(input) > 0:
    print("len", len(input), index, beacon_pythagoras_map)
    scanner = copy.deepcopy(input[index])
    pythagoras = calc_pythagoras(scanner)

    matches = 0
    for dist in pythagoras.keys():
        if dist in beacon_pythagoras_map.keys():
            matches += 1

    print(matches)
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
            beacon_value = beacon_pythagoras_map[key]

            if not (contains_unique_numbers(curr_value[0]) and contains_unique_numbers(curr_value[1])):
                continue

            print("bff", key, "beacon", beacon_value, "curr", curr_value)

            # + + +
            # + + -
            # - + +
            # + - +
            # + - -
            # - + -
            # - - +
            # - - -

            do_flip, move_map = calc_flip_settings(curr_value, beacon_value)



        flipped_pythagoras, unique_coords_map = flip_pythagoras(pythagoras, move_map, do_flip)

        for k, v in flipped_pythagoras.items():
            beacon_pythagoras_map[k] = v
        for m in unique_coords_map:
            beacon_map[m] += 1

        del input[index]
        index = 0
    else:
        index += 1


    print("")

#[print(x) for x in beacon_map.keys()]
print(len(beacon_map.keys()))


# (0,2) -> (2,0) -> (-2,0) -> (0,-2)



# dist 182.01922975334227 ((686, 422, 578), (605, 423, 415)) new ((605, 423, 415), (686, 422, 578))

# ((605, 423, 415), (686, 422, 578))

# ((-537, -823, -458), (-618, -824, -621))
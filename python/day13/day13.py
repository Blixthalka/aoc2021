from collections import defaultdict


def read_file():
    f = open("day13.txt", "r")

    coords = defaultdict(int)
    fold = []

    for line in f:
        if line.strip() == '':
            continue
        if line.startswith("f"):
            vals = line.strip().split()[2].split("=")
            fold.append((vals[0], int(vals[1])))
        else:
            key = tuple(map(lambda x: int(x), line.strip().split(",")))
            coords[key] += 1


    return coords, fold

coords, fold  = read_file()

#print(coords)
#print(fold)

for (f_type, f_val) in fold:
    coords_c = defaultdict(int)
    for (x,y) in coords:

        if f_type == 'x':
            if x < f_val:
                coords_c[(x,y)] += 1
            else:
                dx = f_val - (x - f_val)
                coords_c[(dx,y)] += 1
        elif f_type == 'y':
            if y < f_val:
                coords_c[(x,y)] += 1
            else:
                dy = f_val - (y - f_val)
                coords_c[(x,dy)] += 1

    coords = coords_c

print(len(coords_c))


for y in range(max(map(lambda v: v[1], coords)) + 1):
    for x in range(max(map(lambda v: v[0], coords)) + 1):
        if coords[(x,y)] >= 1:
            print("#", end = "")
        else:
            print(".", end = "")
    print("")

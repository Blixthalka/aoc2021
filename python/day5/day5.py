


def read_file():
    f = open("day5.txt", "r")
    lines = [ parse_line(line) for line in f]

    return lines

def parse_line(line):
    cords = line.split("->")

    cord1 = cords[0].strip().split(",")
    cord2 = cords[1].strip().split(",")

    return [
        [ int(k) for k in cord1],
        [ int(k) for k in cord2]
    ]

lines = read_file()
lines = list(filter(lambda line: (line[0][0] == line[1][0]) != (line[0][1] == line[1][1]), lines))

print(lines)

maxX = 0
maxY = 0

for line in lines:
    for cord in line:
        if cord[0] > maxX:
            maxX = cord[0]
        if cord[1] > maxY:
            maxY = cord[1]

grid = [[0 for i in range(maxY + 1)] for j in range(maxX + 1)]

for line in lines:
    x1 = line[0][0]
    y1 = line[0][1]

    x2 = line[1][0]
    y2 = line[1][1]

    if x1 == x2:
        print("X")
        for y in range(min(y1, y2), max(y1, y2) + 1):
            print('drawing x=' + str(x1) + ', y=' + str(y))
            grid[x1][y] += 1
    elif y1 == y2:
        print("Y")
        for x in range(min(x1, x2), max(x1, x2) + 1):
            print('drawing x=' + str(x) + ', y=' + str(y1))
            grid[x][y1] += 1

sum = 0
for g in grid:
    for k in g:
        if k > 1:
            sum += 1

print(sum)
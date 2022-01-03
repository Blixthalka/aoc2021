def read_file():
    f = open("day11.txt", "r")
    return [ [int(x) for x in line.strip() ] for line in f]

input = read_file()


def increase(x, y, flashed):
    #print("-")
    for dx in range(x-1, x+2):
        for dy in range(y-1, y+2):

            if dx == x and dy == y:
                continue
            if dx < 0 or dy < 0:
                continue
            if dx >= len(input) or dy >= len(input[0]):
                continue
            #print(str(x) + " " + str(y) + " " + str(dx) + " " + str(dy))

            input[dx][dy] += 1
            if input[dx][dy] > 9 and (dx,dy) not in flashed:
                flashed.append((dx,dy))
                increase(dx, dy, flashed)
            #print(str(input_cp[dx][dy]) + " " + str(dx) + " " + str(dy))

flashes = 0



for i in range(0, 300):

    for x in range(0, len(input)):
        for y in range(0, len(input[x])):
            input[x][y] += 1



    flashed = []

    for x in range(0, len(input)):
        for y in range(0, len(input[x])):
            if input[x][y] > 9 and (x,y) not in flashed:
                flashed.append((x,y))
                increase(x, y, flashed)


    for x in range(0, len(input)):
        for y in range(0, len(input[x])):
            if input[x][y] > 9:
                input[x][y] = 0

    asdf = True
    for x in range(0, len(input)):
        for y in range(0, len(input[x])):
            if input[x][y] != 0:
                asdf = False
    if asdf:
        print(i +1 )
        break;



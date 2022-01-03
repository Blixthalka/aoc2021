

def read_file():
    f = open("day9.txt", "r")
    return [ [ int(v) for v in line.strip()] for line in f]





input = read_file()


points = []


def less(input, value, i, j):
    if i == -1 or j == -1:
        return True

    if i == len(input) or j == len(input[0]):
        return True

    return value < input[i][j]

for i in range(len(input)):
    for j in range(len(input[i])):
        value = input[i][j]
        check = [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1)
        ]
        res = True
        for (ic, jc) in check:
            res = res and less(input, value, ic, jc)
        if res:
            points.append(value + 1)


print(sum(points))
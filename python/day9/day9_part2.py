
import functools

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


def inspect(input, i, j):
    if i == -1 or j == -1:
        return True

    if i == len(input) or j == len(input[0]):
        return True

    return input[i][j] == 9

def search(input, stack, checked, in_basin):
    if len(stack) == 0:
        return in_basin

    (i, j) = stack.pop()

    if (i,j) in checked:
        return search(input, stack, checked, in_basin)

    checked.append((i,j))

    if inspect(input, i, j):
        return search(input, stack, checked, in_basin)

    in_basin.append(input[i][j])


    check = [
        (i + 1, j),
        (i - 1, j),
        (i, j + 1),
        (i, j - 1)
    ]

    stack.extend(check)
    return search(input, stack, checked, in_basin)


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
            points.append((i,j))


res = sorted([len(search(input, [p], [], [])) for p in points], reverse=True)[:3]

v = functools.reduce(lambda a, b: a * b, res)




print(v)
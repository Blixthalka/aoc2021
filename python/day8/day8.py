

def read_file():
    f = open("day8.txt", "r")
    res = []
    for line in f:
        v = line.strip().split("|")

        first = v[0].split()
        second = v[1].split()
        res.append((first, second))

    return res



input = read_file()

one = 2
four = 4
seven = 3
eight = 8

sum = 0
for (_, out) in input:
    for v in out:
        length = len(v)
        if length == 2 or length == 4 or length == 3 or length == 7:
            print(v)
            sum += 1

print(sum)
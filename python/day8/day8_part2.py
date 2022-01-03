

def read_file():
    f = open("day8.txt", "r")
    res = []
    for line in f:
        v = line.strip().split("|")

        first = v[0].split()
        second = v[1].split()
        res.append((first, second))

    return res


def find_length(inp, length):
    for i in inp:
        v = sort(i)
        if len(v) == length:
            #return sort(v)
            return v

def find(inp, length, other, amount_of_same, not_this = ""):
    for i in inp:
        v = sort(i)
        if len(v) == length and v != not_this:
            sum = 0
            for c in v:
                if c in other:
                    sum += 1
            if sum == amount_of_same:
                #return sort(v)
                return v


def sort(value):
    vals = sorted(value)
    res = ""
    for v in vals:
        res += v
    return res

def decode(inp):
    one = find_length(inp, 2)
    four = find_length(inp, 4)
    seven = find_length(inp, 3)
    eight = find_length(inp, 7)
    six = find(inp, 6, one, 1)
    nine = find(inp, 6, four, 4)
    zero = find(inp, 6, four, 3, six)
    three = find(inp, 5, one, 2)
    five = find(inp, 5, six, 5)
    two = find(inp, 5, one, 1, five)

    dict = {
        zero: "0",
        one: "1",
        two: "2",
        three: "3",
        four: "4",
        five: "5",
        six: "6",
        seven: "7",
        eight: "8",
        nine: "9"
    }

    if len(dict) != 10:
        print(dict)
        print(inp)
        exit(1)

    return dict

input = read_file()

sum = 0

for (inp, out) in input:
    dict = decode(inp)
    print(dict)
    local = ""
    for v in out:
        local += dict[sort(v)]
    sum += int(local)

print(sum)
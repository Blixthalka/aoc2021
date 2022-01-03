def read_file():
    f = open("day10.txt", "r")
    return [ line.strip() for line in f]

input = read_file()


scoring_table = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

expected_table = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

print(input)

score = 0
for row in input:
    stack = []
    for char in row:
        if char in scoring_table:
            expected = expected_table[stack.pop()]
            if char != expected:
                score += scoring_table[char]
        else:
            stack.append(char)

print(score)

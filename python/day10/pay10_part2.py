def read_file():
    f = open("day10.txt", "r")
    return [ line.strip() for line in f]

input = read_file()


scoring_table = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

expected_table = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}



score = []
for i, row in enumerate(input):
    stack = []
    exit = False
    for char in row:
        if char in scoring_table:
            expected = expected_table[stack.pop()]
            if char != expected:
                print(char + expected)
                exit = True
                break
        else:
            stack.append(char)

    if exit:
        continue

    print(str(i) + " " + str(stack))
    if len(stack) > 0:
        local_score = 0
        stack.reverse()

        for v in stack:
            local_score = int((local_score * 5) + scoring_table[expected_table[v]])

        score.append(local_score)

sorted_score = sorted(score)

index = len(sorted_score) // 2
print(str(len(sorted_score)) + " " + str(index))
print(sorted_score[index])

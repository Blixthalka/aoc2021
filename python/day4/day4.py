

def read_file():
    f = open("day4.txt", "r")

    boards = []
    board = []

    for i, line in enumerate(f):
        if i == 0:
            numbers = [ int(x.strip()) for x in line.split(",")]
            continue

        if i == 1:
            continue

        vals = line.strip().split()
        #print(vals)
        if len(vals) == 0:
            continue

        board.append([ int(x) for x in vals])

        if i % 6 == 0:
            boards.append(board)
            board = []

    #print(len(boards))
    return (numbers, boards)


def is_bingo(board, drawn_numbers):
    unmarked_sum = 0
    any_match = False

    for i in range(0, len(board)):
        row_match = True
        col_match = True
        for j in range(0, len(board)):
            row_match = row_match and (board[i][j] in drawn_numbers)
            col_match = col_match and (board[j][i] in drawn_numbers)

            if not (board[i][j] in drawn_numbers):
                unmarked_sum += board[i][j]

        any_match = any_match or col_match or row_match

    return (any_match, unmarked_sum)


def run_1():
    (all_numbers, boards) = read_file()
    drawn_numbers = []

    for number in all_numbers:
        drawn_numbers.append(number)
        #print(drawn_numbers)

        for board in boards:
            (match, sum) = is_bingo(board, drawn_numbers)

            if match:
                print(number)
                print(sum)
                return sum * number

Result = run_1()
print(Result)
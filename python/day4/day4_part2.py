

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
        if len(vals) == 0:
            continue

        board.append([ int(x) for x in vals])

        if i % 6 == 0:
            boards.append(board)
            board = []

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

        def filter_board(b):
            (match, sum) = is_bingo(b, drawn_numbers)
            return not match


        if len(boards) > 1:
            boards = list(filter(filter_board, boards))
        elif len(boards) == 1:
            (match, sum) = is_bingo(boards[0], drawn_numbers)
            if match:
                print(number)
                print(sum)
                return sum * number
        else:
            return None

Result = run_1()
print(Result)
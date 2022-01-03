from collections import defaultdict


def read_file():
    f = open("day14.txt", "r")
    ops = {}
    for i, line in enumerate(f):
        if i == 0:
            sequence = line.strip()
            continue
        if line.strip() == "":
            continue

        v = line.strip().split(" -> ")
        ops[v[0]] = v[1]

    return sequence, ops

sequence, ops  = read_file()

print(sequence)

seq = defaultdict(int)

for i in range(len(sequence) - 1):
    seq[sequence[i] + sequence[i+1]] += 1

print(seq)

for z in range(40):
    new_seq = defaultdict(int)
    for operation, num in seq.items():

        operation_value = ops[operation]
        print("ops " + str(operation[0] + operation_value))
        new_seq[operation[0] + operation_value] += num
        new_seq[operation_value + operation[1]] += num

    seq = new_seq
    print(seq)

counter = defaultdict(int)

for operation, num in seq.items():
    counter[operation[0]] += num

counter['B'] += 1

min_l = min(map(lambda x: x[1], counter.items()))
max_l = max(map(lambda x: x[1], counter.items()))

print(max_l)
print(min_l)
print(max_l - min_l)
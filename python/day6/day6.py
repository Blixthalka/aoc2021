from collections import defaultdict
from re import findall

f = open("day6.txt", "r")

values = list(map(int, findall(r'(\d+)', f.readline().strip())))

dict_vals = defaultdict(int)

for v in values:
    dict_vals[v] += 1

for day in range(256):
    new_dict = defaultdict(int)

    for k in dict_vals:
        v = dict_vals[k]

        if k == 0:
            new_dict[6] += v
            new_dict[8] += v
        else:
            new_dict[k - 1] += v

    dict_vals = new_dict

print('res ' + str(sum([dict_vals[k] for k in dict_vals])))
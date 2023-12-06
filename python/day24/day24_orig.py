from collections import defaultdict
from heapq import heappop, heappush
import math
from re import M, findall
import copy
from math import floor, ceil, sqrt
from collections import Counter


def read_file():
    f = open("data.txt", "r")
    return [line.strip().split() for line in f]

input = read_file()
#print(input)

def set(string, index, val):
    tmp = ""
    if index != 0:
        tmp += string[:index]

    tmp += str(val)

    if len(tmp) < 14:
        tmp += string[index+1:]
    return tmp

def eval(instructions, inp):
    inst_index = 0
    vars = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    def var_or_num(ii):
        if ii in vars.keys():
            return vars[ii]
        else:
            return int(ii)

    quit = False
    for instruction in instructions:
        if quit:
            break

        i_type = instruction[0]

        if i_type == 'inp':
            vars[instruction[1]] = int(inp[inst_index])
            inst_index += 1
        elif i_type == 'mul':
            vars[instruction[1]] = vars[instruction[1]] * var_or_num(instruction[2])
        elif i_type == 'add':
            vars[instruction[1]] = vars[instruction[1]] + var_or_num(instruction[2])
        elif i_type == 'div':
            if var_or_num(instruction[2]) < 0:
                quit = True
            else:
                vars[instruction[1]] = vars[instruction[1]] // var_or_num(instruction[2])
        elif i_type == 'mod':
            if var_or_num(instruction[1]) < 0 or var_or_num(instruction[2]) <= 0:
                quit = True
            else:
                vars[instruction[1]] = vars[instruction[1]] % var_or_num(instruction[2])
        elif i_type == 'eql':
            vars[instruction[1]] = 1 if vars[instruction[1]] == var_or_num(instruction[2]) else 0
        #print(instruction, vars)
    return vars['z']

min_z = 9999999999999999999
iters_min_z_same = 0
inp = "41661111121166"
old_inp = None
inp_index = 0
direction = -1

def transform_index(i):
    i += 1
    if i >= 14:
        i = 0
    return i

round = 0


i = 11111111111111

for w in range(1,10):
    print(eval(input, str(w)))


# while True:
#     local_min_z = 999999999999
#     local_min_val = None
#     for inp_index in range(13,0,-1):
#         for plus in range(-1, -15, -1):
#             for _ in range(-14,0):
#                 for v1 in range(1,10):
#                     for v2 in range(1,10):
#                         local_inp = set(inp, inp_index, v1)
#                         local_inp = set(local_inp, transform_index(inp_index + plus), v2)
#                         vars, quit = eval(input, local_inp)
#                         z = vars['z']
#                         print(round, local_inp, min_z, z)

#                         if z < local_min_z:
#                             local_min_z = z
#                             local_min_val = local_inp
#                         elif z == local_min_z and int(local_inp) < int(local_min_val):
#                             local_min_z = z
#                             local_min_val = local_inp

#     round += 1

#     if local_min_z == 0:
#         print("valid", local_min_val)
#         break


#     if local_min_z < min_z:
#         min_z = local_min_z
#         inp = local_min_val
#     else:
#         print("fail")
#         break












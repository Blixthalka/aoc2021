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

def translate():
    inp_index = 0
    for instruction in input:
        i_type = instruction[0]
        if i_type == 'inp':
            print("%s = int(inp[%s])" % (instruction[1], inp_index))
            inp_index += 1
        elif i_type == 'mul':
            print("%s = %s * %s" % (instruction[1], instruction[1], instruction[2]))
        elif i_type == 'add':
            print("%s = %s + %s" % (instruction[1], instruction[1], instruction[2]))
        elif i_type == 'div':
            print("%s = %s // %s" % (instruction[1], instruction[1], instruction[2]))
        elif i_type == 'mod':
            print("%s = %s %% %s" % (instruction[1], instruction[1], instruction[2]))
        elif i_type == 'eql':
            print("%s = 1 if %s == %s else 0" % (instruction[1], instruction[1], instruction[2]))

def tt():
    for inst in input:
        if inst[0] == 'add' and (inst[1] == 'x' or inst[1] == 'y') and inst[2] != '25' and inst[2] != 'w' and inst[2] != 'z' and inst[2] != '1':
            print(inst[2])


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


func_vals = [
    (11, 14, 1),
    (14, 6, 1),
    (15, 6, 1),
    (13, 13,1),
    (-12, 8, 26),
    (10, 8, 1),
    (-15, 7, 26),
    (13, 10, 1),
    (10, 8, 1),
    (-13, 12, 26),
    (-13, 10, 26),
    (-14, 8, 26),
    (-2, 8, 26),
    (-9, 7, 26)
]
memo = {}

def func_all(inp):
    z = 0
    for i, w, in enumerate(inp):
        w = int(w)
        f1, f2, f3 = func_vals[i]
        if (z,w, f1,f2,f3) in memo.keys():
            z = memo[(z,w,f1,f2,f3)]
        else:
            z2 = func(z,w,f1,f2,f3)
            memo[(z,w,f1,f2,f3)] = z2
            z = z2
        print("11",z)

    return z

def func(z, w, f1, f2, f3):
    x = 0 if (z % 26) + f1 == w else 1
    z = ((z // f3) * ((25 * x) + 1)) + ((w + f2) * x)
    return z

aim = [0]
next_aim = []
prev_aim_path = {0: ""}
aim_path = {}
for index in range(13,11,-1):
    f1, f2, f3 = func_vals[index]
    for inte in range(1,8429555):
        for w in range(1,10):
            val = func(inte,w,f1,f2,f3)
            #print(inte, 84295550)
            if val in aim:
                next_aim.append(inte)
                aim_path[inte] = prev_aim_path[val] + str(w)

    print(aim_path)
    prev_aim_path = aim_path
    aim_path = {}
    aim = copy.deepcopy(next_aim)
    print(index, aim)

print(aim_path)
print(min(map(lambda x: int(x), prev_aim_path.values())))

def transform_index(i):
    i += 1
    if i >= 14:
        i = 0
    return i

def solve1():
    i = 11111734686486

    while i < 45989929946199:
        if '0' in str(i):
            i+=1
            continue
        z = func_all(str(i))
        #z = 1
        print(i, z)
        if z == 0:
            print("valid", i)
            break
        i+= 1

def solve2():
    round = 0
    min_z = 9999999999999999999
    inp = "11111142497866"

    while True:
        local_min_z = 999999999999
        local_min_val = None
        for inp_index in range(13,0,-1):
            for plus in range(-1, -15, -1):
                for _ in range(-14,0):
                    for v1 in range(1,10):
                        for v2 in range(1,10):
                            local_inp = set(inp, inp_index, v1)
                            local_inp = set(local_inp, transform_index(inp_index + plus), v2)
                            z = eval(input, local_inp)

                            print(round, local_inp, min_z, z)

                            if z < local_min_z:
                                local_min_z = z
                                local_min_val = local_inp
                            elif z == local_min_z and int(local_inp) < int(local_min_val):
                                local_min_z = z
                                local_min_val = local_inp

        round += 1

        if local_min_z == 0:
            print("valid", local_min_val)
            break

        if local_min_z < min_z:
            min_z = local_min_z
            inp = local_min_val
        else:
            print("fail")
            break



#ss ="45989929946199"
#print(func_all(ss))
#print(eval(input, ss))
#solve1()





from collections import defaultdict
from heapq import heappop, heappush
from re import M, findall
import copy
from math import floor, ceil

def read_line(line):
    stack = []
    curr_list = []
    for i in range(1, len(line) - 1):
        c = line[i]

        if c == '[':
            stack.append(curr_list)
            curr_list = []
        elif c == ']':
            ll = stack.pop()
            ll.append(curr_list)
            curr_list = ll
        elif c == ",":
            pass
        else:
            curr_list.append(int(c))

    return curr_list

def read_file():
    f = open("day18.txt", "r")
    return [read_line(line.strip()) for line in f]

input = read_file()

def reduce(num):

    old_magnitude = None

    while True:
        print("reduce", num)

        exploded = explode(num)
        new_magnitude = magnitude(exploded)
        if old_magnitude != new_magnitude:
            old_magnitude = new_magnitude
            num = exploded
            continue

        splitted = split(exploded)
        new_magnitude = magnitude(splitted)
        if old_magnitude != new_magnitude:
            old_magnitude = new_magnitude
            num = splitted
            continue

        break


    return num


def split(num):
   # print("1", num)
    stack = []
    index = 0
    curr_list = num
    while True:
        #print("i", index, curr_list)
        if index >= len(curr_list):
            if len(stack) == 0:
                break
            else:
                index, curr_list = stack.pop()
                continue

        elem = curr_list[index]

        if isinstance(elem, list):
            stack.append((index + 1, curr_list))
            curr_list = elem
            index = 0
        else:
            if elem > 9:
                curr_list[index] = [floor(elem / 2), ceil(elem / 2)]
                print("split")
                break
            index += 1

    #print("2", curr_list)
    return num


def is_explode(ll, dept):
    return not isinstance(ll[0], list) and not isinstance(ll[1], list) and dept >= 4

def explode(num):
    #print("1", num)
    stack = []
    index = 0
    curr_list = num
    right = None
    latest_left_list = None
    latest_left_index = None

    exploded = False

    while True:
       # print("i", index, curr_list)
        if index >= 2:
            if len(stack) == 0:
                break
            else:
                index, curr_list = stack.pop()
                continue

        elem = curr_list[index]
        #print("asdf", elem, curr_list)

        if exploded and not isinstance(elem, list):
            curr_list[index] += right
            break
        elif not isinstance(elem, list):

            latest_left_list = curr_list
            latest_left_index = index
            index += 1
        elif is_explode(elem, len(stack) + 1) and not exploded:
            exploded = True
            left  = elem[0]
            right = elem[1]
            curr_list[index] = 0
            print("explode", left, right)
            if not latest_left_list is None:
                print(latest_left_list, latest_left_index)
                latest_left_list[latest_left_index] += left
            index += 1
        elif isinstance(elem, list):
            stack.append((index + 1, curr_list))
            curr_list = curr_list[index]
            index = 0

   # print("2", num)
    return num


def elem_magnitude(elem, multiplier):
    if isinstance(elem, list):
        return magnitude(elem) * multiplier
    else:
        return elem * multiplier

def magnitude(num):
    return elem_magnitude(num[0], 3) + elem_magnitude(num[1], 2)


def part1():
    prev = input[0]
    for i in range(1, len(input)):
        curr = input[i]
        prev = reduce([prev, curr])


    print(prev)
    print(magnitude(prev))

def part2():
    m = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if i == j:
                continue

            r1 = magnitude(reduce([copy.deepcopy(input[i]), copy.deepcopy(input[j])]))
            r2 = magnitude(reduce([copy.deepcopy(input[j]), copy.deepcopy(input[i])]))

            m = max(r1, m)
            m = max(r2, m)

            if r1 > m or r2 > m:
                print(i,j)
                print(input[i])
                print(input[j])

    print(m)

part2()

from collections import defaultdict
from heapq import heappop, heappush
import math
from re import M, findall
import copy
from math import floor, ceil, sqrt
from collections import Counter

def read_file():
    f = open("data.txt", "r")
    res = []
    for line in f:
        pos = list(map(int, findall(r'(-?\d+)', line.strip())))[1]
        res.append((pos, 0))
    return res

players = read_file()
print(players)

die = 0
rolls = 0
def t(d):
    d += 1
    if d > 100:
        d = 1
    return d


def throw_die(d):
    first = t(d)
    second = t(first)
    third = t(second)
    return first + second + third, third

def to_hash(ll):
    return tuple(ll)

universes = defaultdict(int)
universes[to_hash(players)] += 1

sum_wins = [0, 0]

def calc_score(d1,d2,d3, prev_pos, prev_score):
    p1_die_outcome = d1 + d2 + d3

    p1_local_pos = prev_pos + p1_die_outcome
    while p1_local_pos > 10:
        p1_local_pos -= 10
    return prev_score + p1_local_pos, p1_local_pos


while len(universes) > 0:
    universes_c = defaultdict(int)
    print(len(universes))
    for ((p1_pos, p1_score), (p2_pos, p2_score)), nr_universes in universes.items():
        for p1d1 in range(1,4):
            for p1d2 in range(1,4):
                for p1d3 in range(1,4):
                    p1_local_score, p1_local_pos = calc_score(p1d1, p1d2, p1d3, p1_pos, p1_score)
                    if p1_local_score >= 21:
                        sum_wins[0] += nr_universes
                        continue
                    for p2d1 in range(1,4):
                        for p2d2 in range(1,4):
                            for p2d3 in range(1,4):
                                p2_local_score, p2_local_pos = calc_score(p2d1, p2d2, p2d3, p2_pos, p2_score)
                                if p2_local_score >= 21:
                                    sum_wins[1] += nr_universes
                                else:
                                    universes_c[(p1_local_pos, p1_local_score), (p2_local_pos, p2_local_score)] += nr_universes

        #print(c)

    universes = universes_c



print(sum_wins)
print(max(sum_wins))




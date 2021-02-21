#!/usr/bin/env python3.8

I=open('../03.txt').read().split("\n")

# Part 1.
def findTrees(right,down):
    pos = trees = 0
    for y in range(0,len(I),down):
        if I[y][pos % len(I[y])] == '#':
            trees += 1
        pos += right
    return trees

print(findTrees(3,1))

# Part 2.
paths = [(1,1),
         (3,1),
         (5,1),
         (7,1),
         (1,2)]

import math

print(math.prod([findTrees(path[0],path[1]) for path in paths]))

#!/usr/bin/python3

import math

I=open('../02.txt').read()

# Part 1.
def paper(box):
    l=[int(s) for s in box.split("x")]
    p=[math.prod(L) for L in [l[:i]+l[i+1:] for i in range(3)]]
    return sum(2*p)+min(p)
print(sum([paper(box) for box in I]))

# Part 2.
def ribbon(box):
    l=sorted([int(s) for s in box.split("x")])
    return 2*sum(l[:-1])+math.prod(l)
print(sum([ribbon(box) for box in I]))

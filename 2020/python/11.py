#!/usr/bin/env python3.9
def printm(m):
    for r in m:
        print(r)
    print()

pi = open('../011.sample.txt').read().split('\n')
pi = [[c for c in s] for s in pi]
g = pi.copy()
printm(g)
h = len(pi)
w = len(pi[0])

def us(y: int, x: int, gen: list[list[str]]) -> str:
    yl,yu = y-1,y+2
    xl,xu = x-1,x+2
    if y == 0:
        yl = 0
    elif y == h-1:
        yu = h
    if x == 0:
        xl = 0
    elif x == w-1:
        xu = w
    c = 0
    for Y in range(yl,yu):
        for X in range(xl,xu):
            if X != x and Y != y:
                c += gen[Y][X] == '#'
    if gen[y][x] == 'L' and c == 0:
        gen[y][x] = '#'
    elif gen[y][x] == '#' and c >= 4:
        gen[y][x] = 'L'
    return gen[y][x]

def ng(gen: list[list[str]], c: int) -> int:
    c += 1
    ngen = gen[:]
    for y in range(h):
        for x in range(w):
            ngen[y][x] = us(y,x,gen)
    printm(gen)
    printm(ngen)
    if ngen == gen:
        return c
    else:
        return ng(ngen, c)

print(ng(g,0))
printm(pi)

#!/usr/bin/python3

input=open('../05.txt').read().split("\n")

def part(lst,dir):
    if dir in ('F','L'):
        return lst[:int(len(lst)/2)]
    elif dir in ('B','R'):
        return lst[int(len(lst)/2):]

# Part 1.
def findSeat(seat):
    y = list(range(128))
    x = list(range(8))
    for char in seat[:7]:
        y = part(y,char)
    for char in seat[-3:]:
        x = part(x,char)
    return y.pop(),x.pop()

ids = []
for seat in input:
    row, column = findSeat(seat)
    ids.append(row * 8 + column)

# 983 is too high.
print(max(ids))

# Part 2.
ids = sorted(ids)
for i in range(1,len(ids)):
    if abs(ids[i-1] - ids[i]) != 1:
        print(ids[i] - 1)
        break

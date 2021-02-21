#!/usr/bin/python3

I=open('../3.txt').read()
x=y=0

def move_santa(s):
    global x,y
    if s=="v":
        y-=1
    elif s=="^":
        y+=1
    elif s=="<":
        x-=1
    elif s==">":
        x+=1
    return (x,y)

# Part 1.
print(len(set([(0,0)]+[move_santa(s) for s in I])))

x=y=X=Y=0
def move_robo_santa(s):
    global X,Y
    if s=="v":
        Y-=1
    elif s=="^":
        Y+=1
    elif s=="<":
        X-=1
    elif s==">":
        X+=1
    return (X,Y)

# Part 2.
print(len(set([(0,0)]+[move_santa(s) for s in I[1::2]]+[move_robo_santa(s) for s in I[::2]])))

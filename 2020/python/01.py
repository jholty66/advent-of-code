#!/usr/bin/python3

# Part 1.
I=open('../1.txt').read().split("\n")
I=[int(x) for x in I]

for i in range(len(I)):
    for j in range(i,len(I)):
        if I[i]+I[j] == 2020:
            print(I[i]*I[j])

# Part 2.
for i in range(len(I)):
    for j in range(i,len(I)):
        for k in range(j,len(I)):
            if I[i]+I[j]+I[k] == 2020:
                print(I[i]*I[j]*I[k])

#!/usr/bin/python3

I=open(../'1.txt').read()

# Part 1.
print(sum([1 if x=="(" else -1 for x in I]))

# Part 2.
sum=0
i=0
while True:
    if sum==-1:
        break
    elif I[i]=="(":
        sum+=1
    else:
        sum+=-1
    i+=1
print(i)

#!/usr/bin/python3

I=open("2.in").read().split("\n")
I=[l.split(" ") for l in I]

# Part 1.
ans = 0
for password in I:
    bounds = [int(i) for i in password[0].split('-')]
    if password[2].count(password[1][0]) in range(bounds[0],bounds[-1]+1):
        ans += 1

print(ans)

# Part 2.

#!/usr/bin/python3

I=open('../2.txt').read().split("\n")
I=[l.split(" ") for l in I]

for password in I:
    password[0] = [int(i) for i in password[0].split('-')]
    password[1] = password[1][:-1]

# Part 1.
print(sum([1 for password in I if password[2].count(password[1][0]) in range(password[0][0],password[0][1]+1)]))

# Part 2.
print(sum([(password[2][password[0][0]-1] == password[1]) != (password[2][password[0][1]-1] == password[1]) for password in I]))

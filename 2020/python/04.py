#!/usr/bin/python3

# Split passports by newline.
I=open('../04.txt').read().split('\n\n')

# Make all feilds be split by space. Create a list for each passport
# where each file is a string.
I = list(map(lambda passport: passport.replace('\n', ' ').split(' '), I))

# Part 1.

# Copy input
# Filter out entries of 'cid' in all passports.
# Then filter all for passport with seven feilds.
I = list(filter(lambda passport: len(set(filter(lambda feild: feild[:3] != 'cid', passport))) == 7, I))
print(len(I))

# Part 2.

# Change each passport into dictionary where each item is the field
# associating each key with its value.
I = list(map(lambda passport: dict(map(lambda feild: feild.split(':'), passport)), I))

a = 0
for p in I:
    if p["hgt"][-2:] in ('cm','in'):
        a += \
        int(p["byr"]) in range(1920,2003) and \
        int(p["iyr"]) in range(2010,2021) and \
        int(p["eyr"]) in range(2020,2031) and \
        ((p['hgt'][-2:] == 'cm' and int(p["hgt"][:-2]) in range(150,194)) or (p['hgt'][-2:] == 'in' and int(p["hgt"][:-2]) in range(59,77))) and \
        p['hcl'][0] == '#' and all(char in "0123456789abcdef" for char in p["hcl"][1:]) and \
        p["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth") and \
        len(p["pid"]) == 9 and all(char in '0123456789' for char in p['pid'])

print(a)

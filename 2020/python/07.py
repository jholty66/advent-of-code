import re

input = open('../07.txt').read().split('\n')

# Part 1.
def lr(rule: str) -> list[str, list[str]]:
    rule = re.sub('bags?\s?', '', rule)[:-2].split(' contain ')
    rule[1] = [re.findall('[a-z]+\s[a-z]+$', bag)[0] for bag in rule[1].split(' , ')]
    return rule

rules = list(map(lambda rule: lr(rule), input))

def findBags(rules: list[str], bags: list[str]) -> int:
    matches = 0
    newbags = []
    for rule in rules:
        if any(bag in rule[1] for bag in bags) and not any(rule[0] == bag for bag in bags):
            matches += 1
            newbags.append(rule[0])
    bags += newbags
    if matches == 0:
        return len(bags) - 1
    else:
        return findBags(rules, bags)

print(findBags(rules, ['shiny gold']))

# Part 2.
def fr(rule: str) -> tuple[str, list[list[int, str]]]:
    rule = re.sub('bags?\s?', '', rule)[:-2].split(' contain ')
    x = [c.split(' ', 1) for c in rule[1].split(' , ')]
    for y in range(len(x)):
        if x[y][0] == 'no':
            x[y][0] = 0
        else:
            x[y][0] = int(x[y][0])
    rule[1] = x
    return tuple(rule)

rules = dict(map(lambda rule: fr(rule), input))

def countBags(rules: dict[str, dict[int, str]], bag: str) -> int:
    bags = [b for b in rules[bag] if b[1] != 'other']
    if len(bags) == 0:
        return 1
    else:
        return sum(bag[0] * countBags(rules, bag[1]) for bag in bags)

# lb 16614
print(countBags(rules, 'shiny gold'))

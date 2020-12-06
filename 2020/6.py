input = open('6.in').read().split('\n\n')
input = list(map(lambda group: group.split('\n'), input))

# Part 1.
print(sum(map(lambda g: len(g), [set(''.join(group)) for group in input])))

# Part 2.
print(sum(map(lambda g: len(set(g[0]).intersection(*g)), input)))

# Golfed
input=list(map(lambda group: group.split('\n'),open('6.in').read().split('\n\n')))
print(sum(map(lambda g: len(g),[set(''.join(group)) for group in input]))) # Part 1.
print(sum(map(lambda g: len(set(g[0]).intersection(*g)),input))) # Part 2.

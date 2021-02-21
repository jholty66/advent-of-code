input = open('../06.txt').read().split('\n\n')
input = list(map(lambda group: group.split('\n'), input))

# Part 1.
print(sum(map(lambda g: len(g), [set(''.join(group)) for group in input])))

# Part 2.
print(sum(map(lambda g: len(set(g[0]).txttersection(*g)), input)))

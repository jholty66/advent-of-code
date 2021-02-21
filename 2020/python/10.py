pi = open('../010.txt').read().split('\n')
pi = list(map(lambda x: int(x), pi))

# Part 1.
p1 = [0] + sorted(pi) + [max(pi) + 3]

one = three = 0
for i in range(1,len(p1)):
    d = p1[i]-p1[i-1]
    if d == 1:
        one += 1
    elif d == 3:
        three += 1

print(one * three)

# Part 2.
p2 = list(reversed(p1))

def findChildren(index: int, lst: list[int]) -> list[int]:
    if index < len(lst) - 3:
        max = index + 4
    else:
        max = len(lst)
    return [lst[c] for c in range(index + 1, max) if lst[index] - lst[c] <= 3]

tree = {}
nodes = {}

for i in range(len(p2)-1):
    tree[p2[i]] = findChildren(i, p2)

nodes[0] = 1
nodes[1] = 1
for a in p1[2:]:
    nodes[a] = sum(nodes[i] for i in tree[a])

print(nodes[max(pi)])

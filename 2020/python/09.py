pi = open('../09.txt').read().split('\n')[:-1] # Last character is a newline.
pi = list(map(lambda x: int(x), pi))

# Part 1.
p = 25
c = 0

def isValid(list: list[int], index: int, preamble: int) -> any:
    for i in range(index, index + preamble):
        for j in range(i + 1, index + preamble):
            if list[i] + list[j] == list[index + preamble]:
                return True
    return False, list[index + preamble], index + preamble

while True:
    ans = isValid(pi, c, p)
    if ans != True:
        print(ans[1])
        break
    c += 1

# Part 2.
index = ans[2]
invalid = ans[1]

for i in range(index):
    for j in range(i + 1, index):
        lst = pi[i:j]
        s = sum(lst)
        if s == invalid:
            print(min(lst) + max(lst))
            break

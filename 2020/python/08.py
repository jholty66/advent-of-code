pi = open('../08.txt').read().split('\n')

instructions = []
for i in range(len(pi)):
    instructions.append(pi[i].split(' '))

# First instruction starts at 0.
# Part 1.
counter = acc = 0
ei = [0]

while True:
    if instructions[counter][0] == 'acc':
        acc += eval(instructions[counter][1])
        counter += 1
    elif instructions[counter][0] == 'jmp':
        counter += eval(instructions[counter][1])
    elif instructions[counter][0] == 'nop':
        counter += 1
    else:
        print('Unknown instruction.')
    if counter in ei:
        break
    else:
        ei.append(counter)
print(acc)

# Part 2.
def testInstruction(instructions: list[list[str, str]]) -> int:
    instructions = str(instructions)
    for i in range(len(instructions)):
        ni = eval(instructions)
        print(ni[i][0])
        if ni[i][0] == 'jmp':
            if eval(ni[i][1]) != 0:
                ni[i][0] = 'nop'
        elif ni[i][0] == 'nop':
            ni[i][0] = 'jmp'

        acc = 0
        counter = 0
        ei [0]
        while True:
            if ni[counter][0] == 'acc':
                acc += eval(ni[counter][1])
                counter += 1
            elif ni[counter][0] == 'jmp':
                counter += eval(ni[counter][1])
            elif ni[counter][0] == 'nop':
                counter += 1
            else:
                print('Unknown instruction.')
            if counter in ei:
                break
            elif counter == 624:
                return acc
            else:
                ei.append(counter)

print(testInstruction(instructions))

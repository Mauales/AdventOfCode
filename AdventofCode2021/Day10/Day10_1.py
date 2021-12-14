import numpy as np

file = open("input.txt")
# file = open("test.txt")

total = 0
complement = {'(' : ')','[' : ']','{' : '}','<' : '>'}
cost = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137}

for line in file:
    pile = []
    for char in list(line.rstrip()):
        #print(char)
        if char in ['(','[','{','<']:
            pile.append(char)
        else:
            last = pile.pop()
            if char != complement[last]:
                # print("\n" + line, end="")
                # print(f"Expected {complement[last]} but found {char} \n")
                total += cost[char]
                break
file.close()

print(total)
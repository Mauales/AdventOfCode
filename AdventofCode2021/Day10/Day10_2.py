import numpy as np

file = open("input.txt")
# file = open("test.txt")

totals = []
complement = {'(' : ')','[' : ']','{' : '}','<' : '>'}
cost = { ')' : 1, ']' : 2, '}' : 3, '>' : 4}

for line in file:
    added = []
    pile = []
    for char in list(line.rstrip()):
        if char in ['(','[','{','<']:
            pile.append(char)
        else:
            last = pile.pop()
            if char != complement[last]:
                pile=[]
                break
    total = 0
    if len(pile) != 0:
        for missing in pile[::-1]:
            #print(total)
            total *= 5
            total += cost[complement[missing]]
        totals.append(total)

file.close()

print(sorted(totals)[int(len(totals)/2)])
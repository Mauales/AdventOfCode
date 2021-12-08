import numpy as np
file = open("input.txt")
# file = open("test.txt")

count = 0

for line in file:
    pos = line.split("|")[1][1:].rstrip().split(" ")
    count += sum([len(x) in [2,3,4,7] for x in pos])
print(count)
file.close()
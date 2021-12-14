from io import TextIOWrapper
import numpy as np
file = open("input.txt")
# file = open("test.txt")

count = 0
mapa = []

for line in file:
    mapa.append(list(map(int, list(line.rstrip()))))
file.close()

for i in range(len(mapa)):
    for j in range(len(mapa[0])):
        center = mapa[i][j]
        top = mapa[i-1][j] if i != 0 else 10
        bot = mapa[i+1][j] if i != len(mapa)-1 else 10 
        left = mapa[i][j-1] if j != 0 else 10 
        right = mapa[i][j+1] if j != len(mapa[0])-1 else 10
        if (top>center and bot>center and left>center and right>center):
            count += center +1 
            # print(f"Minimum at : {i}, {j} with value {center}")
print(count)
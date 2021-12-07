import numpy as np
file = open("input.txt")
# file = open("test.txt")

mapa = np.zeros((1000,1000))
i = 0
for line in file:
    ori, end = line.rstrip().split(" -> ")

    oriCol, oriRow = list(map(int, ori.split(",")))
    endCol, endRow = list(map(int, end.split(",")))
    # print((oriCol, oriRow), (endCol, endRow))
    vector = np.array([endCol-oriCol, endRow-oriRow])
    # print(vector)
    step = vector / max(abs(vector))
    mapa[oriRow,oriCol]+=1
    # print(step)
    while abs(oriCol - endCol) + abs(oriRow - endRow) != 0:
        oriCol += int(step[0])
        oriRow += int(step[1])
        mapa[oriRow, oriCol] += 1
        # print((oriCol, oriRow), (endCol, endRow))
        
    # print(mapa)
print(np.count_nonzero(mapa>=2))
file.close()

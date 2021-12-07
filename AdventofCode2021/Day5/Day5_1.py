import numpy as np
file = open("input.txt")
# file = open("test.txt")

mapa = np.zeros((1000,1000))

for line in file:
    ori, end = line.rstrip().split(" -> ")

    oriY, oriX = list(map(int, ori.split(",")))
    endY, endX = list(map(int, end.split(",")))
    if oriX == endX:
        # print((oriX, oriY),(endX, endY))
        oriY, endY = sorted([oriY, endY]) 
        for ys in range(oriY, endY+1):
            mapa[oriX,ys] += 1
    elif oriY == endY:
        # print((oriX, oriY),(endX, endY))
        oriX, endX = sorted([oriX, endX]) 
        for xs in range(oriX, endX+1):
            mapa[xs,oriY] += 1
    else:
        continue
print(np.count_nonzero(mapa>=2))
file.close()

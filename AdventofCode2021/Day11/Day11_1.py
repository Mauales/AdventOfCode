import numpy as np

file = open("input.txt")
# file = open("test.txt")

test_step1 = """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""

mapa_test_step1 = [np.array(list(map(int,list(x)))) for x in test_step1.split("\n")]

test_step2 = """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""

mapa_test_step2 = [np.array(list(map(int,list(x)))) for x in test_step2.split("\n")]

total = 0
mapa = []

for line in file:
    mapa.append(np.array(list(map(int,list(line.rstrip())))))
file.close()

def get_surrounding_values(x, y, newmap):
    top = newmap[x-1][y] if x != 0 else -1
    bot = newmap[x+1][y] if x != len(newmap)-1 else -1 
    left = newmap[x][y-1] if y != 0 else -1 
    right = newmap[x][y+1] if y != len(newmap[0])-1 else -1
    topleft = newmap[x-1][y-1] if x != 0 and y != 0 else -1
    topright = newmap[x-1][y+1] if x != 0 and y != len(newmap[0])-1 else -1
    botleft = newmap[x+1][y-1] if x != len(newmap)-1 and y != 0 else -1
    botright = newmap[x+1][y+1] if x != len(newmap)-1 and y != len(newmap)-1 else -1
    return [x for x in [top, bot, left, right, topleft, topright, botleft, botright] if x >= 0]

# assert get_surrounding_values(0,0, mapa) == [2,4,7]

def get_surrounding_coord(x, y):
    top = (x-1, y) if x != 0 else ""
    bot = (x+1, y) if x != len(mapa)-1 else ""
    left = (x, y-1) if y != 0 else "" 
    right = (x, y+1) if y != len(mapa[0])-1 else ""
    topleft = (x-1, y-1) if x != 0 and y != 0 else ""
    topright = (x-1, y+1) if x != 0 and y != len(mapa[0])-1 else ""
    botleft = (x+1, y-1) if x != len(mapa)-1 and y != 0 else ""
    botright = (x+1, y+1) if x != len(mapa)-1 and y != len(mapa)-1 else ""
    return [k for k in [top, bot, left, right, topleft, topright, botleft, botright] if k != ""]

def get_over_nine(mapa):
    over_nine = []
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] > 9:
                over_nine.append((i, j))
    return over_nine

def explode_surroundings(mapa, targets):
    for pos in targets:
        mapa[pos[0]][pos[1]] = 0
        for increase in get_surrounding_coord(pos[0], pos[1]):
            if mapa[increase[0]][increase[1]] != 0:
                mapa[increase[0]][increase[1]] += 1
    return mapa

def one_step(mapa, total):
    mapa = [k+1 for k in mapa]
    to_explode = get_over_nine(mapa)
    while len(to_explode) != 0:
        total += len(to_explode)
        mapa = explode_surroundings(mapa, get_over_nine(mapa))
        to_explode = get_over_nine(mapa)
    # print(mapa, len(get_over_nine(mapa)))
    return mapa, total

# mapa, total = one_step(mapa, total)
# print(total, end="\n\n")
# assert np.array_equal(mapa, mapa_test_step1)
# mapa, total = one_step(mapa, total)
# print(total, end="\n\n")
# assert np.array_equal(mapa, mapa_test_step2)

for _ in range(100):
    mapa, total = one_step(mapa, total)
print(total)
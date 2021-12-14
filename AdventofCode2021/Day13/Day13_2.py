import numpy as np
np.set_printoptions(edgeitems=10,linewidth=180)
file = open("input.txt")
# file = open("test.txt")

total = 0
dots = []
folds = []

for line in file:
    if "," in line:
        x,y = list(map(int, line.rstrip().split(",")))
        dots.append((x,y))
    if "fold" in line:
        pre = line.rstrip().split("=")
        axis = pre[0][-1:]
        val = int(pre[1])
        folds.append((axis, val))
file.close()


for fold in folds:
    print(f"Fold {fold[0]}: {fold[1]}")
    if fold[0] == "x":
        dots_to_move = [x for x in dots if x[0] > fold[1]]
        # print(dots_to_move)
        unmodified_dots = [g for g in dots if g not in dots_to_move]
        new_dots = [((fold[1]*2)-x, y) for (x,y) in dots_to_move]
    else:
        dots_to_move = [x for x in dots if x[1] > fold[1]]
        unmodified_dots = [g for g in dots if g not in dots_to_move]
        # print(dots_to_move)
        new_dots = [(x,(2*fold[1])-y) for (x,y) in dots_to_move]
    print(new_dots)
    dots = unmodified_dots + new_dots

y_max = max([i[1] for i in dots])
x_max = max([i[0] for i in dots])
print("X :", "0", x_max)
print("Y :", "0", y_max)   


mapa = []
row = [" " for _ in range(max([i[0] for i in dots])+1)]
for _ in range(max([i[1] for i in dots])+1):
    mapa.append(row)
mapa = np.array(mapa)

for dot in dots:
    #print(dot)
    mapa[dot[1]][dot[0]] = "#"
print(mapa)
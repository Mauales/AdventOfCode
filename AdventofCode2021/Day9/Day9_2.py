from io import TextIOWrapper
import numpy as np
file = open("input.txt")
# file = open("test.txt")

mapa = []

for line in file:
    mapa.append(list(map(int, list(line.rstrip()))))
file.close()

def get_surrounding_values(x, y):
    top = mapa[x-1][y] if x != 0 else 9
    bot = mapa[x+1][y] if x != len(mapa)-1 else 9 
    left = mapa[x][y-1] if y != 0 else 9 
    right = mapa[x][y+1] if y != len(mapa[0])-1 else 9
    return top, bot, left, right

def get_surrounding_coord(x, y):
    top = (x-1, y) if x != 0 else ""
    bot = (x+1, y) if x != len(mapa)-1 else ""
    left = (x, y-1) if y != 0 else "" 
    right = (x, y+1) if y != len(mapa[0])-1 else ""
    return [k for k in [top, bot, left, right] if k != ""]

valles = []
def get_low_points():
    low_p = []
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            center = mapa[i][j]
            top, bot, left, right = get_surrounding_values(i, j)
            if (top>center and bot>center and left>center and right>center):
                low_p.append((i,j))
    return low_p

def next_step(point, basin):
    value = mapa[point[0]][point[1]]
    for neigh in get_surrounding_coord(point[0], point[1]):
        neigh_val = mapa[neigh[0]][neigh[1]]
        if neigh_val > value and neigh_val != 9:
            basin.append(neigh)
            next_step(neigh, basin)

def get_basins(start):
    basin = [start]
    next_step(start, basin)
    return basin

total = 1
basin_list = []
for low_point in get_low_points():
    basin_list.append(len(set(get_basins(low_point))))

for m in sorted(basin_list)[-3:]:
    total *= m

print(total)
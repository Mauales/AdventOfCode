import numpy as np
file = open("input.txt")
#file = open("test.txt")

for line in file:
    pos = np.array(list(map(int, line.rstrip().split(","))))
file.close()

best_pos = -1
best_cost = np.inf

for dest in range(max(pos)):
    cost = np.sum(np.absolute(pos - dest))
    if cost < best_cost:
        best_cost = cost
        print(f"Better Position: {dest}, Cost: {cost}")

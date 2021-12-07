import numpy as np
file = open("input.txt")
# file = open("test.txt")

for line in file:
    pos = np.array(list(map(int, line.rstrip().split(","))))
file.close()

best_pos = -1
best_cost = np.inf

def consume(value):
    total = sum([x for x in range(value+1)])
    return total

for dest in range(max(pos)):
    distance = np.absolute(pos - dest)
    # print(distance)
    transformed = [consume(x) for x in distance]
    # print(transformed)
    cost = sum(transformed)
    # print(cost)
    if cost < best_cost:
        best_cost = cost
        print(f"Better Position: {dest}, Cost: {cost}")

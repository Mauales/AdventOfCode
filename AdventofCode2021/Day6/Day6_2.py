import numpy as np
file = open("input.txt")
#file = open("test.txt")

population = [0 for x in range(9)]

for line in file:
    indiv = np.array(list(map(int, line.rstrip().split(","))))
file.close()

for i in indiv:
    population[i] += 1
print(population)
for i in range(256):
    births = population.pop(0) 
    population.append(births)
    population[6] += births

print(sum(population))
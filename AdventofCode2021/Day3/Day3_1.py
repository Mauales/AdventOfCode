import numpy as np
file = open("input.txt")
#file = open("test.txt")

inicode = np.array(list(map(int, list(file.readline().rstrip()))))
total  = inicode
count = 1
for line in file:
    code = np.array(list(map(int, list(line.rstrip()))))
    total += code
    count += 1

print(f"Count: {count}")
gamma = ''.join([str(int(x>count/2)) for x in total])
print(f"Gamma: {gamma}, Decimal: {int(gamma,2)}")
epsilon = ''.join([str(int(x<count/2)) for x in total])
print(f"Epsilon: {epsilon}, Decimal: {int(epsilon,2)}")

print(f"Result :{int(gamma,2) * int(epsilon,2)}")

file.close()
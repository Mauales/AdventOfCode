import numpy as np
import copy

file = open("input.txt")
#file = open("test.txt")

inicode = np.array(list(map(int, list(file.readline().rstrip()))))
total  = inicode
lenBinCode = len(inicode)
count = 1
filtered = [copy.deepcopy(inicode)]

for line in file:
    code = np.array(list(map(int, list(line.rstrip()))))
    filtered.append(code) 
    total += code
    count += 1

def get_most_abundant(code_list, position):
    sum_bitwise = np.sum(code_list,axis=0)[position]
    if sum_bitwise == len(code_list)/2:
        return -1
    else:
        return sum_bitwise > len(code_list)/2


o2 = np.array(copy.deepcopy(filtered))
co2 = np.array(copy.deepcopy(filtered))
result  = 1
o2_completed = False
co2_completed = False

for position in range(lenBinCode):
    o2_abundant = int(get_most_abundant(o2, position))
    co2_abundant = int(not bool(get_most_abundant(co2, position)))
    
    if o2_abundant != -1:
        o2_mask = [x[position] == o2_abundant for x in o2]
    else:
        o2_mask = [x[position] == 1 for x in o2]
    o2 = o2[o2_mask]
    
    if co2_abundant != -1:
        co2_mask = [x[position] == co2_abundant for x in co2]
    else:
        co2_mask = [x[position] == 0 for x in co2]
    co2 = co2[co2_mask]

    if len(o2) == 1 and not o2_completed:
        o2_result  = "".join([str(x) for x in o2[0]])
        print(f"O2: {o2_result}, Decimal: {int(o2_result,2)}", end = "\n")
        result *= int(o2_result,2)
        o2_completed = True
    if len(co2) == 1 and not co2_completed:
        co2_result  = "".join([str(x) for x in co2[0]])
        print(f"CO2: {co2_result}, Decimal: {int(co2_result,2)}", end = "\n")
        result *= int(co2_result,2)
        co2_completed = True
print(f"Calculated: {result}")
file.close()
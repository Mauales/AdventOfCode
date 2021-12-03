file = open("input.txt")
#file = open("test.txt")

x = 0
depth = 0
aim = 0
for line in file:
    command, value = line.rstrip().split(" ")
    if command == "forward":
        x += int(value)
        depth += (int(value)*aim)
    elif command == "up":
        aim -= int(value)
    else:
        aim += int(value)
    #print(f"x = {x}, y = {depth}, aim = {aim}")

print(f"x = {x}, y = {depth}")
print(f"Result: {x*depth}")

file.close()
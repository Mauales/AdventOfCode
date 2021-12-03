file = open("input.txt")
#file = open("test.txt")

x = 0
y = 0

for line in file:
    command, value = line.rstrip().split(" ")
    if command == "forward":
        x += int(value)
    elif command == "up":
        y -= int(value)
    else:
        y += int(value)

print(f"x = {x}, y = {y}")
print(f"Result: {x*y}")

file.close()
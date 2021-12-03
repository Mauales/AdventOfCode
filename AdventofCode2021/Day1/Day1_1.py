file = open("input_day1.txt")
#file = open("test.txt")

start = int(file.readline().rstrip())
increases = 0

for line in file:
    next = int(line.rstrip())
    if next > start:
        print(f"{next} is greater than {start}")
        increases += 1
    start = next

print(f"Total increases: {increases}")

file.close()
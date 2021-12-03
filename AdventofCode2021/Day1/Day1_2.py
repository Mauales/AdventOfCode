file = open("input_day1.txt")
#file = open("test.txt")

window = [int(file.readline().rstrip()) for x in range(3)]
increases = 0

for line in file:
    next = int(line.rstrip())
    window_pre = sum(window)
    window.pop(0)
    window.append(next)
    window_next = sum(window)
    if window_next > window_pre:
        increases += 1

print(f"Total increases: {increases}")

file.close()
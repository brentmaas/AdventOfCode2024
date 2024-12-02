safe = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        increasing = True
        decreasing = True
        diff = True
        reports = [int(i) for i in line.split()]
        for i in range(1, len(reports)):
            increasing = increasing and reports[i] > reports[i-1]
            decreasing = decreasing and reports[i] < reports[i-1]
            diff = diff and abs(reports[i] - reports[i-1]) <= 3
        if (increasing or decreasing) and diff:
            safe += 1
print(safe)
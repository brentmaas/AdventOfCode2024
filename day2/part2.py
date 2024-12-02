def is_safe(report, trimmed):
    increasing = True
    decreasing = True
    diff = True
    for i in range(1, len(report)):
        increasing = increasing and report[i] > report[i-1]
        decreasing = decreasing and report[i] < report[i-1]
        diff = diff and abs(report[i] - report[i-1]) <= 3
    if (increasing or decreasing) and diff:
        return True
    if not trimmed:
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            if is_safe(new_report, True):
                return True
    return False

safe = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        report = [int(i) for i in line.split()]
        if is_safe(report, False):
            safe += 1
print(safe)
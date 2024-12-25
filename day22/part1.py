total = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        num = int(line)
        for _ in range(2000):
            num = num ^ ((num << 6) & 16777215)
            num = num ^ (num >> 5)
            num = num ^ ((num << 11) & 16777215)
        total += num
print(total)
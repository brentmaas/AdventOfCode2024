nums = []
diffs = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        num = int(line)
        nums.append([num % 10])
        diffs.append([])
        for _ in range(2000):
            oldnum = num
            num = num ^ ((num << 6) & 16777215)
            num = num ^ (num >> 5)
            num = num ^ ((num << 11) & 16777215)
            nums[-1].append(num % 10)
            diffs[-1].append((num % 10) - (oldnum % 10))

total_bananas = {}
for i in range(len(diffs)):
    checked = []
    for j in range(len(diffs[i]) - 3):
        if not tuple(diffs[i][j:j+4]) in checked:
            checked.append(tuple(diffs[i][j:j+4]))
            if tuple(diffs[i][j:j+4]) in total_bananas:
                total_bananas[tuple(diffs[i][j:j+4])] += nums[i][j+4]
            else:
                total_bananas[tuple(diffs[i][j:j+4])] = nums[i][j+4]
print(max(total_bananas.values()))
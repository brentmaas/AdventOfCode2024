left = []
right = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        left_i, right_i = [int(i) for i in line.split()]
        left.append(left_i)
        if not right_i in right:
            right[right_i] = 1
        else:
            right[right_i] += 1
score = 0
for num in left:
    if num in right:
        score += num * right[num]
print(score)
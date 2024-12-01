left = []
right = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        left_i, right_i = [int(i) for i in line.split()]
        left.append(left_i)
        right.append(right_i)
left.sort()
right.sort()
distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])
print(distance)
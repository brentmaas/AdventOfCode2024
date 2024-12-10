field = []
score = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        field.append([int(i) for i in line])
        score.append([1 if i == '9' else 0 for i in line])
for i in range(8, -1, -1):
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == i:
                if x > 0 and field[y][x] == field[y][x-1] - 1:
                    score[y][x] += score[y][x-1]
                if x < len(field[y]) - 1 and field[y][x] == field[y][x+1] - 1:
                    score[y][x] += score[y][x+1]
                if y > 0 and field[y][x] == field[y-1][x] - 1:
                    score[y][x] += score[y-1][x]
                if y < len(field) - 1 and field[y][x] == field[y+1][x] - 1:
                    score[y][x] += score[y+1][x]
total_score = 0
for y in range(len(field)):
    for x in range(len(field[y])):
        if field[y][x] == 0:
            total_score += score[y][x]
print(total_score)
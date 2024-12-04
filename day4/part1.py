word_search = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        word_search.append(line)

num = 0
for y in range(len(word_search)):
    for x in range(len(word_search[y])):
        if word_search[y][x] == 'X':
            left = x >= 3
            right = x < len(word_search[y]) - 3
            up = y >= 3
            down = y < len(word_search) - 3
            if left and word_search[y][x-3:x] == "SAM":
                num += 1
            if right and word_search[y][x+1:x+4] == "MAS":
                num += 1
            if up and word_search[y-1][x] == "M" and word_search[y-2][x] == "A" and word_search[y-3][x] == "S":
                num += 1
            if down and word_search[y+1][x] == "M" and word_search[y+2][x] == "A" and word_search[y+3][x] == "S":
                num += 1
            if left and up and word_search[y-1][x-1] == "M" and word_search[y-2][x-2] == "A" and word_search[y-3][x-3] == "S":
                num += 1
            if left and down and word_search[y+1][x-1] == "M" and word_search[y+2][x-2] == "A" and word_search[y+3][x-3] == "S":
                num += 1
            if right and up and word_search[y-1][x+1] == "M" and word_search[y-2][x+2] == "A" and word_search[y-3][x+3] == "S":
                num += 1
            if right and down and word_search[y+1][x+1] == "M" and word_search[y+2][x+2] == "A" and word_search[y+3][x+3] == "S":
                num += 1
print(num)
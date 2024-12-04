word_search = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        word_search.append(line)

num = 0
for y in range(1, len(word_search) - 1):
    for x in range(1, len(word_search[y]) - 1):
        if word_search[y][x] == 'A' and ((word_search[y-1][x-1] == "M" and word_search[y+1][x+1] == "S") or (word_search[y-1][x-1] == "S" and word_search[y+1][x+1] == "M")) and ((word_search[y-1][x+1] == "M" and word_search[y+1][x-1] == "S") or (word_search[y-1][x+1] == "S" and word_search[y+1][x-1] == "M")):
            num += 1
print(num)
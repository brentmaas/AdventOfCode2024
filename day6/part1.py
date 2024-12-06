x = -1
y = -1
dx = 0
dy = -1
field = []
visited = []
num = 1
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        if '^' in line:
            x = line.index('^')
            y = len(field)
        field.append(line)
        visited.append([False for _ in range(len(line))])
visited[y][x] = True
while 0 <= x + dx < len(field[0]) and 0 <= y + dy < len(field):
    if field[y+dy][x+dx] == '#':
        dx, dy = -dy, dx
    else:
        x += dx
        y += dy
        if not visited[y][x]:
            num += 1
        visited[y][x] = True
print(num)
import copy

x = -1
y = -1
dx = 0
dy = -1
field = []
visited = []
num = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        if '^' in line:
            x = line.index('^')
            y = len(field)
        field.append(line)
        visited.append([[] for _ in range(len(line))])
visited[y][x].append((dx, dy))

def is_looping(ox, oy):
    xi = x
    yi = y
    dxi = dx
    dyi = dy
    visitedi = copy.deepcopy(visited)
    while 0 <= xi + dxi < len(field[0]) and 0 <= yi + dyi < len(field):
        if field[yi+dyi][xi+dxi] == '#' or (yi + dyi == oy and xi + dxi == ox):
            dxi, dyi = -dyi, dxi
        else:
            xi += dxi
            yi += dyi
            if (dxi, dyi) in visitedi[yi][xi]:
                return True
            else:
                visitedi[yi][xi].append((dxi, dyi))
    return False

for y_try in range(len(field)):
    for x_try in range(len(field[y_try])):
        if field[y_try][x_try] != '#' and not (x_try == x and y_try == y) and is_looping(x_try, y_try):
            num += 1

print(num)
def can_push(x, y, dx, dy):
    if field[y][x] == '[':
        return can_push(x + dx, y + dy, dx, dy) and (dy == 0 or can_push(x + dx + 1, y + dy, dx, dy))
    if field[y][x] == ']':
        return can_push(x + dx, y + dy, dx, dy) and (dy == 0 or can_push(x + dx - 1, y + dy, dx, dy))
    if field[y][x] == '@':
        return can_push(x + dx, y + dy, dx, dy)
    return field[y][x] == '.'

def push(x, y, dx, dy):
    if dx == 0 and field[y+dy][x+dx] == '[':
        push(x + dx + 1, y + dy, dx, dy)
    if dx == 0 and field[y+dy][x+dx] == ']':
        push(x + dx - 1, y + dy, dx, dy)
    if field[y+dy][x+dx] != '.':
        push(x + dx, y + dy, dx, dy)
    field[y][x], field[y+dy][x+dx] = field[y+dy][x+dx], field[y][x]

field = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        if '@' in line:
            x = line.index('@') * 2
            y = len(field)
        row = []
        for c in line:
            if c == '#':
                row += ['#', '#']
            elif c == 'O':
                row += ['[', ']']
            elif c == '.':
                row += ['.', '.']
            elif c == '@':
                row += ['@', '.']
        field.append(row)
    
    while line := f.readline().rstrip():
        for c in line:
            if c == '<':
                dx = -1
                dy = 0
            elif c == 'v':
                dx = 0
                dy = 1
            elif c == '>':
                dx = 1
                dy = 0
            elif c == '^':
                dx = 0
                dy = -1
            if can_push(x, y, dx, dy):
                push(x, y, dx, dy)
                x += dx
                y += dy

total = 0
for j in range(len(field)):
    for i in range(len(field[j])):
        if field[j][i] == '[':
            total += 100 * j + i
print(total)
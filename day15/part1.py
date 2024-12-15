field = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        if '@' in line:
            x = line.index('@')
            y = len(field)
        field.append([c for c in line])
    
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
            i = 0
            while field[y+i*dy][x+i*dx] in ['@', 'O']:
                i += 1
            if field[y+i*dy][x+i*dx] == '.':
                for j in range(i, 0, -1):
                    field[y+j*dy][x+j*dx] = field[y+(j-1)*dy][x+(j-1)*dx]
                field[y][x] = '.'
                x += dx
                y += dy

total = 0
for j in range(len(field)):
    for i in range(len(field[j])):
        if field[j][i] == 'O':
            total += 100 * j + i
print(total)
field = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        if 'S' in line:
            sx = line.index('S')
            sy = len(field)
        if 'E' in line:
            ex = line.index('E')
            ey = len(field)
        field.append([c for c in line])
check_dead_ends = True
while check_dead_ends:
    check_dead_ends = False
    for y in range(1, len(field) - 1):
        for x in range(1, len(field[y]) - 1):
            if field[y][x] == '.' and sum([field[y+dy][x+dy] == '#' for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]) == 3:
                field[y][x] = '#'
                check_dead_ends = True
to_check = [(sx, sy, 1, 0)]
scores = {(sx, sy, 1, 0): 0}
while len(to_check) > 0:
    cx, cy, cdx, cdy = to_check.pop()
    if field[cy+cdy][cx+cdx] != '#' and (not (cx + cdx, cy + cdy, cdx, cdy) in scores or scores[(cx + cdx, cy + cdy, cdx, cdy)] > scores[(cx, cy, cdx, cdy)] + 1):
        scores[(cx + cdx, cy + cdy, cdx, cdy)] = scores[(cx, cy, cdx, cdy)] + 1
        to_check.append((cx + cdx, cy + cdy, cdx, cdy))
    if not (cx, cy, -cdy, cdx) in scores or scores[(cx, cy, -cdy, cdx)] > scores[(cx, cy, cdx, cdy)] + 1000:
        scores[(cx, cy, -cdy, cdx)] = scores[(cx, cy, cdx, cdy)] + 1000
        to_check.append((cx, cy, -cdy, cdx))
    if not (cx, cy, cdy, -cdx) in scores or scores[(cx, cy, cdy, -cdx)] > scores[(cx, cy, cdx, cdy)] + 1000:
        scores[(cx, cy, cdy, -cdx)] = scores[(cx, cy, cdx, cdy)] + 1000
        to_check.append((cx, cy, cdy, -cdx))
print(min([scores[(ex, ey, idx, idy)] for idx, idy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if (ex, ey, idx, idy) in scores]))
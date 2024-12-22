import copy

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
to_check = [(sx, sy, 1, 0, [(sx, sy)])]
scores = {(sx, sy, 1, 0): 0}
end_paths = []
best_score = None
while len(to_check) > 0:
    cx, cy, cdx, cdy, path = to_check.pop()
    if field[cy+cdy][cx+cdx] != '#' and (not (cx + cdx, cy + cdy, cdx, cdy) in scores or scores[(cx + cdx, cy + cdy, cdx, cdy)] >= scores[(cx, cy, cdx, cdy)] + 1):
        scores[(cx + cdx, cy + cdy, cdx, cdy)] = scores[(cx, cy, cdx, cdy)] + 1
        if field[cy+cdy][cx+cdx] == 'E':
            if best_score is None or scores[(cx + cdx, cy + cdy, cdx, cdy)] < best_score:
                best_score = scores[(cx + cdx, cy + cdy, cdx, cdy)]
                end_paths = [copy.copy(path) + [(ex, ey)]]
            elif scores[(cx + cdx, cy + cdy, cdx, cdy)] == best_score:
                end_paths.append(copy.copy(path) + [(ex, ey)])
            continue
        else:
            to_check.append((cx + cdx, cy + cdy, cdx, cdy, copy.copy(path) + [(cx + cdx, cy + cdy)]))
    if not (cx, cy, -cdy, cdx) in scores or scores[(cx, cy, -cdy, cdx)] >= scores[(cx, cy, cdx, cdy)] + 1000:
        scores[(cx, cy, -cdy, cdx)] = scores[(cx, cy, cdx, cdy)] + 1000
        to_check.append((cx, cy, -cdy, cdx, copy.copy(path)))
    if not (cx, cy, cdy, -cdx) in scores or scores[(cx, cy, cdy, -cdx)] >= scores[(cx, cy, cdx, cdy)] + 1000:
        scores[(cx, cy, cdy, -cdx)] = scores[(cx, cy, cdx, cdy)] + 1000
        to_check.append((cx, cy, cdy, -cdx, copy.copy(path)))
good_seats = set()
for path in end_paths:
    for seat in path:
        good_seats.add(seat)
print(len(good_seats))
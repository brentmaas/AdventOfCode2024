field = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        if 'S' in line:
            sx = line.index('S')
            sy = len(field)
        if 'E' in line:
            ex = line.index('E')
            ey = len(field)
        field.append(line)

cache = [[None for _ in range(len(field[0]))] for _ in range(len(field))]
cache[ey][ex] = 0
to_check = set([(ex, ey, 0)])
while len(to_check) > 0:
    x, y, steps = to_check.pop()
    if field[y][x-1] != '#' and (cache[y][x-1] is None or cache[y][x-1] > steps + 1):
        cache[y][x-1] = steps + 1
        to_check.add((x - 1, y, steps + 1))
    if field[y][x+1] != '#' and (cache[y][x+1] is None or cache[y][x+1] > steps + 1):
        cache[y][x+1] = steps + 1
        to_check.add((x + 1, y, steps + 1))
    if field[y-1][x] != '#' and (cache[y-1][x] is None or cache[y-1][x] > steps + 1):
        cache[y-1][x] = steps + 1
        to_check.add((x, y - 1, steps + 1))
    if field[y+1][x] != '#' and (cache[y+1][x] is None or cache[y+1][x] > steps + 1):
        cache[y+1][x] = steps + 1
        to_check.add((x, y + 1, steps + 1))

time_to_save = 100
max_cheat = 20
h = {}
total = 0
for y in range(1, len(field) - 1):
    for x in range(1, len(field[y]) - 1):
        if field[y][x] != '#':
            local_cache = [[None for _ in range(len(field[0]))] for _ in range(len(field))]
            local_cache[y][x] = 0
            ends = {}
            to_check = set([(x, y, 0)])
            while len(to_check) > 0:
                cx, cy, steps = to_check.pop()
                if steps >= max_cheat:
                    continue
                if cx > 0 and (local_cache[cy][cx-1] is None or local_cache[cy][cx-1] > steps + 1):
                    local_cache[cy][cx-1] = steps + 1
                    to_check.add((cx - 1, cy, steps + 1))
                if cx > 0 and field[cy][cx-1] != '#':
                    if not (cx - 1, cy) in ends or ends[(cx - 1, cy)] > steps + 1:
                        ends[(cx - 1, cy)] = steps + 1
                if cx < len(field[0]) - 1 and (local_cache[cy][cx+1] is None or local_cache[cy][cx+1] > steps + 1):
                    local_cache[cy][cx+1] = steps + 1
                    to_check.add((cx + 1, cy, steps + 1))
                if cx < len(field[0]) - 1 and field[cy][cx+1] != '#':
                    if not (cx + 1, cy) in ends or ends[(cx + 1, cy)] > steps + 1:
                        ends[(cx + 1, cy)] = steps + 1
                if cy > 0 and (local_cache[cy-1][cx] is None or local_cache[cy-1][cx] > steps + 1):
                    local_cache[cy-1][cx] = steps + 1
                    to_check.add((cx, cy - 1, steps + 1))
                if cy > 0 and field[cy-1][cx] != '#':
                    if not (cx, cy - 1) in ends or ends[(cx, cy - 1)] > steps + 1:
                        ends[(cx, cy - 1)] = steps + 1
                if cy < len(field) - 1 and (local_cache[cy+1][cx] is None or local_cache[cy+1][cx] > steps + 1):
                    local_cache[cy+1][cx] = steps + 1
                    to_check.add((cx, cy + 1, steps + 1))
                if cy < len(field) - 1 and field[cy+1][cx] != '#':
                    if not (cx, cy + 1) in ends or ends[(cx, cy + 1)] > steps + 1:
                        ends[(cx, cy + 1)] = steps + 1
            for endx, endy in ends:
                time_saved = cache[y][x] - cache[endy][endx] - ends[(endx, endy)]
                if time_saved >= time_to_save:
                    if time_saved in h:
                        h[time_saved] += 1
                    else:
                        h[time_saved] = 1
                    total += 1
print(total)
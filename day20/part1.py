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
total = 0
for y in range(1, len(field) - 1):
    for x in range(1, len(field[y]) - 1):
        if field[y][x] == '#':
            nearby = []
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if field[y+dy][x+dx] != '#':
                    nearby.append(cache[y+dy][x+dx])
            if len(nearby) > 0 and max(nearby) - min(nearby) - 2 >= time_to_save:
                total += 1
print(total)
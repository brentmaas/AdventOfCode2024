l = 71
field = [[False for _ in range(l)] for _ in range(l)]
i = 0

def try_bytes():
    steps = [[None for _ in range(l)] for _ in range(l)]
    steps[0][0] = 0
    to_check = set([(0, 0)])
    while len(to_check) > 0:
        cx, cy = to_check.pop()
        if cx == l - 1 and cy == l - 1:
            return True
        if cx > 0 and not field[cy][cx-1] and steps[cy][cx-1] is None:
            steps[cy][cx-1] = steps[cy][cx] + 1
            to_check.add((cx - 1, cy))
        if cx < l - 1 and not field[cy][cx+1] and steps[cy][cx+1] is None:
            steps[cy][cx+1] = steps[cy][cx] + 1
            to_check.add((cx + 1, cy))
        if cy > 0 and not field[cy-1][cx] and steps[cy-1][cx] is None:
            steps[cy-1][cx] = steps[cy][cx] + 1
            to_check.add((cx, cy - 1))
        if cy < l - 1 and not field[cy+1][cx] and steps[cy+1][cx] is None:
            steps[cy+1][cx] = steps[cy][cx] + 1
            to_check.add((cx, cy + 1))
    return False

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        x, y = [int(i) for i in line.split(',')]
        field[y][x] = True
        i += 1
        if i >= 1024 and not try_bytes():
            print(f"{x},{y}")
            break
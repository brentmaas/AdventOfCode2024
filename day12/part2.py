field = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        field.append(line)
regions = [[None for _ in range(len(field[0]))] for _ in range(len(field))]
num_regions = 0
area = {}
perimeter = {}
for y in range(len(field)):
    for x in range(len(field[y])):
        if regions[y][x] is None:
            regions[y][x] = num_regions
            to_check = [(x, y)]
            area[num_regions] = 1
            perimeter[num_regions] = 0
            while len(to_check) > 0:
                xc, yc = to_check.pop(0)
                if xc > 0 and regions[yc][xc-1] is None and field[yc][xc-1] == field[y][x]:
                    to_check.append((xc - 1, yc))
                    regions[yc][xc-1] = num_regions
                    area[num_regions] += 1
                if xc < len(field[y]) - 1 and regions[yc][xc+1] is None and field[yc][xc+1] == field[y][x]:
                    to_check.append((xc + 1, yc))
                    regions[yc][xc+1] = num_regions
                    area[num_regions] += 1
                if yc > 0 and regions[yc-1][xc] is None and field[yc-1][xc] == field[y][x]:
                    to_check.append((xc, yc - 1))
                    regions[yc-1][xc] = num_regions
                    area[num_regions] += 1
                if yc < len(field) - 1 and regions[yc+1][xc] is None and field[yc+1][xc] == field[y][x]:
                    to_check.append((xc, yc + 1))
                    regions[yc+1][xc] = num_regions
                    area[num_regions] += 1
            num_regions += 1

def do_perimeter(x0, y0, dx0, dy0):
    p = 0
    xcheck = x0
    ycheck = y0
    dxcheck = dx0
    dycheck = dy0
    if 0 <= x0 + dx0 < len(field[y0]) and 0 <= y0 + dy0 < len(field) and field[y0+dy0][x0+dx0] == field[y0][x0]:
        xc, yc = x0 + dx0, y0 + dy0
        dx, dy = dx0, dy0
        p = 0
    else:
        xc, yc = x0, y0
        dx, dy = -dy0, dx0
        p = 1
    while (xc, yc, dx, dy) != (x0, y0, dx0, dy0):
        if yc < ycheck or (yc == ycheck and xc < xcheck) or (xcheck == xc and ycheck == yc and dx < dxcheck) or (xcheck == xc and ycheck == yc and dx == dxcheck and dy < dycheck):
            xcheck = xc
            ycheck = yc
            dxcheck = dx
            dycheck = dy
        if 0 <= xc + dy < len(field[y0]) and 0 <= yc - dx < len(field) and field[yc-dx][xc+dy] == field[y0][x0]:
            xc += dy
            yc -= dx
            dx, dy = dy, -dx
            p += 1
        elif 0 <= xc + dx < len(field[y0]) and 0 <= yc + dy < len(field) and field[yc+dy][xc+dx] == field[y0][x0]:
            xc += dx
            yc += dy
        else:
            dx, dy = -dy, dx
            p += 1
    return p, (xcheck, ycheck, dxcheck, dycheck)

checked = []
p, c = do_perimeter(0, 0, 1, 0)
perimeter[regions[0][0]] += p
checked.append(c)
for y in range(len(regions)):
    for x in range(len(regions[y])):
        if x > 0 and regions[y][x] != regions[y][x-1]:
            p, c = do_perimeter(x, y, 0, -1)
            if not c in checked:
                perimeter[regions[y][x]] += p
                checked.append(c)
        if x < len(regions[y]) - 1 and regions[y][x] != regions[y][x+1]:
            p, c = do_perimeter(x, y, 0, 1)
            if not c in checked:
                perimeter[regions[y][x]] += p
                checked.append(c)
        if y > 0 and regions[y][x] != regions[y-1][x]:
            p, c = do_perimeter(x, y, 1, 0)
            if not c in checked:
                perimeter[regions[y][x]] += p
                checked.append(c)
        if y < len(regions) - 1 and regions[y][x] != regions[y+1][x]:
            p, c = do_perimeter(x, y, -1, 0)
            if not c in checked:
                perimeter[regions[y][x]] += p
                checked.append(c)

total = 0
for region in area:
    total += area[region] * perimeter[region]
print(total)
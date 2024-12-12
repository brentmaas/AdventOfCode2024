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
                elif xc == 0 or field[yc][xc-1] != field[y][x]:
                    perimeter[num_regions] += 1
                if xc < len(field[y]) - 1 and regions[yc][xc+1] is None and field[yc][xc+1] == field[y][x]:
                    to_check.append((xc + 1, yc))
                    regions[yc][xc+1] = num_regions
                    area[num_regions] += 1
                elif xc == len(field[y]) - 1 or field[yc][xc+1] != field[y][x]:
                    perimeter[num_regions] += 1
                if yc > 0 and regions[yc-1][xc] is None and field[yc-1][xc] == field[y][x]:
                    to_check.append((xc, yc - 1))
                    regions[yc-1][xc] = num_regions
                    area[num_regions] += 1
                elif yc == 0 or field[yc-1][xc] != field[y][x]:
                    perimeter[num_regions] += 1
                if yc < len(field) - 1 and regions[yc+1][xc] is None and field[yc+1][xc] == field[y][x]:
                    to_check.append((xc, yc + 1))
                    regions[yc+1][xc] = num_regions
                    area[num_regions] += 1
                elif yc == len(field) - 1 or field[yc+1][xc] != field[y][x]:
                    perimeter[num_regions] += 1
            num_regions += 1
total = 0
for region in area:
    total += area[region] * perimeter[region]
print(total)
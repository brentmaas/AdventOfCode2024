field = []
antennae = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        for i in range(len(line)):
            if 'A' <= line[i] <= 'Z' or 'a' <= line[i] <= 'z' or '0' <= line[i] <= '9':
                if line[i] in antennae:
                    antennae[line[i]].append((i, len(field)))
                else:
                    antennae[line[i]] = [(i, len(field))]
        field.append(line)

antinodes = set()
for frequency in antennae:
    for i in range(len(antennae[frequency]) - 1):
        for j in range(i + 1, len(antennae[frequency])):
            dx = antennae[frequency][i][0] - antennae[frequency][j][0]
            dy = antennae[frequency][i][1] - antennae[frequency][j][1]
            x1 = antennae[frequency][i][0] + dx
            y1 = antennae[frequency][i][1] + dy
            x2 = antennae[frequency][j][0] - dx
            y2 = antennae[frequency][j][1] - dy
            if 0 <= x1 < len(field[0]) and 0 <= y1 < len(field):
                antinodes.add((x1, y1))
            if 0 <= x2 < len(field[0]) and 0 <= y2 < len(field):
                antinodes.add((x2, y2))
print(len(antinodes))
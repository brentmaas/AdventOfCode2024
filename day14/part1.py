width, height = 101, 103
t = 100
pos = []
vel = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        line_pos, line_vel = line.split()
        pos.append((int(line_pos[2:line_pos.index(",")]), int(line_pos[line_pos.index(",")+1:])))
        vel.append((int(line_vel[2:line_vel.index(",")]), int(line_vel[line_vel.index(",")+1:])))
quads = [0, 0, 0, 0]
for i in range(len(pos)):
    x = (pos[i][0] + vel[i][0] * t) % width
    y = (pos[i][1] + vel[i][1] * t) % height
    if x < width // 2 and y < height // 2:
        quads[0] += 1
    elif x > width // 2 and y < height // 2:
        quads[1] += 1
    elif x < width // 2 and y > height // 2:
        quads[2] += 1
    elif x > width // 2 and y > height // 2:
        quads[3] += 1
print(quads[0] * quads[1] * quads[2] * quads[3])
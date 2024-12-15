width, height = 101, 103
pos = []
vel = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        line_pos, line_vel = line.split()
        pos.append((int(line_pos[2:line_pos.index(",")]), int(line_pos[line_pos.index(",")+1:])))
        vel.append((int(line_vel[2:line_vel.index(",")]), int(line_vel[line_vel.index(",")+1:])))
t = 8280
img = [["." for _ in range(width)] for _ in range(height)]
for i in range(len(pos)):
    x = (pos[i][0] + vel[i][0] * t) % width
    y = (pos[i][1] + vel[i][1] * t) % height
    img[y][x] = "#"
for row in img:
    print("".join(row))
print(t)
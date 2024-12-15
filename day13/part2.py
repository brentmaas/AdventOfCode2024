total = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        dx_a = int(line[line.index("X")+2:line.index(",")])
        dy_a = int(line[line.index("Y")+2:])
        line = f.readline().rstrip()
        dx_b = int(line[line.index("X")+2:line.index(",")])
        dy_b = int(line[line.index("Y")+2:])
        line = f.readline().rstrip()
        x_prize = int(line[line.index("X")+2:line.index(",")]) + 10000000000000
        y_prize = int(line[line.index("Y")+2:]) + 10000000000000
        f.readline()
        
        n_a = round((y_prize - dy_b * x_prize / dx_b) / (dy_a - dx_a * dy_b / dx_b))
        n_b = round((x_prize - n_a * dx_a) / dx_b)
        if n_a * dx_a + n_b * dx_b == x_prize and n_a * dy_a + n_b * dy_b == y_prize:
            total += 3 * n_a + n_b
print(total)
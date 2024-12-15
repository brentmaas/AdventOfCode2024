total = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        dx_a = int(line[line.index("X")+2:line.index(",")])
        dy_a = int(line[line.index("Y")+2:])
        line = f.readline().rstrip()
        dx_b = int(line[line.index("X")+2:line.index(",")])
        dy_b = int(line[line.index("Y")+2:])
        line = f.readline().rstrip()
        x_prize = int(line[line.index("X")+2:line.index(",")])
        y_prize = int(line[line.index("Y")+2:])
        f.readline()
        
        n_a = max(x_prize // dx_a, y_prize // dy_a) + 1
        n_b = 0
        min_tokens = None
        while n_a >= 0:
            if n_a * dx_a + n_b * dx_b == x_prize and n_a * dy_a + n_b * dy_b == y_prize:
                min_tokens = 3 * n_a + n_b if min_tokens is None else min(min_tokens, 3 * n_a + n_b)
            if n_a * dx_a + n_b * dx_b >= x_prize and n_a * dy_a + n_b * dy_b >= y_prize:
                n_a -= 1
            else:
                n_b += 1
        if not min_tokens is None:
            total += min_tokens
print(total)
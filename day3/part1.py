total = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        while line:
            if "mul(" in line:
                mul_index = line.index("mul(")
                line = line[mul_index+4:]
                left = 0
                while len(line) > 0 and '0' <= line[0] <= '9':
                    left = 10 * left + int(line[0])
                    line = line[1:]
                if len(line) == 0 or line[0] != ',':
                    continue
                line = line[1:]
                right = 0
                while len(line) > 0 and '0' <= line[0] <= '9':
                    right = 10 * right + int(line[0])
                    line = line[1:]
                if len(line) == 0 or line[0] != ')':
                    continue
                total += left * right
                line = line[1:]
            else:
                break
print(total)
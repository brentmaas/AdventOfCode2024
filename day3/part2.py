total = 0
do = True
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        while line:
            if "mul(" in line or "do()" in line or "don't()" in line:
                mul_index = line.index("mul(") if "mul(" in line else len(line)
                do_index = line.index("do()") if "do()" in line else len(line)
                dont_index = line.index("don't()") if "don't()" in line else len(line)
                if mul_index < do_index and mul_index < dont_index:
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
                    if do:
                        total += left * right
                    line = line[1:]
                elif do_index < dont_index:
                    line = line[do_index+4:]
                    do = True
                else:
                    line = line[dont_index+7:]
                    do = False
            else:
                break
print(total)
registers = {}
with open("Input.txt", "r") as f:
    registers["A"] = int(f.readline().rstrip()[len("Register A: "):])
    registers["B"] = int(f.readline().rstrip()[len("Register B: "):])
    registers["C"] = int(f.readline().rstrip()[len("Register C: "):])
    f.readline()
    program = [int(i) for i in f.readline().rstrip()[len("Program: "):].split(',')]

def get_combo_operand(operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    return None

ip = 0
output = []
while ip < len(program):
    instruction = program[ip]
    operand = program[ip+1]
    if instruction == 0:
        registers["A"] //= 2 ** get_combo_operand(operand)
    elif instruction == 1:
        registers["B"] ^= operand
    elif instruction == 2:
        registers["B"] = get_combo_operand(operand) % 8
    elif instruction == 3:
        if registers["A"] != 0:
            ip = operand
            continue
    elif instruction == 4:
        registers["B"] ^= registers["C"]
    elif instruction == 5:
        output.append(str(get_combo_operand(operand) % 8))
    elif instruction == 6:
        registers["B"] = registers["A"] // 2 ** get_combo_operand(operand)
    elif instruction == 7:
        registers["C"] = registers["A"] // 2 ** get_combo_operand(operand)
    ip += 2
print(",".join(output))
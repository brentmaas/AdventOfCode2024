wires = {}
gates = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        wire, value = line.split(": ")
        wires[wire] = int(value)
    while line := f.readline().rstrip():
        left, operand, right, _ , result = line.split()
        gates[result] = (left, operand, right)
xybits = len(wires) // 2
zbits = max([int(gate[1:]) for gate in gates if gate.startswith('z') and '0' <= gate[1] <= '9' and '0' <= gate[2] <= '9']) + 1

def solve_wire(wire):
    if wire in wires:
        return wires[wire]
    left, operand, right = gates[wire]
    if operand == "AND":
        if (left in wires and wires[left] == 0) or (right in wires and wires[right] == 0) or solve_wire(left) == 0 or solve_wire(right) == 0:
            wires[wire] = 0
        else:
            wires[wire] = 1
    elif operand == "XOR":
        wires[wire] = solve_wire(left) ^ solve_wire(right)
    elif (left in wires and wires[left] == 1) or (right in wires and wires[right] == 1) or solve_wire(left) == 1 or solve_wire(right) == 1:
        wires[wire] = 1
    else:
        wires[wire] = 0
    return wires[wire]

result = 0
for i in range(zbits - 1, -1, -1):
    result <<= 1
    result += solve_wire(f"z{i:02}")
print(result)
import copy

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

gates["z08"], gates["cdj"] = gates["cdj"], gates["z08"]
gates["z16"], gates["mrb"] = gates["mrb"], gates["z16"]
gates["z32"], gates["gfm"] = gates["gfm"], gates["z32"]
gates["dhm"], gates["qjd"] = gates["qjd"], gates["dhm"]

def solve_wire(wires, gates, wire):
    if wire in wires:
        return wires[wire]
    left, operand, right = gates[wire]
    if operand == "AND":
        if (left in wires and wires[left] == 0) or (right in wires and wires[right] == 0) or solve_wire(wires, gates, left) == 0 or solve_wire(wires, gates, right) == 0:
            wires[wire] = 0
        else:
            wires[wire] = 1
    elif operand == "XOR":
        wires[wire] = solve_wire(wires, gates, left) ^ solve_wire(wires, gates, right)
    elif (left in wires and wires[left] == 1) or (right in wires and wires[right] == 1) or solve_wire(wires, gates, left) == 1 or solve_wire(wires, gates, right) == 1:
        wires[wire] = 1
    else:
        wires[wire] = 0
    return wires[wire]

def solve(wires0, gates0):
    cwires = copy.copy(wires0)
    cgates = copy.copy(gates0)
    result = 0
    for i in range(zbits - 1, -1, -1):
        result <<= 1
        result += solve_wire(cwires, cgates, f"z{i:02}")
    return result

#Check wires
# for i in range(xybits):
#     twires = {}
#     for j in range(xybits):
#         twires[f"x{j:02}"] = 1 if i == j else 0
#         twires[f"y{j:02}"] = 1 if i == j else 0
#     print(i, 2 << i == solve(twires, gates), 2 << i, solve(twires, gates))

#Dump wires
# solve(wires, gates)
# 
# def print_gates(gate, depth=0, prefix=""):
#     print("  " * depth, prefix, gate, gates[gate])
#     i, j = 0, 2
#     if gates[gate][2] in gates and (gates[gates[gate][2]][1] == "XOR" or (gates[gates[gate][2]][1] == "AND" and not (gates[gate][0] in gates and gates[gates[gate][0]][1] == "XOR"))):
#         i, j = 2, 0
#     if gates[gate][i] in gates:
#         print_gates(gates[gate][i], depth + 1, "1")
#     if gates[gate][j] in gates:
#         print_gates(gates[gate][j], depth + 1, "2")
# 
# for i in range(zbits):
#     print_gates(f"z{i:02}")

print(",".join(["z08", "cdj", "z16", "mrb", "z32", "gfm", "qjd", "dhm"]))
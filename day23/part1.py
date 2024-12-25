conns = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        left, right = line.split("-")
        if left in conns:
            conns[left].append(right)
        else:
            conns[left] = [right]
        if right in conns:
            conns[right].append(left)
        else:
            conns[right] = [left]
found = set()
for pc in conns:
    if len(conns[pc]) >= 2:
        for i in range(len(conns[pc]) - 1):
            for j in range(i + 1, len(conns[pc])):
                if conns[pc][i] in conns[conns[pc][j]] and (pc.startswith('t') or conns[pc][i].startswith('t') or conns[pc][j].startswith('t')) and not (trio := ",".join(sorted([pc, conns[pc][i], conns[pc][j]]))) in found:
                    found.add(trio)
print(len(found))
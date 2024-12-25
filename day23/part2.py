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
largest = []
for pc in conns:
    cluster = [pc] + conns[pc]
    i = 1
    while i < len(cluster):
        pc2 = cluster[i]
        if all([pc3 in conns[pc2] for pc3 in cluster[:i]]):
            i += 1
        else:
            cluster.pop(i)
    if len(cluster) > len(largest):
        largest = cluster
print(",".join(sorted(largest)))
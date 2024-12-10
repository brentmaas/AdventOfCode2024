ids = []
lengths = []
with open("Input.txt", "r") as f:
    disk_map = f.readline().rstrip()
    for i in range(len(disk_map)):
        ids.append(len(ids) // 2 if i % 2 == 0 else None)
        lengths.append(int(disk_map[i]))
while None in ids:
    if ids[-1] is None or lengths[-1] == 0:
        ids.pop(-1)
        lengths.pop(-1)
    else:
        i_empty = ids.index(None)
        if lengths[i_empty] == lengths[-1]:
            ids[i_empty] = ids[-1]
            ids.pop(-1)
            lengths.pop(-1)
        elif lengths[i_empty] > lengths[-1]:
            ids.insert(i_empty, ids[-1])
            lengths[i_empty] -= lengths[-1]
            lengths.insert(i_empty, lengths[-1])
            ids.pop(-1)
            lengths.pop(-1)
        else:
            ids[i_empty] = ids[-1]
            lengths[-1] -= lengths[i_empty]
checksum = 0
total_length = 0
for i in range(len(ids)):
    checksum += ids[i] * ((total_length + lengths[i]) * (total_length + lengths[i] - 1) - total_length * (total_length - 1)) // 2
    total_length += lengths[i]
print(checksum)
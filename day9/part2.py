ids = []
lengths = []
with open("Input.txt", "r") as f:
    disk_map = f.readline().rstrip()
    for i in range(len(disk_map)):
        ids.append(len(ids) // 2 if i % 2 == 0 else None)
        lengths.append(int(disk_map[i]))
i = len(ids) - 1
while i >= 0:
    if not ids[i] is None:
        for j in range(i):
            if ids[j] is None:
                if lengths[j] == lengths[i]:
                    ids[j] = ids[i]
                    if i == len(ids) - 1:
                        ids.pop(i)
                        lengths.pop(i)
                    else:
                        ids[i] = None
                    break
                elif lengths[j] > lengths[i]:
                    ids.insert(j, ids[i])
                    lengths[j] -= lengths[i]
                    lengths.insert(j, lengths[i])
                    if i == len(ids) - 2:
                        ids.pop(i + 1)
                        lengths.pop(i + 1)
                    else:
                        ids[i+1] = None
                    break
    i -= 1
checksum = 0
total_length = 0
for i in range(len(ids)):
    if not ids[i] is None:
        checksum += ids[i] * ((total_length + lengths[i]) * (total_length + lengths[i] - 1) - total_length * (total_length - 1)) // 2
    total_length += lengths[i]
print(checksum)
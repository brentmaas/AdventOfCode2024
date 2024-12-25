keys = []
locks = []
with open("Input.txt", "r") as f:
    while True:
        rows = []
        for _ in range(7):
            rows.append(f.readline().rstrip())
        
        is_key = '.' in rows[0]
        columns = [0 for _ in range(len(rows[0]))]
        for i in range(0 if is_key else 1, len(rows) - 1 if is_key else len(rows)):
            for j in range(len(rows[i])):
                columns[j] += 1 if rows[i][j] == '#' else 0
        
        if is_key:
            keys.append(columns)
        else:
            locks.append(columns)
        
        if len(f.readline()) == 0:
            break

total = 0
for lock in locks:
    for key in keys:
        fits = True
        for i in range(len(key)):
            if lock[i] + key[i] > 5:
                fits = False
        if fits:
            total += 1
print(total)
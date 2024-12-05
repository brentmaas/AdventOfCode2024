total = 0
rules = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        left, right = [int(i) for i in line.split('|')]
        if left in rules:
            rules[left].add(right)
        else:
            rules[left] = set([right])
    while line := f.readline().rstrip():
        pages = [int(i) for i in line.split(',')]
        valid = True
        for i in range(len(pages)):
            if pages[i] in rules and rules[pages[i]] & set(pages[:i]):
                valid = False
                break
        if valid:
            total += pages[len(pages)//2]
print(total)
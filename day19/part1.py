cache = {}
def is_possible(design):
    if design in cache:
        return cache[design]
    #print(design)
    if design in patterns:
        cache[design] = True
        return True
    fitting_patterns = [pattern for pattern in patterns if design.startswith(pattern)]
    cache[design] = any([is_possible(design[len(pattern):]) for pattern in fitting_patterns])
    return cache[design]

possible = 0
with open("Input.txt", "r") as f:
    patterns = sorted(f.readline().rstrip().split(", "))
    f.readline()
    while line := f.readline().rstrip():
        if is_possible(line):
            possible += 1
print(possible)
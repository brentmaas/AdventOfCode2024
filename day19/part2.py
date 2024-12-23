cache = {}
def is_possible(design):
    if len(design) == 0:
        return 1
    if design in cache:
        return cache[design]
    fitting_patterns = [pattern for pattern in patterns if design.startswith(pattern)]
    cache[design] = sum([is_possible(design[len(pattern):]) for pattern in fitting_patterns])
    return cache[design]

possible = 0
with open("Input.txt", "r") as f:
    patterns = sorted(f.readline().rstrip().split(", "))
    f.readline()
    while line := f.readline().rstrip():
        possible += is_possible(line)
print(possible)
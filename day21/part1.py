import copy

keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
dirpad = [[None, '^', 'A'], ['<', 'v', '>']]

def get_path(pad, path, sx, sy):
    outpath = []
    x, y = sx, sy
    for key in path:
        yt = [row for row in range(len(pad)) if key in pad[row]][0]
        xt = pad[yt].index(key)
        if pad[yt][x] is None or xt == x or yt == y:
            if xt > x:
                outpath += ['>' for _ in range(xt - x)]
            elif xt < x:
                outpath += ['<' for _ in range(x - xt)]
            if yt > y:
                outpath += ['v' for _ in range(yt - y)]
            elif yt < y:
                outpath += ['^' for _ in range(y - yt)]
        elif pad[y][xt] is None:
            if yt > y:
                outpath += ['v' for _ in range(yt - y)]
            elif yt < y:
                outpath += ['^' for _ in range(y - yt)]
            if xt > x:
                outpath += ['>' for _ in range(xt - x)]
            elif xt < x:
                outpath += ['<' for _ in range(x - xt)]
        else:
            outpath += [[[], []]]
            if yt > y:
                outpath[-1][0] += ['v' for _ in range(yt - y)]
                outpath[-1][1] += ['v' for _ in range(yt - y)]
            elif yt < y:
                outpath[-1][0] += ['^' for _ in range(y - yt)]
                outpath[-1][1] += ['^' for _ in range(y - yt)]
            if xt > x:
                outpath[-1][0] += ['>' for _ in range(xt - x)]
                outpath[-1][1] = ['>' for _ in range(xt - x)] + outpath[-1][1]
            elif xt < x:
                outpath[-1][0] += ['<' for _ in range(x - xt)]
                outpath[-1][1] = ['<' for _ in range(x - xt)] + outpath[-1][1]
        outpath += ['A']
        x, y = xt, yt
    outpaths = [[]]
    for segment in outpath:
        if type(segment) == list:
            outpaths = outpaths + copy.deepcopy(outpaths)
            for i in range(len(outpaths) // 2):
                outpaths[i] += segment[0]
                outpaths[i+len(outpaths)//2] += segment[1]
        else:
            for i in range(len(outpaths)):
                outpaths[i].append(segment)
    return set(["".join(outpath) for outpath in outpaths])

total = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        paths1 = get_path(keypad, line, 2, 3)
        paths2 = set([])
        for path1 in paths1:
            paths2 |= get_path(dirpad, path1, 2, 0)
        paths3 = set([])
        for path2 in paths2:
            paths3 |= get_path(dirpad, path2, 2, 0)
        total += min([len(path3) for path3 in paths3]) * int(line[:-1])
print(total)
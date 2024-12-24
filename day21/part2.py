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
                outpath[-1][1] += ['<' for _ in range(x - xt)]
                outpath[-1][0] = ['<' for _ in range(x - xt)] + outpath[-1][0]
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
    return ["".join(outpath) for outpath in outpaths]

cache = {}
total = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        paths = get_path(keypad, line, 2, 3)
        pathdicts = []
        for path in paths:
            pathdicts.append({})
            i = 0
            while 'A' in path[i:]:
                j = path[i:].index('A')
                segment = path[i:i+j+1]
                if segment in pathdicts[-1]:
                    pathdicts[-1][segment] += 1
                else:
                    pathdicts[-1][segment] = 1
                i += j + 1
        for _ in range(25):
            newdicts = []
            for pathdict in pathdicts:
                newdicts.append({})
                for segment in pathdict:
                    if not segment in cache:
                        cache[segment] = {}
                        segmentpaths = get_path(dirpad, segment, 2, 0)
                        lengths = [len(segmentpath) for segmentpath in segmentpaths]
                        imin = lengths.index(min(lengths))
                        minsegmentpath = segmentpaths[imin]
                        i = 0
                        while 'A' in minsegmentpath[i:]:
                            j = minsegmentpath[i:].index('A')
                            segmentsegment = minsegmentpath[i:i+j+1]
                            if segmentsegment in cache[segment]:
                                cache[segment][segmentsegment] += 1
                            else:
                                cache[segment][segmentsegment] = 1
                            i += j + 1
                    for cachesegment in cache[segment]:
                        if cachesegment in newdicts[-1]:
                            newdicts[-1][cachesegment] += cache[segment][cachesegment] * pathdict[segment]
                        else:
                            newdicts[-1][cachesegment] = cache[segment][cachesegment] * pathdict[segment]
            pathdicts = newdicts
        total += min([sum([pathdict[c] * len(c) for c in pathdict]) for pathdict in pathdicts]) * int(line[:-1])
print(total)
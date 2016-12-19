bway = 'A K Q J T'.split()

for L in open('cattd.txt', 'r').read().splitlines():
    if '//' in L:
        continue
    if len(L) < 10:
        continue
    f = L.split()
    if f[0][0] in bway and f[0][1] in bway and f[2][0] in bway and f[2][1] in bway:
        if f[1] == '->':
            print '"' + f[0] + '" ' + f[1] + ' "' + f[2] + '";'
        elif f[1] == '<-':
            print '"' + f[2] + '" -> "' + f[0] + '";'

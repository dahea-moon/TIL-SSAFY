import sys
sys.stdin = open('4861_input.txt', 'r')


def findpail(full, rc, lp):
    pail = ''
    if rc == lp:
        for n in range(rc):
            if full[n] == full[n][::-1]:
                pail = ''.join(full[n])
                return pail
    else:
        for n in range(rc):
            for i in range(rc-lp+1):
                if full[n][i:i+lp] == full[n][i:i+lp][::-1]:
                    pail = ''.join(full[n][i:i+lp])
                    return pail


T = int(input())
for tc in range(1, T + 1):
    rc, lp = map(int, input().split())
    words = [[i for i in input()] for m in range(rc)]
    rows = []
    cols = []

    for r in range(rc):
        rows.append(words[r])

    for c in range(rc):
        col = []
        for r in range(rc):
            col.append(words[r][c])
        cols.append(col)

    result = ''
    if findpail(rows, rc, lp) != None:
        result = findpail(rows, rc, lp)
    elif findpail(cols, rc, lp) != None:
        result = findpail(cols, rc, lp)

    print(result)

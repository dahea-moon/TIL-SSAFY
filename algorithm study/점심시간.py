import sys
sys.stdin = open('test.txt', 'r')


def solve(comb):
    global noOfppl, pplToStair, time, res
    goings = [[], []]
    for p in range(noOfppl):
        if comb[p] == 0:
            goings[0] += [pplToStair[0][p]]
        else:
            goings[1] += [pplToStair[1][p]]

    tmp = []
    for q in range(2):
        t = time[q]
        curtime = 0
        curstair = []
        goings[q].sort(reverse=True)
        while 1:
            curtime += 1
            for h in range(len(goings[q])-1, -1, -1):
                if goings[q][h] == 0:
                    if len(curstair) == 3:
                        pass
                    else:
                        curstair += [t]
                        goings[q].pop()
                else:
                    goings[q][h] -= 1

            if len(curstair) > 0:
                for l in range(len(curstair)-1, -1, -1):
                    curstair[l] -= 1
                    if curstair[l] == 0:
                        curstair.pop(l)

            if len(goings[q]) == len(curstair) == 0:
                break

        tmp += [curtime+1]

    candi = max(tmp)
    if candi < res:
        res = candi
        return

def powerset(k, n):
    global comb
    if k == n:
       solve(comb)
    else:
        for z in range(2):
            comb[k] = z
            powerset(k+1, n)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]

    ppl = []
    stairs = []
    time = []
    for r in range(n):
        for c in range(n):
            if room[r][c] == 1:
                ppl += [(r, c)]
            elif room[r][c] > 1:
                stairs += [(r, c)]
                time += [room[r][c]]

    noOfppl = len(ppl)
    pplToStair = [[0]*noOfppl, [0]*noOfppl]
    for i in range(2):
        sr, sc = stairs[i]
        for j in range(noOfppl):
            pr, pc = ppl[j]
            d = abs(pr-sr) + abs(pc-sc)
            pplToStair[i][j] = d

    comb = [0]*noOfppl
    res = 999999
    powerset(0, noOfppl)
    print('#{} {}'.format(tc, res))
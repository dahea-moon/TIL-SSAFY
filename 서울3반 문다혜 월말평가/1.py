import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    roads = [list(map(int, input().split())) for _ in range(N)]

    mincost = 9999999999
    height = 0
    for r in range(N):
        tmp = []
        candis = set()
        for c in range(N):
            tmp += [roads[r][c]]
            candis.add(roads[r][c])
        tmp2 = tmp[:]
        for i in range(N):
            for j in range(N):
                if j != r:
                    tmp2 += [roads[j][i]]
                    candis.add(roads[j][i])
            for candi in candis:
                chk_cost = 0
                for num in tmp2:
                    if num > candi:
                        chk_cost += (num-candi)
                    elif num < candi:
                        chk_cost += (candi-num)
                if chk_cost < mincost:
                    mincost = chk_cost
                    height = candi
                elif chk_cost == mincost:
                    if candi < height:
                        height = candi
            tmp2 = tmp[:]

    print('#{} {} {}'.format(tc, mincost, height))

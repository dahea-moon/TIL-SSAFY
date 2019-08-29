import sys
sys.stdin = open('walls.txt', 'r')

def route(mr, mc, wall):
    if wall == 1:
        if mc == 0:
            if mr == -1:
                mr = 0
                mc = 1
                return mr,mc
            else:
                mr = 0
                mc = -1
                return mr,mc
        elif mr == 0:
            if mc == 1:
                mr = -1
                mc = 0
                return mr, mc
            else:
                mr = 1
                mc = 0
                return mr, mc
    if wall == 2:
        if mc == 0:
            if mr == -1:
                mr = 0
                mc = -1
                return mr,mc
            else:
                mr = 0
                mc = 1
                return mr,mc
        elif mr == 0:
            if mc == 1:
                mr = 1
                mc = 0
                return mr, mc
            else:
                mr = -1
                mc = 0
                return mr, mc

for tc in range(3):
    N = int(input())
    forest = [list(map(int, input().split())) for _ in range(N)]

    r = c = 0
    mr = 0
    mc = 1
    cnt = -1
    while 1:
        if r >= N or r < 0 or c >= N or c < 0:
            break
        else:
            cnt += 1
            if forest[r][c] == 0:
                r += mr
                c += mc
            else:
                mr, mc = route(mr, mc, forest[r][c])
                r += mr
                c += mc

    print(cnt)

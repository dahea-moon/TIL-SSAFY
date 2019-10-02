import sys
sys.stdin = open('input', 'r')

def finding(sr, sc, e, chksum, minerals):
    global mineralamount, total, n, chkli
    if e == 0:
        if chksum > mineralamount:
            mineralamount = chksum
        return

    if minerals == chkli:
        mineralamount = total
        return

    for i in range(n):
        if minerals[i] != 0:
            dist, am = minerals[i]
            if e - dist < 0:
                if chksum > mineralamount:
                    mineralamount = chksum
                return
            else:
                minerals[i] = 0
                finding(sr, sc, e-dist, chksum+am, minerals)
                minerals[i] = (dist, am)
                if mineralamount == total:
                    break
    return

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    planet = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if planet[r][c] == 1:
                sr, sc = r, c

    minerals = []
    total = 0
    for r in range(N):
        for c in range(M):
            mineral = planet[r][c]
            if 2 <= mineral <= 200:
                dis = (abs(sr - r) + abs(sc - c)) * 2
                if dis <= C:
                    minerals.append((dis, mineral))
                    total += mineral

    n = len(minerals)
    chkli = [0]*n
    mineralamount = 0
    finding(sr, sc, C, 0, minerals)
    print('#{} {}'.format(tc, mineralamount))



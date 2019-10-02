import sys
sys.stdin = open('imigration.txt', 'r')

def imigrate(l, h, key):
    global times, mintime
    mid = (l+h) // 2

    pn = 0
    for i in range(N):
        pn += mid // times[i]

    if pn >= key:

        dn = 0
        for i in range(N):
            dn += (mid-1) // times[i]
        if dn < key:
            mintime = mid
            return

        imigrate(l, mid, key)
    else:
        imigrate(mid, h, key)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    times = [0]*N
    for i in range(N):
        times[i] = int(input())

    mintime = 99999
    maxtime = max(times)*M
    imigrate(0, maxtime, M)
    print('#{} {}'.format(tc, mintime))

import sys
sys.stdin = open('5208.txt', 'r')

def charging(i, g):
    global stations, ns, cnt, minc

    if cnt > minc:
        return

    nxt = stations[i] + ns[i]
    if nxt >= g:
        if cnt < minc:
            minc = cnt
        return
    else:
        for s in range(i+1, nxt):
            cnt += 1
            charging(s, g)
            cnt -= 1


T = int(input())
for tc in range(1, T+1):
    stations = list(map(int, input().split()))
    goal = stations[0]
    stations = stations[1:]
    ns = [x for x in range(1, goal)]

    cnt = 0
    minc = 9999
    charging(0, goal)
    print('#{} {}'.format(tc, minc))
import sys
sys.stdin = open('input', 'r')

def finding(i, candis, cookies, chk):
    global minidis
    if chk > minidis:
        return

    if i == 6:
        if chk < minidis:
            minidis = chk
        return
    else:
        sr, sc = candis[i]
        for j in range(6):
            if cookies[j] != 0:
                tmp = cookies[j]
                dis = abs(sr-cookies[j][0])+abs(sc-cookies[j][1])
                cookies[j] = 0
                finding(i+1, candis, cookies, chk+dis)
                cookies[j] = tmp


T = int(input())
for _ in range(T):
    tc = int(input())
    robots = [list(map(int, input().split())) for _ in range(10)]

    candis = []
    cookies = []
    for r in range(10):
        for c in range(10):
            if robots[r][c] == 9:
                candis.append((r, c))
            if 1 <= robots[r][c] <= 6:
                cookies.append((r, c))
        if len(candis) == 6 and len(cookies) == 6:
            break

    minidis = 9999999
    finding(0, candis, cookies, 0)
    print('#{} {}'.format(tc, minidis))

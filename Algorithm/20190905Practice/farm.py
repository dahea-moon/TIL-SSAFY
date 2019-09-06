import sys
sys.stdin = open('farm.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    std = N // 2
    hap = 0

    s = 0
    for r in range(std):
        hap += farm[r][std]
        for i in range(1, s+1):
            hap += farm[r][std+i]
            hap += farm[r][std-i]
        s += 1

    s = std
    for r in range(std, N):
        hap += farm[r][std]
        for i in range(s, 0, -1):
            hap += farm[r][std+i]
            hap += farm[r][std-i]
        s -= 1

    print('#{} {}'.format(tc, hap))
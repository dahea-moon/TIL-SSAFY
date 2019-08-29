import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    colors = [list(map(int, input().split())) for i in range(K)]
    canvas = [[0]*M for n in range(N)]

    for color in colors:
        cnt = 0
        r1, c1, r2, c2, co = color[0], color[1], color[2], color[3], color[4]
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if canvas[r][c] > co:
                    cnt += 1

        if cnt == 0:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    canvas[r][c] = co

    num = [0]*11
    for g in range(N):
        for s in range(M):
            i = canvas[g][s]
            num[i] += 1

    maxcnt = 0
    for t in num:
        if t > maxcnt:
            maxcnt = t

    print('#{} {}'.format(tc, maxcnt))
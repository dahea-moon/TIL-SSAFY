import sys
sys.stdin = open('1.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    colors = [list(map(int, input().split())) for _ in range(M)]
    pan = [[0]*(N+1) for n in range(N+1)]

    for i in range(M):
        LU = (colors[i][0], colors[i][1])
        RD = (colors[i][2], colors[i][3])

        for r in range(LU[0], RD[0]+1):
            for c in range(LU[1], RD[1]+1):
                pan[r][c] = i+1

    cnt = 0
    for i in range(1, M+1):
        for r in range(0,N+1):
            for c in range(0,N+1):
                if pan[r][c] == i:
                    cnt +=1

    print('#{} {}'.format(tc,cnt))

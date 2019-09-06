import sys
sys.stdin = open('osello_input.txt', 'r')

def isin(r,c):
    if 0 < r <= N and 0 < c <= N:
        return True
    return False

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    pan = [[0]*(N+1) for _ in range(N+1)]
    h= N // 2
    pan[h][h] = pan[h+1][h+1] = 2
    pan[h + 1][h] = pan[h][h+1] = 1

    for _ in range(M):
        r, c, T = tuple(map(int, input().split()))
        pan[r][c] = T

        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]

        for i in range(8):
            tr = r + dx[i]
            tc = c + dy[i]
            if isin(tr,tc) and pan[tr][tc] != T and pan[tr][tc] != 0:
                cr = tr + dx[i]
                cc = tc + dy[i]
                while isin(cr,cc):
                    if pan[cr][cc] == T:
                        while cr != tr or cc != tc:
                            cr -= dx[i]
                            cc -= dy[i]
                            pan[cr][cc] = T
                        break
                    elif pan[cr][cc] == 0:
                        break
                    else:
                        cr += dx[i]
                        cc += dy[i]

    pan = sum(pan, [])
    W = pan.count(2)
    B = pan.count(1)
    print('#{} {} {}'.format(t, B, W))
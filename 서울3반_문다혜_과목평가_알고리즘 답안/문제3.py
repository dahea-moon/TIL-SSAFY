import sys
sys.stdin = open('3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [0]*N
    for r in range(N):
        arr[r] = list(map(int, input().split()))

    visited = [[0] * N for _ in range(N)]

    stack = []
    flag1 = True
    cnt = 0
    while flag1:
        g = 0
        flag2 = True
        while flag2:
            for s in range(N):
                if arr[g][s] > 1 and visited[g][s] == 0:
                    stack.append((g,s))
                    visited[g][s] = 1
                    SX = g
                    SY = s
                    flag2 = False
                    break
            else:
                if g == N-1:
                    flag2 = False
                else:
                    g += 1


        if g == N-1:
            flag1 = False
        else:
            while stack:
                dx = [0, 0, -1, 1, -1, -1, 1, 1]
                dy = [-1, 1, 0, 0, -1, 1, 1, -1]
                start = stack[-1]
                for i in range(8):
                    testX = start[0] + dx[i]
                    testY = start[1] + dy[i]
                    if 0 <= testY <= N-1 and 0 <= testX <= N-1:
                        if arr[testX][testY] > 0 and visited[testX][testY] == 0:
                            stack.append((testX, testY))
                            visited[testX][testY] = 1
                            break
                else:
                    stack.pop()
            cnt += 1

    print('#{} {}'.format(tc, cnt))
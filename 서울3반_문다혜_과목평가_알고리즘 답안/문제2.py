import sys
sys.stdin = open('2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    arr = [0]*N
    for r in range(N):
        arr[r] = list(map(int, input().split()))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    char = []
    for r in range(N-K+1):
        for c in range(M-K+1):
            X = r
            Y = c
            sum_k = arr[r][c]
            for d in range(4):
                for _ in range(K-1):
                    X += dx[d]
                    Y += dy[d]
                    sum_k += arr[X][Y]
            sum_k -= arr[X][Y]
            char.append(sum_k)

    result = max(char)
    print('#{} {}'.format(tc, result))

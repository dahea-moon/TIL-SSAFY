import sys
sys.stdin = open('fly_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pan = [list(map(int, input().split())) for _ in range(N)]

    maxsum = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum = 0
            for m in range(r, r+M):
                for n in range(c, c+M):
                    sum += pan[m][n]

                    if sum > maxsum:
                        maxsum = sum

    print('#{} {}'.format(tc, maxsum))

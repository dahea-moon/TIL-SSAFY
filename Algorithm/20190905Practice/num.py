import sys
sys.stdin = open('nums.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    origin = [input().split() for _ in range(N)]
    result = [[0]*3 for _ in range(N)]

    i = 0
    j = -1
    for r in range(N-1, -1, -1):
        res90 = res180 = res270 = ''
        for c in range(N):
            res270 += origin[c][r]
        for c in range(N-1, -1, -1):
            res180 += origin[r][c] # 180
            res90 += origin[c][r] # 270
        result[j][0] = res90
        result[i][1] = res180
        result[i][2] = res270
        i += 1
        j -= 1

    print('#{}'.format(tc))
    for c in range(N):
        for r in range(3):
            print(result[c][r], end=' ')
        print()

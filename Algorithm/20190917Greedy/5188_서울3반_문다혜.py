import sys
sys.stdin = open('5188.txt', 'r')

def findminsum(arr, r, c, chksum):
    global minsum

    if r == N or c == N:
        return
    if r == N-1 and c == N-1:
        chksum += arr[r][c]
        if chksum < minsum:
            minsum = chksum
    else:
        chksum += arr[r][c]
        findminsum(arr, r+1, c, chksum)
        findminsum(arr, r, c+1, chksum)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]

    minsum = 999999
    findminsum(pan, 0, 0, 0)
    print('#{} {}'.format(tc, minsum))

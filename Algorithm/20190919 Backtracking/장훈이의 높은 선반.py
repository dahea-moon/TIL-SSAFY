import sys
sys.stdin = open('장훈이의 높은 선반.txt', 'r')

def height(n, r, chksum):
    global heights, b, minh

    if chksum > minh:
        return
    if r == 0:
        if chksum < minh and chksum >= b:
            minh = chksum
    elif n < r:
        return
    else:
        chksum += heights[n - 1]
        height(n - 1, r - 1, chksum)
        chksum -= heights[n - 1]
        height(n - 1, r, chksum)


T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))

    minh = 999999
    for i in range(1, n + 1):
        chksum = 0
        height(n, i, chksum)

    print('#{} {}'.format(tc, minh-b))



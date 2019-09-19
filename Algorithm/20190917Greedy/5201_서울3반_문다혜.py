import sys
sys.stdin = open('5201.txt', 'r')

def findmax(arr):
    maxval = max(arr)
    i = arr.index(maxval)
    arr[i] = 0
    return maxval


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    chk = [0]*N
    trucks = list(map(int, input().split()))

    res = 0

    while 1:
        curcon = findmax(container)
        curtruck = findmax(trucks)
        if curcon == 0 or curtruck == 0:
            break
        if curcon > curtruck:
            while curcon > curtruck:
                curcon = findmax(container)
                if curcon <= curtruck:
                    res += curcon
        else:
            res += curcon

    print('#{} {}'.format(tc, res))
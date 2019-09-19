import sys
sys.stdin = open('5189.txt', 'r')

def perm(arr, n, k):
    global  workstation, mincost
    if k == n:
        tmp = [1] + arr + [1]
        cost = 0
        for i in range(N):
            cost += workstation[tmp[i]-1][tmp[i+1]-1]
        if cost < mincost:
            mincost = cost
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(arr, n, k + 1)
            arr[i], arr[k] = arr[k], arr[i]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    workstation = [list(map(int, input().split())) for _ in range(N)]
    candis = [x for x in range(2, N+1)]

    mincost = 9999999
    perm(candis, N-1, 0)
    print('#{} {}'.format(tc, mincost))
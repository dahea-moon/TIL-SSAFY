import sys
sys.stdin = open('4881_input.txt', 'r')


def isPromising(i, cursum):
    global minsum, visited
    res = []
    for n in range(N):
        if not visited[n]:
            res.append(n)
    return res


def findingSum(i, k, N, cursum):
    global arr, minsum

    if k == N:
        if cursum < minsum:
            minsum = cursum
    else:
        k += 1
        res = isPromising(i, cursum)
        for c in res:
            visited[c] = True
            if cursum + arr[i][c] < minsum:
                findingSum(i+1, k, N, cursum+arr[i][c])
            visited[c] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for m in range(N)]
    visited = [False]*N
    print(arr)

    minsum = 91
    k = 0
    cursum = 0
    i = 0
    findingSum(i,k,N,cursum)
    print(minsum)



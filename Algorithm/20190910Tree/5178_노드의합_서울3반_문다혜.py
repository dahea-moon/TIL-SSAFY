import sys
sys.stdin = open('5178.txt', 'r')

def tree(n):
    if n == 1:
        return
    if n % 2:
        trees[n // 2] = trees[n] + trees[n-1]
        tree(n-2)
    else:
        trees[n // 2] = trees[n]
        tree(n-1)


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    trees = [0]*(N+1)

    for _ in range(M):
        node = list(map(int, input().split()))
        trees[node[0]] = node[1]

    tree(N)

    print('#{} {}'.format(tc, trees[L]))


import sys
sys.stdin = open('binary.txt', 'r')

def binary_tree(n):
    global cnt, N
    if n > N:
        return
    if nodes[n]:
        binary_tree(2*n)
        cnt += 1
        node = cnt
        tree[n] = node
        binary_tree(2*n+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nodes = [i for i in range(N+1)]
    tree = [0]*(N+1)
    cnt = 0
    binary_tree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
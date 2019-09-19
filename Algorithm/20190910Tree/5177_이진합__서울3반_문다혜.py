import sys
sys.stdin = open('5177.txt', 'r')

def traverse(n):
    if n < 1:
        return
    if tree[n//2] > tree[n]:
        tree[n//2], tree[n] = tree[n], tree[n//2]
        traverse(n // 2)

def heap(n):
    global N
    if n > N:
        return
    tree.append(numbers[n])
    traverse(n)
    heap(n+1)

def ancestor(n):
    global ances
    if n < 1:
        return
    ancestor(n // 2)
    ances += tree[n//2]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    tree = [0]

    heap(1)

    ances = 0
    ancestor(N)
    print('#{} {}'.format(tc, ances))

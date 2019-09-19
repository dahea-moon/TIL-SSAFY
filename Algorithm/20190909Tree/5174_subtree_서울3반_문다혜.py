import sys
sys.stdin = open('subtree.txt', 'r')

def tree(relation, node):
    global cnt

    if relation[node]:
        cnt += 1
        if relation[node][0]:
            tree(relation, relation[node][0])
        if relation[node][1]:
            tree(relation, relation[node][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lines = list(map(int, input().split()))

    relation = [[0] * 2 for _ in range(E+2)]

    for i in range(0, E*2, 2):
        if relation[lines[i]][0] == 0:
            relation[lines[i]][0] = lines[i + 1]
        else:
            relation[lines[i]][1] = lines[i + 1]

    cnt = 0
    tree(relation, N)
    print('#{} {}'.format(tc, cnt))

import sys
sys.stdin = open('4871.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())

    link = [0]*E
    i = 0
    for _ in range(E):
        link[i] = tuple(map(int,input().split()))
        i += 1

    S, G = map(int, input().split())

    matrix = [[0]*(V+1) for _ in range(V+1)]
    for e in range(E):
        a = link[e][0]
        b = link[e][1]
        matrix[a][b] = 1

    check = [True] + [False]*V
    stack = [S]
    result = 0
    while stack:
        for idx, val in enumerate(matrix[stack[-1]]):
            if val == 1 and check[idx] != True:
                if idx == G:
                    result = 1
                else:
                    stack.append(idx)
                    check[idx] = True
                    break
        else:
            stack.pop(-1)

    print('#{} {}'.format(tc, result))
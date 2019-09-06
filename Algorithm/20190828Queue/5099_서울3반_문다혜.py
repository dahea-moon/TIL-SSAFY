import sys
sys.stdin = open('5099_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))

    burn = [0]*N
    for i in range(N):
        burn[i] = [pizzas[i], i]

    i = 0
    while len(burn) != 1:
        burn[0][0] //= 2

        if burn[0][0] != 0:
            burn.append(burn.pop(0))
        else:
            if N + i >= M:
                burn.pop(0)
            else:
                burn.pop(0)
                burn.append([pizzas[N+i], N+i])
                i += 1

    print('#{} {}'.format(tc, burn[0][1]+1))


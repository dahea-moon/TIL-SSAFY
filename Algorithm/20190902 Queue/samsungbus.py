import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [0]*(N+1)
    B = [0] * (N + 1)
    for i in range(1, N+1):
        a, b = map(int,input().split())
        A[i] = a
        B[i] = b

    P = int(input())
    RP = [0]*P
    for i in range(P):
        RP[i] = int(input())

    PS = [0 for _ in range(5001)]
    for n in range(1,N+1):
        for x in range(A[n], B[n]+1):
            if x in RP:
                PS[x] += 1

    result = ''
    for p in RP:
        result += str(PS[p]) + ' '

    print('#{} {}'.format(tc, result))



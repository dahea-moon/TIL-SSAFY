import sys
sys.stdin = open('4864_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    P = input()
    F = input()

    PL = len(P)
    FL = len(F)

    i = 0
    j = 0
    while j < PL and i < FL:
        if F[i] != P[j]:
            i -= j
            j = -1
        i = i + 1
        j = j + 1
    if j == PL:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))
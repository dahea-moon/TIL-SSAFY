import sys
sys.stdin = open('5186.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    output = ''
    while N != 1:
        N *= 2
        if N > 1:
            output += str(int(N))
            N = N - int(N)
        elif N == 1:
            output += '1'
        else:
            output += '0'

        if len(output) == 13:
            output = 'overflow'
            break


    print('#{} {}'.format(tc, output))
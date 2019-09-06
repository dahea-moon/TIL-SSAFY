import sys
sys.stdin = open('4880_input.txt', 'r')

def winner(c,d):
    if rsp[c] == 1 and rsp[d] == 2:
        return d
    elif rsp[c] == 2 and rsp[d] == 3:
        return d
    elif rsp[c] == 3 and rsp[d] == 1:
        return d
    return c


def div(a,b):
    if a == b:
        return a

    if a+1 == b:
        return winner(a,b)

    c = div(a, (a+b)//2)
    d = div((a+b)//2+1, b)
    return winner(c,d)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rsp = [0] + list(map(int, input().split()))
    print('#{} {}'.format(tc,div(1,N)))

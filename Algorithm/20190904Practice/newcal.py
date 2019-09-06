import sys
sys.stdin = open('newcal.txt', 'r')

def andc(n):
    cnt = 0
    num = 0
    while 1:
        cnt += 1
        for i in range(1, cnt+1):
            num += 1
            if num == n:
                x = i
                y = cnt-i+1
                return x, y

def sharpc(x,y):
    num = 0
    for i in range(1, x+y):
        if i == x+y-1:
            for _ in range(x):
                num += 1
        else:
            for _ in range(i):
                num += 1
    return num

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())
    x1, y1 = andc(p)
    x2, y2 = andc(q)
    print('#{} {}'.format(tc, sharpc(x1+x2, y1+y2)))

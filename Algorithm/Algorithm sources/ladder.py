import sys
sys.stdin = open('input.txt', 'r')

def iswall(r,c):
    if r > 99 or r < 0 or c < 0 or c > 99:
        return False
    else:
        return True

def finding(r, c, m, g):
    if m == 1:
        if iswall(r, c+1) and g[r][c+1] == 1:
            return r, c+1, 1
        elif iswall(r+1, c) and g[r+1][c] == 1:
            return r+1, c, 3
    elif m == 2:
        if iswall(r, c-1) and g[r][c-1] == 1:
            return r, c-1, 2
        elif iswall(r+1, c) and g[r+1][c] == 1:
            return r+1, c, 3
    elif m == 3:
        if iswall(r, c+1) and g[r][c+1] == 1:
            return r, c+1, 1
        elif iswall(r, c-1) and g[r][c-1] == 1:
            return r, c-1, 2
        elif iswall(r+1, c) and g[r+1][c] == 1:
            return r+1, c, 3


for tc in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    mincnt = 1000
    for x in range(100):
        cnt = 0
        if ladder[0][x] == 1:
            r = cnt = 0
            c = x
            m = 3
            while r != 99:
                if 0 <= r <100 and 0 <= c < 100:
                    r, c, m = finding(r, c, m, ladder)
                    cnt += 1
            
            if cnt <= mincnt:
                mincnt = cnt
                result = x
    
    print('#{} {}'.format(tc, result))



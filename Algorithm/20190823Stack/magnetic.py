import sys
sys.stdin = open('magnetic_input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    magnets = [list(map(int, input().split())) for n in range(N)]

    cnt = 0
    for c in range(100):
        r = 0
        while r < 100:
            if magnets[r][c] == 1:
                if r == 99:
                    r+=1
                else:
                    for m in range(r+1, 100):
                        if magnets[m][c] == 2:
                            cnt += 1
                            r = m+1
                            break
                        elif m == 99:
                            r = 100
                            break
            else:
                r += 1

    print('#{} {}'.format(tc, cnt))
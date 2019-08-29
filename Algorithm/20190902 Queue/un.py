import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bunk = [list(map(int, input().split())) for _ in range(N)]
    dx = [0,1]
    dy = [1,0]
    chems = [[] for _ in range(N**2)]

    for r in range(N):
        for c in range(N):
            if bunk[r][c] > 0:
                height = width = 0
                testr = r
                testc = c
                while bunk[testr][testc] != 0:
                    testr += dx[1]
                    testc += dy[1]
                    height += 1

                testr = r
                testc = c
                while bunk[testr][testc] != 0:
                    testr += dx[0]
                    testc += dy[0]
                    width += 1

                for m in range(r, r+height):
                    for n in range(c, c+width):
                        bunk[m][n] = 0

                sp = width*height
                if not chems[sp]:
                    chems[sp] = [height, width]
                else:
                    if chems[width*height][0] < width:
                        chems[width * height+1] = [height, width]
                    else:
                        chems[width * height - 1] = [height, width]

    res = sum(chems,[])
    res = list(map(str, res))
    num = len(res) // 2
    res = str(num) + ' ' + ' '.join(res)
    print('#{} {}'.format(tc, res))



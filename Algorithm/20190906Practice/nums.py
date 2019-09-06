import sys
sys.stdin = open('nums.txt', 'r')

def numbers(r, c, number, idx):
    global pan, result

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    number += str(pan[r][c])

    if idx == 7:
        result.add(number)
        return
    else:
        for i in range(4):
            tstr = r + dx[i]
            tstc = c + dy[i]
            if 0 <= tstc < 4 and 0 <= tstr < 4:
                numbers(tstr, tstc, number, idx+1)

T = int(input())
for tc in range(1, T+1):
    pan = [list(map(int, input().split())) for _ in range(4)]
    result = set()

    for r in range(4):
        for c in range(4):
            number = ''
            numbers(r, c, number, 1)

    print('#{} {}'.format(tc, len(result)))




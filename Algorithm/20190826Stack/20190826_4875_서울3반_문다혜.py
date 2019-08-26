import sys
sys.stdin = open('input_10_100.txt', 'r')


def ispromising(r, c, maze):
    if maze[r][c] == 0:
        maze[r][c] = 1
        return 1
    elif maze[r][c] == 1:
        return 0
    elif maze[r][c] == 2:
        return 2


def findingroute(r, c, g, maze):
    if ispromising(r, c, maze) == g:
        return 1
    else:
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]
        for i in range(4):
            testr = r + dx[i]
            testc = c + dy[i]
            if 0 <= testr <= N - 1 and 0 <= testc <= N - 1:
                n = ispromising(testr, testc, maze)
                if n:
                    res = findingroute(testr, testc, g, maze)
                    if res == 1:
                        return 1
    return 0

def start(maze,N):
    for m in range(N):
        for n in range(N):
            if maze[m][n] == 3:
                return m, n


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for i in range(N)]

    start_r, start_c = start(maze,N)

    print('#{} {}'.format(tc,findingroute(start_r,start_c,2,maze)))
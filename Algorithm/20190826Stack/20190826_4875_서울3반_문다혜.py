import sys
sys.stdin = open('4875_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for i in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 3:
                start_r = r
                start_c = c


            for i in range(4):
                testr = r + dx[i]
                testc = c + dy[i]
                if 0 <= testr <= N-1 and 0 <= testc <= N-1:
                    if maze[testr][testc] == 0:
                        r = testr
                        c = testc
                        maze[r][c] = 1
                    elif maze[testr][testc] == 2:
                        print(1)


import sys
sys.stdin = open('5105_input.txt', 'r')


def isin(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    else:
        return False


def route(maze, q):
    global front, rear, cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while front != rear:
        front += 1
        curr = q[front]

        for i in range(4):
            tr = curr[0] + dx[i]
            tc = curr[1] + dy[i]
            if isin(tr, tc) and maze[tr][tc] in [0, 3]:
                if maze[tr][tc] == 3:
                    return visited[curr[0]][curr[1]]
                else:
                    maze[tr][tc] = 1
                    q.append((tr, tc))
                    rear += 1
                    visited[tr][tc] = visited[curr[0]][curr[1]] + 1
    return 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for r in range(N-1,-1,-1):
        for c in range(N):
            if maze[r][c] == 2:
                s = (r, c)
                break

    front = rear = -1
    q = []
    q.append(s)
    rear += 1
    maze[s[0]][s[1]] = 1
    cnt = 0
    print('#{} {}'.format(t, route(maze,q)))







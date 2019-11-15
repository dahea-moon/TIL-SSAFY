import sys
sys.stdin = open('test.txt', 'r')


def is_wall(x, y):
    global n
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


def dfs(r, c, dir, cnt):
    global cafes, visited, maxi, cafe_vari, sr ,sc
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    # result
    if r == sr and c == sc and cnt > 1:
        if cnt > maxi:
            maxi = cnt
        return

    for i in range(2):
        if dir == 3 and i == 1:
            if tr == sr and tc == sc:
                dfs(tr, tc, dir + i, cnt + 1)

        else:
            tr, tc = r + dx[dir+i], c + dy[dir+i]
            if is_wall(tr, tc) and not visited[tr][tc] and not cafe_vari[cafes[tr][tc]]:
                visited[tr][tc] = 1
                cafe_vari[cafes[tr][tc]] = 1
                dfs(tr, tc, dir + i, cnt + 1)
                visited[tr][tc] = 0
                cafe_vari[cafes[tr][tc]] = 0

            elif tr == sr and tc == sc:
                dfs(tr, tc, dir + i, cnt + 1)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cafes = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    cafe_vari = [0] * 101
    maxi = -1
    for r in range(n-1):
        for c in range(1, n-1):
            cafe_vari[cafes[r][c]] = 1
            sr, sc = r, c
            dfs(r, c, 0, 0)
            cafe_vari[cafes[r][c]] = 0

    print('#{} {}'.format(tc, maxi))
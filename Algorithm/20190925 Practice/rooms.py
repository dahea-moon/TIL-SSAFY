import sys
sys.stdin = open('rooms.txt', 'r')

def ispromising(r, c):
    global dx, dy, visited
    candis = []
    for i in range(4):
        tx = r + dx[i]
        ty = c + dy[i]
        if 0 <= tx < N and 0 <= ty < N:
            if (rooms[tx][ty]-rooms[r][c]) == 1:
                candis.append((tx,ty))
    return candis


def finding(cr, cc, visited, startr, startc):
    global maxi, cnt, tmp, rooms

    candis = ispromising(cr, cc)
    if not candis:
        chk[startr][startc] = (rooms[startr][startc], cnt)
        return
    else:
        for candi in candis:
            nr, nc = candi
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                cnt += 1
                finding(nr, nc, visited, startr, startc)
                cnt -= 1
                visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    chk = [[0]*N for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    maxi = 0
    cnt = 1
    for r in range(N):
        for c in range(N):
            finding(r, c, visited, r, c)

    chk = sum(chk, [])
    chk = sorted(chk, key= lambda x: x[1], reverse=True)
    val, cnt = chk[0]
    for can in chk:
        if can[1] == cnt:
            if can[0] < val:
                val = can[0]
        else:
            break

    print('#{} {} {}'.format(tc, val, cnt))
import sys
sys.stdin = open('test.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    grid = [[0]*701 for _ in range(701)]
    live = [[0]*701 for _ in range(701)]
    for j in range(n):
        cur = list(map(int, input().split()))
        for i in range(m):
            grid[349+j][349+i] = cur[i]
            live[349+j][349+i] = 1


    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    time = 0
    while time <= k:
        time += 1
        for r in range(701):
            for c in range(701):
                # 비활성화 to 활성화
                if grid[r][c] != 0 and live[r][c] == 1 :

                # 퍼진다
                if grid[r][c] != 0 and live[r][c] == 2 :
                    for h in range(4):
                        tr, tc = r + dx[h], c + dy[h]
                        if grid[tr][tc] == 0:



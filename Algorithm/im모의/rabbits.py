import sys
sys.stdin = open('test2.txt', 'r')

forest = [list(map(int, input().split())) for _ in range(10)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

catch = 0
for r in range(10):
    for c in range(10):
        if forest[r][c] == 3:
            for i in range(8):
                testr = r + dy[i]
                testc = c + dx[i]
                while 1:
                    if 0 <= testr < 10 and 0 <= testc < 10:
                        if forest[testr][testc] == 1:
                            catch += 1
                            forest[testr][testc] = 0
                            testr += dy[i]
                            testc += dx[i]
                        elif forest[testr][testc] == 2:
                            break
                        else:
                            testr += dy[i]
                            testc += dx[i]
                    else:
                        break

print(catch)

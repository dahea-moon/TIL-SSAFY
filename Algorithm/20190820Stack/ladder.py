import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    dx = [0, 0, -1]
    dy = [1, -1, 0]

    for idx in range(100):
        if ladder[99][idx] == 2:
            goal = idx

    x_axis = 98
    start = ladder[x_axis][goal]
    while x_axis != 0:
        for i in range(3):
            testx = x_axis + dx[i]
            testy = goal + dy[i]
            if 0 <= testx < 100 and 0 <= testy < 100:
                if ladder[testx][testy] == 1:
                    ladder[x_axis][goal] = 0
                    x_axis = testx
                    goal = testy
                    break
    print(goal)

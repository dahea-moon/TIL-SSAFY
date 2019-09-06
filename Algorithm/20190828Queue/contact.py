import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N, S = map(int, input().split())
    raw = list(map(int, input().split()))

    links = [0]*(N // 2)
    a = 0
    for i in range(0, N, 2):
        links[a] = (raw[i], raw[i+1])
        a += 1

    calls = [[0]*101 for _ in range(101)]
    for link in links:
        calls[link[0]][link[1]] = 1

    last = []
    front = rear = -1
    q = [(1, S)]
    rear += 1
    called = [S]

    while front != rear:
        front += 1
        cr = q[front][1]
        d = q[front][0]

        cnt = 0
        for c in range(101):
            if c not in called and calls[cr][c]:
                q.append((d+1, c))
                calls[cr][c] = 0
                calls[c][cr] = 0
                rear += 1
                called.append(c)
                cnt += 1

        if cnt == 0:
            last.append((d, cr))

    last.sort()
    print('#{} {}'.format(tc,last[-1][1]))

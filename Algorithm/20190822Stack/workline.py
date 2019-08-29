import sys
sys.stdin = open('input.txt', 'r')


def work(g, s, v):
    global queue
    order = ''
    visited = [0] * (v + 1)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            order += str(t) + ' '
        for i in range(len(g[t])):
            if g[t][i] == 1:
                g[0][i] -= 1
                if g[0][i] == 0 and not visited[i]:
                    queue.append(i)

    return order

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    links = list(map(int, input().split()))
    lines = [[0]*(V+1) for v in range(V+1)]
    queue = []

    for i in range(0, len(links)-1, 2):
        link = links[i:i+2]
        lines[link[0]][link[1]] = 1

    for c in range(1, V+1):
        for r in range(1, V+1):
            if lines[c][r] == 1:
                lines[0][r] += 1

    for n in range(1, V+1):
        if lines[0][n] == 0:
            queue.append(n)

    s = queue[0]
    print('#{} {}'.format(tc,work(lines,s,V)))
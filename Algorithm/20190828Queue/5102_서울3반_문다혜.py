import sys
sys.stdin = open('5102_input.txt', 'r')

def route(S, G, q):
    global links, lines, front, rear
    # visited = [0]*(V+1)

    while front != rear:
        front += 1
        cr = q[front]

        for c in range(1, V + 1):
            if links[cr[0]][c] == 1:
                if c == G:
                    return cr[1]
                else:
                    q.append((c,cr[1]+1))
                    rear += 1
                    links[cr[0]][c] = 0
                    links[c][cr[0]] = 0

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lines = [0]*E
    for i in range(E):
        lines[i] = tuple(map(int, input().split()))

    links = [[0]*(V+1) for _ in range(V+1)]
    for line in lines:
        links[line[0]][line[1]] = 1
        links[line[1]][line[0]] = 1

    S, G = map(int, input().split())

    front = rear = -1
    q = []
    q.append((S,1))
    rear += 1

    print('#{} {}'.format(tc, route(S, G, q)))

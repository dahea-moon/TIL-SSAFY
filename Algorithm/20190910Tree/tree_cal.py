import sys
sys.stdin = open('input.txt', 'r')

def treecal(n):
    global nodes, N
    if n > N:
        return
    if nodes[n][1]:
        treecal(nodes[n][1])
    if nodes[n][2]:
        treecal(nodes[n][2])
    if nodes[n][0] == '+':
        l = nodes[n][1]
        r = nodes[n][2]
        nodes[n][0] = int(nodes[l][0]) + int(nodes[r][0])
    elif nodes[n][0] == '-':
        l = nodes[n][1]
        r = nodes[n][2]
        nodes[n][0] = int(nodes[l][0]) - int(nodes[r][0])
    elif nodes[n][0] == '*':
        l = nodes[n][1]
        r = nodes[n][2]
        nodes[n][0] = int(nodes[l][0]) * int(nodes[r][0])
    elif nodes[n][0] == '/':
        l = nodes[n][1]
        r = nodes[n][2]
        nodes[n][0] = int(nodes[l][0]) // int(nodes[r][0])


for tc in range(1, 11):
    N = int(input())
    nodes = [[0]*3 for _ in range(N+1)]

    for _ in range(N):
        node = input().split()
        s = int(node[0])
        nodes[s][0] = node[1]
        if len(node) > 2:
            nodes[s][1] = int(node[2])
        if len(node) > 3:
            nodes[s][2] = int(node[3])

    print(nodes)
    treecal(1)
    print('#{} {}'.format(tc, nodes[1][0]))


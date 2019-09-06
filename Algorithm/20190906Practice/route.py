import sys
sys.stdin = open('route.txt', 'r')

def distance(perm):
    global com, home, N
    distance = 0

    distance += abs(com[0]-perm[0][0])+abs(com[1]-perm[0][1])
    distance += abs(perm[N-1][0]-home[0])+abs(perm[N-1][1]-home[1])

    for i in range(N-1):
        distance += abs(perm[i][0]-perm[i+1][0])+abs(perm[i][1]-perm[i+1][1])

    return distance

def permutation(k):
    global mindis, nodes, N

    if k == N:
        dis = distance(nodes)

        if dis < mindis:
            mindis = dis

        return

    else:
        for i in range(k, N):
            nodes[k], nodes[i] = nodes[i], nodes[k]
            permutation(k+1)
            nodes[k], nodes[i] = nodes[i], nodes[k]



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    raws = tuple(map(int, input().split()))
    com = raws[0:2]
    home = raws[2:4]

    nodes = [0]*N
    j = 0
    for i in range(4, 2*(N+2)-1, 2):
        nodes[j] = raws[i:i+2]
        j += 1

    mindis = 10000
    permutation(0)
    print('#{} {}'.format(tc, mindis))






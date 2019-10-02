import sys
sys.stdin = open('birthdayparty.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    links = []
    for _ in range(M):
        links += list(map(int, input().split()))

    relations = [[0]*(N+1) for _ in range(N+1)]
    for i in range(0, len(links), 2):
        relations[links[i]][links[i+1]] = 1
        relations[links[i+1]][links[i]] = 1

    que = [1]
    visited = [0]*(N+1)
    cnt = 0
    while que:
        cur = que.pop(0)
        visited[cur] = 1
        print(cur)
        for node in range(len(relations[cur])):
            if cur != 1:
                if not visited[node] and relations[cur][node] and relations[1][cur]:
                    que.append(node)
                    cnt += 1
                    visited[node] = 1
            else:
                if not visited[node] and relations[cur][node]:
                    que.append(node)
                    cnt += 1
                    visited[node] = 1

    print('#{} {}'.format(tc, cnt))
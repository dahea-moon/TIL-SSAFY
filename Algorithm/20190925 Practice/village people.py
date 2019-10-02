import sys
sys.stdin = open('village_people.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    relations = [[] for _ in range(N+1)]
    for _ in range(M):
        p, c = map(int, input().split())
        relations[p].append(c)
        relations[c].append(p)

    visited = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            que = [0] * 101
            front = rear = -1
            rear += 1
            que[rear] = i
            while rear != front:
                front += 1
                cur= que[front]
                for people in relations[cur]:
                    if not visited[people]:
                        visited[people] = 1
                        rear += 1
                        que[rear] = people

    print('#{} {}'.format(tc, cnt))
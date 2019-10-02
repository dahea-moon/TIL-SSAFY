import sys
sys.stdin = open('5248.txt', 'r')

# def makeset(relation, node, depth):
#     global visited, cnt
#
#     visited[node] = 1
#     if relation[node]:
#         for i in relation[node]:
#             if visited[i]:
#                 for s in relation[node]:
#                     visited[s] = 1
#                 return
#         if depth == 0:
#             cnt += 1
#         for i in relation[node]:
#             if not visited[i]:
#                 makeset(relation, i, depth+1)
#             else:
#                 return
#     else:
#         if depth == 0:
#             cnt += 1
#
#     return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lines = list(map(int, input().split()))

    relation = [[] for _ in range(N+1)]

    for i in range(0, len(lines), 2):
        relation[lines[i]].append(lines[i+1])
        relation[lines[i+1]].append(lines[i])

    visited = [0]*(N+1)
    cnt = 0
    for node in range(1, N+1):
        if not visited[node]:
           visited[node] = 1
           que = [(node, 0)]
           while que:
               cur, depth = que.pop(0)
               visited[cur] = 1
               if depth == 0:
                   cnt += 1
               if relation[cur]:
                   for i in relation[cur]:
                       if not visited[i]:
                           que.append((i, depth+1))

    print('#{} {}'.format(tc, cnt))
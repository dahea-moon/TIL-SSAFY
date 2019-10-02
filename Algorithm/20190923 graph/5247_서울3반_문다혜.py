from collections import deque
import sys
sys.stdin = open('5247.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    que = deque()
    que.append((n, 0))
    visited = [0]*(10**6 + 1)

    while que:
        n, cnt = que.popleft()
        if n == m:
            break
        for i in range(4):
            if i == 0 and 0 < n*2 < 1000001:
                if not visited[n*2]:
                    que.append((n*2, cnt + 1))
                    visited[n*2] = 1
            if i == 1 and 0 < n-1 < 1000001:
                if not visited[n-1]:
                    que.append((n-1, cnt + 1))
                    visited[n-1] = 1
            if i == 2 and 0 < n+1 < 1000001:
                if not visited[n+1]:
                    que.append((n+1, cnt + 1))
                    visited[n+1] = 1
            if i == 3 and 0 < n-10 < 1000001:
                if not visited[n-10]:
                    que.append((n-10, cnt + 1))
                    visited[n-10] = 1

    print('#{} {}'.format(tc, cnt))






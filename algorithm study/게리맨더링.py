import sys
sys.stdin = open('test.txt', 'r')

def powersetlist(li):
    r = [[]]
    for l in li:
        temp = [x+[l] for x in r]
        r += temp

    return r

def bfs(candi):
    global towns, n
    nn = len(candi)
    visited = [0]*(n+1)
    cnt = 1
    q = [0]*nn
    front = -1
    rear = 0
    q[rear] = candi[0]
    visited[candi[0]] = 1

    while front != rear:
        front += 1
        start = q[front]
        for node in towns[start]:
            if node in candi and not visited[node]:
                visited[node] = 1
                cnt += 1
                rear += 1
                q[rear] = node

    if cnt == nn:
        return True
    else:
        return  False


n = int(input())
ppl = [0] + list(map(int, input().split()))
towns = [0]*(n+1)

# node tree로 저장
for i in range(n):
    tmp = list(map(int, input().split()))
    towns[i+1] = tmp[1:]

raw = [j for j in range(1, n+1)]
candis = powersetlist(raw)
k = len(candis)
res = 9999999
for s in range(k):
    if candis[s] and candis[k-(s+1)]:
        if bfs(candis[s]) and bfs(candis[k-(s+1)]):
            vote1 = 0
            for p in candis[s]:
                vote1 += ppl[p]

            vote2 = 0
            for p in candis[k-(s+1)]:
                vote2 += ppl[p]

            diff = abs(vote1-vote2)
            if diff < res:
                res = diff

print(res if res != 9999999 else -1)


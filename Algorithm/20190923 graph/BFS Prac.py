data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

links = [[0]*8 for _ in range(8)]
for i in range(0, len(data), 2):
    links[data[i]][data[i+1]] = 1
    links[data[i+1]][data[i]] = 1

#반복문
que = [0]*7
front = rear = -1
rear += 1
que[rear] = 1
visited = [0]*8
while front != rear:
    front += 1
    cur = que[front]
    visited[cur] = 1
    for node in range(len(links[cur])):
        if links[cur][node] and not visited[node]:
            rear += 1
            que[rear] = node
            visited[node] = 1


print(que)

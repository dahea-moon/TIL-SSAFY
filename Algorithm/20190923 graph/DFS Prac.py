data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

links = [[0]*8 for _ in range(8)]
for i in range(0, len(data), 2):
    links[data[i]][data[i+1]] = 1
    links[data[i+1]][data[i]] = 1

#반복문
stack = [1]
visited = [0]*8
route = []
while stack:
    cur = stack.pop()
    if not visited[cur]:
        route.append(cur)
    visited[cur] = 1
    for node in range(len(links[cur])):
        if links[cur][node]:
            if not visited[node]:
                stack.append(node)
print(route)

#재귀
visited = [0]*8
route = []
def dfs(graph, v):
    route.append(v)
    visited[v] = 1
    for node in range(len(links[v])):
        if links[v][node] and not visited[node]:
            dfs(graph,node)

dfs(links, 1)
print(route)


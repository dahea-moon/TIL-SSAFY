sides = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
map = [[0]*8 for i in range(8)]
for r in range(0,len(sides),2):
    map[sides[r]][sides[r+1]] = 1
    map[sides[r+1]][sides[r]] = 1

def bfs(g, s):
    visited = [False]*8
    queue = []
    queue.append(s)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            print(t)
        for i in range(len(g[t])):
            if g[t][i] == 1 and not visited[i]:
                queue.append(i)

bfs(map,1)







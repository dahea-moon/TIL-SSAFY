tree = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
visited = [0]*14

relation = [[0]*2 for _ in range(14)]

for i in range(0, len(tree), 2):
    if relation[tree[i]][0] == 0:
        relation[tree[i]][0] = tree[i+1]
    else:
        relation[tree[i]][1] = tree[i+1]

def tree(relation, node):
    global visited
    if relation[node]:
        visited[node] = 1
        print(node)
        if relation[node][0]:
            tree(relation, relation[node][0])
        if relation[node][1]:
            tree(relation, relation[node][1])

tree(relation, 1)

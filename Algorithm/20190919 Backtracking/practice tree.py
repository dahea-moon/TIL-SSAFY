tree = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
visited = [0]*14

relation = [[0]*2 for _ in range(14)]

for i in range(0, len(tree), 2):
    if relation[tree[i]][0] == 0:
        relation[tree[i]][0] = tree[i+1]
    else:
        relation[tree[i]][1] = tree[i+1]

def front_tree(relation, node):
    global visited
    if relation[node]:
        visited[node] = 1
        print(node, end=' ')
        if relation[node][0]:
            front_tree(relation, relation[node][0])
        if relation[node][1]:
            front_tree(relation, relation[node][1])


def inorder_tree(relation, node):
    global visited
    if relation[node]:
        if relation[node][0]:
            inorder_tree(relation, relation[node][0])
        visited[node] = 1
        print(node, end=' ')
        if relation[node][1]:
            inorder_tree(relation, relation[node][1])


def lastorder_tree(relation, node):
    global visited
    if relation[node]:
        if relation[node][0]:
            lastorder_tree(relation, relation[node][0])
        if relation[node][1]:
            lastorder_tree(relation, relation[node][1])
        visited[node] = 1
        print(node, end=' ')

front_tree(relation, 1)
print()
inorder_tree(relation, 1)
print()
lastorder_tree(relation, 1)



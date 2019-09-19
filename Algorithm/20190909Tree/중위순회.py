import sys
sys.stdin = open('input.txt', 'r')

def inorder_tree(graph, node):
    global word
    if graph[node]:
        if graph[node][1]:
            inorder_tree(graph, graph[node][1])
        word += graph[node][0]
        if graph[node][2]:
            inorder_tree(graph, graph[node][2])


for tc in range(1, 11):
    N = int(input())
    nodes = [[0]*3 for _ in range(N+1)]
    for _ in range(N):
        node_info = input().split()
        s = len(node_info)
        node = int(node_info[0])
        nodes[node][0] = node_info[1]
        if s > 2:
            nodes[node][1] = int(node_info[2])
        if s > 3:
            nodes[node][2] = int(node_info[3])

    word = ''
    inorder_tree(nodes, 1)
    print('#{} {}'.format(tc, word))